from evengsdk.client import EvengClient
import os
import io
import re
import time
import random
import string
import netmiko
from netmiko import ConnectHandler
from netmiko.exceptions import ReadTimeout


################################## EVE-NG ##################################
# Step1: Select image(PRODUCT)
HOST = '192.168.241.128'
CLEAR_LOG = True                            # Clear current log
PRE_CONF = True                            # Initiator(for probing)
LAB_NAME = "test_lab"                       # emulator path
# LAB_NAME = "bgp"
# PRODUCT = 'xrv'                             # Cisco
# PRODUCT = 'xrv2'
PRODUCT = 'xrv9k'
PRODUCT = 'iol'
# PRODUCT = 'iol2'
# PRODUCT = 'iol3'
# PRODUCT = 'csr'
# PRODUCT = 'csr2'
# PRODUCT = 'csr3'


# PRODUCT = 'arv'                             # Huawei
# PRODUCT = 'arv2'
# PRODUCT = 'arv3'
# PRODUCT = 'arv4'
# PRODUCT = 'cRPD'                            # Juniper
# PRODUCT = 'cRPD2'

################################### Input ###################################
# Step2: Select command prefix (To specify view/mode, go to corresponding class and modify the PRE_CMDS)

# Cisco-IOS/XE/XR
COMMAND = 'router bgp'
# COMMAND = 'arp'
# COMMAND = 'bfd'
# COMMAND = 'bfd-template'
# COMMAND = 'bridge'
# COMMAND = 'bridge-domain'
# COMMAND = 'cef'
# COMMAND = 'clns'
# COMMAND = 'clock'
COMMAND = 'crypto'
COMMAND = 'domain'
COMMAND = 'fhrp'
COMMAND = 'flow'
COMMAND = 'frame-relay'
COMMAND = 'ip'


# COMMAND = 'interface'
# COMMAND = 'decnet'
# COMMAND = 'dlsw'

# COMMAND = 'access-list'
# COMMAND = 'router eigrp'
# COMMAND = 'router isis'
# COMMAND = 'router iso-igrp'
# COMMAND = 'router lisp'
# COMMAND = 'router mobile'
# COMMAND = 'router odr'
# COMMAND = 'router ospf'
# COMMAND = 'router ospfv3' 
# COMMAND = 'router rip' 


# COMMAND = 'router static'
# COMMAND = 'interface'
# COMMAND = 'ip security multilevel'  # interface g 1
# COMMAND = 'access-list'
# COMMAND = 'ip route static'
# COMMAND = 'ip route'


# Huawei        
# COMMAND = 'bgp'
# COMMAND = 'isis'
# COMMAND = 'ospf'
# COMMAND = 'ospfv3'
# COMMAND = 'ip route-static'
# COMMAND = 'rip'
# COMMAND = 'l2vpn-family evpn'
# COMMAND = 'dhcp'


# Juniper
# COMMAND = 'set protocols bgp'
# COMMAND = 'set protocols isis'
# COMMAND = 'set protocols ospf'
# COMMAND = 'set protocols ospf3'
# COMMAND = 'set routing-options static'


################################## Paths ##################################
# Step3: Select mode (Probing/Templatization) by assign path (GRAPH_PATH)
DOT_PATH = "D:/Graphviz/bin/dot"                            # graphviz location
LOG_PATH = f"logs/{PRODUCT}"
PROBE_FILE = "logs/probe.log"
cmd = COMMAND.replace(' ', '_')
GRAPH_PATH = None
# GRAPH_PATH = f"graphs/{PRODUCT}/config/{cmd}/{cmd}_111.graphml"
# GRAPH_PATH = f"graphs/{PRODUCT}/Huawei/{cmd}/{cmd}_111.graphml"
# GRAPH_PATH = f"graphs/{PRODUCT}/edit/{cmd}/{cmd}_111.graphml"

############################### DAG-Ablation ###############################
# Step4: (Optional) Ablation
ABLAT = [1, 1, 1, 1]  
# ABLAT = [1, 1, 0, 1] 
COMPO_CHECK = True if ABLAT[0]==1 else False                # If Inter-command check for command composition
REPET_CHECK = True if ABLAT[1]==1 else False                # If Dense repetition check for infinite repetition
PERMU_CHECK = True if ABLAT[2]==1 else False                # If Dense repetition check for option permutation
COMBI_CHECK = True if ABLAT[3]==1 else False                # If regular evquivalence check for branch combination
MGEND = True                # if merge end
# MGEND = False
CROSS = True                # If probe view


# SLEEP = 5                  # Interval period (min)
# MAX_CYCLES =12
SLEEP = 60 * 4                  # Interval period (min)
MAX_CYCLES = 32

MAX_NODES = 25
MAX_BRANCHES = 5
MAX_LOOP = 3
# SPACE_BEFORE_CANDIDATE = 5






class LabModel:
    def __init__(self, host: str, lab_name: str = 'test_lab', description: str = 'test', log_file: str = None):
        self.host = host
        self.client = None
        self.path = f'{lab_name}.unl' if lab_name else 'test_lab.unl'

        # 【connect eveng】
        client = EvengClient(host, log_file=log_file)
        client.disable_insecure_warnings()
        client.login(username="admin", password="eve")
        client.set_log_level("DEBUG")
        self.client = client

        # 【create if not exists】
        exist = False
        for lab in self.client.api.list_folders()['data']['labs']:
            if lab['file'] == lab_name + '.unl':
                self.path = lab['path']
                exist = True
        if not exist:
            lab = {"name": lab_name, "description": description, "path": '/'}
            resp = self.client.api.create_lab(**lab)

            if resp['status'] == "success":
                print(f"已创建lab:【{lab_name}】\n{description}")
                self.path = f"{lab['path']}{lab['name']}.unl"
            else:
                raise ValueError('lab创建失败')
        

    def find_node(self, name: str) -> bool:
        dics = self.client.api.list_nodes(self.path)['data']

        if not dics:
            return False
        for dic in dics.values():
            if name == dic['name']:
                return True
        else:
            return False

    def start_node(self, name: str):
        node_info = self.client.api.get_node_by_name(self.path, name)
        if node_info['status'] != 2:
            self.client.api.start_node(self.path, node_info['id'])
    
    def get_id(self, name: str) -> int:
        node_info = self.client.api.get_node_by_name(self.path, name)
        node_id = node_info['id']
        # tmp1 = client.api.get_node_config_by_id(path, node_id)
        # tmp2 = client.api.get_node_interfaces(path, node_id)
        return node_id

    def get_port(self, name: str) -> int:
        node_info = self.client.api.get_node_by_name(self.path, name)
        url = node_info['url']
        port = url.split(':')[-1]
        return port



class DeviceModel:
    def __init__(self):
        self.lab = LabModel(HOST, LAB_NAME)
        self.conn: netmiko.BaseConnection
        self.vendor: str
        self.END: str
        self.PRE_PROMPT: str
        
        
        os.makedirs(LOG_PATH, exist_ok=True)
        # lab.start_node(TEMPLATE)


    def echo2dict(self, echo: str, templ: str) -> tuple[str, dict]:
        """
        Parsing echo to dictionary
        
        :param echo: raw echo
        :type echo: str
        :return: cleaned echo, dict{field: description}
        :rtype: tuple[str, dict]
        """
        
        lines = []
        branches = {}
        echo = echo.split('?')[-1]

        if self.END in echo and templ:          
            branches['END'] = self.END          # eg. {'END': '<cr>'}
        for line in echo.split('\n'):
            if self.END in line or not line:    
                continue
            stripped_line = line.strip()
            if re.match(r"\s{5,}\S+", line):    # 【if multiple lines】
                # An async notification may precede the first help row.
                if lines:
                    lines[-1] += stripped_line
            elif stripped_line:
                lines.append(stripped_line)
        
        for line in lines:
            # 【candidate field: description】
            if self.PRE_PROMPT in line:
                continue
            match_double = re.match(r'^(.+?) {2,}(.+)$', line)    
            if match_double:
                key = match_double.group(1)
                desc = match_double.group(2)
            elif '  ' not in line:
                key = line
                desc = line
            else:
                raise ValueError(f'Undefined match: {line}')
            
            # 【exclude special field】
            if key in self.OMIT_FLDS_TEST:              #  or bool(re.fullmatch(r'^word[a-zA-Z]{4}$', field))
                # print(f'(⚠️Dismiss "{key}" halfway)')
                continue
            elif key in self.OMIT_FLDS and not templ :
                # print(f'(⚠️Dismiss "{key}" in the beginning)')
                continue
            # elif templ.count(key+' ') >= 3:             # exclude recursive
            #     print(f'(⚠️Dismiss repeated "{key}" (x3))')
            #     continue
            elif re.match(r'word.+', key):                
                continue
            else:
                branches[key] = desc
      
        return echo, branches

    def if_send(self, templ: str) -> bool:
        return CROSS

    def randn(self, min, max, ceiling=None) -> int:
        if ceiling:
            if max <= ceiling:
                return random.randint(min, max)
            elif min <= ceiling:
                return random.randint(min, ceiling)
            else:
                return min
        else:
            return random.randint(min, max)
    
    def process_complete_cmd(self, cmd: str):
        self.conn.write_channel(cmd)    

    def clear_input(self, input_text: str = ''):
        """Clear the current CLI input line."""
        self.conn.write_channel('\x08' * len(input_text))

    def restore_input(self, command: str, branch_input: str):
        """Restore the pending parent command after probing a branch."""
        self.clear_input(branch_input)

    def recover_prompt(self, pattern: str | None = None) -> bool:
        """Cancel a partially entered command and resynchronize the session."""
        original_timeout = getattr(self.conn, 'read_timeout_override', None)
        try:
            if isinstance(original_timeout, (int, float)) and original_timeout > 0:
                self.conn.read_timeout_override = min(original_timeout, 15)
            else:
                self.conn.read_timeout_override = 15
            self.clear_input()
            self.conn.write_channel('\x03\n')
            time.sleep(min(self.conn.select_delay_factor(1) * 0.25, 1.0))
            self.conn.clear_buffer()
            self.conn.write_channel('\n')
            time.sleep(min(self.conn.select_delay_factor(1) * 0.25, 1.0))
            self.conn.find_prompt(pattern=pattern) if pattern else self.conn.find_prompt()
            return True
        except (ReadTimeout, OSError, ValueError):
            return False
        finally:
            self.conn.read_timeout_override = original_timeout

    def _send_command_with_recovery(
        self,
        command: str,
        pattern: str,
        *,
        cmd_verify: bool = False,
        normalize: bool = False,
        retry: bool = True,
    ) -> str:
        """Send a command with one bounded prompt-recovery attempt."""
        try:
            return self.conn.send_command(
                command, pattern, cmd_verify=cmd_verify, normalize=normalize
            )
        except ReadTimeout:
            if not self.recover_prompt(pattern):
                raise
            if not retry:
                raise
            original_timeout = getattr(self.conn, 'read_timeout_override', None)
            try:
                if isinstance(original_timeout, (int, float)) and original_timeout > 0:
                    self.conn.read_timeout_override = min(original_timeout, 30)
                else:
                    self.conn.read_timeout_override = 30
                return self.conn.send_command(
                    command, pattern, cmd_verify=cmd_verify, normalize=normalize
                )
            finally:
                self.conn.read_timeout_override = original_timeout

    def _find_prompt_with_recovery(self, pattern: str | None = None) -> str:
        """Find the prompt, retrying once after synchronizing the session."""
        original_timeout = getattr(self.conn, 'read_timeout_override', None)
        try:
            if isinstance(original_timeout, (int, float)) and original_timeout > 0:
                self.conn.read_timeout_override = min(original_timeout, 30)
            else:
                self.conn.read_timeout_override = 30
            try:
                return self.conn.find_prompt(pattern=pattern) if pattern else self.conn.find_prompt()
            except ReadTimeout:
                if not self.recover_prompt(pattern):
                    raise
                return self.conn.find_prompt(pattern=pattern) if pattern else self.conn.find_prompt()
        finally:
            self.conn.read_timeout_override = original_timeout

    def get_view(self) -> str:
        """
        return view with []
        """
        view = self.conn.find_prompt()
        delay_factor = self.conn.select_delay_factor(1)
        sleep_time = delay_factor * 0.25
        self.conn.clear_buffer()
        self.conn.write_channel('\n')
        time.sleep(sleep_time)
        prompt = self.conn.read_channel().strip()
        count = 0
        while count <= 12 and not prompt:
            if not prompt:
                self.conn.write_channel('\n')
                time.sleep(sleep_time)
                prompt = self.conn.read_channel().strip()
                if sleep_time <= 3:
                    # Double the sleep_time when it is small
                    sleep_time *= 2
                else:
                    sleep_time += 1
            count += 1

        if not prompt:
            raise ValueError(f"Unable to find prompt: {prompt}")
        view = prompt.split('\n')[-1]
        view = view.strip()
        
        # if detect_error:
        #     if ''

        if re.search(r'\[.*?\]', view):
            return view
        elif re.search(r'<.*?>', view):
            return "[ROOT]" 
        else:
            raise ValueError("Unexpected Prompt")



#############################################################################################################################
# Cisco
#############################################################################################################################
class CiscoModel(DeviceModel):
    def __init__(self):
        super().__init__()
        self.vendor = 'Cisco'
        self.END = '<cr>'
        self.os: str

        self.OMIT_FLDS = [# skip if first
            'abort', 'alias',
            'commit', 'copy', 'describe', 'do', 'default',
            'end', 'exit', 'exit-address-family', 'exit-if-topo', 'exit-service-family', 'exit-sf-interface',
            'exit-bmp-server-mode',
            'history', 'hostname', 'man',
            'exclude-item', 
            'no',
            'pwd', 'rollback', 'root', 'save', 'show', 
            # 'redistribute',, 'describe' 'description',
        ]
        self.OMIT_FLDS_TEST = [# skip anywhere
            # 'template',
            # '0/0/0/1', '0/0/0/2', '0/0/0/3',
            'clear', 'do-exec', 'exit',
            'describe', 'help', 'upgrade-cli',
            # 'apply-group', 'apply-group-append', 'apply-group-remove',
            'Failed','UNKNOWN', '\'cfg', #'redistribute', #'topology',
            '(', ')'
        ]

        

    def echo2dict(self, echo: str, templ: str):
        # Strip only a complete trailing Cisco prompt.  Help headers such as
        # "Router configuration commands:" are valid output, not prompts.
        echo = re.sub(self._prompt_pattern(), '', self._clean_async_output(echo))

        echo, branches = super().echo2dict(echo, templ)

        if 'LINE' in templ:
            if 'LINE' in branches:
                del branches['LINE']

        return echo, branches

    def _prompt_pattern(self) -> str:
        return rf'(?m:^\s*{re.escape(self.PRE_PROMPT)}[^\r\n#>]*?(?:\([^\r\n)]*\))?[#>]\s*$)'

    def _clean_async_output(self, echo: str) -> str:
        """Remove Cisco timestamped syslog text from CLI help output."""
        # Preserve a CLI question mark that shares a line with a notification.
        syslog = r'\*?[A-Z][a-z]{2}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}(?:\.\d+)?:\s+[^\r\n?]*'
        return re.sub(syslog, '', echo)
  
    def detect_error(self, echo: str) -> bool:
        echo = self._clean_async_output(echo)
        # IOS can advertise a keyword in context-sensitive help, then hand it
        # to IOS.sh instead of the CLI parser.  Its explanatory text is not a
        # help listing and must never be expanded as successor commands.
        if 'The command you have entered is available in the IOS.sh.' in echo:
            return True
        return bool(re.search(r'% (?:Unrecognized|Invalid|Unknown|Ambiguous)', echo))

    def get_view(self) -> str:

        view = ''
        count = 0
        text_input_prompt = (
            r"Enter TEXT message\.\s+End with the character '[^'\r\n]'\."
        )
        prompt_or_text_input = f"{self._prompt_pattern()}|{text_input_prompt}"
        while (not re.search(r"\(.*\)", view)) and count<12:
            try:
                view = self._find_prompt_with_recovery(prompt_or_text_input)
            except ReadTimeout:
                raise ReadTimeout(
                    f"Unable to synchronize Cisco prompt after {count + 1} attempts."
                )
            count += 1
            terminator = re.search(r"End with the character '([^'\r\n])'\.", view)
            if terminator:
                self.conn.write_channel(f"{terminator.group(1)}\n")
        if not re.search(r"\(.*\)", view):
            raise ValueError(f"Unexpected Cisco prompt: {view[-120:]}")
        view = view.split('(')[-1].split(')')[0]
        return f"[{view}]"

    def recover_prompt(self, pattern: str | None = None) -> bool:
        """Resynchronize Cisco input without leaving the current config view."""
        original_timeout = getattr(self.conn, 'read_timeout_override', None)
        try:
            if isinstance(original_timeout, (int, float)) and original_timeout > 0:
                self.conn.read_timeout_override = min(original_timeout, 15)
            else:
                self.conn.read_timeout_override = 15
            self.clear_input()
            self.conn.write_channel('\n')
            time.sleep(min(self.conn.select_delay_factor(1) * 0.25, 1.0))
            self.conn.clear_buffer()
            self.conn.write_channel('\n')
            time.sleep(min(self.conn.select_delay_factor(1) * 0.25, 1.0))
            self.conn.find_prompt(pattern=pattern) if pattern else self.conn.find_prompt()
            return True
        except (ReadTimeout, OSError, ValueError):
            return False
        finally:
            self.conn.read_timeout_override = original_timeout

    def clear_input(self, input_text: str = ''):
        # During DFS backtracking only the current branch is removed; the
        # parent prefix must remain on the IOS input line.  Ctrl-U is reserved
        # for prompt recovery, where the complete line is intentionally reset.
        if input_text:
            self.conn.write_channel('\x08' * len(input_text))
        else:
            self.conn.write_channel('\x15')

    def restore_input(self, command: str, branch_input: str):
        """Reset the line and rewrite the exact Cisco parent command."""
        self.clear_input()
        self.conn.write_channel(command)

    def get_instance(self, branch: str, desc: str, space: str) -> tuple[str, str, str]:
        match_range = re.match(r'^<([-+]?\d+)[-,]([-+]?\d+|[0-9A-Fa-f]+)>([.:-]?).*', branch)
        if match_range:                                         
            min = int(match_range.group(1))
            if 'f' in match_range.group(2).lower():                     # 16
                max = int(match_range.group(2), 16)
                instance = random.randint(min, max)
                return f"{instance:x}", branch, space
            else:                                               # 10
                max = int(match_range.group(2))
                if max<min:
                    instance = '0'
                else:
                    # instance = str(random.randint(min, max)) 
                    instance = str(min)       
            if match_range.group(3):                            # '.'':''-'
                instance += match_range.group(3)
                space = ''
                return instance, branch, space
            else:
                return instance, branch, space
        elif 'X:X::X' in branch:
            if 'X:X:X:X::X/<0-128>' == branch:
                return '1::1/24', f"<{branch}>", space
            if 'prefix' in desc.lower() or 'length' in desc.lower():
                return '1::1/24', f"<{branch}>", space                  # ipv6 with prefix
            else:
                return '1::1', f"<{branch}>", space                     # ipv6
        elif 'XX.XXXX. ... .XXX.XX' == branch:
            return '00', f"<{branch}>", space
        elif 'A.B.C.D' in branch:
            if 'A.B.C.D:' == branch:
                return '10.0.0.1:', f"<{branch}>", ''
            if 'mask' in desc.lower() or 'length' in branch:     # ipv4 with mask
                if self.os in ['IOS-XE', 'IOS']:
                    return '255.255.0.0', '<mask>', space
                elif self.os == 'IOS-XR':
                    return '10.0.0.1/24', f"<{branch}/mask>", space             
            else:                                               # ipv4
                return '10.0.0.1', f"<{branch}>", space                
        elif 'XX.YY' in branch:
            return '11.11', branch if re.match(r'<.*>', branch) else f"<{branch}>", space
        elif 'XX.XXXX...' == branch:
            return '11:1111', f"<{branch}>", space
        elif '<0x0-0xFFFFFFFF>' == branch:
            return '0x0', branch, space
        elif '<0-0>' == branch:
            return '0', branch, space
        elif 'H.H.H' == branch:                                 # mac
            return '1.1.1', f"<{branch}>", space
        elif 'N.H.H.H' == branch:
            return '1.1.1.1', f"<{branch}>", space
        elif 'N.H' == branch:
            return '10.1', f"<{branch}>", space
        elif 'N:H' == branch:
            return '1:1', f"<{branch}>", space
        elif 'aa:nn' == branch:
            return '11:00', f"<{branch}>", space
        elif 'hh:mm' == branch:
            return '11:11', f"<{branch}>", space
        elif 'X.121 Addr' == branch:
            return '460812345678', f"<{branch}>", space
        elif 'Start-End' == branch:
            return '10-20', f"<{branch}>", space
        elif branch in ['Hex-string', 'Hex-data']:
            return '000000000001', f"<{branch}>", space
        elif 'ASN:nn or IP-address:nn' == branch:
            return '65001:100', f"<{branch}>", space
        elif 'hh:mm:ss' == branch:
            return '1:1:1', f"<{branch}>", space
        elif 'R/S/I/P' in branch:                               # hardware
            return '0/0/0/0', f"<{branch}>", space
        elif 'MONTH' == branch:
            return 'Jan', '<MONTH>', space
        elif 'WORD' == branch:                                  # 
            if 'format string' in desc:
                return r'"%s"', f"<{branch}>", space
            elif 'seperator' in desc:
                return ':', f"<{branch}>", space
            elif 'hex digits' in desc:
                search = re.search(r'(\d+) hex digits', desc)
                return f"{'1'*int(search.group(1))}", f"<{branch}>", space
            else:  
                rand = ''.join(random.sample(string.ascii_letters, 4))
                instance = 'word' + rand
                return instance, f"<{branch}>", space
        else:                                                   
            return branch, branch, space

    def remove_bgp_process(self, process_cmd: str):
        """Remove a temporary IOS BGP process and leave config mode ready."""
        self.conn.write_channel('\x15')
        self.send_command(f'no {process_cmd}', cmd_verify=False)
        
    
    def into_last_view(self, cmd: str, view: str):
        for _ in range(12):
            self.send_command('exit', cmd_verify=False) 
            if self.get_view() == view:
                break
        else:
            raise ReadTimeout(f"Unable to return to Cisco view {view}.")
        self.conn.write_channel(cmd)

    def search_command(self, cmd) -> str:
        return self._send_command_with_recovery(
            f"{cmd}?", '#', normalize=False
        )

    def send_command(self, instance, cmd_verify=True, normalize=True) -> str:
        return self._send_command_with_recovery(
            instance,
            r'#|]',
            cmd_verify=cmd_verify,
            normalize=normalize,
            retry=False,
        )
    



class Xrv9kModel(CiscoModel):
    def __init__(self, name=None):
        super().__init__()
        self.os = 'IOS-XR'
        NODE = {
            "name": name if name else 'xrv9k',
            "template": 'xrv9k',
            "image": 'xrv9k-fullk9-7.7.1',
            "ethernet": 7,
            "ram": 16384,
            "cpu": 4
        }
        if self.lab.find_node(NODE['name']):
            print(f"\"{NODE['name']}\" existed")
        else:
            self.lab.client.api.add_node(self.lab.path, **NODE)
            print(f"\"{NODE}\" created")

        DEVICE = {
            "device_type": "cisco_xr_telnet",               # 指定 Telnet 驱动
            "host": HOST,
            "username": 'cisco', 
            "password": '111111',
            "port": self.lab.get_port(NODE['name']),
            "timeout": 120,
            "default_enter": '\n',
            "session_log": f"{LOG_PATH}/{COMMAND}.log",
            "fast_cli": False,
            "read_timeout_override": 300
        }
        self.conn = ConnectHandler(**DEVICE)
        self.PRE_PROMPT = 'RP/0/RP0/CPU' # 'RP/0/RP0/CPU0'

        ['BVI', 'Bundle-Ether', 'Bundle-POS', 'EightHundredGigE', 'FastEthernet', 
         'FiftyGigE', 'FortyGigE', 'FourHundredGigE', 'GigabitEthernet', 'HundredGigE', 
         'Loopback', 'MgmtEth', 'Multilink', 'Null', 'SRP', 'Serial', 'TenGigE', 
         'TwentyFiveGigE', 'TwoHundredGigE', 'lpts', 'nve', 'preconfigure', 'tunnel-ip', 
         'tunnel-ipsec', 'tunnel-mte', 'tunnel-te', 'tunnel-tp']


        self.OMIT_FLDS_TEST.extend( [# skip anywhere
            # 'template',
            '0/0/0/1', '0/0/0/2', '0/0/0/3',
            'BVI', 'Bundle-POS',
            'EightHundredGigE', 'FastEthernet', 'FiftyGigE', 'FortyGigE', 'FourHundredGigE', 'HundredGigE', 
            'Multilink','SRP', 'Serial', 'TenGigE', 'TwentyFiveGigE', 'TwoHundredGigE',
            'lpts', 'nve', 'preconfigure',
            'tunnel-ipsec', 'tunnel-mte', 'tunnel-te', 'tunnel-tp'
            'describe', 
            # 'apply-group', 'apply-group-append', 'apply-group-remove',
        ] )
        # self.conn.enable()    
        # self.conn.disable_paging()

        # commit replace
        if PRE_CONF:
            PRE_CMDS = ["config"]   #, 'router bgp 1', 'address-family ipv4 unicast'】
            for cmd in PRE_CMDS:
                self.send_command(cmd)


class XrvModel(CiscoModel):
    def __init__(self, name=None):
        super().__init__()
        self.os = 'IOS-XR'
        NODE = {
            "name": name if name else 'xrv',
            "template": 'xrv',
            "image": 'xrv-6-3-1-cml',
            "ethernet": 4,
            "ram": 3072,
            "cpu": 1
        }
        if self.lab.find_node(NODE['name']):
            print(f"\"{NODE['name']}\" existed")
        else:
            self.lab.client.api.add_node(self.lab.path, **NODE)
            print(f"\"{NODE['name']}\" created")
        DEVICE = {
            "device_type": "cisco_xr_telnet",               
            "host": HOST,
            "port": self.lab.get_port(NODE['name']),
            "username": 'cisco', 
            "password": 'cisco',
            "timeout": 120,
            "default_enter": '\n',
            "session_log": f"{LOG_PATH}/{COMMAND}.log",
            "fast_cli": False,
            "read_timeout_override": 300
        }
        self.conn = ConnectHandler(**DEVICE)
        self.PRE_PROMPT = 'RP/0/0/CPU0'
        # self.conn.enable()    
        # self.conn.disable_paging()
        self.OMIT_FLDS_TEST = [# skip anywhere
            # 'template',
            '0/0/0/1', '0/0/0/2', '0/0/0/3',
            'CEM', 'EightHundredGigE', 'FastEthernet', 'FiftyGigE', 'FortyGigE', 'FourHundredGigE', 'HundredGigE', 'IMA', 'TwentyFiveGigE', 'TwoHundredGigE',
            'BVI', 'Bundle-Ether', 'Bundle-POS', 'SRP', 'lpts', 'Multilink', 'nve', 'tunnel-ipsec', 'tunnel-mte', 'tunnel-te', 'tunnel-tp',
            'tunnel-ip', 'TenGigE', 'PW-IW', 'PW-Ether', 'POS',
            'help',
            # 'apply-group', 'apply-group-append', 'apply-group-remove',
            'Failed','UNKNOWN', '\'cfg', #'redistribute', #'topology',
            '(', ')'
        ]

        if PRE_CONF:
            PRE_CMDS = ["config"]   #, 'router bgp 1', 'address-family ipv4 unicast'
            for cmd in PRE_CMDS:
                self.send_command(cmd)
    

class IosModel(CiscoModel):
    def __init__(self, name=None):
        super().__init__()
        self.os = 'IOS'
        NODE = {
            "name": name if name else 'R',
            "template": 'R',
            # "image": 'vios-adventerprisek9-m.spa.159-3.m10',
            "image": 'l3-AdvEnterpriseK9-M2_157_3_May_2018.bin',
            "ethernet": 4,
            "ram": 3072,
            "cpu": 1
        }
        if self.lab.find_node(NODE['name']):
            print(f"\"{NODE['name']}\" existed")
        else:
            self.lab.client.api.add_node(self.lab.path, **NODE)
            print(f"\"{NODE['name']}\" created")
        DEVICE = {
            "device_type": "cisco_ios_telnet",               
            "host": HOST,
            "port": self.lab.get_port(NODE['name']),
            "username": 'cisco', 
            "password": 'cisco',
            "timeout": 120,
            "default_enter": '\n',
            "session_log": f"{LOG_PATH}/{COMMAND}.log",
            "fast_cli": False,
            "read_timeout_override": 300
        }
        self.conn = ConnectHandler(**DEVICE)
        self.PRE_PROMPT = 'Router'
        # try:
        #     # Keep asynchronous notifications out of help responses.
        #     self.send_command('terminal no monitor', cmd_verify=False)
        # except (ReadTimeout, OSError, ValueError) as exc:
        #     print(f'! terminal no monitor failed: {type(exc).__name__}: {exc}')
        # self.conn.enable()    
        # self.conn.disable_paging()
        self.OMIT_FLDS_TEST.extend( [# skip anywhere
            # 'template',
            # '0/0/0/1', '0/0/0/2', '0/0/0/3',
            'Async', 'Auto-Template', 'BDI', 'BVI', 'CDMA-Ix', 'CTunnel', 'Dialer', 
            'GMPLS', 'Group-Async', 'LISP', 'LongReachEthernet', 'Lspvif', 'MFR', 'Multilink',
            'Pseudowire', 'Vif', 'Virtual-PPP', 'Virtual-Template', 'Virtual-TokenRing',
            'vmi',
            # 'apply-group', 'apply-group-append', 'apply-group-remove',
        ] )

        if PRE_CONF:
            # stop log: no logging console
            # Router(config)#line vty 0 4
            # Router(config-line)#logging synchronous
            # backup: copy running-config startup-config; <ENTER>
            PRE_CMDS = ["enable", "configure replace nvram:startup-config", "Y", "Y", "configure terminal"] 
            # PRE_CMDS = ["enable", "configure replace nvram:startup-config", "Y", "configure terminal"]
            for cmd in PRE_CMDS:
                self.send_command(cmd)

    def send_command_file(self, config_file: str):
        primitive = ["enable", "configure terminal"]
        for cmd in primitive:
            self.send_command(cmd)

        with open(config_file, "rt", encoding="utf-8") as cfg_file:
            commands = cfg_file.readlines()
        revised_cmds = [line.strip() for line in commands if not re.match(r"^\s*(!|#)", line)]
        self.conn.send_config_set(revised_cmds)


class CsrModel(CiscoModel):
    def __init__(self, name=None):
        super().__init__()
        self.os = 'IOS-XE'
        NODE = {
            "name": name if name else 'CSR',
            "template": 'C8K',
            # "image": 'csr1000vng-170304a-cml',
            "image": 'c8000v-17-06-01a-cml',
            "ethernet": 4,
            "ram": 4096,
            "cpu": 2
        }
        if self.lab.find_node(NODE['name']):
            print(f"\"{NODE['name']}\" existed")
        else:
            self.lab.client.api.add_node(self.lab.path, **NODE)
            print(f"\"{NODE['name']}\" created")
        DEVICE = {
            "device_type": "cisco_ios_telnet",               
            "host": HOST,
            "port": self.lab.get_port(NODE['name']),
            "username": 'cisco', 
            "password": 'cisco',
            "timeout": 120,
            "default_enter": '\n',
            "session_log": f"{LOG_PATH}/{COMMAND}.log",
            "fast_cli": False,
            "read_timeout_override": 300
        }
        self.conn = ConnectHandler(**DEVICE)
        self.PRE_PROMPT = 'Router'
        # self.conn.enable()    
        # self.conn.disable_paging()
        self.OMIT_FLDS_TEST = [# skip anywhere
            # 'template',
            'ACR', 'ATM-ACR', 'Analysis-Module', 'AppNav-Compress', 'AppNav-UnCompress', 
            'Async', 'Auto-Template', 'BD-VIF', 'BDI', 'BVI', 'Bluetooth', 'CDMA-Ix', 
            'CEM-ACR', 'CEM-PG', 'CTunnel', 'Container', 'Dialer', 'EsconPhy', 
            'Ethernet-Internal', 'Fcpa', 'Filter', 'Filtergroup', 'GMPLS', #'GigabitEthernet', 
            'Group-Async', 'IMA-ACR', 'LISP', 'LongReachEthernet', 'Lspvif', #'Loopback', 
            'MFR', 'Multilink', 'NVI', 'Null', 'Overlay', 'PROTECTION_GROUP', 'Port-channel', 
            'Portgroup', 'Pos-channel', 'SBC', 'SDH_ACR', 'SERIAL-ACR', 'SONET_ACR', 
            'SSLVPN-VIF', 'SYSCLOCK', 'Serial-PG', 'Service-Engine', 'TLS-VIF', 'Tunnel', 
            'Tunnel-tp', 'VPN', 'Vif', 'Vir-cem-ACR', 'Virtual-PPP', 'Virtual-Template', 
            'Virtual-TokenRing', 'VirtualPortGroup', 'Vlan', 'multiservice', 'nve', 
            'pseudowire', 'range', 'ucse', 'vasileft', 'vasiright', 'vmi', 'voaBypassIn', 
            'voaBypassOut', 'voaFilterIn', 'voaFilterOut', 'voaIn', 'voaOut',
            'af11', 'af12', 'af13', 'af21', 'af22', 'af23', 'af31', 'af32', 'af33', 'af41', 'af42', 'af43',
            'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6', 'cs7', 
            # 'apply-group', 'apply-group-append', 'apply-group-remove',
            #'redistribute', #'topology',
            '(', ')'
        ]
        
        if PRE_CONF:
            # no log: no logging console
            # backup: copy running-config startup-config; <ENTER>
            # PRE_CMDS = ["enable", "configure replace nvram:startup-config", "Y", "Y", "configure terminal", 'interface g 1'] 
            PRE_CMDS = ["enable", "configure replace nvram:startup-config", "Y",  "configure terminal"]
            for cmd in PRE_CMDS:
                self.send_command(cmd)


    def if_send(self, templ: str):
        if re.match(r"default .*", templ):
            return False
        elif re.match(r"exit.*", templ):
            return False
        else:
            return CROSS
        
    def send_command_file(self, config_file: str):
        primitive = ["enable", "configure terminal"]
        for cmd in primitive:
            self.send_command(cmd)

        with open(config_file, "rt", encoding="utf-8") as cfg_file:
            commands = cfg_file.readlines()
        revised_cmds = [line.strip() for line in commands if not re.match(r"^\s*(!|#)", line)]
        self.conn.send_config_set(revised_cmds)



#############################################################################################################################
# Huawei
#############################################################################################################################
class HuaweiModel(DeviceModel):
    def __init__(self):
        super().__init__()
        self.vendor = 'Huawei'
        self.END = '<cr>'
        self.PRE_PROMPT = 'view commands:'

        self.OMIT_FLDS = [
            'display', 'mtrace',
            'ping', 'quit',
            'return', 'rollback', 'save', 'screen-width', 'tracert',
            'undo'
        ]
        self.OMIT_FLDS_TEST = []

    def add_command(self, cmd: str):
        """
        Add command without enter
        """
        self.conn.write_channel(cmd)

    def echo2dict(self, echo: str, templ: str):
        if self.PRE_PROMPT in echo:            # prompt when new view occur
            echo = echo.rpartition(self.PRE_PROMPT)[-1]
        return super().echo2dict(echo, templ)

    def detect_error(self, echo: str) -> bool:
        return True if 'Error:' in echo else False

    def get_instance(self, branch: str, desc: str, space: str) -> tuple[str, str, str]:
        match_scope = re.search(r'<(\d+)-(\d+)>', branch)
        if 'asdot format' in desc:
            return '1.1', branch, space
        elif match_scope:                                         
            min = int(match_scope.group(1))
            max = int(match_scope.group(2)) 
            if 'INTEGER' in branch:                            # 为带范围的参数
                instance = str(self.randn(min, max, 65535))     # 限制长度
            elif 'STRING' in branch:                           # 为字符串
                str_num = self.randn(min, max, 7)               # 限制长度
                instance = ''.join(random.sample(string.ascii_letters, str_num))
            elif '<0-0>' == branch:
                return '0/0/0', branch, space
            else:
                raise ValueError('Unexpeted Param')
            return instance, branch, space          
        # elif 'x:x::x:x<X:X::X:X>' in branch:                    # 为ipv6地址
        elif 'X:X::X:X' in branch:
            ip = f"{self.randn(1, 9999)}:{self.randn(1, 9999)}::{self.randn(1, 9999)}:{self.randn(1, 9999)}"
            return ip, branch, space                     
        elif 'X.X.X.X' in branch:
            if 'mask' in desc.lower():                          # 为ipv4地址的掩码
                return "255.255.255.0", branch, space             
            else:                                               # 为ipv4地址 
                ip = f"{self.randn(1, 255)}.{self.randn(1, 255)}.{self.randn(1, 255)}.{self.randn(1, 255)}"
                return ip, branch, space                
        elif 'MAC_ADDR<XXXX-XXXX-XXXX>' in branch:              # 为mac地址
            mac = f"{self.randn(1000, 9999)}-{self.randn(1000, 9999)}-{self.randn(1000, 9999)}"
            return mac, branch, space
        elif 'XXXX.XXXX.XXXX' in branch:
            id = f"{self.randn(1000, 9999)}.{self.randn(1000, 9999)}.{self.randn(1000, 9999)}"
            return id, branch, space
        elif 'HEX' == branch:
            return 'a', branch, space
        elif 'HEX<0x...><0x0,0xffff>' in branch:                # 为16进制
            hex = f"0x{self.randn(1, 9999)}"
            return hex, branch, space
        elif 'XX.XXXX. ... .XXXX.XX' == branch:
            return '11.1111.1111.1111.1111.00', branch, space
        else:                                                   # 为关键词
            return branch, branch, space


    def get_view(self) -> str:
        """
        返回带[]的视图名称
        """
        view = self.conn.find_prompt()
        delay_factor = self.conn.select_delay_factor(1)
        sleep_time = delay_factor * 0.25
        self.conn.clear_buffer()
        self.conn.write_channel('\n')
        time.sleep(sleep_time)
        prompt = self.conn.read_channel().strip()
        count = 0
        while count <= 12 and not prompt:
            if not prompt:
                self.conn.write_channel('\n')
                time.sleep(sleep_time)
                prompt = self.conn.read_channel().strip()
                if sleep_time <= 3:
                    # Double the sleep_time when it is small
                    sleep_time *= 2
                else:
                    sleep_time += 1
            count += 1


        if not prompt:
            raise ValueError(f"Unable to find prompt: {prompt}")
        view = prompt.split('\n')[-1]
        view = view.strip()
        
        # if detect_error:
        #     if ''

        if re.search(r'\[.*?\]', view):
            return view
        elif re.search(r'<.*?>', view):
            return "[ROOT]" 
        else:
            raise ValueError("Unexpected Prompt")
        
    def into_last_view(self, cmd: str, view: str):
        while True:
            self.send_command('quit', cmd_verify=False)       
            if self.get_view() == view:
                break
        
        self.conn.write_channel(cmd)
        

    def process_complete_cmd(self, cmd: str):
        # echo = self.send_command('undo ' + cmd)
        # if "[Y/N]" in echo:
        #     self.send_command('Y')
        super().process_complete_cmd(cmd)
    
    def search_command(self, cmd) -> str:
        return self.conn.send_command(f"{cmd}?", r'\[.*?\]', cmd_verify=False, normalize=False)
        

    def send_command(self, instance, cmd_verify=True, normalize=True) -> str:
        return self.conn.send_command(instance, r'\[.*?\]|\(.*?\)', cmd_verify=cmd_verify, normalize=normalize)



class ArvModel(HuaweiModel):
    def __init__(self, name=None):
        super().__init__()
        NODE = {
            "name": name if name else 'AR1000v',
            "template": 'AR1000v',
            "image": 'huaweiar1k-5.170-V300R021C00SPC100T-Auto-update-esn',
            "ethernet": 6,
            "ram": 2048,
            "cpu": 1
        }
        if self.lab.find_node(NODE['name']):
            print(f"\"{NODE['name']}\" existed")
        else:
            self.lab.client.api.add_node(self.lab.path, **NODE)
            print(f"\"{NODE['name']}\" created")

        DEVICE = {
            "device_type": "huawei_telnet",               # 指定 Telnet 驱动
            "host": HOST,
            "port": self.lab.get_port(NODE['name']),
            "username": 'test',
            "password": '111111AA',
            "timeout": 5,
            "default_enter": '\n',
            "session_log": f"{LOG_PATH}/{COMMAND}.log",
            "fast_cli": False,
            "read_timeout_override": 300
        }
        self.conn = ConnectHandler(**DEVICE)
        # self.conn.enable()    
        # self.conn.disable_paging()

        if PRE_CONF:
            # To stop autoconfig: undo autoconfig enable; q; save
            # To save the configuration: save backup.cfg
            PRE_CMDS = ["startup saved-configuration backup.cfg", "system-view", "user-interface console 0", "screen-length 0", "screen-width 511", "y", "q"]
            # PRE_CMDS = ["startup saved-configuration backup.cfg", "system-view", "user-interface console 0", "screen-length 0", "screen-width 511", "y", "q", "bgp 1"]
            # PRE_CMDS = ["system-view", "user-interface console 0", "screen-length 0", "screen-width 511", "y", "q"]
            # 【预处理】
            for cmd in PRE_CMDS:
                self.send_command(cmd)

    def send_command_file(self, config_file: str):
        # primitive = ["enable", "configure terminal"]
        # for cmd in primitive:
        #     self.send_command(cmd)

        with open(config_file, "rt", encoding="utf-8") as cfg_file:
            commands = cfg_file.readlines()
        revised_cmds = [line.strip() for line in commands if not re.match(r"^\s*(!|#)", line)]
        self.conn.send_config_set(revised_cmds)


class CE12800Model(HuaweiModel):
    def __init__(self, name=None):
        super().__init__()
        NODE = {
            "name": name if name else 'CE12800-CE',
            "template": 'CE12800-CE',
            "image": 'huaweice12800-V200R005C10SPC607B607-EmulatedLab-v4',
            "ethernet": 12,
            "ram": 2048,
            "cpu": 2
        }
        if self.lab.find_node(NODE['name']):
            print(f"\"{NODE['name']}\" existed")
        else:
            self.lab.client.api.add_node(self.lab.path, **NODE)
            print(f"\"{NODE['name']}\" created")

        DEVICE = {
            "device_type": "huawei_telnet",               # 指定 Telnet 驱动
            "host": HOST,
            "port": self.lab.get_port(NODE['name']),
            "timeout": 5,
            "default_enter": '\n',
            "session_log": f"{LOG_PATH}/{COMMAND}.log",
            "fast_cli": False,
            "read_timeout_override": 300
        }
        self.conn = ConnectHandler(**DEVICE)
        # self.conn.enable()    
        # self.conn.disable_paging()
        if PRE_CONF:
            PRE_CMDS = ["startup saved-configuration backup.cfg", "system-view", "user-interface console 0", "screen-length 0", "screen-width 511", "y", "q"]
            # 【预处理】
            for cmd in PRE_CMDS:
                self.send_command(cmd)
    
    
        

#############################################################################################################################
# Juniper
#############################################################################################################################
class JuniperModel(DeviceModel):
    def __init__(self):
        super().__init__()
        self.vendor = 'Juniper'
        self.END = '<[Enter]>'
        self.PRE_PROMPT = 'Possible completions:'

        self.OMIT_FLDS = [# 开头出现直接跳过，允许中途出现(Only allow edit/set to be the beginning)
            'activate', 'annotate', 'commit', 'copy', 'deactivate', 'delete', 
            'exit', 'extension', 'help', 'insert', 'load', 'prompt', 'protect', 
            'quit', 'rename', 'replace', 'rollback', 'run', 'save', 'show',
            'status', 'top', 'unprotect', 'up', 'wildcard',
            'edit'
        ]
        self.OMIT_FLDS_TEST = ['|', '&&', '||', '!', '(', ')', '[', ']']
        # self.OMIT_FLDS_TEST = ['|']

    def add_command(self, cmd: str):
        """
        Add command without enter
        """
        self.conn.write_channel(cmd)
    
    def echo2dict(self, echo, templ: str):
        new_branches = dict()

        if self.PRE_PROMPT in echo:            # 进入新视图时会有一个prompt
            echo = echo.rpartition(self.PRE_PROMPT)[-1]

        match_list = re.search(r'^(.+)\n\[.+\]', echo, re.DOTALL)
        if match_list:
            echo = match_list.group(1)

        if 'No valid completions' in echo:
            return echo, new_branches
        
        echo, branches = super().echo2dict(echo, templ)
        for field in branches.keys():
            match_container = re.match(r'^> (.+)', field)
            match_group = re.match(r'\+ (.+)', field)
            if match_container:
                new_branches[match_container.group(1)] = '> ' + branches[field]
            elif match_group:                    # +后面是可重复的字段 暂时跳过
                continue
                key = match_group.group(1)
                if key+' ' not in templ:        # 若未重复出现
                    new_branches[key] = '+ ' + branches[field]
                else:
                    new_branches[match_group.group(1)] = '+ ' + branches[field]
            else:
                new_branches[field] = branches[field]

        return echo, new_branches


    def detect_error(self, echo: str) -> bool:
        return True if 'Error:' in echo else False

    def get_instance(self, branch: str, desc: str, space: str) -> tuple[str, str, str]:
        if re.match(r'<.+>', branch):
            match_integer = re.search(r'\((\d+)..(\d+)', desc)
            match_time = re.search(r'\(YYYY-MM-DD', desc)
            if match_integer:
                min = int(match_integer.group(1))
                max = int(match_integer.group(2)) 
                instance = str(self.randn(min, max, 255))           # 限制长度
                return instance, branch, space
            elif match_time:
                return '2026-1-1', branch, space
            elif 'mac-address' in branch:
                return '00:11:22:33:44:55', branch, space
            elif 'addr' in branch:
                ip = f"{self.randn(1, 255)}.{self.randn(1, 255)}.{self.randn(1, 255)}.{self.randn(1, 255)}"
                return ip, branch, space
            elif any(item==branch for item in ['<neighbor-sysid>', '<remote-node-iso>']):
                return '1111.1111.1111', branch, space
            elif '<net-iso>' == branch:
                return '49.0001.1921.6800.1001.00', branch, space
            elif 'BGP community identifier' in desc:
                return '65001:100', branch, space
            
            elif '<sid>' == branch or any(n in branch+desc for n in ['name']):
                instance = ''.join(random.sample(string.ascii_letters, 4))
                return 'word'+instance, branch, space
            
            elif branch in ['<micro-sid-value>', '<metric_value>', '<metric>', '<tag>'] or any(n in branch+desc for n in ['second', 'time', 'offset', 'identifier', 'bit', 'preference', 'id', 'number']):
                instance = str(self.randn(1, 60))
                return instance, branch, space
            
            else:                                                    
                instance = ''.join(random.sample(string.ascii_letters, 4))
                return 'word'+instance, branch, space

        else:                                                   # 为关键词
            return branch, branch, space


    def get_view(self) -> str:
        """
        返回带[]的视图名称
        """
        view = self.conn.find_prompt()
        delay_factor = self.conn.select_delay_factor(1)
        sleep_time = delay_factor * 0.25
        self.conn.clear_buffer()
        self.conn.write_channel('\n')
        time.sleep(sleep_time)
        prompt = self.conn.read_channel().strip()
        count = 0
        while count <= 12 and not prompt:
            if not prompt:
                self.conn.write_channel('\n')
                time.sleep(sleep_time)
                prompt = self.conn.read_channel().strip()
                if sleep_time <= 3:
                    # Double the sleep_time when it is small
                    sleep_time *= 2
                else:
                    sleep_time += 1
            count += 1
        if not prompt:
            raise ValueError(f"Unable to find prompt: {prompt}")
        
        view = prompt.split('\n')[0]
        view = view.strip()

        if re.search(r'\[.*?\]', view):
            return view
        elif re.search(r'<.*?>', view):
            return "[ROOT]" 
        else:
            raise ValueError("Unexpected Prompt")
        
    def if_send(self, templ: str):
        if 'edit ' in templ:                   # 只有edit开头的enter才是视图跳转
            return CROSS and True
        else:
            return False

    
    def into_last_view(self, cmd: str, view: str):
        while True:
            self.send_command('quit', cmd_verify=False)       
            if self.get_view() == view:
                break
        self.conn.write_channel(cmd)
        

    def process_complete_cmd(self, cmd: str):
        # echo = self.send_command('undo ' + cmd)
        # if "[Y/N]" in echo:
        #     self.send_command('Y')
        super().process_complete_cmd(cmd)
    
    def search_command(self, cmd) -> str:
        return self.conn.send_command(f"{cmd}?", '#', cmd_verify=False, normalize=False)
        # echo = self.conn.send_command(f"{cmd}", '#', cmd_verify=False, normalize=False)
        # if self.detect_error(echo):
        #     raise ValueError("Invalid")
        # else:
        #     return self.conn.send_command("?", '#', cmd_verify=False, normalize=False)

    def send_command(self, instance, cmd_verify=True, normalize=True) -> str:
        return self.conn.send_command(instance, '#', cmd_verify=cmd_verify, normalize=normalize)



class cRPDModel(JuniperModel):
    def __init__(self, name=None):
        super().__init__()
        NODE = {
            "name": name if name else 'cRPD',
            "template": 'cRPD',
            "image": 'crpd-23.4R2-S4.11',
            "ethernet": 8,
            "ram": 4096,
            "cpu": 2
        }
        if self.lab.find_node(NODE['name']):
            print(f"\"{NODE['name']}\" existed")
        else:
            self.lab.client.api.add_node(self.lab.path, **NODE)
            print(f"\"{NODE['name']}\" created")

        DEVICE = {
            "device_type": "juniper_junos_telnet",               # 指定 Telnet 驱动
            "host": HOST,
            "port": self.lab.get_port(NODE['name']),
            "username": 'root',
            "password": 'clab123',
            "timeout": 5,
            "default_enter": '\n',
            "session_log": f"{LOG_PATH}/{COMMAND}.log",
            "fast_cli": False,
            "read_timeout_override": 300
        }
        self.conn = ConnectHandler(**DEVICE)
        # self.conn.enable()    
        # self.conn.disable_paging()

        if PRE_CONF:
            PRE_CMDS = ["configure", 'rollback 0']
            # 【预处理】
            for cmd in PRE_CMDS:
                self.send_command(cmd)




if __name__ == "__main__":
    model = CE12800Model()
