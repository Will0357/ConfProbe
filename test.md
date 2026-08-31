# 手册中存在模板
## 模板语法错误
### BGP
> **<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">site-of-originspan></font>****<font style="color:rgb(88, 88, 91);"> </font>****<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">[</font>**_**<font style="color:rgb(88, 88, 91);">as-number:nn | ip-address:nn</font>**_**<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">]</font>**
>

> **<font style="color:rgb(88, 88, 91);">address-family</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">{</font>**<font style="color:rgb(88, 88, 91);">ipv4</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">{</font>**<font style="color:rgb(88, 88, 91);">labeled-unicast</font>**<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);">multicast</font>**<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);">unicast</font>**<font style="color:rgb(88, 88, 91);">} | </font>**<font style="color:rgb(88, 88, 91);">ipv6</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">{</font>**<font style="color:rgb(88, 88, 91);">unicast</font>**<font style="color:rgb(88, 88, 91);">} | </font>**<font style="color:rgb(88, 88, 91);">l2vpn vpls-vpws</font>**<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);">vpnv4 </font>**<font style="color:rgb(88, 88, 91);">{</font>**<font style="color:rgb(88, 88, 91);"> unicast</font>**<font style="color:rgb(88, 88, 91);">} | </font>**<font style="color:rgb(88, 88, 91);">vpnv6 {unicast</font>****<font style="color:#DF2A3F;"> | </font>****<font style="color:rgb(88, 88, 91);">}</font>**<font style="color:rgb(88, 88, 91);">}</font>
>

### ISIS
> **<font style="color:rgb(88, 88, 91);">data-plane</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">segment-routing</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">| </font>**<font style="color:rgb(88, 88, 91);">ip</font>**
>

## 模板缺少范围限制，只能从镜像中得知
## 手册表达方式的局限
1. 不同地址族下有命令的差异，拆分出更细粒度的模板

> **<font style="color:rgb(88, 88, 91);">address-family</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">{</font>**<font style="color:rgb(88, 88, 91);">ipv4</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">{</font>**<font style="color:rgb(88, 88, 91);">labeled-unicast</font>**<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);">multicast</font>**<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);">unicast</font>**<font style="color:rgb(88, 88, 91);">} | </font>**<font style="color:rgb(88, 88, 91);">ipv6</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">{</font>**<font style="color:rgb(88, 88, 91);">unicast</font>**<font style="color:rgb(88, 88, 91);">} | </font>**<font style="color:rgb(88, 88, 91);">l2vpn vpls-vpws</font>**<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);">vpnv4 </font>**<font style="color:rgb(88, 88, 91);">{</font>**<font style="color:rgb(88, 88, 91);"> unicast</font>**<font style="color:rgb(88, 88, 91);">} | </font>**<font style="color:rgb(88, 88, 91);">vpnv6 {unicast</font>****<font style="color:#DF2A3F;"> | </font>****<font style="color:rgb(88, 88, 91);">}</font>**<font style="color:rgb(88, 88, 91);">}</font>
>

2. 缺视图

> **<font style="color:rgb(88, 88, 91);">address-family ipv4</font>**<font style="color:rgb(88, 88, 91);"> { </font>**<font style="color:rgb(88, 88, 91);">apply-group </font>**_<font style="color:rgb(88, 88, 91);">group-name</font>_<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">exclude-group</font>****<font style="color:rgb(88, 88, 91);"> </font>**_<font style="color:rgb(88, 88, 91);">group-name</font>_<font style="color:rgb(88, 88, 91);"> } 可在 mpls/global视图下</font>[https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/mpls/command/reference/b-mpls-cr-asr9000/mpls-oam-commands.html?bookSearch=true](https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/mpls/command/reference/b-mpls-cr-asr9000/mpls-oam-commands.html?bookSearch=true)；[https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/system_management/command/reference/b-system-managment-cr-asr9000/configuration-management-commands.html?dtid=osscdc000283&linkclickid=srch#wp3145726977](https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/system_management/command/reference/b-system-managment-cr-asr9000/configuration-management-commands.html?dtid=osscdc000283&linkclickid=srch#wp3145726977)
>

## 手册编排/不连续性/高耦合性
### BGP
> **<font style="color:rgb(88, 88, 91);">手册写bgp nexthop resolution </font>****<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">allow-default</font>**
>
> **<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">实际</font>****<font style="color:rgb(88, 88, 91);">nexthop resolution </font>****<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">allow-default</font>**
>

### ISIS
> <font style="background-color:#FBDE28;">routing cr:</font> **<font style="color:rgb(88, 88, 91);">link-group</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">link-group-name</font>_
>
> <font style="background-color:#FBDE28;">routing cg:  </font>_ _
>
> **<font style="color:rgb(88, 88, 91);">link-group </font>**_<font style="color:rgb(88, 88, 91);">link-group-name</font>_<font style="color:rgb(88, 88, 91);"> { </font>**<font style="color:rgb(88, 88, 91);">[ metric-offset </font>**_<font style="color:rgb(88, 88, 91);">count</font>_<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);">maximum</font>**<font style="color:rgb(88, 88, 91);"> ] | [</font>**<font style="color:rgb(88, 88, 91);"> minimum-members</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">count</font>_<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);">revert-members</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">count</font>_<font style="color:rgb(88, 88, 91);"> ] }</font>
>
> **<font style="color:rgb(88, 88, 91);">link-group </font>**_<font style="color:rgb(88, 88, 91);">link-group-name</font>_<font style="color:rgb(88, 88, 91);"> [ </font>**<font style="color:rgb(88, 88, 91);">level</font>**<font style="color:rgb(88, 88, 91);"> { </font>**<font style="color:rgb(88, 88, 91);">1</font>**<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);">2</font>**<font style="color:rgb(88, 88, 91);"> } ]</font>
>

## 手册缺少命令分支
### BGP
> **<font style="color:rgb(88, 88, 91);">advertise</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">local-labeled-route</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">safi-unicast</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">disable -> </font>**<font style="color:rgb(88, 88, 91);">P: </font><font style="color:#DF2A3F;">[disable]</font>
>

> **<font style="color:rgb(88, 88, 91);">redistribute部分：</font>**
>
> **<font style="color:rgb(88, 88, 91);">redistribute application [metric </font>**_<font style="color:rgb(88, 88, 91);">metric-value</font>_**<font style="color:rgb(88, 88, 91);">] [route-policy </font>**_<font style="color:rgb(88, 88, 91);">route-policy-name</font>_**<font style="color:rgb(88, 88, 91);">]</font>**
>
> **<font style="color:rgb(88, 88, 91);">redistribute lisp [metric </font>**_<font style="color:rgb(88, 88, 91);">metric-value</font>_**<font style="color:rgb(88, 88, 91);">] [route-policy </font>**_<font style="color:rgb(88, 88, 91);">route-policy-name</font>_**<font style="color:rgb(88, 88, 91);">]</font>**
>
> **<font style="color:rgb(88, 88, 91);">redistribute mobile [metric </font>**_<font style="color:rgb(88, 88, 91);">metric-value</font>_**<font style="color:rgb(88, 88, 91);">] [route-policy </font>**_<font style="color:rgb(88, 88, 91);">route-policy-name</font>_**<font style="color:rgb(88, 88, 91);">]</font>**
>
> **<font style="color:rgb(88, 88, 91);">redistribute subscriber [metric </font>**_<font style="color:rgb(88, 88, 91);">metric-value</font>_**<font style="color:rgb(88, 88, 91);">] [route-policy </font>**_<font style="color:rgb(88, 88, 91);">route-policy-name</font>_**<font style="color:rgb(88, 88, 91);">]</font>**
>
> **<font style="color:rgb(88, 88, 91);">redistribute ospvv3 ...</font>**
>

> **<font style="color:rgb(88, 88, 91);">advertisement-interval</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">seconds P：advertisement-interval</font>_<font style="color:rgb(88, 88, 91);"> <seconds> [<seconds>](可能是一个update一个withdraw</font>_
>

> **<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">maximum-prefix</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">maximum</font>_<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">[</font>_<font style="color:rgb(88, 88, 91);">threshold</font>_<font style="color:rgb(88, 88, 91);">]</font><font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">[</font>**<font style="color:rgb(88, 88, 91);">warning-only</font>**<font style="color:rgb(88, 88, 91);">]</font><font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">[</font>**<font style="color:rgb(88, 88, 91);">restart</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">time-interval</font>_<font style="color:rgb(88, 88, 91);">] </font>
>
> **<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">maximum-prefix</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">maximum</font>_<font style="color:rgb(88, 88, 91);"> </font><font style="color:#DF2A3F;">[discard-extra-paths]</font><font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">[</font>_<font style="color:rgb(88, 88, 91);">threshold</font>_<font style="color:rgb(88, 88, 91);">]</font><font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">[</font>**<font style="color:rgb(88, 88, 91);">warning-only</font>**<font style="color:rgb(88, 88, 91);">]</font><font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">[</font>**<font style="color:rgb(88, 88, 91);">restart</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">time-interval</font>_<font style="color:rgb(88, 88, 91);">]</font>
>

> <font style="color:rgb(17, 24, 39);">egress-engineering -> egress-engineering [inheritance-disable]</font>
>

> **<font style="color:rgb(88, 88, 91);">attribute</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">large-community</font>**<font style="color:rgb(88, 88, 91);"> { </font>**<font style="color:rgb(88, 88, 91);">discard</font>**<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">treat-as-withdraw</font>**<font style="color:rgb(88, 88, 91);"> }</font><img src="https://cdn.nlark.com/yuque/0/2026/png/49996548/1778484044206-a1014267-77ba-4a35-afe1-e9cadea1148f.png" width="379" title="" crop="0,0,1,1" id="uce948c27" class="ne-image">
>

> <font style="color:rgb(17, 24, 39);background-color:rgb(251, 252, 254);">bgp multipath as-path ignore {</font><font style="color:#AD1A2B;background-color:rgb(251, 252, 254);">exact-match</font><font style="color:rgb(17, 24, 39);background-color:rgb(251, 252, 254);">|onwards}</font>
>

> **<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">prefix-sid</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">[ </font>**<font style="color:rgb(88, 88, 91);">strict-spf</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">] { </font>**<font style="color:rgb(88, 88, 91);">index</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">sid-index</font>_<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">| </font>**<font style="color:rgb(88, 88, 91);">absolute</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">sid-value</font>_<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">} [ </font>**<font style="color:rgb(88, 88, 91);">n-flag-clear</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">] [ </font>**<font style="color:rgb(88, 88, 91);">explicit-null</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">] </font><font style="color:#DF2A3F;">[</font>**<font style="color:#DF2A3F;">PHP-disable</font>**<font style="color:#DF2A3F;">]</font>
>
> <font style="color:#DF2A3F;">Disable Penultimate Hop Popping</font>
>

### ISIS
> **<font style="color:rgb(88, 88, 91);">distribute bgp-ls</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">[instance-id</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">value</font>_**<font style="color:rgb(88, 88, 91);">]</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">[level</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">{</font>**<font style="color:rgb(88, 88, 91);">1 </font>**<font style="color:rgb(88, 88, 91);">| </font>**<font style="color:rgb(88, 88, 91);">2</font>**<font style="color:rgb(88, 88, 91);">}</font>**<font style="color:rgb(88, 88, 91);">]</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">[throttle</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">time</font>_**<font style="color:rgb(88, 88, 91);">] -> P: [bgp-ls|link-state]</font>**
>

> **<font style="color:rgb(88, 88, 91);">trace</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">[</font>**<font style="color:rgb(88, 88, 91);">detailed</font>**<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);">severe</font>**<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);">standard</font>**<font style="color:rgb(88, 88, 91);">]</font><font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">max-trace-entries</font>_<img src="https://cdn.nlark.com/yuque/0/2026/png/49996548/1778570937979-1d013569-c0c4-40e7-863d-906e96111efc.png" width="150" title="" crop="0,0,1,1" id="hhyOl" class="ne-image">
>

> <font style="color:rgb(17, 24, 39);background-color:rgb(228, 238, 249);">fast-reroute per-prefix srlg-protection weighted-global [level <1-2>]</font><img src="https://cdn.nlark.com/yuque/0/2026/png/49996548/1778573054250-3c193051-16fc-4121-a760-b807d0f67b26.png" width="368.5" title="" crop="0,0,1,1" id="u25ce2dde" class="ne-image">
>

### OSPF
> <font style="color:rgb(0, 51, 102);background-color:rgb(255, 242, 189);">capability {opaque disable</font><font style="color:#AD1A2B;background-color:rgb(255, 242, 189);">|lls disable|type7 prefer</font><font style="color:rgb(0, 51, 102);background-color:rgb(255, 242, 189);">}</font>
>
> <font style="color:rgb(17, 24, 39);background-color:rgb(255, 242, 189);">shutdown </font><font style="color:#AD1A2B;background-color:rgb(255, 242, 189);">[on-reload|host-mode]</font>
>

### static
> <img src="https://cdn.nlark.com/yuque/0/2026/png/49996548/1778573624960-9b2e83a8-ed2a-4f94-b21b-26a23e276845.png" width="367.5" title="" crop="0,0,1,1" id="u051396a5" class="ne-image">
>

## 手册缺少支持的视图
### BGP
1. af-group

> **<font style="color:rgb(88, 88, 91);">accept-own</font>**<font style="color:rgb(88, 88, 91);"> [</font>**<font style="color:rgb(88, 88, 91);">inheritance-disable</font>**<font style="color:rgb(88, 88, 91);">] -- [neighbor vpn]</font>
>

2. af-group+neighbor-ipv46

> **<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">site-of-origin</font>****<font style="color:rgb(88, 88, 91);"> </font>****<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">[</font>**_**<font style="color:rgb(88, 88, 91);">as-number:nn | ip-address:nn</font>**_**<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">]</font>**
>

2. session-group

> **<font style="color:rgb(88, 88, 91);">neighbor</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">ip-address</font>_<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">internal-vpn-client [neighbor/vrf]</font>**
>

> **<font style="color:rgb(88, 88, 91);">idle-watch-time</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">number</font>_
>

3. vrf-neighbor

> **<font style="color:rgb(88, 88, 91);">attribute-filter</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">group</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">group-name </font>_<font style="color:rgb(88, 88, 91);">-- [router/neighbor]</font>
>

> **<font style="color:rgb(88, 88, 91);">bmp-activate</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">server</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">server-id</font>_<font style="color:rgb(88, 88, 91);"> -- [neighbor]</font>
>

> **<font style="color:rgb(88, 88, 91);">dscp</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">value -- </font>_<font style="color:rgb(88, 88, 91);">[neighbor/neighbor group/neighbor session group]</font>
>

> **<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">egress-engineering </font>**<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">-- [neighbor] </font>[https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/segment-routing/command/reference/b-seg-routing-cr-asr9k/m-segment-routing-command-reference.html?dtid=osscdc000283&linkclickid=srch#wp3657570492](https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/segment-routing/command/reference/b-seg-routing-cr-asr9k/m-segment-routing-command-reference.html?dtid=osscdc000283&linkclickid=srch#wp3657570492)
>

> **<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">ignore-connected-check</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">[</font>**<font style="color:rgb(88, 88, 91);">inheritance-disable</font>**<font style="color:rgb(88, 88, 91);">] -- [neighbor/neighbor group/neighbor session group]</font>
>

> **<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">keychain</font>**<font style="color:rgb(88, 88, 91);"> [</font>_<font style="color:rgb(88, 88, 91);">name </font>_<font style="color:rgb(88, 88, 91);">| </font>**<font style="color:rgb(88, 88, 91);">inheritance-disable</font>**<font style="color:rgb(88, 88, 91);">] -- [neighbor/neighbor group/neighbor session group]</font>
>

> **<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">precedence</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">value </font>_<font style="color:rgb(88, 88, 91);"> -- [neighbor/neighbor group/neighbor session group]</font>
>

> **<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">tcp</font>****<font style="color:rgb(88, 88, 91);"> mss inheritance-disable </font>**<font style="color:rgb(88, 88, 91);"> -- [neighbor/neighbor group/neighbor session group]</font>
>

4. vrf-neighbor-ipv46

> **<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">send-community-gshut-ebgp</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">[</font>**<font style="color:rgb(88, 88, 91);">inheritance-disable</font>**<font style="color:rgb(88, 88, 91);">] (send-extended-community-ebgp却表明了vrf）</font>
>

### ISIS
> **<font style="color:rgb(88, 88, 91);">segment-routing local-block </font>**_<font style="color:rgb(88, 88, 91);">starting_value</font>_<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">ending_value -- 【global config】</font>_
>

### OSPF
1. 少OSPF

> **<font style="color:rgb(88, 88, 91);">affinity-map</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">affinity name</font>_<font style="color:rgb(88, 88, 91);">{ </font>**<font style="color:rgb(88, 88, 91);">bit-position</font>**_<font style="color:rgb(88, 88, 91);">value</font>_<font style="color:rgb(88, 88, 91);"> } -- [ISIS]</font>
>

> <font style="color:rgb(17, 24, 39);background-color:rgb(251, 252, 254);">ucmp {prefix-list <WORD>|delay-interval <1-5000>|variance <101-10000>} -- [ISIS]</font>
>

# 手册中不存在模板
## 命令仅在示例中
### BGP
> bgp confederation peers<img src="https://cdn.nlark.com/yuque/0/2026/png/49996548/1778121715252-204a53ec-d5fe-4fcd-b2f4-65eb81381edc.png?x-oss-process=image%2Fcrop%2Cx_0%2Cy_0%2Cw_1055%2Ch_210" width="620.4000244140625" title="" crop="0,0,1,0.9303" id="ZLfEq" class="ne-image"><img src="https://cdn.nlark.com/yuque/0/2026/png/49996548/1778121795760-eea9d7a6-bda1-41d0-894f-35f1724aad94.png?x-oss-process=image%2Fformat%2Cwebp" width="214" title="" crop="0,0,1,1" id="hKBie" class="ne-image">
>

> **<font style="color:rgb(88, 88, 91);">tcp mss </font>**<font style="color:rgb(88, 88, 91);"><int></font>
>
> <img src="https://cdn.nlark.com/yuque/0/2026/png/49996548/1778305353298-72d494bd-0b6f-41f9-86ce-2b78b46663da.png" width="510.60003662109375" title="" crop="0,0,1,1" id="u6cad74b1" class="ne-image">
>

> mpls activate
>
> <img src="https://cdn.nlark.com/yuque/0/2026/png/49996548/1778325817313-fa9a546c-5cf7-4cb6-a4ce-8561d4f2dbef.png" width="476.79998779296875" title="" crop="0,0,1,1" id="u310cf2f5" class="ne-image">
>

> update in filtering<img src="https://cdn.nlark.com/yuque/0/2026/png/49996548/1778338334776-833c76db-8283-4fb0-a6af-7c57af11b064.png" width="627.2" title="" crop="0,0,1,1" id="mCG3o" class="ne-image">
>

> **<font style="color:rgb(88, 88, 91);">maximum-peers</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">number</font>_
>

> **<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">allocate-label</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">{</font>**<font style="color:rgb(88, 88, 91);">route-policy</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">route-policy-name</font>_<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);">all</font>**<font style="color:rgb(88, 88, 91);">} </font><font style="color:#AD1A2B;">[unlabeled-path] trouble-shooting的例子中</font>
>
> [https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/216498-labeled-and-unlabeled-together-on-one-bg.html?linkclickid=aisrch](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/216498-labeled-and-unlabeled-together-on-one-bg.html?linkclickid=aisrch)
>

> adjacencies<img src="https://cdn.nlark.com/yuque/0/2026/png/49996548/1778491085275-95c491d7-ed23-4faf-9ddd-2a05481d78a4.png" width="349" title="" crop="0,0,1,1" id="u0b65824b" class="ne-image">
>

### ISIS
> segment-routing irv6	locator
>
> <img src="https://cdn.nlark.com/yuque/0/2026/png/49996548/1778503450903-d444972a-3c22-471c-b756-c092825a06ff.png" width="163" title="" crop="0,0,1,1" id="u80513e9e" class="ne-image">
>

> attestation application {flex-algo|traffic-engineering} trust-vector<img src="https://cdn.nlark.com/yuque/0/2026/png/49996548/1778568895584-197aa1c4-8ace-430c-bff5-bd94b4f714f1.png" width="319.5" title="" crop="0,0,1,1" id="u7e1af503" class="ne-image">
>

> max-metric delay te （但其他分支却有记录模板）<img src="https://cdn.nlark.com/yuque/0/2026/png/49996548/1778569814691-730fef9c-b3b7-46ec-a507-2737d8726bf5.png" width="483.5" title="" crop="0,0,1,1" id="udb0fe151" class="ne-image">
>

### OSPF
> <font style="color:rgb(17, 24, 39);">cost-fallback anomaly delay {te-metric|igp-metric} {increment <1-65534>|multiplier <1-255>|value <1-65535>}</font>
>
> <font style="color:rgb(17, 24, 39);">er</font>
>

## 命令在别的版本手册中
### BGP
> <font style="color:rgb(88, 88, 91);">[bgp] as-list <name> 出现在更新版本的手册中</font>
>

> <font style="color:rgb(17, 24, 39);">nexthop mpls forwarding ibgp 仅出现在NCS 5500 的手册例子中</font>
>
> [https://www.cisco.com/c/en/us/td/docs/iosxr/ncs5500/bgp/26xx/configuration/guide/b-bgp-cg-ncs5500-26xx/implementing-bgp.html?linkclickid=aisrch](https://www.cisco.com/c/en/us/td/docs/iosxr/ncs5500/bgp/26xx/configuration/guide/b-bgp-cg-ncs5500-26xx/implementing-bgp.html?linkclickid=aisrch)
>

> <font style="color:rgb(17, 24, 39);background-color:rgb(237, 244, 251);">enforce-first-as / enforce-first-as-disable 在别的版本命令参考中 对应enforce-first-as [disable]</font>
>

> <font style="color:rgb(17, 24, 39);background-color:rgb(255, 242, 189);">bgp origin-as validation signal ibgp</font>
>

> <font style="color:rgb(17, 24, 39);background-color:rgb(228, 238, 249);">local address {A.B.C.D or X:X::X|inheritance-disable} -- [sessiongroup]</font>
>

> **<font style="color:rgb(88, 88, 91);">bgp</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">log</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">neighbor</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">changes</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">disable -> </font>**<font style="color:rgb(88, 88, 91);">P: {</font><font style="color:#DF2A3F;"> detail |</font><font style="color:rgb(88, 88, 91);"> disable } </font>[https://www.cisco.com/c/en/us/td/docs/iosxr/cisco8000/bgp/cumulative/command/reference/b-bgp-cr-cisco8000/m-bgp-commands-8k.html?linkclickid=aisrch#wp3900582909](https://www.cisco.com/c/en/us/td/docs/iosxr/cisco8000/bgp/cumulative/command/reference/b-bgp-cr-cisco8000/m-bgp-commands-8k.html?linkclickid=aisrch#wp3900582909)
>

> **<font style="color:rgb(88, 88, 91);">remove-private-as</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">[</font>**<font style="color:rgb(88, 88, 91);">inheritance-disable</font>**<font style="color:rgb(88, 88, 91);">]</font><font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">[</font>**<font style="color:rgb(88, 88, 91);">entire-aspath</font>**<font style="color:rgb(88, 88, 91);">] -> P: </font><font style="color:#DF2A3F;">[inbound]</font><font style="color:rgb(88, 88, 91);"> -- 在cisco8000中出现inbound</font>[https://www.cisco.com/c/en/us/td/docs/iosxr/cisco8000/bgp/cumulative/command/reference/b-bgp-cr-cisco8000/b-bgp-cr-cisco8000_CLT_chapter.html?bookSearch=true](https://www.cisco.com/c/en/us/td/docs/iosxr/cisco8000/bgp/cumulative/command/reference/b-bgp-cr-cisco8000/b-bgp-cr-cisco8000_CLT_chapter.html?bookSearch=true)
>

> **<font style="color:rgb(88, 88, 91);">bgp origin-as validation </font>****<font style="color:#DF2A3F;">signal ibgp</font>**
>

> epe backup enable -- c8000cg的例子中
>

> **<font style="color:rgb(88, 88, 91);">bgp origin-as validation time</font>**<font style="color:rgb(88, 88, 91);"> { </font>_<font style="color:rgb(88, 88, 91);">prefix-validation-time </font>_<font style="color:rgb(88, 88, 91);">| </font>**<font style="color:rgb(88, 88, 91);">off</font>**<font style="color:rgb(88, 88, 91);">}</font>
>
> <font style="color:rgb(88, 88, 91);">NCS5500/5000</font>
>

> <font style="color:rgb(17, 24, 39);background-color:rgb(237, 244, 251);">ebgp-send-extcommunity-dmz </font><font style="color:rgb(0, 51, 102);background-color:rgb(237, 244, 251);"> [inheritance-disable]</font><font style="color:rgb(17, 24, 39);background-color:rgb(237, 244, 251);"> -- nc5500/560 例子中，且缺分支</font>
>

> <font style="color:rgb(0, 51, 102);background-color:rgb(237, 244, 251);">ebgp-recv-extcommunity-dmz [inheritance-disable] ..</font>
>

### ISIS
> **<font style="color:rgb(88, 88, 91);">prefix-sid</font>**<font style="color:rgb(88, 88, 91);"> [</font>**<font style="color:rgb(88, 88, 91);">strict-spf</font>**<font style="color:rgb(88, 88, 91);">] { </font>**<font style="color:rgb(88, 88, 91);">index</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">sid-index</font>_<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);">absolute</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">sid-value</font>_<font style="color:rgb(88, 88, 91);"> } [</font>**<font style="color:rgb(88, 88, 91);">n-flag-clear</font>**<font style="color:rgb(88, 88, 91);">] [</font>**<font style="color:rgb(88, 88, 91);">explicit-null</font>**<font style="color:rgb(88, 88, 91);">] </font><font style="color:#DF2A3F;">[</font>**<font style="color:#DF2A3F;background-color:rgb(250, 231, 156);">php-disable</font>**<font style="color:#DF2A3F;">]</font>
>
> <font style="color:#DF2A3F;">在C8000中</font>
>

> flex-algo <num> srlg exclude-any C8000
>

> <font style="background-color:rgb(249, 242, 244);">flex-algo <num></font><font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);"> prefix-metric </font><font style="color:rgb(88, 88, 91);">NCS5500/500</font>
>

> **<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">lsp-check-interval</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">seconds</font>_<font style="color:rgb(88, 88, 91);"> [ </font>**<font style="color:rgb(88, 88, 91);">level</font>**<font style="color:rgb(88, 88, 91);"> { </font>**<font style="color:rgb(88, 88, 91);">1</font>**<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);">2</font>**<font style="color:rgb(88, 88, 91);"> }]</font><font style="color:rgb(0, 51, 102);background-color:rgb(237, 244, 251);"> -----xr 12000 cg</font>
>

> <font style="color:rgb(17, 24, 39);background-color:rgb(228, 238, 249);">receive application flex-algo delay app-only --- NCS560</font>
>

### OSPF
> **<font style="color:rgb(88, 88, 91);">dead-interval</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">{</font>_<font style="color:rgb(88, 88, 91);">seconds</font>_<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);">minimal</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">hello-multiplier</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">multiplier</font>_<font style="color:rgb(88, 88, 91);">}    在IOS中</font>
>

## 手册未提及
### BGP
> <font style="color:rgb(17, 24, 39);background-color:rgb(251, 252, 254);">[ipv4/6 unicast] rnh install extcomm [only] -- Install remote nexthop in extended community and opaque format</font>
>

> <font style="color:rgb(17, 24, 39);">[ipv4/6 mvpn] segmented-multicast</font>
>

> <font style="color:rgb(0, 51, 102);">[ipv4/6 mvpn] global-table-multicast</font>
>

> <font style="color:rgb(17, 24, 39);background-color:rgb(237, 244, 251);">[bgp] bgp install diversion --  Install diversion path to RIB/CEF</font>
>

> <font style="color:rgb(0, 51, 102);background-color:rgb(237, 244, 251);">bgp log message disable  -- </font><font style="color:rgb(0, 51, 102);background-color:rgb(237, 244, 251);">Disable inbound and outbound message logging for all neighbors under</font>
>
> <font style="color:rgb(0, 51, 102);background-color:rgb(237, 244, 251);">the vrf</font>
>

> <font style="color:rgb(17, 24, 39);">bgp read-only --  Allow duplicate table config and disable update generation</font>
>

> <font style="color:rgb(0, 51, 102);background-color:rgb(228, 238, 249);">log message {out|in} {<1-100>|inheritance-diable|disable}</font>
>

> <font style="color:rgb(17, 24, 39);background-color:rgb(255, 242, 189);">bgp install diversion</font>
>

> bgp multipath use cluster-list-length -- 
>

> rpki datafile <WORD>
>

> **<font style="color:rgb(255, 255, 255);background-color:rgb(0, 112, 210);">log format brief</font>**
>

### ISIS
> <font style="color:rgb(0, 51, 102);background-color:rgb(237, 244, 251);">purge-transmit strict </font><font style="color:rgb(17, 24, 39);"> [level-1|level-2]</font>
>

> <font style="color:rgb(17, 24, 39);background-color:rgb(237, 244, 251);">triggers <WORD></font>
>

> monitor-convergence track-ip-frr
>

### OSPF
> <font style="color:rgb(0, 51, 102);background-color:rgb(237, 244, 251);">apply-weight bandwidth [<1-4294967>]</font>
>

> <font style="color:rgb(0, 51, 102);background-color:rgb(237, 244, 251);">apply-weight bandwidth [<1-4294967>]</font>
>

> <font style="color:rgb(17, 24, 39);">delay normalize interval <1-16777215> [offset <0-16777215>]</font>
>

> srlg admin-weight name <><img src="https://cdn.nlark.com/yuque/0/2026/png/49996548/1778567011961-1df60a8f-faca-4428-9a18-eb07b429d1aa.png" width="220" title="" crop="0,0,1,1" id="u10ca804f" class="ne-image"> <font style="color:#DF2A3F;">(ISIS和OSPF)</font>
>

> summary-in [disable|enable]
>

> <font style="color:rgb(17, 24, 39);">external-out [enable|disable]</font>
>

> <font style="color:rgb(17, 24, 39);background-color:rgb(251, 252, 254);">trace size <WORD> {65536|32768|1024|2048|16384|256|8192|512|4096|0}</font>
>

# 设备问题
> 
>

# Probe < Manual（未归因）
## 缺少部分分支
### BGP
> **<font style="color:rgb(88, 88, 91);">route-policy</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">aggregate-route-policy-name</font>_<font style="color:rgb(88, 88, 91);"> [ </font>**<font style="color:rgb(88, 88, 91);">set aggregate-contributor</font>**<font style="color:rgb(88, 88, 91);"> ] -> P: </font>**<font style="color:rgb(88, 88, 91);">route-policy</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">aggregate-route-policy-name</font>_
>

> **<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">optimal-route-reflection</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">orr-group-name</font>_<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">primary-ip-address</font>_<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">[secondary-ip-address] [tertiary-ip-address] router-policy </font>_<font style="color:rgb(88, 88, 91);">{ </font>**<font style="color:rgb(88, 88, 91);">addpath name</font>**<font style="color:rgb(88, 88, 91);"> } P: </font>**<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">optimal-route-reflection</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">orr-group-name</font>_<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">primary-ip-address</font>_
>

> **<font style="color:rgb(88, 88, 91);">rpki</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">server</font>**<font style="color:rgb(88, 88, 91);"> { </font>_<font style="color:rgb(88, 88, 91);">host-name</font>_<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">| ip-address</font>_<font style="color:rgb(88, 88, 91);"> } P: </font>**<font style="color:rgb(88, 88, 91);">rpki</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">server</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">host-name</font>_
>

### ISIS
> **<font style="color:rgb(88, 88, 91);">address-family</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">{</font>**<font style="color:rgb(88, 88, 91);">ipv4</font>**<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);">ipv6</font>**<font style="color:rgb(88, 88, 91);">}</font><font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">multicast</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">topology</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">topo-name</font>_<font style="color:rgb(88, 88, 91);"> </font><font style="color:#AD1A2B;">[</font>**<font style="color:#AD1A2B;">maximum</font>**<font style="color:#AD1A2B;"> </font>**<font style="color:#AD1A2B;">prefix</font>**<font style="color:#AD1A2B;"> </font>_<font style="color:#AD1A2B;">prefix-limit</font>_<font style="color:#AD1A2B;">]</font>
>

> **<font style="color:rgb(88, 88, 91);">distribute link-state</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:#AD1A2B;">[ </font>**<font style="color:#AD1A2B;">exclude-external</font>**<font style="color:#AD1A2B;"> </font>**<font style="color:#AD1A2B;">exclude-interarea route-policy</font>**<font style="color:#AD1A2B;"> </font>_<font style="color:#AD1A2B;">name</font>_<font style="color:#AD1A2B;"> ]</font>
>

## 设备未提取到命令
### BGP
> **<font style="color:rgb(88, 88, 91);">additional-paths</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">install</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">backup</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">[</font>**<font style="color:rgb(88, 88, 91);">disable</font>**<font style="color:rgb(88, 88, 91);">]</font>
>

> **<font style="color:rgb(88, 88, 91);">bgp</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">write-limit</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">group-limit</font>_<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">global-limit</font>_<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">[</font>**<font style="color:rgb(88, 88, 91);">desynchronize</font>**<font style="color:rgb(88, 88, 91);">]</font>
>

> **<font style="color:rgb(88, 88, 91);">bgp</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">best-path sr-policy</font>**<font style="color:rgb(88, 88, 91);"> { </font>**<font style="color:rgb(88, 88, 91);">force</font>**<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);">prefer</font>**<font style="color:rgb(88, 88, 91);"> }</font>
>

> **<font style="color:rgb(88, 88, 91);">bgp</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">lpts-secure-binding</font>**
>

> **<font style="color:rgb(88, 88, 91);">distributed</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">speaker</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">id</font>_
>

> **<font style="color:rgb(88, 88, 91);">bgp</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">write-limit</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">group-limit</font>_<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">global-limit</font>_<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">[</font>**<font style="color:rgb(88, 88, 91);">desynchronize</font>**<font style="color:rgb(88, 88, 91);">]</font>
>

> **<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">advertise gateway-ip-disable </font>**[**https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/lxvpn/command/reference/b-lxvpn-cr-asr9000/EVPN-commands.html?utm_source=chatgpt.com#concept_dcx_j5w_kfc**](https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/lxvpn/command/reference/b-lxvpn-cr-asr9000/EVPN-commands.html?utm_source=chatgpt.com#concept_dcx_j5w_kfc)
>

> **<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">allowconfedas-in</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">confederation-as-count</font>_
>

> **<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">speaker-id</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">id</font>_
>

> **<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">update</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">in</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">error-handling</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">treat-as-withdraw</font>**
>

### ISIS
> <font style="color:rgb(0, 51, 102);">ipfrr lfa exclude interface <type> <interface-path-id></font>
>

> <font style="color:rgb(17, 24, 39);">ipfrr lfa level { 1 | 2 }</font>
>

### OSPF
> <font style="color:rgb(0, 51, 102);background-color:rgb(237, 244, 251);">exchange-timer <exchange-time-in-minutes> hold-time <hold-time-in-minutes> recovery-count <recovery-count></font>
>

# Heterogenity between M&P
## BGP
| Manual | Probe |
| --- | --- |
| **<font style="color:rgb(88, 88, 91);">bgp origin-as validation </font>****<font style="color:#df2a3f;">enable</font>** | **<font style="color:rgb(88, 88, 91);">bgp origin-as validation {</font>****<font style="color:#df2a3f;">enable|disable}</font>** |
| **<font style="color:rgb(88, 88, 91);">domain-distinguisher</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:#DF2A3F;">unique-id</font>_ | **<font style="color:rgb(88, 88, 91);">domain-distinguisher</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:#DF2A3F;"><int>:A.B.C.D</font> |
| **<font style="color:rgb(88, 88, 91);">import</font>**<font style="color:rgb(88, 88, 91);"> [ </font>**<font style="color:rgb(88, 88, 91);">stitching-rt</font>**<font style="color:rgb(88, 88, 91);"> ] </font>**<font style="color:#DF2A3F;">reoriginate</font>**<font style="color:#DF2A3F;"> </font><font style="color:rgb(88, 88, 91);">[ </font>**<font style="color:rgb(88, 88, 91);">stitching-rt</font>**<font style="color:rgb(88, 88, 91);"> ]</font> | **<font style="color:rgb(88, 88, 91);">import</font>**<font style="color:rgb(88, 88, 91);"> [ </font>**<font style="color:rgb(88, 88, 91);">stitching-rt</font>**<font style="color:rgb(88, 88, 91);"> ] </font>**<font style="color:#DF2A3F;">re-originate</font>**<font style="color:rgb(88, 88, 91);"> [ </font>**<font style="color:rgb(88, 88, 91);">stitching-rt</font>**<font style="color:rgb(88, 88, 91);"> ]</font> |
| **<font style="color:rgb(88, 88, 91);">aigp</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">send-cost-community</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">{</font>_<font style="color:rgb(88, 88, 91);">cost-id</font>_<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);">disable</font>**<font style="color:rgb(88, 88, 91);">}</font><font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">poi</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">{</font>**<font style="color:rgb(88, 88, 91);">igp-cost</font>**<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);">pre-bestpath</font>**<font style="color:rgb(88, 88, 91);">}</font><font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">[</font>**<font style="color:rgb(88, 88, 91);">transitive</font>**<font style="color:rgb(88, 88, 91);">]</font> | **<font style="color:rgb(88, 88, 91);">aigp</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:#DF2A3F;">send cost-community</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">{</font>_<font style="color:rgb(88, 88, 91);">cost-id</font>_<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);">disable</font>**<font style="color:rgb(88, 88, 91);">}</font><font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">poi</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">{</font>**<font style="color:rgb(88, 88, 91);">igp-cost</font>**<font style="color:rgb(88, 88, 91);"> | </font>**<font style="color:rgb(88, 88, 91);">pre-bestpath</font>**<font style="color:rgb(88, 88, 91);">}</font><font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">[</font>**<font style="color:rgb(88, 88, 91);">transitive</font>**<font style="color:rgb(88, 88, 91);">]</font> |
| **<font style="color:rgb(88, 88, 91);">timers</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">bgp</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">keepalive</font>_<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">hold-time</font>_ | **<font style="color:rgb(88, 88, 91);">timers</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">bgp</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">keepalive</font>_<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">hold-time </font>__<font style="color:#DF2A3F;">minimum-acceptable-holdtime-for-neighbor</font>_ |
| **<font style="color:rgb(88, 88, 91);">graceful-maintenance</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">{</font>**<font style="color:rgb(88, 88, 91);">activate</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">[</font>**<font style="color:rgb(88, 88, 91);">as-prepends</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">as-prepends-value</font>_<font style="color:rgb(88, 88, 91);">]</font><font style="color:rgb(88, 88, 91);"> </font><font style="color:rgb(88, 88, 91);">[</font>**<font style="color:rgb(88, 88, 91);">inheritance-disable</font>**<font style="color:rgb(88, 88, 91);">] | [</font>**<font style="color:rgb(88, 88, 91);">local-preference</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">local-pref-value</font>_<font style="color:rgb(88, 88, 91);">]</font><font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">inheritance-disable</font>**<font style="color:rgb(88, 88, 91);">}</font> | <img src="https://cdn.nlark.com/yuque/0/2026/png/49996548/1778494905134-df72364d-bbd3-48b0-bd93-51ca467f3472.png" width="305" title="" crop="0,0,1,1" id="ufb6f310a" class="ne-image"> |
| **<font style="color:rgb(88, 88, 91);">update wait-install</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">delay</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">startup</font>**<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">seconds </font>_ | **<font style="color:rgb(88, 88, 91);">update wait-install</font>** |
|  | **<font style="color:rgb(88, 88, 91);"></font>** |


## ISIS
| **<font style="color:rgb(88, 88, 91);">adjacency</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">stagger</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:#DF2A3F;">{</font>**<font style="color:#DF2A3F;">disable</font>**<font style="color:rgb(88, 88, 91);"> | </font>_<font style="color:rgb(88, 88, 91);">initial-num-nbr</font>_<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">max-num-nbr</font>_<font style="color:#DF2A3F;">} </font><font style="color:rgb(88, 88, 91);">    </font><br/><font style="color:rgb(88, 88, 91);">default: <1-65535></font> | **<font style="color:rgb(88, 88, 91);">adjacency</font>**<font style="color:rgb(88, 88, 91);"> </font>**<font style="color:rgb(88, 88, 91);">stagger</font>**<font style="color:rgb(88, 88, 91);"> </font><font style="color:#DF2A3F;">[</font>_<font style="color:rgb(88, 88, 91);">nitial-num-nbr</font>_<font style="color:rgb(88, 88, 91);"> </font>_<font style="color:rgb(88, 88, 91);">max-num-nbr</font>_<font style="color:#DF2A3F;">]</font><br/><font style="color:rgb(88, 88, 91);">default: <2-65000></font> |
| --- | --- |


### OSPF
| **<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">segment-routing</font>****<font style="color:rgb(88, 88, 91);"> prefix-sid-map receive</font>** | **<font style="color:rgb(88, 88, 91);background-color:rgb(250, 231, 156);">segment-routing</font>****<font style="color:rgb(88, 88, 91);"> prefix-sid-map receive </font>****<font style="color:#DF2A3F;">disable</font>** |
| --- | --- |
| | |


# 



