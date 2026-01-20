<h1 align="center">🛡️ All-Defense-Tool</h1>

<div align="center">
  <p><strong>全网优秀的开源攻防武器项目集成库</strong></p>
</div>


---

首先恭喜你发现了宝藏。本项目集成了全网优秀的开源攻防武器项目，包含信息收集工具（自动化利用工具、资产发现工具、目录扫描工具、子域名收集工具、指纹识别工具、端口扫描工具、各种插件....etc...），漏洞利用工具（各大CMS、OA利用工具、中间件利用工具、反序列化利用工具、数据库利用工具等项目........），内网渗透工具（隧道代理、密码提取、木马免杀、域渗透.....）、应急响应工具、甲方运维工具、等其他安全攻防资料整理，供攻防双方使用。

> 🔄 **更新**：本项目**每周自动更新**，自动获取并填充项目的最新更新时间，能够快速发现活跃工具。 
> ⚠️ **工欲善其事必先利其器，不知道有哪些工具，不会用工具，不懂工具原理，怎么写出适合自己的工具？**

## 免责声明


> **重点提醒：本项目工具来源于互联网，是否含带木马及后门请自行甄别！！请大家提高警惕！！！**
>
> 1. 本项目所有内容,仅供学习和研究使用,请勿使用项目的技术手段用于非法用途,任何人造成的任何负面影响,与本人无关.
> 2. 本文档所有内容、新闻皆不代表本人态度、立场,如果有建议或方案,欢迎提交 issues，不受理Pull request
> 3. 不会收取任何广告费用,展示的所有工具链接与本人无任何利害关系
>
> **温馨提醒**：不要沉迷于攻防而忘了吃饭喔~ 🍚
>
> - 在家做饭方法指南：[HowToCook](https://github.com/Anduin2017/HowToCook)

## 📚 目录


* [🛠️ 半/全自动化利用工具](#半全自动化利用工具)
* [🔍 信息收集工具](#信息收集工具)
  * [资产发现工具](#资产发现工具)
  * [子域名收集工具](#子域名收集工具)
  * [目录扫描工具](#目录扫描工具)
  * [指纹识别工具](#指纹识别工具)
  * [端口扫描工具](#端口扫描工具)
  * [Burp插件](#burp插件)
  * [浏览器插件](#浏览器插件)
  * [邮箱&钓鱼](#邮箱钓鱼)
  * [社工个人信息收集类](#社工个人信息收集类)
  * [APP/公众号/小程序相关工具](#app公众号小程序相关工具)
  * [常用小工具](#常用小工具)
* [💣 漏洞利用工具](#漏洞利用工具)
  * [漏洞扫描框架/工具](#漏洞扫描框架工具)
  * [中间件/应用漏洞利用工具](#中间件应用漏洞利用工具)
  * [重点cms利用工具](#重点cms利用工具)
  * [信息泄露利用工具](#信息泄露利用工具)
  * [数据库利用工具](#数据库利用工具)
  * [爆破利用工具](#爆破利用工具)
  * [全网字典收集](#全网字典收集)
  * [常规漏洞利用工具](#常规漏洞利用工具)
  * [反序列化利用工具](#反序列化利用工具)
  * [内存马注入工具](#内存马注入工具)
  * [代码审计辅助工具-通用](#代码审计辅助工具-通用)
  * [代码审计辅助工具-java](#代码审计辅助工具-java)
  * [代码审计辅助工具-php](#代码审计辅助工具-php)
  * [代码审计辅助工具-dotNET](#代码审计辅助工具-dotnet)
  * [通用型WAF绕过](#通用型waf绕过)
* [🏰 内网渗透工具](#内网渗透工具)
  * [后渗透辅助工具](#后渗透辅助工具)
  * [webshell管理工具](#webshell管理工具)
  * [c2管理工具](#c2管理工具)
  * [提权项目](#提权项目)
  * [内网收集工具](#内网收集工具)
  * [横向移动工具](#横向移动工具)
  * [域渗透工具](#域渗透工具)
  * [密码提取工具](#密码提取工具)
  * [隧道代理工具](#隧道代理工具)
  * [优秀免杀项目](#优秀免杀项目)
  * [权限维持工具](#权限维持工具)
* [🏗️ 基础设施搭建](#基础设施搭建)
  * [攻防环境部署](#攻防环境部署)
  * [代理池](#代理池)
  * [靶场清单](#靶场清单)
  * [漏洞订阅&安全推送](#漏洞订阅安全推送)
* [🛡️ 运维&甲方&防守方工具](#运维甲方防守方工具)
  * [安全建设](#安全建设)
  * [应急响应笔记](#应急响应笔记)
  * [Linux应急响应工具](#linux应急响应工具)
  * [Windows应急响应工具](#windows应急响应工具)
  * [webshell查杀工具](#webshell查杀工具)
  * [内存马查杀工具](#内存马查杀工具)
  * [防守辅助分析工具](#防守辅助分析工具)
  * [溯源反制工具](#溯源反制工具)
* [📚 其他安全资料整理](#其他安全资料整理)
  * [JAVA安全研究](#java安全研究)
  * [AI安全](#ai安全)
  * [安全面试](#安全面试)
  * [实战红蓝资料集锦](#实战红蓝资料集锦)
  * [云安全资料](#云安全资料)

# 🛠️ 半/全自动化利用工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | --------------------------------------------- |
| 单兵作战武器库，你值得拥有 | https://github.com/yaklang/yakit |
| ScopeSentry-网络空间测绘、子域名枚举、端口扫描、敏感信息发现、漏洞扫描、分布式节点 | https://github.com/Autumn-27/ScopeSentry-Scan |
| CyberEdge 是一款精心设计的互联网资产测绘工具，为网络安全专业人士提供精准、高效的扫描体验。 | https://github.com/Symph0nia/CyberEdge |
| dddd是一款使用简单的批量信息收集,供应链漏洞探测工具，旨在优化红队工作流，减少伤肝的机械性操作。支持从Hunter、Fofa批量拉取目标 | https://github.com/SleepingBag945/dddd |
| 一款GUI界面的渗透工具，将部分人工经验转换为自动化，集成了渗透过程中常用到的一些功能，目前集成了端口扫描、端口爆破、web指纹扫描、漏洞扫描、漏洞利用以及编码转换功能，后续会持续更新。 | https://github.com/lz520520/railgun |
| 安全服务集成化工具平台 | https://github.com/qiwentaidi/Slack |
| 密探渗透测试工具包含资产信息收集，子域名爆破，搜索语法，资产测绘（FOFA，Hunter，quake, ZoomEye），指纹识别，敏感信息采集，文件扫描、端口扫描、批量信息权重查询、密码字典等功能 | https://github.com/kkbo8005/mitan |
| **Nemo**是用来进行自动化信息收集的一个简单平台，通过集成常用的信息收集工具和技术，实现对内网及互联网资产信息的自动收集，提高隐患排查和渗透测试的工作效率。 | https://github.com/hanc00l/nemo_go |
| DarkAngel 是一款全自动白帽漏洞扫描器，从hackerone、bugcrowd资产监听到漏洞报告生成、企业微信通知。 | https://github.com/Bywalks/DarkAngel |
| 分布式资产信息收集和漏洞扫描平台 | https://github.com/1in9e/gosint |
| 一条龙服务，只需要输入根域名即可全方位收集相关资产，并检测漏洞。也可以输入多个域名、C段IP等，具体案例见下文。 | https://github.com/0x727/ShuiZe_0x727 |
| 自动化巡航扫描框架（可用于红队打点评估） | https://github.com/b0bac/ApolloScanner |
| 可针对指定IP段、资产清单、存活网段自动化进行端口扫描以及TCP指纹识别和Banner抓取 | https://github.com/lcvvvv/kscan |
| 集成 vscan、nuclei、ksubdomain、subfinder等，充分自动化、智能化 并对这些集成的项目进行代码级别优化、参数优化，个别模块,如 vscan filefuzz部分进行了重写 | https://github.com/GhostTroops/scan4all |
| 一个辅助平常渗透测试项目或者攻防项目快速打点的综合工具 | https://github.com/P1-Team/AlliN |
| 一个漏洞扫描器粘合剂,添加目标后30款工具自动调用 | https://github.com/78778443/QingScan |
| 从子域名、端口服务、漏洞、爬虫等一体化的资产管理系统 | https://github.com/CTF-MissFeng/bayonet |
| 一个高度可定制Web自动化扫描框架 | https://github.com/r3curs1v3-pr0xy/vajra |
| reconFTW 集成了30个工具的信息收集利器 | https://github.com/six2dez/reconftw |
| 自动化侦查框架 | https://github.com/yogeshojha/rengine |
|  |  |
|  |  |
|  |  |

# 🔍 信息收集工具


## 资产发现工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | -------------------------------------------- |
| reconFTW 集成了30个工具的信息收集利器 | https://github.com/six2dez/reconftw |
| 资产无限巡航扫描系统 | https://github.com/awake1t/linglong |
| SRC子域名资产监控 | https://github.com/LangziFun/LangSrcCurise |
| 快速侦察与目标关联的互联网资产，构建基础资产信息库。 | https://github.com/TophantTechnology/ARL |
| 集成GoogleHacking语法来进行信息收集 | https://github.com/TebbaaX/GRecon |
| 从第三方平台获取目标网页内容 | https://github.com/tomnomnom/waybackurls |
| 从多个网站提取目标相关信息 | https://github.com/lc/gau |
| 集合了多个网络测绘平台，可以快速在多个网络测绘平台搜索信息并且合并展示及导出。 | https://github.com/ExpLangcn/InfoSearchAll |
| 调用fofa\ZoomEye\360quake的官方api---GUI界面 | https://github.com/xzajyjs/ThunderSearch |
| 集成多个网络资产测绘平台的搜索工具 | https://github.com/Kento-Sec/AsamF |
| 一个简单实用的FOFA客户端 By flashine | https://github.com/wgpsec/fofa_viewer |
| 0_zone_zpi脚本 | https://github.com/lemonlove7/0_zone |
| icp备案查询、企业资产快速收集工具 | https://github.com/SiJiDo/IEyes |
| 一款基于各大企业信息API的工具 | https://github.com/wgpsec/ENScan_GO |
| 基于斗象灯塔ARL修改后的版本。相比原版，增加了OneForAll、中央数据库，修改了altDns | https://github.com/ki9mu/ARL-plus-docker |
| 灯塔（最新版）指纹添加脚本！ | https://github.com/loecho-sec/ARL-Finger-ADD |
|  |  |
|  |  |
|  |  |
|  |  |

## 子域名收集工具

| 项目简介 | 项目地址 |
| ---------------------------------------- | ----------------------------------------------- |
| 在线子域名收集 | https://rapiddns.io/subdomain |
| ksubdomain 无状态子域名爆破工具 | https://github.com/knownsec/ksubdomain |
| 一款功能强大的子域收集工具 | https://github.com/shmilylty/OneForAll |
| 通过使用被动在线资源来发现网站的有效子域 | https://github.com/projectdiscovery/subfinder |
| src子域名监控 | https://github.com/LangziFun/LangSrcCurise |
| 从 github 上发现子域名 | https://github.com/gwen001/github-subdomains |
| Layer子域名挖掘机 | https://github.com/euphrat1ca/LayerDomainFinder |
| 好用且强大的子域名扫描工具 | https://github.com/yunxu1/dnsub |
|  |  |
|  |  |

## 目录扫描工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------------- |
| Web path scanner  目录扫描工具 | https://github.com/maurosoria/dirsearch |
| 用Rust编写的快速，简单，递归的内容发现工具 | https://github.com/epi052/feroxbuster |
| Directory/File, DNS and VHost busting tool written in Go | https://github.com/OJ/gobuster |
| 用Go编写的模糊测试工具 | https://github.com/ffuf/ffuf |
| Next Generation HTTP Dir/File Fuzz Tool | https://github.com/chainreactors/spray |
| 通过提取自动加载和静态地址中的JS和页面内容，解析Webpack打包和使用正则匹配技术，发现API接口及Base URL。 | https://github.com/0x727/ChkApi_0x727 |
| Fast passive URL enumeration tool. | https://github.com/chainreactors/urlfounder |
| 一个高级web目录、文件扫描工具 | https://github.com/H4ckForJob/dirmap |
| 网站的敏感目录发掘工具 | https://github.com/deibit/cansina |
| 御剑后台扫描工具珍藏版 | https://www.fujieace.com/hacker/tools/yujian.html |
| 使用GoLang开发的目录/子域扫描器 | https://github.com/ReddyyZ/urlbrute |
| 御剑目录扫描专业版 | https://github.com/foryujian/yjdirscan |
| 类似JSFinder的golang实现，更快更全更舒服 | https://github.com/pingc0y/URLFinder |
| 爬虫 可以发现搜索引擎发现不了的目录 | https://github.com/jaeles-project/gospider |
| katana 是 projectdiscovery 项目中的一个网页链接抓取工具，可以自动解析js文件。新一代爬行框架。 | https://github.com/projectdiscovery/katana |
| dontgo403 是一个绕过 40X 错误的工具。 | https://github.com/devploit/dontgo403 |
| 从JavaScript中提取URL、路径、机密和其他有趣的部分 | https://github.com/BishopFox/jsluice |
| 爬网站JS文件，自动fuzz api接口，指定api接口（针对前后端分离项目，可指定后端接口地址），回显api响应 | https://github.com/ttstormxx/jjjjjjjjjjjjjs |
|  |  |

## 指纹识别工具

| 项目简介 | 项目地址 |
| -------------------------------------------------------- | ------------------------------------------------ |
| 红队重点攻击系统指纹探测工具 | https://github.com/EdgeSecurityTeam/EHole |
| EHole(棱洞)魔改。可对路径进行指纹识别；支持识别出来的重点资产进行漏洞检测(支持从hunter和fofa中提取资产)支持对ftp服务识别及爆破 | https://github.com/lemonlove7/EHole_magic |
| 跨平台指纹识别工具 | https://github.com/0x727/ObserverWard |
| Glass是一款针对资产列表的快速指纹识别工具 | https://github.com/s7ckTeam/Glass |
| 红队行动下的重点资产指纹识别工具 | https://github.com/P001water/P1finger |
| Resources一款红队在大量的资产中存活探测与重点攻击系统指纹探测工具 | https://github.com/EASY233/Finger |
| TideFinger——指纹识别小工具，汲取整合了多个web指纹库 | https://github.com/TideSec/TideFinger |
| 【暂未开源】一个Go版(更强大)的TideFinger指纹识别工具，可对web和主机指纹进行识别探测，整合梳理互联网指纹2.3W余条，在效率和指纹覆盖面方面进行了平衡和优化。 | https://github.com/TideSec/TideFinger_Go |
| Golang实现Wappalyzer 指纹识别 | https://github.com/projectdiscovery/wappalyzergo |
| 功能齐全的Web指纹识别和分享平台，内置了一万多条互联网开源的指纹信息。 | https://github.com/b1ackc4t/14Finger |
| 一个web应用程序指纹识别工具 | https://github.com/urbanadventurer/WhatWeb |



## 端口扫描工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ----------------------------------------------------- |
| **MX1014** 是一个遵循 **“短平快”** 原则的灵活、轻便和快速端口扫描器 (满足红队需求的出网测试、网段探测和快速高危端口扫描等需求) | https://github.com/L-codes/MX1014 |
| naabu 用 go 编写的快速端口扫描器 | https://github.com/projectdiscovery/naabu |
| TXPortMap 实用型的端口扫描、服务识别工具 | https://github.com/4dogs-cn/TXPortMap |
| 使用Golang开发的高并发网络扫描、服务探测工具 | https://github.com/Adminisme/ServerScan |
| masnmapscan 一款端口扫描器。整合了masscan和nmap两款扫描器 | https://github.com/hellogoldsnakeman/masnmapscan-V1.0 |
| gonmap是一个go语言的nmap端口扫描库 | https://github.com/lcvvvv/gonmap |
| 光速扫描 | http://pan.baidu.com/s/1pLjaQKF |
| 在线端口扫描1 | http://coolaf.com/tool/port |
| 在线端口扫描2 | http://tool.cc/port/ |
|  |  |



## 前端加解密工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------- |
| 浏览器内存漫游解决方案 | https://github.com/JSREI/ast-hook-for-js-RE |
| 一款支持多种加密算法、或直接执行浏览器JS代码的BurpSuite插件。 | https://github.com/whwlsfb/BurpCrypto |
| 一个想让你测试加密流量像测试明文一样简单高效的 Burp 插件。 | https://github.com/outlaws-bai/Galaxy |
| 根据自定义来达到对数据包的处理（适用于加解密、爆破等），类似mitmproxy，不同点在于经过了burp中转 | https://github.com/f0ng/autoDecoder |
| 远程调用(rpc)浏览器方法，免去抠代码补环境 | https://github.com/jxhczhl/JsRpc |
| 基于CDP实现的远程JS debug工具 | https://github.com/1oid/remotejs |
| 一款利用爬虫技术实现前端JS加密自动化绕过的渗透测试工具 | https://github.com/LiChaser/SpiderX |
|  |  |

## Burp插件

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------------------- |
| 有关burpsuite的插件(非商店),文章以及使用技巧的收集 | https://github.com/Mr-xn/BurpSuite-collections |
| 一个集成的BurpSuite漏洞探测插件 | https://github.com/Tsojan/TsojanScan |
| HaE 请求高亮标记与信息提取的辅助型 BurpSuite 插件 | https://github.com/gh0stkey/HaE |
| 分析、拆解HTTP协议报文，提取HTTP协议报文中的参数、路径、文件、参数值等信息，并统计出现的频次，帮助用户构建出具有实战应用价值的Fuzzing字典。 | https://github.com/gh0stkey/CaA |
| 一个集成的BurpSuite漏洞探测插件2 | https://github.com/kN6jq/gatherBurp |
| OneScan是递归目录扫描的BurpSuite插件。 | https://github.com/vaycore/OneScan |
| 解析提取接口路径+参数 | https://github.com/xnl-h4ck3r/GAP-Burp-Extension |
| 一款基于BurpSuite的被动式shiro检测插件 | https://github.com/pmiaowu/BurpShiroPassiveScan |
| 一款基于BurpSuite的被动式FastJson检测插件 | https://github.com/pmiaowu/BurpFastJsonScan |
| 一个简单的Fastjson反序列化检测burp插件 | https://github.com/Maskhe/FastjsonScan |
| fastjson利用，支持tomcat、spring回显，哥斯拉内存马；回显利用链为dhcp、ibatis、c3p0 | https://github.com/skisw/fastjson-exp |
| 添加一些右键菜单让burp用起来更顺畅 | https://github.com/bit4woo/knife |
| domain_hunter_pro 一个资产管理类的Burp插件 | https://github.com/bit4woo/domain_hunter_pro |
| 新一代子域名主/被动收集工具 | https://github.com/Acmesec/Sylas |
| GadgetProbe Burp插件 用来爆破远程类查找Java反序列化 | https://github.com/BishopFox/GadgetProbe |
| HopLa 自动补全 Payload 的 BurpSuite插件 | https://github.com/synacktiv/HopLa |
| 验证码识别 | https://github.com/f0ng/captcha-killer-modified |
| 伪造ip地址 | https://github.com/TheKingOfDuck/burpFakeIP |
| 自动发送请求 | https://github.com/nccgroup/AutoRepeater |
| 自动探测请求走私漏洞 | https://github.com/portswigger/http-request-smuggler |
| 用于在所有请求中自动执行 SSRF 检测 | https://github.com/ethicalhackingplayground/ssrf-king |
| 主要用于简化和解决Burpsuite对Http的一些操作. | https://github.com/MaskCyberSecurityTeam/BurpHttpHelper |
| 用于Outlook用户信息收集，在已登录Outlook账号后，可以使用该插件自动爬取所有联系人的信息 | https://github.com/KrystianLi/OutLook |
| 提取参数插件 | https://github.com/goddemondemongod/god_param |
| 这是一款burp插件，用于Outlook 网页版用户信息收集，在已登录Outlook 网页版账号后，可以使用该 | https://github.com/KrystianLi/ExchangeOWA |
| 对权限绕过自动化bypass的burpsuite插件 | https://github.com/0x727/BypassPro |
| Tls指纹特征绕过插件\ | Bypass | burp-awesome-tls |
| BurpSuite插件实现被动指纹识别+网站提取链接+OA爆破，可帮助我们发现更多资产。 | https://github.com/shuanx/BurpFingerPrint |
| 攻防演练过程中，我们通常会用浏览器访问一些资产，但很多未授权/敏感信息/越权隐匿在已访问接口过html、JS文件等，该插件能让我们发现未授权/敏感信息/越权/登陆接口等。 | https://github.com/shuanx/BurpAPIFinder |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

## 浏览器插件

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------------- |
| Hack-Tools  适用于红队的浏览器扩展插件 | https://github.com/LasCC/Hack-Tools |
| 基于chrome、firefox插件的被动式信息泄漏检测工具 | https://github.com/momosecurity/FindSomething |
| superSearchPlus是聚合型信息收集插件，支持综合查询，资产测绘查询，信息收集 敏感信息提取 js资源扫描 目录扫描 vue组件扫描 整合了目前常见的资产测绘平台 同时支持数据导出 | https://github.com/dark-kingA/superSearchPlus |
| SwitchyOmega 浏览器的代理插件 | https://github.com/FelisCatus/SwitchyOmega |
| Chrome插件.使用DevTools查找DOM XSS | https://github.com/filedescriptor/untrusted-types |
| FOFA Pro view 是一款FOFA Pro 资产展示浏览器插件 | https://github.com/fofapro/fofa_view |
| mitaka 用于 OSINT 搜索的Chrome和Firefox扩展 | https://github.com/ninoseki/mitaka |
| Git History 查看git存储库文件的历史记录 | https://githistory.xyz/ |
| 一款可以检测WEB蜜罐并阻断请求的Chrome插件 | https://github.com/cnrstar/anti-honeypot |
| 一款完全被动监听的谷歌插件，用于高危指纹识别、蜜罐特征告警和拦截、机器特征对抗。 | https://github.com/graynjo/Heimdallr |
| SourceDetector是一个自动发现.map文件，并帮你下载到本地的一个chrome extension。 | https://github.com/Lz1y/SourceDetector-dist |

## 邮箱&钓鱼

| 项目简介 | 项目地址 |
| ---------------------------------------------- | ------------------------------------------------------ |
| 邮箱自动化收集爬取 | https://github.com/Taonn/EmailAll |
| 通过搜索引擎爬取电子邮件 | https://github.com/Josue87/EmailFinder |
| 批量检查邮箱账密有效的  Python 脚本 | https://github.com/rm1984/IMAPLoginTester |
| Coremail邮件系统组织通讯录导出脚本 | https://github.com/dpu/coremail-address-book |
| 拥有在线模板设计、发送诱骗广告等功能的钓鱼系统 | https://github.com/gophish/gophish |
| Swaks SMTP界的瑞士军刀 | https://github.com/jetmore/swaks |
| 一个在线的任意发件人发送Email邮件网站 | http://tool.chacuo.net/mailanonymous |
| EwoMail是基于Linux的企业邮箱服务器 | https://github.com/gyxuehu/EwoMail |
| 批量发送钓鱼邮箱 | https://github.com/Yang0615777/sendMail |
| 免杀宏生成器 | https://github.com/Inf0secRabbit/BadAssMacros |
| 图标提取 | https://github.com/JarlPenguin/BeCyIconGrabberPortable |
| 图标替换 | https://github.com/guitarfreak/SetIcon |
| 红蓝对抗：钓鱼演练资源汇总&备忘录 | https://github.com/tib36/PhishingBook |
| 剑指钓鱼基建快速部署自动化 | https://github.com/taielab/Taie-AutoPhishing |
| 一款适用于红蓝对抗中的仿真钓鱼系统 | https://github.com/xiecat/goblin |

## 社工个人信息收集类

| 项目简介 | 项目地址 |
| ------------------------------------------------------ | ------------------------------------------------------------ |
| 从大量站点中收集用户个人信息 | https://github.com/soxoj/maigret |
| 根据邮箱自动搜索泄漏的密码信息 | https://github.com/D4Vinci/Cr3dOv3r |
| 密码泄露搜集 | https://archive.org/search.php?query= |
| 从部分站点中收集个人信息 | https://github.com/n0tr00t/Sreg |
| 输入人名或邮箱地址, 自动从互联网爬取关于此人的信息 | https://github.com/famavott/osint-scraper |
| 通过脉脉用户猜测企业邮箱 | https://github.com/Ridter/Mailget |
| 社工字典密码生成 | https://github.com/Mebus/cupp |
| 社会工程学密码生成器，是一个利用个人信息生成密码的工具 | https://github.com/zgjx6/SocialEngineeringDictionaryGenerator |
| 在线密码生成器 | https://zzzteph.github.io/weakpass/ |
|  |  |

## APP/公众号/小程序相关工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------------------- |
| （推荐）微信小程序反编译工具，.wxapkg 文件扫描 + 解密 + 解包工具 | https://github.com/wux1an/wxapkg |
| 全自动化，微信小程序 wxapkg 包 源代码还原工具, 线上代码安全审计 | https://github.com/biggerstar/wedecode |
| 微信小程序辅助渗透-自动化 | https://github.com/eeeeeeeeee-code/e0e1-wx |
| 自动化反编译微信小程序，小程序安全评估工具，发现小程序安全问题，自动解密，解包，可还原工程目录，支持Hook，小程序修改 | https://github.com/Ackites/KillWxapkg |
| 一个反编译微信小程序的工具，仓库也收集各种微信小程序/小游戏.wxapkg文件 | https://github.com/ezshine/wxapkg-convertor |
| 微信小程序主包解密工具 | https://github.com/BlackTrace/pc_wxapkg_decrypt |
| 微信小程序反编译 | https://github.com/qwerty472123/wxappUnpacker |
| 微信小程序反编译 | https://github.com/r3x5ur/wxapkg-unpacker |
| 微信小程序信息在线收集，wxapkg源码包内提取信息 | https://github.com/moyuwa/wechat_appinfo_wxapkg |
| WeChatOpenDevTool 微信小程序强制开启开发者工具 | https://github.com/x0tools/WeChatOpenDevTools |
| WeChatOpenDevTool 微信小程序强制开启开发者工具py | https://github.com/JaveleyQAQ/WeChatOpenDevTools-Python |
| Resources移动端(Android、iOS、WEB、H5、静态网站)信息收集扫描工具 | https://github.com/kelvinBen/AppInfoScanner |
| 一款适用于以APP病毒分析、APP漏洞挖掘、APP开发、HW行动/红队/渗透测试团队为场景的移动端(Android、iOS)辅助分析工具 | https://github.com/sulab999/AppMessenger |
| apk爬虫工具可提取包内url等信息 | https://github.com/dwisiswant0/apkleaks |
| 安卓应用层抓包通杀脚本 | https://github.com/r0ysue/r0capture |
| 用于存取记录以前的基址和小程序文件 | https://github.com/eeeeeeeeee-code/wx-hook |



## 常用小工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ---------------------------------------------- |
| 好用的去重对比工具 | https://github.com/tomnomnom/anew |
| 视觉侦查工具，用于信息收集屏幕截图 | https://github.com/sensepost/gowitness |
| 一款jar包分析小工具 | https://github.com/4ra1n/jar-analyzer |
| 参数FUZZ小工具 | https://github.com/s0md3v/Arjun |
| 一款用于快速导出URL、Domain和IP的小工具 | https://github.com/mstxq17/MoreFind |
| Xtools 是一款 Sublime Text 插件，同时是一款简单的资产处理、命令行调用工具。 | https://github.com/chasingboy/Xtools |
| 对Web渗透项目资产进行快速存活验证 | https://github.com/AabyssZG/Web-SurvivalScan |
| 二进制文件切割&合并工具 | https://github.com/AabyssZG/BinaryCutting-Tool |
| 命令执行写任意文件，主要用于命令执行但不出网情况 | https://github.com/Ar3h/putter |
| 一个 CLASS 文件混淆工具，支持方法名/字段名/参数名引用分析和重命名混淆方式，支持字符串提取/整型异或混淆/垃圾代码花指令混淆/等方式，支持方法和字段的隐藏，配置简单，容易上手 | https://github.com/jar-analyzer/class-obf |



# 💣 漏洞利用工具

## 漏洞扫描框架/工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 高危漏洞精准检测与深度利用框架 | https://github.com/woodpecker-framework/woodpecker-framwork-release |
| 基于简单 YAML 的 DSL 的快速且可定制的漏洞扫描器。 | https://github.com/projectdiscovery/nuclei |
| afrog 是一款性能卓越、快速稳定、PoC 可定制化的漏洞扫描工具 | https://github.com/zan8in/afrog |
| EZ是一款集信息收集、端口扫描、服务暴破、URL爬虫、指纹识别、被动扫描为一体的跨平台漏洞扫描器。 | https://github.com/m-sec-org/EZ |
| 一款功能强大的安全评估工具 | https://github.com/chaitin/xray |
| 网络安全测试工具 | https://github.com/gobysec/Goby |
| 开源的远程漏洞测试框架 | https://github.com/knownsec/pocsuite3 |
| 全新的开源在线 poc 测试框架 | https://github.com/jweny/pocassist |
| 一个应用于web安全领域的漏洞批量扫描框架 | https://github.com/bigblackhat/oFx |
| 是一款 web 漏洞扫描和验证工具 | https://github.com/zhzyker/vulmap |
| 一款全面而强大的漏洞扫描和利用工具 | https://github.com/yhy0/Jie |
| 自动整合全网Nuclei的漏洞POC，实时同步更新最新POC！ | https://github.com/ExpLangcn/NucleiTP |
|  |  |

## 中间件/应用漏洞利用工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Spring漏洞综合利用工具 | https://github.com/savior-only/Spring_All_Reachable |
| 针对SpringBoot的开源渗透框架，以及Spring相关高危漏洞利用工具 | https://github.com/AabyssZG/SpringBoot-Scan |
| 一款java漏洞集合工具 | https://github.com/pureqh/Hyacinth |
| WeblogicTool，GUI漏洞利用工具，支持漏洞检测、命令执行、内存马注入、密码解密等（深信服深蓝实验室天威战队强力驱动） | https://github.com/KimJun1010/WeblogicTool |
| shiro 反序列 命令执行辅助检测工具 | https://github.com/wyzxxz/shiro_rce_tool |
| shiro反序列化漏洞综合利用,包含（回显执行命令/注入内存马）修复原版中NoCC的问题 | https://github.com/SummerSec/ShiroAttack2 |
| shiro反序列化漏洞综合利用,包含（回显执行命令/注入内存马） | https://github.com/j1anFen/shiro_attack |
| 复杂请求下的Shiro反序列化利用工具 | https://github.com/sma11new/Pyke-Shiro |
| Fastjson扫描器，可识别版本、依赖库、autoType状态等。 | https://github.com/a1phaboy/FastjsonScan |
|  |  |
| Jboss（和 Java 反序列化漏洞）验证和利用工具 | https://github.com/joaomatosf/jexboss |
| Dubbo反序列化一键快速攻击测试工具 | https://github.com/threedr3am/dubbo-exp |
| jenkins-attack-framework 针对 Jenkins 的攻击框架 | https://github.com/Accenture |
| 一款Jenkins的综合漏洞利用工具 | https://github.com/TheBeastofwar/JenkinsExploit-GUI |
| log4j漏洞利用工具 | https://github.com/kozmer/log4j-shell-poc |
| 一款针对Vcenter的综合利用工具，包含目前最主流的CVE-2021-21972、CVE-2021-21985以及CVE-2021-22005以及log4j，提供一键上传webshell，命令执行或者上传公钥使用SSH免密连接 | https://github.com/Schira4396/VcenterKiller |
| Vcenter综合渗透利用工具包-GUI | https://github.com/W01fh4cker/VcenterKit |
| WeblogicTool，GUI漏洞利用工具，支持漏洞检测、命令执行、内存马注入、密码解密等（深信服深蓝实验室天威战队强力驱动） | https://github.com/KimJun1010/WeblogicTool |
| Weblogic漏洞利用图形化工具 支持注入内存马、一键上传webshell、命令执行 | https://github.com/sp4zcmd/WeblogicExploit-GUI |
| Weblogic一键漏洞检测工具，V1.5，更新时间：20200730 | https://github.com/rabbitmask/WeblogicScan |
| weblogic 漏洞扫描工具。包含2020 | https://github.com/0xn0ne/weblogicScanner |
| woodpecker框架weblogic信息探测插件 | https://github.com/woodpecker-appstore/weblogic-infodetector |
| STS2G Struts2漏洞扫描利用工具 - Golang版 | https://github.com/xwuyi/STS2G |
| Struts2-Scan Struts2全漏洞扫描利用工具 | https://github.com/HatBoy/Struts2-Scan |
| Struts2全版本漏洞检测工具 by:ABC_123 | https://github.com/abc123info/Struts2VulsScanTools |
| Confluence-OGNL一键注入内存shell | https://github.com/BeichenDream/CVE-2022-26134-Godzilla-MEMSHELL |
| Confluence CVE 2021，2022，2023 利用工具，支持命令执行，哥斯拉，冰蝎 内存马注入 | https://github.com/Lotus6/ConfluenceMemshell |
| ResourcesYApi接口管理平台远程命令执行 | https://github.com/Tas9er/YApiRCE |
| Nacos JRaft Hessian 反序列化 RCE 加载字节码 注入内存马 不出网利用 | https://github.com/c0olw/NacosRce |
| Nacos漏洞综合利用GUI工具，集成了默认口令漏洞、SQL注入漏洞、身份认证绕过漏洞、反序列化漏洞的检测及其利用 | https://github.com/charonlight/NacosExploitGUI |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

## 重点cms利用工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | --------------------------------------------- |
| 高危漏洞利用工具 | https://github.com/White-hua/Apt_t00ls |
| OA漏洞利用工具，基于Apt-T00ls二次开发工具 | https://github.com/R4gd0ll/I-Wanna-Get-All |
| OA综合利用工具，集合将近20款OA漏洞批量扫描 | https://github.com/LittleBear4/OA-EXPTOOL |
| OAExploit一款基于产品的一键扫描工具。 | https://github.com/achuna33/MYExploit |
| 支持自定义Poc文件的图形化漏洞利用工具 | https://github.com/bcvgh/daydayEXP |
| 漏洞POC基本适用ThinkPHP全版本漏洞 | https://github.com/zangcc/Aazhen-RexHa |
| Thinkphp(GUI)漏洞利用工具，支持各版本TP漏洞检测，命令执行，getshell。 | https://github.com/Lotus6/ThinkphpGUI |
| ThinkPHP 漏洞 综合利用工具, 图形化界面, 命令执行, 一键getshell, 批量检测, 日志遍历, session包含, 宝塔绕过 | https://github.com/bewhale/thinkphp_gui_tools |
| 致远OA综合利用工具 | https://github.com/Summer177/seeyon_exp |
| 致远OA综合利用工具GUI-V1.0 | https://github.com/God-Ok/SeeyonExploit-GUI |
| 通达OA综合利用工具 | https://github.com/xinyu2428/TDOA_RCE |
| 蓝凌OA漏洞利用工具/前台无条件RCE/文件写入 | https://github.com/yuanhaiGreg/LandrayExploit |
| 泛微OA漏洞综合利用脚本 | https://github.com/z1un/weaver_exp |
| 泛微oa漏洞利用工具 | https://github.com/TD0U/WeaverScan |
| 帆软bi反序列化漏洞利用工具 | https://github.com/yecp181/Frchannel |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

## 信息泄露利用工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | --------------------------------------------------------- |
| 六大云存储，泄露利用检测工具 | https://github.com/UzJu/Cloud-Bucket-Leak-Detection-Tools |
| AK资源管理工具，阿里云/腾讯云 AccessKey AccessKeySecret | https://github.com/wyzxxz/aksk_tool |
| 阿里云accesskey利用工具 | https://github.com/mrknow001/aliyun-accesskey-Tools |
| swagger-exp Swagger  REST API 信息泄露利用工具 | https://github.com/lijiejie/swagger-exp |
| swagger-hack 自动化爬取并测试所有swagger-ui.html接口 | https://github.com/jayus0821/swagger-hack |
| heapdump敏感信息查询工具 | https://github.com/wyzxxz/heapdump_tool |
| HeapDump敏感信息提取工具 | https://github.com/whwlsfb/JDumpSpider |
| Packer Fuzzer  针对Webpack等前端打包工具所构造的网站进行检测的扫描工具 | https://github.com/rtcatc/Packer-Fuzzer |
| .git源代码泄露利用工具 | https://github.com/BugScanTeam/GitHack |
| .cvs源代码泄露利用工具 | https://github.com/kost/dvcs-ripper.git |
| .DS_store文件泄露利用工具 | https://github.com/lijiejie/ds_store_exp |
| SvnExploit支持SVN源代码泄露全版本Dump源码 | https://github.com/admintony/svnExploit |
| git-dumper 从网站转储git存储库的工具 | https://github.com/arthaud/git-dumper |
| GitDorker  通过使用大型的dorks库来从GitHub抓取敏感信息 | https://github.com/obheda12/GitDorker |
| 从JavaScript文件中提取敏感信息 | https://github.com/m4ll0k/SecretFinder |
| 功能比较多的一个JavaScript侦查自动化脚本 | https://github.com/KathanP19/JSFScan.sh |
| 子域名接管漏洞检测工具，支持30+云服务托管检测 | https://github.com/Ice3man543/SubOver |
| 一个小程序、公众号、企业微信、飞书、钉钉等泄露secert后利用工具 | https://github.com/mrknow001/API-Explorer |
| 互联网厂商API利用工具。 | https://github.com/pykiller/API-T00L |
| 混合盘APP - 网盘搜索、磁力搜索 - 搜索20个百度网盘、阿里网盘、夸克网盘以及磁力资源 | https://github.com/misiai/hunhepan |
| 云资产管理工具 目前工具定位是云安全相关工具，目前是两个模块 云存储工具、云服务工具， 云存储工具主要是针对oss存储、查看、删除、上传、下载、预览等等 云服务工具主要是针对rds、服务器的管理，查看、执行命令、接管等等 | https://github.com/dark-kingA/cloudTools |

## 数据库利用工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ---------------------------------------------- |
| MDUT 2.0 数据库利用工具 | https://github.com/SafeGroceryStore/MDUT |
| 数据库综合利用工具 | https://github.com/Ryze-T/Sylas |
| 综合高危漏洞利用工具(包含各大数据库) | https://github.com/Liqunkit/LiqunKit_ |
| 一款用Go语言编写的数据库自动化提权工具 | https://github.com/Hel10-Web/Databasetools |
| Team IDE 工具 集成MySql、Oracle、金仓、达梦、神通等数据库、SSH、FTP、Redis、Zookeeper、Kafka、Elasticsearch等管理工具 | https://github.com/team-ide/ |
| sqlserver利用工具，可上传下载文件，xp_cmdshell与sp_oacreate执行命令回显和clr加载程序集执行相应操作。 | https://github.com/uknowsec/SharpSQLTools |
| 通过套接字重用通过受损的 Microsoft SQL Server  在受限环境中执行横向移动 | https://github.com/blackarrowsec/mssqlproxy |
| ODAT：Oracle 数据库攻击工具 | https://github.com/quentinhardy/odat |
| Redis未授权访问漏洞利用工具 | https://github.com/n0b0dyCN/redis-rogue-server |
| Redis未授权访问漏洞利用工具2 | https://github.com/Ridter/redis-rce |
| Redis 漏洞利用工具 | https://github.com/yuyan-sec/RedisEXP |
| redis主从复制rce的go版本 | https://github.com/zyylhn/redis_rce |

## 爆破利用工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------ |
| 还是推荐fscan吧，还是还用，更新也快 | https://github.com/shadow1ng/fscan |
| zombie主要为了解决需要全场景(外网、内网、云)的服务的口令爆破功能 | https://github.com/chainreactors/zombie |
| 爆破神器，懂得都懂 | https://github.com/vanhauser-thc/thc-hydra |
| 超级弱口令检查工具是一款Windows平台的弱口令审计工具 | https://github.com/shack2/SNETCracker |
| FTP,SSH,MYSQL,MSSQL等弱口令爆破工具 | https://github.com/BBD-YZZ/week-passwd |
|  |  |
| 一款面向企业的渗透测试字典生成工具。 | https://github.com/ccc-f/Fdict |
| 爆破Azure, ADFS, OWA, O365, Teams，smtp | https://github.com/nodauf/GoMapEnum |
| Boom 是一款基于无头浏览器的智能 Web 弱口令（后台密码）爆破工具 | https://github.com/Fly-Playgroud/Boom |

## 全网字典收集

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ---------------------------------------------------------- |
| 用户名密码字典生成工具(将中文汉字姓名转成14种格式的拼音、IP地址处理、网络设备密码生成) | https://github.com/abc123info/UserNameDictTools |
| 该工具是使用javaFX开发的基于信息收集进行组合生成密码字典的工具，可以快速组成密码字典。 | https://github.com/kkbo8005/dicttools |
| 一个字典列表生成框架 | https://github.com/glitchedgitz/cook |
| 渗透测试、SRC漏洞挖掘、爆破、Fuzzing等字典收集项目 | https://github.com/insightglacier/Dictionary-Of-Pentesting |
| 1337 Wordlists for Bug Bounty Hunting | https://github.com/0xPugazh/fuzz4bounty |
| Fuzz 字典,一个就够了 | https://github.com/TheKingOfDuck/fuzzDicts |
| Web 模糊测试字典与一些Payloads | https://github.com/gh0stkey/Web-Fuzzing-Box |
| 安全评估期间使用的多种类型列表的集合 | https://github.com/danielmiessler/SecLists |
| 渗透测试仪和Bug赏金猎人的 Payload 库 | https://github.com/sh377c0d3/Payloads |
| 基于实战沉淀下的各种弱口令字典 | https://github.com/fuzz-security/SuperWordlist |
| 各类漏洞的 TOP25 参数字典 | https://github.com/lutfumertceylan/top25-parameter |
| 提取收集以往泄露的密码中符合条件的强弱密码 | https://github.com/r35tart/RW_Password |
| 实战沉淀字典 | https://github.com/SexyBeast233/SecDictionary |

## 常规漏洞利用工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Web 渗透测试 /CTF 的有用的payload大全 | https://github.com/swisskyrepo/PayloadsAllTheThings |
| 您将在其中找到我在 CTF、现实生活应用程序以及阅读研究和新闻中学到的每一个技巧 / 技巧 / 任何东西。 | https://github.com/HackTricks-wiki/hacktricks |
| DalFox 是一款功能强大的开源 XSS 扫描工具和参数分析器、实用工具 | https://github.com/hahwul/dalfox |
| 基于DOM的快速XSS漏洞扫描程序 | https://github.com/dwisiswant0/findom-xss |
| 一款基于 Chromium的XSS检测工具 | https://github.com/v8blink/Chromium-based-XSS-Taint-Tracking |
| 很常用的XSS平台 | https://github.com/beefproject/beef |
| Fast CRLF injection scanning tool | https://github.com/Nefcore/CRLFsuite |
| 快速 CORS 错误配置漏洞扫描程序 | https://github.com/chenjj/CORScanner |
| xxe利用工具 | https://github.com/BuffaloWill/oxml_xxe |
| xxe利用工具2 | https://github.com/whitel1st/docem |
| UEditor编辑器批量GetShell / Code By:Tas9er | https://github.com/Tas9er/UEditorGetShell |
| 子域名接管工具 | https://github.com/michenriksen/aquatone |
| 用于查找常见的Nginx错误配置和漏洞。 | https://github.com/stark0de/nginxpwner |
| 文件包含自动化利用工具 | https://github.com/hansmach1ne/lfimap |
| 文件包含利用工具 | https://github.com/mzfr/liffy |
| 具有交互式界面的自动 SSTI 检测工具 | https://github.com/vladko312/SSTImap |
| A simple SSRF-testing sheriff written in Go | https://github.com/teknogeek/ssrf-sheriff |
| SSRFmap，利用它可检测与利用 SSRF 漏洞， 同时它也整合了一些常用漏洞可以结合 SSRF 去利用 | https://github.com/swisskyrepo/SSRFmap |
| 用于测试、调整和破解JSON Web令牌的工具包 | https://github.com/ticarpi/jwt_tool |
| jwt hack是jwt黑客/安全测试的工具。支持En/解码JWT，生成JWT攻击和非常快速破解的有效载荷（dict/brutefoce） | https://github.com/hahwul/jwt-hack |
| XSS spider - 66/66 wavsep XSS detected | https://github.com/DanMcInerney/xsscrapy |
| 针对JWT渗透开发的漏洞验证/密钥爆破工具，针对CVE-2015-9235/空白密钥/未验证签名攻击/CVE-2016-10555/CVE-2018-0114/CVE-2020-28042的结果生成用于FUZZ，也可使用字典/字符枚举(包括JJWT)的方式进行爆破(JWT Crack) | https://github.com/z-bool/Venom-JWT |

## 反序列化利用工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| JYso是一个可以用于 jndi 注入攻击和生成反序列化数据流的工具。 | https://github.com/qi4L/JYso |
| 生成 Java 反序列化负载的概念验证 | https://github.com/Whoopsunix/PPPYSO |
| 项目为 ysoserial [su18] 专版，取名为 ysuserial ，在原项目 [ysoserial](https://github.com/frohoff/ysoserial) 基础上魔改而来 | https://github.com/su18/ysoserial/ |
| 图形化Java反序列化利用工具，集成Ysoserial | https://github.com/0ofo/Deswing |
| jndi注入工具v1.4 | https://github.com/WhiteHSBG/JNDIExploit |
| JNDI服务利用工具 RMI/LDAP，支持部分场景回显、内存shell，高版本JDK场景下利用等，fastjson rce命令执行，log4j rce命令执行 漏洞检测辅助工具 | https://github.com/wyzxxz/jndi_tool |
| TopicsYsomap是一款适配于各类实际复杂环境的Java反序列化利用框架，可动态配置具备不同执行效果的Java反序列化利用链payload。 | https://github.com/wh1t3p1g/ysomap |
| 原版反序列化利用工具 | https://github.com/frohoff/ysoserial |
| ysoserial修改版，着重修改`ysoserial.payloads.util.Gadgets.createTemplatesImpl`使其可以通过引入自定义class的形式来执行命令、内存马、反序列化回显 | https://github.com/Y4er/ysoserial |
| 魔改版ysoserial，有更多方便的命令 | https://kgithub.com/woodpecker-framework/ysoserial-for-woodpecker |
| 解决FastJson、Jackson、Log4j2、原生JNDI注入漏洞的高版本JDKBypass利用，探测本地可用反序列化gadget达到命令执行、回显命令执行、内存马注入 | https://github.com/exp1orer/JNDI-Inject-Exploit |
| MySQL Fake Server (纯Java实现，内置常见Java反序列化Payload，支持GUI版和命令行版，提供Dockerfile) | https://github.com/4ra1n/mysql-fake-server |
| rmi打内存马工具，适用于目标用不了ldap的情况 | https://github.com/novysodope/RMI_Inj_MemShell |
| marshalsec是一款java反序列利用工具，其可以很方便的起一个ldap或rmi服务，通过这些服务来去访问攻击者准备好的恶意执行类来达到远程命令执行或入侵的目的。 | https://github.com/mbechler/marshalsec |
| 使用 agent 实现反序列化 utf8 overlong | https://github.com/Ar3h/utf8-overlong-agent |

## 内存马注入工具

| 项目简介 | 项目地址 |
| ---------------------------------------- | ---------------------------------------------------------- |
| 一款支持高度自定义的 Java 内存马生成工具 | https://github.com/pen4uin/java-memshell-generator-release |
| Java内存马注入工具 | https://github.com/WisteriaTiger/JundeadShell |
| 拿来即用的Tomcat内存马 | https://github.com/ce-automne/TomcatMemShell |
| Memory WebShell Generator | https://github.com/hosch3n/msmap |
| 用Java agent实现内存马等功能 | https://github.com/ethushiroha/JavaAgentTools |
| 多功能 java agent 内存马 | https://github.com/veo/vagent |



## 代码审计辅助工具-通用

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------------- |
| 这是一个调用chatGPT进行代码审计的工具。 | https://github.com/Kento-Sec/chatGPT-CodeReview |
| 源代码静态分析工具，支持Java、PHP、C#、Python、Go等27种编程语言，而且能够集成在IDE、Jenkins、Git等服务。 | https://www.sonarqube.org |
| 一种适用于 C++、C#、VB、PHP、Java、PL/SQL 和 COBOL 的自动化代码安全审查工具。 | https://sourceforge.net/projects/visualcodegrepp/ |
| 开源安全产品源码，IDS、IPS、WAF、蜜罐等 | https://github.com/birdhan/SecurityProduct |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |



## 代码审计辅助工具-java

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 一个用于分析Jar包的GUI工具，可以用多种方式搜索你想要的信息，自动构建方法调用关系，支持分析Spring框架（A Java GUI Tool for Analyzing Jar） | https://github.com/4ra1n/jar-analyzer-gui |
| 一款轻量级匹配Sink点的代码审计扫描器，为了帮助红队过程中快速代码审计的小工具 | https://github.com/Zjackky/CodeScan |
| “铲子”是一款简单易用的JAVA SAST工具，旨在为安全工程师提供一款简单、好用、价格厚道的代码安全扫描产品，支持语言: java（Servlet、spring、dubbo、thirft、mybatis、jsp） ，采用轻量级污点分析，铲子会将java、xml（mybatis、dubbo）等统一构建数据流图，然后进行污点分析，无需编译，也可以反编译扫描jar或class，内置了 sql 注入、命令注入、文件上传、ssrf 等常见漏洞规则，用户可以自定义规则。 | https://github.com/Chanzi-keji/chanzi |
| `SecurityInspector` 是一个静态代码扫描插件，内置了常见的`Java` 代码`Web`漏洞`sink` 点，高危组件调用`sink` 点，识别项目中可能存在的过滤器（如`XSS`过滤器、`SQLI`过滤器等<此功能存在较多`bug` ，将会于正式版上线>），并使用`IDEA`的`PSI` 和`Intercept`机制来对以上内容进行快速定位。 | https://github.com/SpringKill-team/SecurityInspector |
| JavaWeb漏洞审计工具，构建方法调用链并模拟栈帧进行分析 | https://github.com/4ra1n/code-inspector |
| 闭源系统半自动漏洞挖掘工具，针对 jar/war/zip 进行静态代码分析，增加 LLM 大模型能力验证路径可达性，LLM 根据上下文代码环境给出该路径可信分数 | https://github.com/Phelaine/SinkFinder |
| 开源的被动式交互式安全测试(IAST)产品 | https://github.com/HXSecurity/DongTai |
| CodeQLpy是一款基于CodeQL实现的半自动化代码审计工具，目前仅支持java语言。实现从源码反编译，数据库生成，脆弱性发现的全过程，可以辅助代码审计人员快速定位源码可能存在的漏洞。 | https://github.com/webraybtl/CodeQLpy |
| 免费开源的语义代码分析引擎和查询工具 | https://github.com/github/codeql-cli-binaries |
| Java Web应用安全漏洞自动化发现-idea插件 | https://github.com/find-sec-bugs/find-sec-bugs/wiki/IntelliJ-Tutorial |
| IDEA依赖检查插件 | https://github.com/jeremylong/DependencyCheck |
| TABBY 是一个基于[Soot](https://github.com/soot-oss/soot)的 Java 代码分析工具。 | https://github.com/wh1t3p1g/tabby |
| 一个静态代码脆弱性检测系统，支持java源码的审计 | https://github.com/zsdlove/Hades |
| IDEA静态代码安全审计及漏洞一键修复插件 | https://github.com/momosecurity/momo-code-sec-inspector-java |
| IDEA代码审计辅助插件（深信服深蓝实验室天威战队强力驱动） | https://github.com/KimJun1010/inspector?tab=readme-ov-file |
| 一款无需解压直接编辑修改jar包内文件的IDEA插件 | https://github.com/Liubsyy/JarEditor |
| JADX-GUI-AI 是一个在 JADX 基础上增强的智能反编译工具，集成了 AI 辅助功能，可以帮助开发者更好地理解和分析反编译后的代码 | https://github.com/cncsnet1/jadx-gui-ai |
|  |  |
|  |  |

## 代码审计辅助工具-php

| 项目简介 | 项目地址 |
| --------------------------------------------------------- | ------------------------------------------------------------ |
| Seay源代码审计系统 | https://github.com/f1tz/cnseay |
| 查找PHP代码漏洞工具 | https://github.com/ecriminal/phpvuln |
| 一款不错的静态源代码分析工具，主要用来挖掘PHP程序的漏洞。 | [http://rips-scanner.sourceforge.net](http://rips-scanner.sourceforge.net/) |



## 代码审计辅助工具-dotNET

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | --------------------------------------------- |
| NETReactorSlayer一款反混淆神器，适用于Eziriz .NET Reactor工具混淆后的代码，最新版本6.4 | https://github.com/SychicBoy/NETReactorSlayer |
|  |  |
|  |  |







## 通用型WAF绕过

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ---------------------------------------- |
| 绕过瑞数waf的动态验证机制，实现请求包重放，可针对不同网站使用。 | https://github.com/R0A1NG/Botgate_bypass |
| 一个基于fuzz的waf绕过测试工具，当前支持命令执行、SQL注入绕过。 | https://github.com/leveryd/x-waf |







# 🏰 内网渗透工具

## 后渗透辅助工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ----------------------------------------------- |
| 一款轻量级的杀软在线识别的项目 | https://github.com/Aabyss-Team/Antivirus-Scan |
| 在线 Windows 操作系统常见杀软进程/办公软件/shell终端等识别，输入 tasklist /SVC 将内容粘贴 | https://forum.ywhack.com/bountytips.php?process |
| **杀软在线对比** | http://bypass.tidesec.com/bycms |
| 高价值系统的后利用工具 | https://github.com/0linlin0/XPost |
|  |  |





## webshell管理工具

| 项目简介 | 项目地址 |
| -------------------------------------- | ------------------------------------------------- |
| 哥斯拉 | https://github.com/BeichenDream/Godzilla |
| “冰蝎”动态二进制加密网站管理客户端 | https://github.com/rebeyond/Behinder |
| 中国蚁剑是一款开源的跨平台网站管理工具 | https://github.com/AntSwordProject/antSword |
| 一句话WEB端管理工具 | https://github.com/boy-hack/WebshellManager |
| 跨平台版中国菜刀 | https://github.com/Chora10/Cknife |
| 用于生成各类免杀webshell | https://github.com/cseroad/Webshell_Generate |
| 从零学习Webshell免杀手册 | https://github.com/AabyssZG/WebShell-Bypass-Guide |
| webshell收集项目，项目涵盖各种常用脚本 | https://github.com/tennc/webshell |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

## c2管理工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ---------------------------------------------------- |
| cs4.4修改去特征狗狗版(美化ui,去除特征,自带bypass核晶截图等..) | https://github.com/TryGOTry/DogCs4.4/tree/dogcs_v2.1 |
| 跨平台重构了Cobaltstrike Beacon，目前实现的功能具备免杀性，可过Defender、360核晶、卡巴斯基（除内存操作外，如注入原生cs的dll）、火绒 | https://github.com/H4de5-7/geacon_pro |
| 类似于cs | https://github.com/t3l3machus/Villain |
| 是一个 C2前流控制工具，可以避免蓝队，AVs，EDR 检查 | https://github.com/wikiZ/RedGuard |
| 一款可以在不出网的环境下进行反向代理及cs上线的工具 | https://github.com/Daybr4ak/C2ReverseProxy |
| 该工具易于使用，它生成自己的 PowerShell 有效负载并支持加密 (ssl)。 | https://github.com/t3l3machus/hoaxshell |
| 反弹shell就用这个 | https://github.com/WangYihang/Platypus |
| PingRAT使用ICMP有效载荷通过防火墙秘密传递C2流量。 | https://github.com/umutcamliyurt/PingRAT |
| Empire 是一个后利用和对手模拟框架，用于帮助红队和渗透测试人员。 | https://github.com/BC-SECURITY/Empire |
| Metasploit（MSF）是一个免费的、可下载的框架，通过它可以很容易地获取、开发并对计算机软件漏洞实施攻击。 | https://github.com/rapid7/metasploit-framework |
|  |  |



## 提权项目

| 项目简介 | 项目地址 |
| --------------------------------------------------------- | --------------------------------------- |
| Linux自动提权 | https://github.com/liamg/traitor |
| 提权辅助页 | https://i.hacking8.com/tiquan/ |
| 全平台系统提权辅助工具 | https://github.com/carlospolop/PEASS-ng |
| 一个聚合了linux、windows、macOS的提权漏洞合集，带复现过程 | https://github.com/Ascotbe/Kernelhub |

## 内网扫描工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------ |
| Fscan 一款内网综合扫描工具，方便一键自动化、全方位漏扫扫描。 | https://github.com/shadow1ng/fscan |
| 一款快速探测内网可达网段工具（深信服深蓝实验室天威战队强力驱动） | https://github.com/shmilylty/netspy |
| 下一代RedTeam启发式内网扫描 | https://github.com/1n7erface/Template |
| 内网资产收集、探测主机存活、端口扫描、域控定位、文件搜索、各种服务爆破（SSH、SMB、MsSQL等）、Socks代理，一键自动化+无文件落地扫描 | https://github.com/INotGreen/SharpScan |
| 一个速度极快的内网扫描器，具备端口扫描、协议检测、指纹识别，暴力破解，漏洞探测等功能。支持协议1200+，协议指纹10000+，应用指纹20000+，暴力破解协议10余种 | https://github.com/qi4L/qscan |
| 一款更高、更快、更强的全方位内网扫描工具 | https://github.com/P001water/P1soda |
| Ladon一款用于大型网络渗透的多线程插件化综合扫描神器 | https://github.com/k8gege/Ladon |
| 一款快速探测内网主机信息工具（深信服深蓝实验室天威战队强力驱动） | https://github.com/shmilylty/SharpHostInfo |
| 红队小工具 ，利用DCERPC协议获取Windows机器主机信息和多网卡信息 | https://github.com/Y0-kan/HostInfoScan |
| ATAttack是一款后渗透半自动化侦察工具，它从进攻性和防御性安全角度执行许多面向安全性的主机调查“安全检查”。 | https://github.com/c1y2m3/ATAttack |
| 集权设施扫描器 | https://github.com/Amulab/CAudit |
|  |  |



## 本机收集工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ---------------------------------------------- |
| GodInfo 是一个功能全面的后渗透信息和凭据收集工具，旨在帮助安全测试人员在获得授权访问权限后，快速收集目标系统的信息和凭据。 | https://github.com/Conan924/GodInfo |
| 支持自动化一键 Hunting 主机各类关键信息和凭据，降低后渗透阶段操作的割裂感，有效拓宽后渗透攻击面 | https://github.com/lintstar/SharpHunter |
| 该工具主要用于后渗透方面 | https://github.com/eeeeeeeeee-code/e0e1-config |
| Pillager是一个适用于后渗透期间的信息收集工具，可以收集目标机器上敏感信息，方便下一步渗透工作的进行。 | https://github.com/qwqdanchun/Pillager |
| 强大的敏感信息搜索工具 | https://github.com/Naturehi666/searchall |
| 通用的数据库连接配置信息提取工具 | https://github.com/corener/JavaPassDump |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |



## 横向移动工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | -------------------------------------------------- |
| 横向impacket工具包 | https://github.com/fortra/impacket |
| 基于impacket的免杀横向渗透远程命令执行工具（推荐）。 | https://github.com/XiaoliChan/wmiexec-Pro |
| WMIHACKER是一款免杀横向渗透远程命令执行工具。 | https://github.com/rootclay/WMIHACKER |
| 基于golang实现的impacket | https://github.com/Amzza0x00/go-impacket |
| 工具基于 CrackMapExec,针对大型Windows活动目录(AD)的后渗透工具 | https://github.com/Pennyw0rth/NetExec |
| 一款比较好的CS后渗透模块插件 | https://github.com/pandasec888/taowu-cobalt-strike |
| 一款CS后渗透模块插件，让大家使用一款插件就够了 | https://github.com/d3ckx1/OLa |
| 常见横向移动与域控权限维持方法 | https://xz.aliyun.com/t/9382 |
| 绕过虚拟机登录验证屏幕的工具 | https://github.com/hzphreak/VMInjector |
|  |  |
|  |  |
|  |  |
|  |  |

## 域渗透工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------ |
| 检测域环境内，域机器的本地管理组成员是否存在弱口令和通用口令，对域用户的权限分配以及域内委派查询 | https://github.com/0x727/ShuiYing_0x727 |
| 一个强大的内网域渗透分析工具，构建于 Linkurious 之上 | https://github.com/BloodHoundAD/BloodHound |
| 域内自动化信息搜集利用工具 | https://github.com/wjlab/Darksteel |
|  |  |
|  |  |



## 密码提取工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------------- |
| Mimikatz  Windows 密码抓取神器 | https://github.com/gentilkiwi/mimikatz |
| 各种密码提取 | https://github.com/kerbyj/goLazagne |
| 用于读取常用程序密码，如Navicat、TeamViewer、FileZilla、WinSCP等 | https://github.com/RowTeam/SharpDecryptPwd |
| Xshell，Xftp密码解密工具 | https://github.com/JDArmy/SharpXDecrypt |
| 解密浏览器数据（密码\ | 历史记录\ | 书签 \ | 信用卡 \ | 下载记录）的导出工具，支持全平台主流浏览器。 | https://github.com/moonD4rk/HackBrowserData/ | HackBrowserData |
| HackBrowserData的偏手动版，用于绕过特定情况下edr的限制 | https://github.com/Z3ratu1/HackBrowserDataManual |
| 一款针对向日葵的识别码和验证码提取工具 | https://github.com/wafinfo/Sunflower_get_Password |
| 一键辅助抓取360安全浏览器密码的CobaltStrike脚本以及解密小工具 | https://github.com/hayasec/360SafeBrowsergetpass |
| BrowserGhost  抓取浏览器密码的工具 | https://github.com/QAX-A-Team/BrowserGhost |
| win-brute-logon  无需权限破解任何 Microsoft Windows 用户密码 | https://github.com/DarkCoderSc/win-brute-logon |
| TeamViewer：Bypass杀软 获取 Teamview 密码的工具 | https://github.com/wafinfo/TeamViewer |
| Xdecrypt Xshell  Xftp 密码解密 | https://github.com/dzxs/Xdecrypt |
| 微信客户端取证，可获取用户个人信息(昵称/账号/手机/邮箱/数据库密钥(用来解密聊天记录))；支持获取多用户信息 | https://github.com/AdminTest0/SharpWxDump |
| FakeLogonScreen 是一个伪造 Windows 登录屏幕以获取用户密码的实用程序。输入的密码将根据 Active Directory 或本地计算机进行验证，以确保其正确，然后显示到控制台或保存到磁盘。 | https://github.com/bitsadmin/fakelogonscreen |
| 提取微信聊天记录，将其导出成HTML、Word、CSV文档永久保存，对聊天记录进行分析生成年度聊天报告 | https://github.com/LC044/WeChatMsg |
|  |  |
|  |  |

## 隧道代理工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ---------------------------------------------------- |
| 全平台代理工具，支持多种socks协议 | https://www.proxifier.com/ |
| 开源的跨平台对手仿真/红队框架 | https://github.com/BishopFox/sliver |
| 专注于内网穿透的高性能的反向代理应用 | https://github.com/fatedier/frp |
| Erfrp-frp二开-免杀与隐藏 | https://github.com/Goqi/Erfrp |
| 基于frp-0.58.1魔改二开，随机化socks5账户密码及端口、钉钉上线下线通知、配置文件oss加密读取、域前置防止溯源、源码替换/编译混淆等 | https://github.com/CodeSecurityTeam/frp |
| 一款golang写的支持http与socks5的端口复用小工具，并且可以开启socks5代理。 | https://github.com/TryGOTry/multiplexing_port_socks5 |
| 修改frp支持域前置与配置文件自删除 | https://github.com/uknowsec/frpModify |
| 轻量级、高性能、功能强大的内网穿透代理服务器 | https://github.com/ehang-io/nps |
| 改进的reGeorg版本 | https://github.com/L-codes/Neo-reGeorg |
| 是一款利用dns协议传输tcp数据的工具 | https://github.com/alex-sector/dns2tcp |
| 是一个DNS隧道工具 | https://github.com/iagox86/dnscat2 |
| 一个简单的 reverse ICMP shell | https://github.com/inquisb/icmpsh |
| pingtunnel 是把 tcp/udp/sock5 流量伪装成 icmp  流量进行转发的工具 | https://github.com/esrrhs/pingtunnel |
| 正/反向代理，内网穿透，端口转发 | https://github.com/inconshreveable/ngrok |
| pystinger - 一款使用webshell进行流量转发的出网工具 | https://github.com/FunnyWolf/pystinger |
| goproxy 一款轻量级、功能强大、高性能的多种代理工具 | https://github.com/snail007/goproxy |
| 内网渗透代理、端口转发工具 | http://rootkiter.com/Termite/ |
| golang 实现的windows and linux 端口复用工具。 | https://github.com/p1d3er/port_reuse |
| grs内网穿透工具通过reality协议隐藏特征 | https://github.com/howmp/reality |
|  |  |

## 优秀免杀项目

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ---------------------------------------------- |
| 免杀shellcode加载器，使用go实现，免杀bypass火绒、360、核晶、def等主流杀软 | https://github.com/Pizz33/GobypassAV-shellcode |
| 重写免杀版Gh0st远控、大灰狼远控免杀，目前可免杀360、火绒、腾讯电脑管家等主流杀软。 | https://github.com/SecurityNo1/Gh0st2023 |
| TideSec团队整理的远控免杀系列文章及配套工具，汇总测试了互联网上的几十种免杀工具。 | https://github.com/TideSec/BypassAntiVirus |
| 跟杀软和免杀有关的资料，当前包括200+工具和1300+文章  --Thanks:小雨 | https://github.com/alphaSeclab/anti-av |
| 借助Win-PS2EXE项目编写cna脚本方便快速生成免杀可执行文件 | https://github.com/cseroad/bypassAV |
| 在线免杀平台 | http://bypass.tidesec.com/web/ |
| 掩日 - 免杀执行器生成工具 用于快速生成免杀的 EXE 可执行文件 | https://github.com/1y0n/AV_Evasion_Tool |
| 自动化生成 EDR 软件 Bypass Payload 的工具,一键化签名免杀 | https://github.com/optiv/ScareCrow |
| 梅花K战队写的Nim一键免杀源码 使用nim语言进行shellcode加载 | https://github.com/M-Kings/BypassAv-web |
| 一键窃取文件的图标、资源信息、版本信息、修改时间、数字签名，降低程序熵值 | https://github.com/INotGreen/SharpThief |
| 助力每一位RT队员，快速生成免杀木马 | https://github.com/wangfly-me/LoaderFly |
| 自动化找白文件，用于扫描 EXE 文件的导入表，列出导入的DLL文件，并筛选出非系统DLL，符合条件的文件将被复制到特定的 X64 或 X86 文件夹 | https://github.com/ImCoriander/ZeroEye |

## 权限维持工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | -------------------------------------- |
| 创建隐藏计划任务，权限维持，Bypass AV | https://github.com/0x727/SchTask_0x727 |
| 进行克隆用户、添加用户等账户防护安全检测的轻巧工具 | https://github.com/0x727/CloneX_0x727 |
| ridhijack是一款通过C/C++实现的RID劫持、影子账户、账户克隆工具。 | https://github.com/yanghaoi/ridhijack |
|  |  |

# 🏗️ 基础设施搭建

## 攻防环境部署

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------------ |
| Windows11 Penetration Suite Toolkit 一个开箱即用的windows渗透测试环境 | https://github.com/arch3rPro/Pentest-Windows |
| 红/蓝队环境自动化部署工具 | https://github.com/ffffffff0x/f8x |
| 适合每个人的动态基础设施框架，轻松分配许多不同扫描工具的工作量，包括nmap、ffuf、masscan、核、meg等！ | https://github.com/pry0cc/axiom |
| DNSLOG平台 golang 一键启动版 | https://github.com/yumusb/DNSLog-Platform-Golang |
| 反连助手：发现可以映射本地端口的互联网IP，本工具可从hunter、quake、fofa等网络空间测绘平台，收集、探测互联网IP，并通过配置文件中的端口映射关系，把本地端口映射到互联网IP指定的端口，以便反弹shell等场景下使用。 | https://github.com/thinkoaa/Dlam |
|  |  |

## 代理池

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ---------------------------------------- |
| 一款功能强大的代理检查和IP地址轮转工具 | https://github.com/kitabisa/mubeng |
| deadpool代理池工具，可从hunter、quake、fofa等网络空间测绘平台取高质量socks5代理，或本地导入socks5代理，轮询使用代理进行流量转发。 | https://github.com/thinkoaa/Deadpool |
| 利用fofa搜索socks5开放代理进行代理池轮切的工具 | https://github.com/akkuman/rotateproxy |
| 利用IP地址池进行自动切换Http代理，防止IP封禁。 | https://github.com/Mustard404/Auto_proxy |
| 命令行全局代理--跨平台通用 | https://github.com/rofl0r/proxychains-ng |
| Python爬虫代理IP池(proxy pool) | https://github.com/jhao104/proxy_pool |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

## 靶场清单

通用漏洞类：

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ---------------------------------------------------- |
| 在线靶场 | https://hackmyvm.eu/anon/ |
| Vulfocus 是一个漏洞集成平台，将漏洞环境 docker 镜像，放入即可使用，开箱即用。 | https://github.com/fofapro/vulfocus |
| 基于 Docker-Compose 的预建易受攻击环境 | https://github.com/vulhub/vulhub |
| Spring Boot 相关漏洞学习资料，利用方法和技巧合 | https://github.com/LandGrey/SpringBootVulExploit |
| TerraformGoat 是一个支持多云的云场景漏洞靶场搭建工具，目前支持阿里云、腾讯云、华为云、Amazon Web Services、Google Cloud Platform、Microsoft Azure 六个云厂商的云场景漏洞搭建。 | https://github.com/HXSecurity/TerraformGoat |
| Metarget的名称来源于`meta-`（元）加`target`（目标，靶机），是一个脆弱基础设施自动化构建框架，主要用于快速、自动化搭建从简单到复杂的脆弱云原生靶机环境。 | https://github.com/Metarget/metarget |
| 一个故意易受攻击的CI/CD环境。通过多种挑战学习CI/CD安全性。 | https://github.com/cider-security-research/cicd-goat |
| 一个免费的云本地安全学习实验室列表，包括 CTF、自主研讨会、指导漏洞实验室和研究实验室。 | https://github.com/iknowjason/Awesome-CloudSec-Labs |
| GOAD是一个渗透测试活动目录实验室项目。该实验室的目的是为pentesters提供一个易受攻击的活动目录环境，以便用于练习通常的攻击技术。 | https://github.com/Orange-Cyberdefense/GOAD |

基础漏洞类：

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| FastJson全版本Docker漏洞环境(涵盖1.2.47/1.2.68/1.2.80等版本)，主要包括JNDI注入及高版本绕过、waf绕过、文件读写、原生反序列化、利用链探测绕过、不出网利用等。从黑盒的角度覆盖FastJson深入利用 | https://github.com/lemono0/FastJsonParty |
| 基础漏洞靶场 | https://dvwa.co.uk/ |
| 常见的web漏洞 | https://www.pentesterlab.com/exercises/web_for_pentester/course |
| Java漏洞平台 | https://github.com/j3ers3/Hello-Java-Sec |
| JAVA 漏洞靶场 | https://github.com/tangxiaofeng7/SecExample |
| 一个想帮你总结所有类型的上传漏洞的靶场 | https://github.com/c0ny1/upload-labs |
| SQLI 实验室测试基于错误、基于布尔值、基于时间。 | https://github.com/Audi-1/sqli-labs |
| 一个包含php,java,python,C#等各种语言版本的XXE漏洞Demo | https://github.com/c0ny1/xxe-lab |



## 漏洞订阅&安全推送

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 一个高价值漏洞采集与推送服务 | collect valueable vulnerability and push ithttps://github.com/zema1/watchvuln |
| 一个基于✨HOOK机制的微信机器人，支持🌱安全新闻定时推送【FreeBuf，先知，安全客，奇安信攻防社区】 | https://github.com/ngc660sec/NGCBot |
| 一个方便安全研究人员获取每日安全日报的爬虫和推送程序，目前爬取范围包括先知社区、安全客、Seebug Paper、跳跳糖、奇安信攻防社区、棱角社区以及绿盟、腾讯玄武、天融信、360等实验室博客，持续更新中。 | https://github.com/Le0nsec/SecCrawler |
| Security-related Slide Presentation & Security Research Report（大安全各领域各公司各会议分享的PPT以及各类安全研究报告） | https://github.com/FeeiCN/Security-PPT |
| 实现对网络安全信息聚合，将安全相关的文章，数据，以及历届安全大会演讲的pptx,pdf进行了全文索引，方便检索。 | https://i.hacking8.com/forums/ |
| 网络安全相关的RSS订阅，帮助建立个人情报来源和日常知识库更新 更新频率: 每2个月一次 | https://github.com/zer0yu/CyberSecurityRSS |
| 记录了个人用到的一些获取国内安全资讯的RSS地址。均为中文，方便自己抓取关键字。还有部分大佬的博客。均不分前后。 | https://github.com/zhengjim/Chinese-Security-RSS/ |
| 这个仓库收集了所有在 GitHub 上能找到的 CVE 漏洞利用工具。 | https://github.com/XiaomingX/data-cve-poc |



# 运维&甲方&防守方工具

## 安全建设

| 项目简介 | 项目地址 |
| ------------------------------------------------ | ----------------------------------------------------- |
| 用于记录企业安全规划，建设，运营，攻防的相关资源 | https://github.com/AnyeDuke/Enterprise-Security-Skill |
| 暗网中文网监控爬虫(DEEPMIX) | https://github.com/s045pd/DarkNet_ChineseTrading |

## 应急响应笔记

| 项目简介 | 项目地址 |
| ------------------------------------------- | ------------------------------------------------------------ |
| 应急响应实战笔记，一个安全工程师的自我修养 | https://github.com/Bypass007/Emergency-Response-Notes |
| Linux/Windows/应急响应个人笔记 | https://github.com/wpsec/Emergency-response-notes |
| 应急响应指南 / emergency response checklist | https://github.com/theLSA/emergency-response-checklist |
| NOP-TEAM出品的Windows 应急响应手册 | https://github.com/Just-Hack-For-Fun/Windows-INCIDENT-RESPONSE-COOKBOOK |
|  |  |

## Linux应急响应工具

| 项目简介 | 项目地址 |
| --------------------------------------------------------- | ----------------------------------------------- |
| 主机侧Checklist的自动全面化检测脚本 | https://github.com/grayddq/GScan |
| linux信息收集/应急响应/常见后门/挖矿检测/webshell检测脚本 | https://github.com/al0ne/LinuxCheck |
| uroboros-一个GNU/Linux监视和概要分析工具，专注于单个进程 | https://github.com/evilsocket/uroboros |
| whohk linux下一款强大的应急响应工具 | https://github.com/heikanet/whohk |
| Malwoverview 是用于威胁搜寻的第一响应工具 | https://github.com/alexandreborges/malwoverview |
| Rootkit Hunter Rootkit猎手 | http://rkhunter.sourceforge.net/ |

## Windows应急响应工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| QDoctor是一款非传统意义上的ARK(Anti RootKit)工具。 | https://github.com/QAX-Anti-Virus/QDoctor |
| OpenArk是一款Windows平台上的开源Ark工具. Ark是Anti-Rootkit（对抗恶意程序）的简写, OpenArk目标成为逆向工程师、编程人员的工具，同时也能为那些希望清理恶意软件的用户服务。以后也将会支持更多功能和命令。 | https://github.com/BlackINT3/OpenArk |
| 一个类似于PChunter的多功能分析工具（PChunter已无法适用于最新版windwos） | https://github.com/ClownQq/YDArk/ |
| 包含一系列免费的系统分析工具，如Process Explorer、启动项分析工具 AutoRuns等。 | https://docs.microsoft.com/zh-cn/sysinternals/downloads/ |
| 一个免费，功能强大的多功能工具，可帮助您监视系统资源，调试软件和检测恶意软件。 | https://processhacker.sourceforge.io/ |
| 微软公司出品的日志分析工具，它功能强大，使用简单。 | https://www.microsoft.com/en-us/download/details.aspx?id=24659 |
| 火麒麟-网络安全应急响应工具(系统痕迹采集) | https://github.com/MountCloud/FireKylin |
| APT-Hunter Windows日志事件应急工具 | https://github.com/ahmedkhlief/APT-Hunter |
| 基于Go编写的windows日志分析工具 | https://github.com/Fheidt12/Windows_Log |
| 基于Memprocfs和Volatility的可视化内存取证工具 | https://github.com/Tokeii0/LovelyMem |

## webshell查杀工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ---------------------------------- |
| webshell查杀工具 | http://www.shelldetector.com/ |
| 河马webshell查杀 | https://www.shellpub.com/ |
| kunwu是新一代webshell检测引擎，使用了内置了模糊规则、污点分析模拟执行、机器学习三种高效的检测策略 | https://github.com/kunwu2023/kunwu |

## 内存马查杀工具

| 项目简介 | 项目地址 |
| ---------------------------------------------- | ---------------------------------------------- |
| Alibaba Java诊断利器Arthas | https://github.com/alibaba/arthas |
| 检测绝大部分所谓的内存免杀马 | https://github.com/huoji120/DuckMemoryScan |
| 通过jsp脚本扫描java web Filter/Servlet型内存马 | https://github.com/c0ny1/java-memshell-scanner |
| A java memory web shell extracting tool | https://github.com/LandGrey/copagent |
| 杀内存马的小工具 | https://github.com/r00t4dm/aLIEz |
|  |  |

## 防守辅助分析工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | -------------------------------------------------------- |
| **蓝队分析研判工具箱** | https://github.com/abc123info/BlueTeamTools |
| 一款基于 IP 信誉度信息实现的实时检测 Web 恶意流量的工具 | https://github.com/CRED-CLUB/ARTIF |
| 勒索病毒解密工具汇总 | https://github.com/jiansiting/Decryption-Tools/ |
| Shiro-Cookie解密小工具 | https://github.com/r00tuser111/SerializationDumper-Shiro |
| 这款工具是一款功能强大的网络安全综合工具，旨在为安全从业者、红蓝对抗人员和网络安全爱好者提供全面的网络安全解决方案。它集成了多种实用功能，包括解密、分析、扫描、溯源等，为用户提供了便捷的操作界面和丰富的功能选择。 | https://github.com/HotBoy-java/PotatoTool |

## 溯源反制工具

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------------ |
| 伪造Myslq服务端,并利用Mysql逻辑漏洞来获取客户端的任意文件反击攻击者 | https://github.com/BeichenDream/MysqlT |
| 检测目标Mysql数据库是不是蜜罐 | https://github.com/BeichenDream/WhetherMysqlSham |
| 安全、快捷、高交互、企业级的蜜罐管理系统，护网；支持多种协议蜜罐、蜜签、诱饵等功能。 | https://github.com/seccome/Ehoney |
|  |  |
|  |  |





# 📚 其他安全资料整理

## JAVA安全研究

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------------------- |
| 【三万字原创】完全零基础从0到1掌握Java内存马，公众号：追梦信安 | https://github.com/W01fh4cker/LearnJavaMemshellFromZero |
| 该项目旨在竭尽所能的以简洁清晰的方式分享`Java安全`相关技术，将某些复杂的技术问题简单化，让更多的人能够学会`Java安全`。 | https://github.com/javaweb-sec/javaweb-sec |
| 抽离出 utf-8-overlong-encoding 的序列化逻辑，实现 2 3 字节加密序列化数组 | https://github.com/Whoopsunix/utf-8-overlong-encoding |
| A list for Web Security and Code Audit | https://github.com/ax1sX/SecurityList |
| 实战场景较通用的 Java Rce 相关漏洞的利用方式 | https://github.com/Whoopsunix/JavaRce |
| Web-Security-Learning | https://github.com/CHYbeta/Web-Security-Learning |
| 一款更利于全面学习内存马的注入工具 | https://github.com/ReaJason/MemShellParty |

## AI-LLM相关资料

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ----------------------------------------------------------- |
| 大模型学习导航 | https://github.com/Y4tacker/LLM-Navigation |
| Ai迷思录（应用与安全指南） | https://github.com/Acmesec/theAIMythbook |
| Prompt越狱手册 | https://github.com/Acmesec/PromptJailbreakManual/ |
| 通过各厂商大模型应用中已公开的信息挖掘潜在的安全问题并公开一些技术细节 | https://github.com/LLM-Red-Team |
| AIGC 求职面经、必备基础知识、提示词工程、ChatGPT、Stable Diffusion、Prompt、Embedding、Fintune 等 AIGC 求职你所需要知道的一切~ | https://github.com/EmbraceAGI/AIGC_Interview |
| 《AI 研发提效：构建 AI 辅助编码助手》 | https://github.com/unit-mesh/build-your-ai-coding-assistant |
| MCP-SecurityTools 是一个专注于收录和更新网络安全领域 MCP 的开源项目，旨在汇总、整理和优化各类与 MCP 相关的安全工具、技术及实战经验。 | https://github.com/Ta0ing/MCP-SecurityTools |
| 面向基于MCP的AI工具的综合安全检查清单。由SlowMist构建，以保障大语言模型插件生态系统的安全。 | https://github.com/slowmist/MCP-Security-Checklist |



## 安全面试

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | ------------------------------------------------ |
| 一个2023届毕业生在毕业前持续更新、收集的安全岗面试题及面试经验分享~ | https://github.com/vvmdx/Sec-Interview-4-2023 |
| 网络信息安全从业者面试指南 | https://github.com/FeeiCN/SecurityInterviewGuide |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

## 实战红蓝资料集锦

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | --------------------------------------------- |
| 红蓝对抗以及护网相关工具和资料，内存shellcode（cs+msf）和内存马查杀工具 | https://github.com/Mr-xn/RedTeam_BlueTeam_HW |
| 重生之我是赏金猎人系列，分享自己和团队在SRC、项目实战漏洞测试过程中的有趣案例 | https://github.com/J0o1ey/BountyHunterInChina |
| 国外蓝队攻防知识库 | https://github.com/Purp1eW0lf/Blue-Team-Notes |
|  |  |

## 云安全资料

| 项目简介 | 项目地址 |
| ------------------------------------------------------------ | --------------------------------------------------------- |
| 也许这是国内第一个云安全知识文库 | https://wiki.teamssix.com/About/ |
| 从零开始的Kubernetes攻防 | https://github.com/neargle/my-re0-k8s-security |
| KubeHound 是一个专为 Kubernetes 设计的工具，它通过自动化的方式计算集群内资源之间的潜在攻击路径。这一工具的核心价值在于其能够提供全面的集群扫描，生成直观的攻击图，并提出针对性的保护策略。 | https://github.com/DataDog/KubeHound |
| CDK是一款为容器环境定制的渗透测试工具，在已攻陷的容器内部提供零依赖的常用命令及PoC/EXP。集成Docker/K8s场景特有的 逃逸、横向移动、持久化利用方式，插件化管理 | https://github.com/cdk-team/CDK |
| 云资产管理工具 目前工具定位是云安全相关工具，目前是两个模块 云存储工具、云服务工具， 云存储工具主要是针对oss存储、查看、删除、上传、下载、预览等等 云服务工具主要是针对rds、服务器的管理，查看、执行命令、接管等等 | https://github.com/dark-kingA/cloudTools |
| 六大云存储，泄露利用检测工具 | https://github.com/UzJu/Cloud-Bucket-Leak-Detection-Tools |
| 云环境利用框架 Cloud Exploitation Framework 方便红队人员在获得 AK 的后续工作 | https://github.com/teamssix/cf |
| 云漏洞扫描工具 | https://github.com/Rnalter/ThunderCloud |
| 云渗透测试工具包 | https://github.com/404tk/cloudtoolkit |

------
如果你有更好的提议或者其他想法，欢迎联系。

by--L0una(guchangan1)
