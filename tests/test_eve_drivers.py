import unittest
from unittest.mock import Mock

from netmiko.exceptions import ReadTimeout
from utils.eve_drivers import DeviceModel, IosModel


BGP_HELP = """Router configuration commands:
  address-family           Enter Address Family command mode
  aggregate-address        Configure BGP aggregate entries
  auto-summary             Enable automatic network number summarization
  bgp                      BGP specific commands
  bmp                      BGP Monitoring Protocol
  default                  Set a command to its defaults
  default-information      Control distribution of default information
  default-metric           Set metric of redistributed routes
  distance                 Define an administrative distance
  distribute-list          Filter networks in routing updates
  exit                     Exit from routing protocol configuration mode
  help                     Description of the interactive help system
  maximum-paths            Forward packets over multiple paths
  maximum-secondary-paths  Maximum secondary paths
  neighbor                 Specify a neighbor router
  network                  Specify a network to announce via BGP
  no                       Negate a command or set its defaults
  redistribute             Redistribute information from another routing protocol
  route-server-context     Enter route server context command mode
  scope                    Enter scope command mode
  snmp                     Modify snmp parameters
  synchronization          Perform IGP synchronization
  table-map                Map external entry attributes into routing table
  template                 Enter template command mode
  timers                   Adjust routing timers
"""


class CiscoEchoParsingTest(unittest.TestCase):
    def ios_model(self):
        model = object.__new__(IosModel)
        model.PRE_PROMPT = "Router"
        model.END = "<cr>"
        model.OMIT_FLDS = [
            "abort", "alias", "clear", "commit", "copy", "describe", "do",
            "end", "exit", "hostname", "man", "exclude-item", "no", "pwd",
            "rollback", "root", "save", "show",
        ]
        model.OMIT_FLDS_TEST = ["help", "Failed", "UNKNOWN", "'cfg", "(", ")"]
        return model

    def test_bgp_help_header_is_not_mistaken_for_a_prompt(self):
        _, branches = self.ios_model().echo2dict(BGP_HELP, "")

        self.assertIn("address-family", branches)
        self.assertIn("neighbor", branches)
        self.assertIn("network", branches)
        self.assertNotIn("Router configuration commands:", branches)

    def test_trailing_cisco_prompt_is_removed_without_losing_help(self):
        _, branches = self.ios_model().echo2dict(BGP_HELP + "Router(config-router)#\n", "")

        self.assertIn("address-family", branches)
        self.assertNotIn("Router(config-router)#", branches)

    def test_timestamped_syslog_is_not_treated_as_command_error(self):
        echo = (
            "Router(config-router)#router ospf ?\n"
            "*Aug 10 15:00:33.816: % Unrecognized command\n"
            "Router(config-router)#\n"
        )

        self.assertFalse(self.ios_model().detect_error(echo))

    def test_syslog_question_mark_keeps_following_help_fields(self):
        echo = (
            "Router(config)#access-list ?\n"
            "*Aug 29 00:59:48.611: %PARSE_RC-3-PRC_OUT_OF_RANGE_ENUM: "
            "error code had value 24q sunrpc ?\n"
            "  ack          Match on the ACK bit\n"
            "  dscp         Match packets with given dscp value\n"
        )

        _, branches = self.ios_model().echo2dict(echo, "access-list ")

        self.assertEqual("Match on the ACK bit", branches["ack"])
        self.assertEqual("Match packets with given dscp value", branches["dscp"])

    def test_orphan_continuation_line_is_ignored(self):
        echo = "     orphan continuation\n  valid       A valid field\n"

        _, branches = self.ios_model().echo2dict(echo, "")

        self.assertNotIn("orphan continuation", branches)
        self.assertEqual("A valid field", branches["valid"])

    def test_object_group_unrecognized_command_is_an_error(self):
        echo = (
            "Router(config)#access-list foo ?\n"
            "% Unrecognized command: Object group is not supported here\n"
        )

        self.assertTrue(self.ios_model().detect_error(echo))

    def test_disabled_ios_shell_message_is_treated_as_command_error(self):
        echo = (
            "Router(config-router)#default domain-id null ?\n"
            "The command you have entered is available in the IOS.sh.\n"
            "However, the shell is currently disabled. You can enable\n"
            "Router(config-router)#\n"
        )

        self.assertTrue(self.ios_model().detect_error(echo))

    def test_terminal_only_named_acl_error_is_detected(self):
        echo = '% match-all/match-any are allowed on named ACLs only\n'

        self.assertTrue(self.ios_model().detect_terminal_error(echo))

    def test_removing_bgp_process_clears_the_pending_command_before_undoing(self):
        model = self.ios_model()
        model.conn = Mock()
        model.send_command = Mock(return_value="Router(config)#")

        model.remove_bgp_process("router bgp 1")

        model.conn.write_channel.assert_called_once_with("\x15")
        model.send_command.assert_called_once_with("no router bgp 1", cmd_verify=False)

    def test_cisco_clear_input_preserves_parent_prefix(self):
        model = self.ios_model()
        model.conn = Mock()

        model.clear_input("router ospf ")

        model.conn.write_channel.assert_called_once_with("\x08" * len("router ospf "))

    def test_cisco_clear_input_without_text_resets_the_full_line(self):
        model = self.ios_model()
        model.conn = Mock()

        model.clear_input()

        model.conn.write_channel.assert_called_once_with("\x15")

    def test_cisco_prompt_recovery_clears_the_line_without_ctrl_c(self):
        model = self.ios_model()
        model.conn = Mock()
        model.conn.read_timeout_override = None
        model.conn.select_delay_factor.return_value = 0

        self.assertTrue(model.recover_prompt('#'))

        self.assertEqual(
            [call.args for call in model.conn.write_channel.call_args_list],
            [("\x15",), ("\n",), ("\n",)],
        )
        model.conn.find_prompt.assert_called_once_with(pattern='#')

    def test_cisco_restore_input_rewrites_parent_prefix(self):
        model = self.ios_model()
        model.conn = Mock()

        model.restore_input("router ospf compatible ", "rfc1583 ")

        self.assertEqual(
            model.conn.write_channel.call_args_list[0].args,
            ("\x15",),
        )
        self.assertEqual(
            model.conn.write_channel.call_args_list[1].args,
            ("router ospf compatible ",),
        )

    def test_base_restore_input_removes_only_the_child_branch(self):
        model = object.__new__(DeviceModel)
        model.conn = Mock()

        # Non-Cisco subclasses keep their original branch-only backtracking.
        DeviceModel.restore_input(model, "router ospf compatible ", "rfc1583 ")

        model.conn.write_channel.assert_called_once_with("\x08" * len("rfc1583 "))

    def test_prompt_pattern_survives_netmiko_capture_wrapping(self):
        model = self.ios_model()
        pattern = model._prompt_pattern()

        import re

        re.split(f"({pattern})", "Router(config)#\n", maxsplit=1)

    def test_text_input_prompt_is_terminated_before_reading_the_view(self):
        model = self.ios_model()
        model.conn = Mock()
        model.conn.read_timeout_override = None
        model.conn.find_prompt.side_effect = [
            "Enter TEXT message.  End with the character 'L'.",
            "Router(config)#",
        ]

        self.assertEqual("[config]", model.get_view())
        model.conn.write_channel.assert_called_once_with("L\n")

    def test_normal_prompt_does_not_send_a_text_terminator(self):
        model = self.ios_model()
        model.conn = Mock()
        model.conn.read_timeout_override = None
        model.conn.find_prompt.return_value = "Router(config)#"

        self.assertEqual("[config]", model.get_view())
        model.conn.write_channel.assert_not_called()

    def test_banner_line_remains_a_field(self):
        echo = "  LINE  c banner-text c, where 'c' is a delimiting character\n"

        _, branches = self.ios_model().echo2dict(echo, "banner ")

        self.assertIn("LINE", branches)

    def test_command_timeout_recovers_once(self):
        model = self.ios_model()
        model.conn = Mock()
        model.conn.send_command.side_effect = [ReadTimeout("timeout"), "Router#"]
        model.recover_prompt = Mock(return_value=True)

        result = model.search_command("router ospf ")

        self.assertEqual(result, "Router#")
        model.recover_prompt.assert_called_once()

    def test_side_effecting_command_is_not_replayed_after_timeout(self):
        model = self.ios_model()
        model.conn = Mock()
        model.conn.send_command.side_effect = ReadTimeout("timeout")
        model.recover_prompt = Mock(return_value=True)

        with self.assertRaises(ReadTimeout):
            model.send_command("exit", cmd_verify=False)

        self.assertEqual(model.conn.send_command.call_count, 1)
        model.recover_prompt.assert_called_once()


if __name__ == "__main__":
    unittest.main()
