# All-Defense-Tool
​	 首先恭喜你发现了宝藏。本项目集成了全网优秀的开源攻防武器项目，包含信息收集工具（自动化利用工具、资产发现工具、目录扫描工具、子域名收集工具、指纹识别工具、端口扫描工具、各种插件....etc...），漏洞利用工具（各大CMS、OA利用工具、中间件利用工具、反序列化利用工具、数据库利用工具等项目........），内网渗透工具（隧道代理、密码提取、木马免杀、域渗透.....）、应急响应工具、甲方运维工具、等其他安全攻防资料整理，供攻防双方使用。

​	**工欲善其事必先利其器，不知道有哪些工具，不会用工具，不懂工具原理，怎么写出适合自己的工具？**

## 免责声明

**重点提醒：本项目工具来源于互联网，是否含带木马及后门请自行甄别！！Hvv来即，请大家提高警惕！！！**

1. `本项目所有内容,仅供学习和研究使用,请勿使用项目的技术手段用于非法用途,任何人造成的任何负面影响,与本人无关.`
2. `本文档所有内容、新闻皆不代表本人态度、立场,如果有建议或方案,欢迎提交 issues，不受理Pull request`
3. `不会收取任何广告费用,展示的所有工具链接与本人无任何利害关系`

温馨提醒：不要沉迷于攻防而忘了吃饭喔~

- 程序员在家做饭方法指南。https://github.com/Anduin2017/HowToCook

# 目录

* [半/全自动化利用工具](#半全自动化利用工具)
* [信息收集工具](#信息收集工具)
  * [资产发现工具](#资产发现工具)
  * [子域名收集工具](#子域名收集工具)
  * [目录扫描工具](#目录扫描工具)
  * [指纹识别工具](#指纹识别工具)
  * [端口扫描工具](#端口扫描工具)
  * [Burp插件](#burp插件)
  * [浏览器插件](#浏览器插件)
  * [邮箱&amp;钓鱼](#邮箱钓鱼)
  * [社工个人信息收集类](#社工个人信息收集类)
  * [APP/公众号/小程序相关工具](#app公众号小程序相关工具)
  * [常用小工具](#常用小工具)
* [漏洞利用工具](#漏洞利用工具)
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
  * [代码审计辅助工具\-通用](#代码审计辅助工具-通用)
  * [代码审计辅助工具\-java](#代码审计辅助工具-java)
  * [代码审计辅助工具\-php](#代码审计辅助工具-php)
  * [代码审计辅助工具\-dotNET](#代码审计辅助工具-dotnet)
  * [通用型WAF绕过](#通用型waf绕过)
* [内网渗透工具](#内网渗透工具)
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
* [基础设施搭建](#基础设施搭建)
  * [攻防环境部署](#攻防环境部署)
  * [代理池](#代理池)
  * [靶场清单](#靶场清单)
  * [漏洞订阅&amp;安全推送](#漏洞订阅安全推送)
* [运维&amp;甲方&amp;防守方工具](#运维甲方防守方工具)
  * [安全建设](#安全建设)
  * [应急响应笔记](#应急响应笔记)
  * [Linux应急响应工具](#linux应急响应工具)
  * [Windows应急响应工具](#windows应急响应工具)
  * [webshell查杀工具](#webshell查杀工具)
  * [内存马查杀工具](#内存马查杀工具)
  * [防守辅助分析工具](#防守辅助分析工具)
  * [溯源反制工具](#溯源反制工具)
* [其他安全资料整理](#其他安全资料整理)
  * [JAVA安全研究](#java安全研究)
  * [AI安全](#ai安全)
  * [安全面试](#安全面试)
  * [实战红蓝资料集锦](#实战红蓝资料集锦)
  * [云安全资料](#云安全资料)



# 半/全自动化利用工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>单兵作战武器库，你值得拥有</td>
    <td>https://github.com/yaklang/yakit</td>
    <td>-</td>
  </tr>
  <tr>
    <td>ScopeSentry-网络空间测绘、子域名枚举、端口扫描、敏感信息发现、漏洞扫描、分布式节点</td>
    <td>https://github.com/Autumn-27/ScopeSentry-Scan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>CyberEdge 是一款精心设计的互联网资产测绘工具，为网络安全专业人士提供精准、高效的扫描体验。</td>
    <td>https://github.com/Symph0nia/CyberEdge</td>
    <td>-</td>
  </tr>
  <tr>
    <td>dddd是一款使用简单的批量信息收集,供应链漏洞探测工具，旨在优化红队工作流，减少伤肝的机械性操作。支持从Hunter、Fofa批量拉取目标</td>
    <td>https://github.com/SleepingBag945/dddd</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款GUI界面的渗透工具，将部分人工经验转换为自动化，集成了渗透过程中常用到的一些功能，目前集成了端口扫描、端口爆破、web指纹扫描、漏洞扫描、漏洞利用以及编码转换功能，后续会持续更新。</td>
    <td>https://github.com/lz520520/railgun</td>
    <td>-</td>
  </tr>
  <tr>
    <td>安全服务集成化工具平台</td>
    <td>https://github.com/qiwentaidi/Slack</td>
    <td>-</td>
  </tr>
  <tr>
    <td>密探渗透测试工具包含资产信息收集，子域名爆破，搜索语法，资产测绘（FOFA，Hunter，quake, ZoomEye），指纹识别，敏感信息采集，文件扫描、端口扫描、批量信息权重查询、密码字典等功能</td>
    <td>https://github.com/kkbo8005/mitan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Nemo是用来进行自动化信息收集的一个简单平台，通过集成常用的信息收集工具和技术，实现对内网及互联网资产信息的自动收集，提高隐患排查和渗透测试的工作效率。</td>
    <td>https://github.com/hanc00l/nemo_go</td>
    <td>-</td>
  </tr>
  <tr>
    <td>DarkAngel 是一款全自动白帽漏洞扫描器，从hackerone、bugcrowd资产监听到漏洞报告生成、企业微信通知。</td>
    <td>https://github.com/Bywalks/DarkAngel</td>
    <td>-</td>
  </tr>
  <tr>
    <td>分布式资产信息收集和漏洞扫描平台</td>
    <td>https://github.com/1in9e/gosint</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一条龙服务，只需要输入根域名即可全方位收集相关资产，并检测漏洞。也可以输入多个域名、C段IP等，具体案例见下文。</td>
    <td>https://github.com/0x727/ShuiZe_0x727</td>
    <td>-</td>
  </tr>
  <tr>
    <td>自动化巡航扫描框架（可用于红队打点评估）</td>
    <td>https://github.com/b0bac/ApolloScanner</td>
    <td>-</td>
  </tr>
  <tr>
    <td>可针对指定IP段、资产清单、存活网段自动化进行端口扫描以及TCP指纹识别和Banner抓取</td>
    <td>https://github.com/lcvvvv/kscan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>集成 vscan、nuclei、ksubdomain、subfinder等，充分自动化、智能化 并对这些集成的项目进行代码级别优化、参数优化，个别模块,如 vscan filefuzz部分进行了重写</td>
    <td>https://github.com/GhostTroops/scan4all</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个辅助平常渗透测试项目或者攻防项目快速打点的综合工具</td>
    <td>https://github.com/P1-Team/AlliN</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个漏洞扫描器粘合剂,添加目标后30款工具自动调用</td>
    <td>https://github.com/78778443/QingScan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>从子域名、端口服务、漏洞、爬虫等一体化的资产管理系统</td>
    <td>https://github.com/CTF-MissFeng/bayonet</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个高度可定制Web自动化扫描框架</td>
    <td>https://github.com/r3curs1v3-pr0xy/vajra</td>
    <td>-</td>
  </tr>
  <tr>
    <td>reconFTW 集成了30个工具的信息收集利器</td>
    <td>https://github.com/six2dez/reconftw</td>
    <td>-</td>
  </tr>
  <tr>
    <td>自动化侦查框架</td>
    <td>https://github.com/yogeshojha/rengine</td>
    <td>-</td>
  </tr>
</table>






# 信息收集工具

## 资产发现工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>reconFTW 集成了30个工具的信息收集利器</td>
    <td>https://github.com/six2dez/reconftw</td>
    <td>-</td>
  </tr>
  <tr>
    <td>资产无限巡航扫描系统</td>
    <td>https://github.com/awake1t/linglong</td>
    <td>-</td>
  </tr>
  <tr>
    <td>SRC子域名资产监控</td>
    <td>https://github.com/LangziFun/LangSrcCurise</td>
    <td>-</td>
  </tr>
  <tr>
    <td>快速侦察与目标关联的互联网资产，构建基础资产信息库。</td>
    <td>https://github.com/TophantTechnology/ARL</td>
    <td>-</td>
  </tr>
  <tr>
    <td>集成GoogleHacking语法来进行信息收集</td>
    <td>https://github.com/TebbaaX/GRecon</td>
    <td>-</td>
  </tr>
  <tr>
    <td>从第三方平台获取目标网页内容</td>
    <td>https://github.com/tomnomnom/waybackurls</td>
    <td>-</td>
  </tr>
  <tr>
    <td>从多个网站提取目标相关信息</td>
    <td>https://github.com/lc/gau</td>
    <td>-</td>
  </tr>
  <tr>
    <td>集合了多个网络测绘平台，可以快速在多个网络测绘平台搜索信息并且合并展示及导出。</td>
    <td>https://github.com/ExpLangcn/InfoSearchAll</td>
    <td>-</td>
  </tr>
  <tr>
    <td>调用fofa\ZoomEye\360quake的官方api---GUI界面</td>
    <td>https://github.com/xzajyjs/ThunderSearch</td>
    <td>-</td>
  </tr>
  <tr>
    <td>集成多个网络资产测绘平台的搜索工具</td>
    <td>https://github.com/Kento-Sec/AsamF</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个简单实用的FOFA客户端 By flashine</td>
    <td>https://github.com/wgpsec/fofa_viewer</td>
    <td>-</td>
  </tr>
  <tr>
    <td>0_zone_zpi脚本</td>
    <td>https://github.com/lemonlove7/0_zone</td>
    <td>-</td>
  </tr>
  <tr>
    <td>icp备案查询、企业资产快速收集工具</td>
    <td>https://github.com/SiJiDo/IEyes</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款基于各大企业信息API的工具</td>
    <td>https://github.com/wgpsec/ENScan_GO</td>
    <td>-</td>
  </tr>
  <tr>
    <td>基于斗象灯塔ARL修改后的版本。相比原版，增加了OneForAll、中央数据库，修改了altDns</td>
    <td>https://github.com/ki9mu/ARL-plus-docker</td>
    <td>-</td>
  </tr>
  <tr>
    <td>灯塔（最新版）指纹添加脚本！</td>
    <td>https://github.com/loecho-sec/ARL-Finger-ADD</td>
    <td>-</td>
  </tr>
</table>

  

  



## 子域名收集工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>在线子域名收集</td>
    <td>https://rapiddns.io/subdomain</td>
    <td>-</td>
  </tr>
  <tr>
    <td>ksubdomain 无状态子域名爆破工具</td>
    <td>https://github.com/knownsec/ksubdomain</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款功能强大的子域收集工具</td>
    <td>https://github.com/shmilylty/OneForAll</td>
    <td>-</td>
  </tr>
  <tr>
    <td>通过使用被动在线资源来发现网站的有效子域</td>
    <td>https://github.com/projectdiscovery/subfinder</td>
    <td>-</td>
  </tr>
  <tr>
    <td>src子域名监控</td>
    <td>https://github.com/LangziFun/LangSrcCurise</td>
    <td>-</td>
  </tr>
  <tr>
    <td>从 github 上发现子域名</td>
    <td>https://github.com/gwen001/github-subdomains</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Layer子域名挖掘机</td>
    <td>https://github.com/euphrat1ca/LayerDomainFinder</td>
    <td>-</td>
  </tr>
  <tr>
    <td>好用且强大的子域名扫描工具</td>
    <td>https://github.com/yunxu1/dnsub</td>
    <td>-</td>
  </tr>
</table>

  



## 目录扫描工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>Web path scanner  目录扫描工具</td>
    <td>https://github.com/maurosoria/dirsearch</td>
    <td>-</td>
  </tr>
  <tr>
    <td>用Rust编写的快速，简单，递归的内容发现工具</td>
    <td>https://github.com/epi052/feroxbuster</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Directory/File, DNS and VHost busting tool written in Go</td>
    <td>https://github.com/OJ/gobuster</td>
    <td>-</td>
  </tr>
  <tr>
    <td>用Go编写的模糊测试工具</td>
    <td>https://github.com/ffuf/ffuf</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Next Generation HTTP Dir/File Fuzz Tool</td>
    <td>https://github.com/chainreactors/spray</td>
    <td>-</td>
  </tr>
  <tr>
    <td>提取JS、解析Webpack打包、使用正则匹配技术，发现API接口及Base URL。</td>
    <td>https://github.com/0x727/ChkApi_0x727</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Fast passive URL enumeration tool.</td>
    <td>https://github.com/chainreactors/urlfounder</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个高级web目录、文件扫描工具</td>
    <td>https://github.com/H4ckForJob/dirmap</td>
    <td>-</td>
  </tr>
  <tr>
    <td>网站的敏感目录发掘工具</td>
    <td>https://github.com/deibit/cansina</td>
    <td>-</td>
  </tr>
  <tr>
    <td>御剑后台扫描工具珍藏版</td>
    <td>https://www.fujieace.com/hacker/tools/yujian.html</td>
    <td>-</td>
  </tr>
  <tr>
    <td>使用GoLang开发的目录/子域扫描器</td>
    <td>https://github.com/ReddyyZ/urlbrute</td>
    <td>-</td>
  </tr>
  <tr>
    <td>御剑目录扫描专业版</td>
    <td>https://github.com/foryujian/yjdirscan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>类似JSFinder的golang实现，更快更全更舒服</td>
    <td>https://github.com/pingc0y/URLFinder</td>
    <td>-</td>
  </tr>
  <tr>
    <td>爬虫 可以发现搜索引擎发现不了的目录</td>
    <td>https://github.com/jaeles-project/gospider</td>
    <td>-</td>
  </tr>
  <tr>
    <td>katana 是 projectdiscovery 项目中的一个网页链接抓取工具，可以自动解析js文件。</td>
    <td>https://github.com/projectdiscovery/katana</td>
    <td>-</td>
  </tr>
  <tr>
    <td>dontgo403 是一个绕过 40X 错误的工具。</td>
    <td>https://github.com/devploit/dontgo403</td>
    <td>-</td>
  </tr>
  <tr>
    <td>从JavaScript中提取URL、路径、机密和其他有趣的部分</td>
    <td>https://github.com/BishopFox/jsluice</td>
    <td>-</td>
  </tr>
  <tr>
    <td>爬网站JS文件，自动fuzz api接口，回显api响应</td>
    <td>https://github.com/ttstormxx/jjjjjjjjjjjjjs</td>
    <td>-</td>
  </tr>
</table>




## 指纹识别工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>红队重点攻击系统指纹探测工具</td>
    <td>https://github.com/EdgeSecurityTeam/EHole</td>
    <td>-</td>
  </tr>
  <tr>
    <td>EHole(棱洞)魔改。可对路径进行指纹识别；支持识别出来的重点资产进行漏洞检测(支持从hunter和fofa中提取资产)支持对ftp服务识别及爆破</td>
    <td>https://github.com/lemonlove7/EHole_magic</td>
    <td>-</td>
  </tr>
  <tr>
    <td>跨平台指纹识别工具</td>
    <td>https://github.com/0x727/ObserverWard</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Glass是一款针对资产列表的快速指纹识别工具</td>
    <td>https://github.com/s7ckTeam/Glass</td>
    <td>-</td>
  </tr>
  <tr>
    <td>红队行动下的重点资产指纹识别工具</td>
    <td>https://github.com/P001water/P1finger</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Resources一款红队在大量的资产中存活探测与重点攻击系统指纹探测工具</td>
    <td>https://github.com/EASY233/Finger</td>
    <td>-</td>
  </tr>
  <tr>
    <td>TideFinger——指纹识别小工具，汲取整合了多个web指纹库</td>
    <td>https://github.com/TideSec/TideFinger</td>
    <td>-</td>
  </tr>
  <tr>
    <td>【暂未开源】一个Go版(更强大)的TideFinger指纹识别工具，可对web和主机指纹进行识别探测，整合梳理互联网指纹2.3W余条，在效率和指纹覆盖面方面进行了平衡和优化。</td>
    <td>https://github.com/TideSec/TideFinger_Go</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Golang实现Wappalyzer 指纹识别</td>
    <td>https://github.com/projectdiscovery/wappalyzergo</td>
    <td>-</td>
  </tr>
  <tr>
    <td>功能齐全的Web指纹识别和分享平台，内置了一万多条互联网开源的指纹信息。</td>
    <td>https://github.com/b1ackc4t/14Finger</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个web应用程序指纹识别工具</td>
    <td>https://github.com/urbanadventurer/WhatWeb</td>
    <td>-</td>
  </tr>
</table>



## 端口扫描工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>MX1014 是一个遵循 短平快 原则的灵活、轻便和快速端口扫描器 (满足红队需求的出网测试、网段探测和快速高危端口扫描等需求)</td>
    <td>https://github.com/L-codes/MX1014</td>
    <td>-</td>
  </tr>
  <tr>
    <td>naabu 用 go 编写的快速端口扫描器</td>
    <td>https://github.com/projectdiscovery/naabu</td>
    <td>-</td>
  </tr>
  <tr>
    <td>TXPortMap 实用型的端口扫描、服务识别工具</td>
    <td>https://github.com/4dogs-cn/TXPortMap</td>
    <td>-</td>
  </tr>
  <tr>
    <td>使用Golang开发的高并发网络扫描、服务探测工具</td>
    <td>https://github.com/Adminisme/ServerScan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>masnmapscan 一款端口扫描器。整合了masscan和nmap两款扫描器</td>
    <td>https://github.com/hellogoldsnakeman/masnmapscan-V1.0</td>
    <td>-</td>
  </tr>
  <tr>
    <td>gonmap是一个go语言的nmap端口扫描库</td>
    <td>https://github.com/lcvvvv/gonmap</td>
    <td>-</td>
  </tr>
  <tr>
    <td>光速扫描</td>
    <td>http://pan.baidu.com/s/1pLjaQKF</td>
    <td>-</td>
  </tr>
  <tr>
    <td>在线端口扫描1</td>
    <td>http://coolaf.com/tool/port</td>
    <td>-</td>
  </tr>
  <tr>
    <td>在线端口扫描2</td>
    <td>http://tool.cc/port/</td>
    <td>-</td>
  </tr>
</table>







## 前端加解密工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>浏览器内存漫游解决方案</td>
    <td>https://github.com/JSREI/ast-hook-for-js-RE</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款支持多种加密算法、或直接执行浏览器JS代码的BurpSuite插件。</td>
    <td>https://github.com/whwlsfb/BurpCrypto</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个想让你测试加密流量像测试明文一样简单高效的 Burp 插件。</td>
    <td>https://github.com/outlaws-bai/Galaxy</td>
    <td>-</td>
  </tr>
  <tr>
    <td>根据自定义来达到对数据包的处理（适用于加解密、爆破等），类似mitmproxy，不同点在于经过了burp中转</td>
    <td>https://github.com/f0ng/autoDecoder</td>
    <td>-</td>
  </tr>
  <tr>
    <td>远程调用(rpc)浏览器方法，免去抠代码补环境</td>
    <td>https://github.com/jxhczhl/JsRpc</td>
    <td>-</td>
  </tr>
  <tr>
    <td>基于CDP实现的远程JS debug工具</td>
    <td>https://github.com/1oid/remotejs</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款利用爬虫技术实现前端JS加密自动化绕过的渗透测试工具</td>
    <td>https://github.com/LiChaser/SpiderX</td>
    <td>-</td>
  </tr>
</table>




## Burp插件

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>有关burpsuite的插件(非商店),文章以及使用技巧的收集</td>
    <td>https://github.com/Mr-xn/BurpSuite-collections</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个集成的BurpSuite漏洞探测插件</td>
    <td>https://github.com/Tsojan/TsojanScan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>HaE 请求高亮标记与信息提取的辅助型 BurpSuite 插件</td>
    <td>https://github.com/gh0stkey/HaE</td>
    <td>-</td>
  </tr>
  <tr>
    <td>分析、拆解HTTP协议报文，提取HTTP协议报文中的参数、路径、文件、参数值等信息，并统计出现的频次，帮助用户构建出具有实战应用价值的Fuzzing字典。</td>
    <td>https://github.com/gh0stkey/CaA</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个集成的BurpSuite漏洞探测插件2</td>
    <td>https://github.com/kN6jq/gatherBurp</td>
    <td>-</td>
  </tr>
  <tr>
    <td>OneScan是递归目录扫描的BurpSuite插件。</td>
    <td>https://github.com/vaycore/OneScan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>解析提取接口路径+参数</td>
    <td>https://github.com/xnl-h4ck3r/GAP-Burp-Extension</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款基于BurpSuite的被动式shiro检测插件</td>
    <td>https://github.com/pmiaowu/BurpShiroPassiveScan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款基于BurpSuite的被动式FastJson检测插件</td>
    <td>https://github.com/pmiaowu/BurpFastJsonScan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个简单的Fastjson反序列化检测burp插件</td>
    <td>https://github.com/Maskhe/FastjsonScan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>fastjson利用，支持tomcat、spring回显，哥斯拉内存马；回显利用链为dhcp、ibatis、c3p0</td>
    <td>https://github.com/skisw/fastjson-exp</td>
    <td>-</td>
  </tr>
  <tr>
    <td>添加一些右键菜单让burp用起来更顺畅</td>
    <td>https://github.com/bit4woo/knife</td>
    <td>-</td>
  </tr>
  <tr>
    <td>domain_hunter_pro 一个资产管理类的Burp插件</td>
    <td>https://github.com/bit4woo/domain_hunter_pro</td>
    <td>-</td>
  </tr>
  <tr>
    <td>新一代子域名主/被动收集工具</td>
    <td>https://github.com/Acmesec/Sylas</td>
    <td>-</td>
  </tr>
  <tr>
    <td>GadgetProbe Burp插件 用来爆破远程类查找Java反序列化</td>
    <td>https://github.com/BishopFox/GadgetProbe</td>
    <td>-</td>
  </tr>
  <tr>
    <td>HopLa 自动补全 Payload 的 BurpSuite插件</td>
    <td>https://github.com/synacktiv/HopLa</td>
    <td>-</td>
  </tr>
  <tr>
    <td>验证码识别</td>
    <td>https://github.com/f0ng/captcha-killer-modified</td>
    <td>-</td>
  </tr>
  <tr>
    <td>伪造ip地址</td>
    <td>https://github.com/TheKingOfDuck/burpFakeIP</td>
    <td>-</td>
  </tr>
  <tr>
    <td>自动发送请求</td>
    <td>https://github.com/nccgroup/AutoRepeater</td>
    <td>-</td>
  </tr>
  <tr>
    <td>自动探测请求走私漏洞</td>
    <td>https://github.com/portswigger/http-request-smuggler</td>
    <td>-</td>
  </tr>
  <tr>
    <td>用于在所有请求中自动执行 SSRF 检测</td>
    <td>https://github.com/ethicalhackingplayground/ssrf-king</td>
    <td>-</td>
  </tr>
  <tr>
    <td>主要用于简化和解决Burpsuite对Http的一些操作.</td>
    <td>https://github.com/MaskCyberSecurityTeam/BurpHttpHelper</td>
    <td>-</td>
  </tr>
  <tr>
    <td>用于Outlook用户信息收集，在已登录Outlook账号后，可以使用该插件自动爬取所有联系人的信息</td>
    <td>https://github.com/KrystianLi/OutLook</td>
    <td>-</td>
  </tr>
  <tr>
    <td>提取参数插件</td>
    <td>https://github.com/goddemondemongod/god_param</td>
    <td>-</td>
  </tr>
  <tr>
    <td>这是一款burp插件，用于Outlook 网页版用户信息收集，在已登录Outlook 网页版账号后，可以使用该</td>
    <td>https://github.com/KrystianLi/ExchangeOWA</td>
    <td>-</td>
  </tr>
  <tr>
    <td>对权限绕过自动化bypass的burpsuite插件</td>
    <td>https://github.com/0x727/BypassPro</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Tls指纹特征绕过插件\</td>
    <td>Bypass</td>
    <td>-</td>
  </tr>
  <tr>
    <td>BurpSuite插件实现被动指纹识别+网站提取链接+OA爆破，可帮助我们发现更多资产。</td>
    <td>https://github.com/shuanx/BurpFingerPrint</td>
    <td>-</td>
  </tr>
  <tr>
    <td>攻防演练过程中，我们通常会用浏览器访问一些资产，但很多未授权/敏感信息/越权隐匿在已访问接口过html、JS文件等，该插件能让我们发现未授权/敏感信息/越权/登陆接口等。</td>
    <td>https://github.com/shuanx/BurpAPIFinder</td>
    <td>-</td>
  </tr>
</table>

  

  




## 浏览器插件

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>Hack-Tools  适用于红队的浏览器扩展插件</td>
    <td>https://github.com/LasCC/Hack-Tools</td>
    <td>-</td>
  </tr>
  <tr>
    <td>基于chrome、firefox插件的被动式信息泄漏检测工具</td>
    <td>https://github.com/momosecurity/FindSomething</td>
    <td>-</td>
  </tr>
  <tr>
    <td>雪瞳 是一款用于检测和提取网页中敏感信息的 Chrome 浏览器扩展。帮助用户快速获取网页中的敏感信息，并进行分析和处理</td>
    <td>https://github.com/SickleSec/SnowEyes</td>
    <td>-</td>
  </tr>
  <tr>
    <td>superSearchPlus是聚合型信息收集插件</td>
    <td>https://github.com/dark-kingA/superSearchPlus</td>
    <td>-</td>
  </tr>
  <tr>
    <td>SwitchyOmega 浏览器的代理插件</td>
    <td>https://github.com/FelisCatus/SwitchyOmega</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Chrome插件.使用DevTools查找DOM XSS</td>
    <td>https://github.com/filedescriptor/untrusted-types</td>
    <td>-</td>
  </tr>
  <tr>
    <td>FOFA Pro view 是一款FOFA Pro 资产展示浏览器插件</td>
    <td>https://github.com/fofapro/fofa_view</td>
    <td>-</td>
  </tr>
  <tr>
    <td>mitaka 用于 OSINT 搜索的Chrome和Firefox扩展</td>
    <td>https://github.com/ninoseki/mitaka</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Git History 查看git存储库文件的历史记录</td>
    <td>https://githistory.xyz/</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款可以检测WEB蜜罐并阻断请求的Chrome插件</td>
    <td>https://github.com/cnrstar/anti-honeypot</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款完全被动监听的谷歌插件，用于高危指纹识别、蜜罐特征告警和拦截、机器特征对抗。</td>
    <td>https://github.com/graynjo/Heimdallr</td>
    <td>-</td>
  </tr>
  <tr>
    <td>SourceDetector是一个自动发现.map文件，并帮你下载到本地的一个chrome extension。</td>
    <td>https://github.com/Lz1y/SourceDetector-dist</td>
    <td>-</td>
  </tr>
</table>

## 邮箱&钓鱼

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>邮箱自动化收集爬取</td>
    <td>https://github.com/Taonn/EmailAll</td>
    <td>-</td>
  </tr>
  <tr>
    <td>通过搜索引擎爬取电子邮件</td>
    <td>https://github.com/Josue87/EmailFinder</td>
    <td>-</td>
  </tr>
  <tr>
    <td>批量检查邮箱账密有效的  Python 脚本</td>
    <td>https://github.com/rm1984/IMAPLoginTester</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Coremail邮件系统组织通讯录导出脚本</td>
    <td>https://github.com/dpu/coremail-address-book</td>
    <td>-</td>
  </tr>
  <tr>
    <td>拥有在线模板设计、发送诱骗广告等功能的钓鱼系统</td>
    <td>https://github.com/gophish/gophish</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Swaks SMTP界的瑞士军刀</td>
    <td>https://github.com/jetmore/swaks</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个在线的任意发件人发送Email邮件网站</td>
    <td>http://tool.chacuo.net/mailanonymous</td>
    <td>-</td>
  </tr>
  <tr>
    <td>EwoMail是基于Linux的企业邮箱服务器</td>
    <td>https://github.com/gyxuehu/EwoMail</td>
    <td>-</td>
  </tr>
  <tr>
    <td>批量发送钓鱼邮箱</td>
    <td>https://github.com/Yang0615777/sendMail</td>
    <td>-</td>
  </tr>
  <tr>
    <td>免杀宏生成器</td>
    <td>https://github.com/Inf0secRabbit/BadAssMacros</td>
    <td>-</td>
  </tr>
  <tr>
    <td>图标提取</td>
    <td>https://github.com/JarlPenguin/BeCyIconGrabberPortable</td>
    <td>-</td>
  </tr>
  <tr>
    <td>图标替换</td>
    <td>https://github.com/guitarfreak/SetIcon</td>
    <td>-</td>
  </tr>
  <tr>
    <td>红蓝对抗：钓鱼演练资源汇总&备忘录</td>
    <td>https://github.com/tib36/PhishingBook</td>
    <td>-</td>
  </tr>
  <tr>
    <td>剑指钓鱼基建快速部署自动化</td>
    <td>https://github.com/taielab/Taie-AutoPhishing</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款适用于红蓝对抗中的仿真钓鱼系统</td>
    <td>https://github.com/xiecat/goblin</td>
    <td>-</td>
  </tr>
</table>

## 社工个人信息收集类

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>从大量站点中收集用户个人信息</td>
    <td>https://github.com/soxoj/maigret</td>
    <td>-</td>
  </tr>
  <tr>
    <td>根据邮箱自动搜索泄漏的密码信息</td>
    <td>https://github.com/D4Vinci/Cr3dOv3r</td>
    <td>-</td>
  </tr>
  <tr>
    <td>密码泄露搜集</td>
    <td>https://archive.org/search.php?query=</td>
    <td>-</td>
  </tr>
  <tr>
    <td>从部分站点中收集个人信息</td>
    <td>https://github.com/n0tr00t/Sreg</td>
    <td>-</td>
  </tr>
  <tr>
    <td>输入人名或邮箱地址, 自动从互联网爬取关于此人的信息</td>
    <td>https://github.com/famavott/osint-scraper</td>
    <td>-</td>
  </tr>
  <tr>
    <td>通过脉脉用户猜测企业邮箱</td>
    <td>https://github.com/Ridter/Mailget</td>
    <td>-</td>
  </tr>
  <tr>
    <td>社工字典密码生成</td>
    <td>https://github.com/Mebus/cupp</td>
    <td>-</td>
  </tr>
  <tr>
    <td>社会工程学密码生成器，是一个利用个人信息生成密码的工具</td>
    <td>https://github.com/zgjx6/SocialEngineeringDictionaryGenerator</td>
    <td>-</td>
  </tr>
  <tr>
    <td>在线密码生成器</td>
    <td>https://zzzteph.github.io/weakpass/</td>
    <td>-</td>
  </tr>
</table>




## APP/公众号/小程序相关工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>（推荐）微信小程序反编译工具，.wxapkg 文件扫描 + 解密 + 解包工具</td>
    <td>https://github.com/wux1an/wxapkg</td>
    <td>-</td>
  </tr>
  <tr>
    <td>全自动化，微信小程序 wxapkg 包 源代码还原工具, 线上代码安全审计，支持 Windows, Macos, Linux</td>
    <td>https://github.com/biggerstar/wedecode</td>
    <td>-</td>
  </tr>
  <tr>
    <td>微信小程序辅助渗透-自动化</td>
    <td>https://github.com/eeeeeeeeee-code/e0e1-wx</td>
    <td>-</td>
  </tr>
  <tr>
    <td>自动化反编译微信小程序，小程序安全评估工具，发现小程序安全问题，自动解密，解包，可还原工程目录，支持Hook，小程序修改</td>
    <td>https://github.com/Ackites/KillWxapkg</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个反编译微信小程序的工具，仓库也收集各种微信小程序/小游戏.wxapkg文件</td>
    <td>https://github.com/ezshine/wxapkg-convertor</td>
    <td>-</td>
  </tr>
  <tr>
    <td>微信小程序主包解密工具</td>
    <td>https://github.com/BlackTrace/pc_wxapkg_decrypt</td>
    <td>-</td>
  </tr>
  <tr>
    <td>微信小程序反编译</td>
    <td>https://github.com/qwerty472123/wxappUnpacker</td>
    <td>-</td>
  </tr>
  <tr>
    <td>微信小程序反编译</td>
    <td>https://github.com/r3x5ur/wxapkg-unpacker</td>
    <td>-</td>
  </tr>
  <tr>
    <td>微信小程序信息在线收集，wxapkg源码包内提取信息</td>
    <td>https://github.com/moyuwa/wechat_appinfo_wxapkg</td>
    <td>-</td>
  </tr>
  <tr>
    <td>WeChatOpenDevTool 微信小程序强制开启开发者工具</td>
    <td>https://github.com/x0tools/WeChatOpenDevTools</td>
    <td>-</td>
  </tr>
  <tr>
    <td>WeChatOpenDevTool 微信小程序强制开启开发者工具py</td>
    <td>https://github.com/JaveleyQAQ/WeChatOpenDevTools-Python</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Resources移动端(Android、iOS、WEB、H5、静态网站)信息收集扫描工具</td>
    <td>https://github.com/kelvinBen/AppInfoScanner</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款适用于以APP病毒分析、APP漏洞挖掘、APP开发、HW行动/红队/渗透测试团队为场景的移动端(Android、iOS)辅助分析工具</td>
    <td>https://github.com/sulab999/AppMessenger</td>
    <td>-</td>
  </tr>
  <tr>
    <td>apk爬虫工具可提取包内url等信息</td>
    <td>https://github.com/dwisiswant0/apkleaks</td>
    <td>-</td>
  </tr>
  <tr>
    <td>安卓应用层抓包通杀脚本</td>
    <td>https://github.com/r0ysue/r0capture</td>
    <td>-</td>
  </tr>
  <tr>
    <td>用于存取记录以前的基址和小程序文件</td>
    <td>https://github.com/eeeeeeeeee-code/wx-hook</td>
    <td>-</td>
  </tr>
</table>



## 常用小工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>好用的去重对比工具</td>
    <td>https://github.com/tomnomnom/anew</td>
    <td>-</td>
  </tr>
  <tr>
    <td>视觉侦查工具，用于信息收集屏幕截图</td>
    <td>https://github.com/sensepost/gowitness</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款jar包分析小工具</td>
    <td>https://github.com/4ra1n/jar-analyzer</td>
    <td>-</td>
  </tr>
  <tr>
    <td>参数FUZZ小工具</td>
    <td>https://github.com/s0md3v/Arjun</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款用于快速导出URL、Domain和IP的小工具</td>
    <td>https://github.com/mstxq17/MoreFind</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Xtools 是一款 Sublime Text 插件，同时是一款简单的资产处理、命令行调用工具。</td>
    <td>https://github.com/chasingboy/Xtools</td>
    <td>-</td>
  </tr>
  <tr>
    <td>对Web渗透项目资产进行快速存活验证</td>
    <td>https://github.com/AabyssZG/Web-SurvivalScan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>二进制文件切割&合并工具</td>
    <td>https://github.com/AabyssZG/BinaryCutting-Tool</td>
    <td>-</td>
  </tr>
  <tr>
    <td>命令执行写任意文件，主要用于命令执行但不出网情况</td>
    <td>https://github.com/Ar3h/putter</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个 CLASS 文件混淆工具，支持方法名/字段名/参数名引用分析和重命名混淆方式，支持字符串提取/整型异或混淆/垃圾代码花指令混淆/等方式，支持方法和字段的隐藏，配置简单，容易上手</td>
    <td>https://github.com/jar-analyzer/class-obf</td>
    <td>-</td>
  </tr>
</table>



# 漏洞利用工具

## 漏洞扫描框架/工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>高危漏洞精准检测与深度利用框架</td>
    <td>https://github.com/woodpecker-framework/woodpecker-framwork-release</td>
    <td>-</td>
  </tr>
  <tr>
    <td>基于简单 YAML 的 DSL 的快速且可定制的漏洞扫描器。</td>
    <td>https://github.com/projectdiscovery/nuclei</td>
    <td>-</td>
  </tr>
  <tr>
    <td>afrog 是一款性能卓越、快速稳定、PoC 可定制化的漏洞扫描工具</td>
    <td>https://github.com/zan8in/afrog</td>
    <td>-</td>
  </tr>
  <tr>
    <td>EZ是一款集信息收集、端口扫描、服务暴破、URL爬虫、指纹识别、被动扫描为一体的跨平台漏洞扫描器。</td>
    <td>https://github.com/m-sec-org/EZ</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款功能强大的安全评估工具</td>
    <td>https://github.com/chaitin/xray</td>
    <td>-</td>
  </tr>
  <tr>
    <td>网络安全测试工具</td>
    <td>https://github.com/gobysec/Goby</td>
    <td>-</td>
  </tr>
  <tr>
    <td>开源的远程漏洞测试框架</td>
    <td>https://github.com/knownsec/pocsuite3</td>
    <td>-</td>
  </tr>
  <tr>
    <td>全新的开源在线 poc 测试框架</td>
    <td>https://github.com/jweny/pocassist</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个应用于web安全领域的漏洞批量扫描框架</td>
    <td>https://github.com/bigblackhat/oFx</td>
    <td>-</td>
  </tr>
  <tr>
    <td>是一款 web 漏洞扫描和验证工具</td>
    <td>https://github.com/zhzyker/vulmap</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款全面而强大的漏洞扫描和利用工具</td>
    <td>https://github.com/yhy0/Jie</td>
    <td>-</td>
  </tr>
  <tr>
    <td>自动整合全网Nuclei的漏洞POC，实时同步更新最新POC！</td>
    <td>https://github.com/ExpLangcn/NucleiTP</td>
    <td>-</td>
  </tr>
</table>




## 中间件/应用漏洞利用工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>Spring漏洞综合利用工具</td>
    <td>https://github.com/savior-only/Spring_All_Reachable</td>
    <td>-</td>
  </tr>
  <tr>
    <td>针对SpringBoot的开源渗透框架，以及Spring相关高危漏洞利用工具</td>
    <td>https://github.com/AabyssZG/SpringBoot-Scan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款java漏洞集合工具</td>
    <td>https://github.com/pureqh/Hyacinth</td>
    <td>-</td>
  </tr>
  <tr>
    <td>WeblogicTool，GUI漏洞利用工具，支持漏洞检测、命令执行、内存马注入、密码解密等（深信服深蓝实验室天威战队强力驱动）</td>
    <td>https://github.com/KimJun1010/WeblogicTool</td>
    <td>-</td>
  </tr>
  <tr>
    <td>shiro 反序列 命令执行辅助检测工具</td>
    <td>https://github.com/wyzxxz/shiro_rce_tool</td>
    <td>-</td>
  </tr>
  <tr>
    <td>shiro反序列化漏洞综合利用,包含（回显执行命令/注入内存马）修复原版中NoCC的问题</td>
    <td>https://github.com/SummerSec/ShiroAttack2</td>
    <td>-</td>
  </tr>
  <tr>
    <td>shiro反序列化漏洞综合利用,包含（回显执行命令/注入内存马）</td>
    <td>https://github.com/j1anFen/shiro_attack</td>
    <td>-</td>
  </tr>
  <tr>
    <td>复杂请求下的Shiro反序列化利用工具</td>
    <td>https://github.com/sma11new/Pyke-Shiro</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Fastjson扫描器，可识别版本、依赖库、autoType状态等。</td>
    <td>https://github.com/a1phaboy/FastjsonScan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Jboss（和 Java 反序列化漏洞）验证和利用工具</td>
    <td>https://github.com/joaomatosf/jexboss</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Dubbo反序列化一键快速攻击测试工具</td>
    <td>https://github.com/threedr3am/dubbo-exp</td>
    <td>-</td>
  </tr>
  <tr>
    <td>jenkins-attack-framework 针对 Jenkins 的攻击框架</td>
    <td>https://github.com/Accenture</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款Jenkins的综合漏洞利用工具</td>
    <td>https://github.com/TheBeastofwar/JenkinsExploit-GUI</td>
    <td>-</td>
  </tr>
  <tr>
    <td>log4j漏洞利用工具</td>
    <td>https://github.com/kozmer/log4j-shell-poc</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款针对Vcenter的综合利用工具，包含目前最主流的CVE-2021-21972、CVE-2021-21985以及CVE-2021-22005以及log4j，提供一键上传webshell，命令执行或者上传公钥使用SSH免密连接</td>
    <td>https://github.com/Schira4396/VcenterKiller</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Vcenter综合渗透利用工具包-GUI</td>
    <td>https://github.com/W01fh4cker/VcenterKit</td>
    <td>-</td>
  </tr>
  <tr>
    <td>WeblogicTool，GUI漏洞利用工具，支持漏洞检测、命令执行、内存马注入、密码解密等（深信服深蓝实验室天威战队强力驱动）</td>
    <td>https://github.com/KimJun1010/WeblogicTool</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Weblogic漏洞利用图形化工具 支持注入内存马、一键上传webshell、命令执行</td>
    <td>https://github.com/sp4zcmd/WeblogicExploit-GUI</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Weblogic一键漏洞检测工具，V1.5，更新时间：20200730</td>
    <td>https://github.com/rabbitmask/WeblogicScan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>weblogic 漏洞扫描工具。包含2020</td>
    <td>https://github.com/0xn0ne/weblogicScanner</td>
    <td>-</td>
  </tr>
  <tr>
    <td>woodpecker框架weblogic信息探测插件</td>
    <td>https://github.com/woodpecker-appstore/weblogic-infodetector</td>
    <td>-</td>
  </tr>
  <tr>
    <td>STS2G Struts2漏洞扫描利用工具 - Golang版</td>
    <td>https://github.com/xwuyi/STS2G</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Struts2-Scan Struts2全漏洞扫描利用工具</td>
    <td>https://github.com/HatBoy/Struts2-Scan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Struts2全版本漏洞检测工具 by:ABC_123</td>
    <td>https://github.com/abc123info/Struts2VulsScanTools</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Confluence-OGNL一键注入内存shell</td>
    <td>https://github.com/BeichenDream/CVE-2022-26134-Godzilla-MEMSHELL</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Confluence CVE 2021，2022，2023 利用工具，支持命令执行，哥斯拉，冰蝎 内存马注入</td>
    <td>https://github.com/Lotus6/ConfluenceMemshell</td>
    <td>-</td>
  </tr>
  <tr>
    <td>ResourcesYApi接口管理平台远程命令执行</td>
    <td>https://github.com/Tas9er/YApiRCE</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Nacos JRaft Hessian 反序列化 RCE 加载字节码 注入内存马 不出网利用</td>
    <td>https://github.com/c0olw/NacosRce</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Nacos漏洞综合利用GUI工具，集成了默认口令漏洞、SQL注入漏洞、身份认证绕过漏洞、反序列化漏洞的检测及其利用</td>
    <td>https://github.com/charonlight/NacosExploitGUI</td>
    <td>-</td>
  </tr>
</table>



  

  

## 重点cms利用工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>高危漏洞利用工具</td>
    <td>https://github.com/White-hua/Apt_t00ls</td>
    <td>-</td>
  </tr>
  <tr>
    <td>OA漏洞利用工具，基于Apt-T00ls二次开发工具</td>
    <td>https://github.com/R4gd0ll/I-Wanna-Get-All</td>
    <td>-</td>
  </tr>
  <tr>
    <td>OA综合利用工具，集合将近20款OA漏洞批量扫描</td>
    <td>https://github.com/LittleBear4/OA-EXPTOOL</td>
    <td>-</td>
  </tr>
  <tr>
    <td>OAExploit一款基于产品的一键扫描工具。</td>
    <td>https://github.com/achuna33/MYExploit</td>
    <td>-</td>
  </tr>
  <tr>
    <td>支持自定义Poc文件的图形化漏洞利用工具</td>
    <td>https://github.com/bcvgh/daydayEXP</td>
    <td>-</td>
  </tr>
  <tr>
    <td>漏洞POC基本适用ThinkPHP全版本漏洞</td>
    <td>https://github.com/zangcc/Aazhen-RexHa</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Thinkphp(GUI)漏洞利用工具，支持各版本TP漏洞检测，命令执行，getshell。</td>
    <td>https://github.com/Lotus6/ThinkphpGUI</td>
    <td>-</td>
  </tr>
  <tr>
    <td>ThinkPHP 漏洞 综合利用工具, 图形化界面, 命令执行, 一键getshell, 批量检测, 日志遍历, session包含, 宝塔绕过</td>
    <td>https://github.com/bewhale/thinkphp_gui_tools</td>
    <td>-</td>
  </tr>
  <tr>
    <td>致远OA综合利用工具</td>
    <td>https://github.com/Summer177/seeyon_exp</td>
    <td>-</td>
  </tr>
  <tr>
    <td>致远OA综合利用工具GUI-V1.0</td>
    <td>https://github.com/God-Ok/SeeyonExploit-GUI</td>
    <td>-</td>
  </tr>
  <tr>
    <td>通达OA综合利用工具</td>
    <td>https://github.com/xinyu2428/TDOA_RCE</td>
    <td>-</td>
  </tr>
  <tr>
    <td>蓝凌OA漏洞利用工具/前台无条件RCE/文件写入</td>
    <td>https://github.com/yuanhaiGreg/LandrayExploit</td>
    <td>-</td>
  </tr>
  <tr>
    <td>泛微OA漏洞综合利用脚本</td>
    <td>https://github.com/z1un/weaver_exp</td>
    <td>-</td>
  </tr>
  <tr>
    <td>泛微oa漏洞利用工具</td>
    <td>https://github.com/TD0U/WeaverScan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>帆软bi反序列化漏洞利用工具</td>
    <td>https://github.com/yecp181/Frchannel</td>
    <td>-</td>
  </tr>
</table>

  

## 信息泄露利用工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>六大云存储，泄露利用检测工具</td>
    <td>https://github.com/UzJu/Cloud-Bucket-Leak-Detection-Tools</td>
    <td>-</td>
  </tr>
  <tr>
    <td>AK资源管理工具，阿里云/腾讯云 AccessKey AccessKeySecret</td>
    <td>https://github.com/wyzxxz/aksk_tool</td>
    <td>-</td>
  </tr>
  <tr>
    <td>阿里云accesskey利用工具</td>
    <td>https://github.com/mrknow001/aliyun-accesskey-Tools</td>
    <td>-</td>
  </tr>
  <tr>
    <td>swagger-exp Swagger  REST API 信息泄露利用工具</td>
    <td>https://github.com/lijiejie/swagger-exp</td>
    <td>-</td>
  </tr>
  <tr>
    <td>swagger-hack 自动化爬取并测试所有swagger-ui.html接口</td>
    <td>https://github.com/jayus0821/swagger-hack</td>
    <td>-</td>
  </tr>
  <tr>
    <td>heapdump敏感信息查询工具</td>
    <td>https://github.com/wyzxxz/heapdump_tool</td>
    <td>-</td>
  </tr>
  <tr>
    <td>HeapDump敏感信息提取工具</td>
    <td>https://github.com/whwlsfb/JDumpSpider</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Packer Fuzzer  针对Webpack等前端打包工具所构造的网站进行检测的扫描工具</td>
    <td>https://github.com/rtcatc/Packer-Fuzzer</td>
    <td>-</td>
  </tr>
  <tr>
    <td>.git源代码泄露利用工具</td>
    <td>https://github.com/BugScanTeam/GitHack</td>
    <td>-</td>
  </tr>
  <tr>
    <td>.cvs源代码泄露利用工具</td>
    <td>https://github.com/kost/dvcs-ripper.git</td>
    <td>-</td>
  </tr>
  <tr>
    <td>.DS_store文件泄露利用工具</td>
    <td>https://github.com/lijiejie/ds_store_exp</td>
    <td>-</td>
  </tr>
  <tr>
    <td>SvnExploit支持SVN源代码泄露全版本Dump源码</td>
    <td>https://github.com/admintony/svnExploit</td>
    <td>-</td>
  </tr>
  <tr>
    <td>git-dumper 从网站转储git存储库的工具</td>
    <td>https://github.com/arthaud/git-dumper</td>
    <td>-</td>
  </tr>
  <tr>
    <td>GitDorker  通过使用大型的dorks库来从GitHub抓取敏感信息</td>
    <td>https://github.com/obheda12/GitDorker</td>
    <td>-</td>
  </tr>
  <tr>
    <td>从JavaScript文件中提取敏感信息</td>
    <td>https://github.com/m4ll0k/SecretFinder</td>
    <td>-</td>
  </tr>
  <tr>
    <td>功能比较多的一个JavaScript侦查自动化脚本</td>
    <td>https://github.com/KathanP19/JSFScan.sh</td>
    <td>-</td>
  </tr>
  <tr>
    <td>子域名接管漏洞检测工具，支持30+云服务托管检测</td>
    <td>https://github.com/Ice3man543/SubOver</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个小程序、公众号、企业微信、飞书、钉钉等泄露secert后利用工具</td>
    <td>https://github.com/mrknow001/API-Explorer</td>
    <td>-</td>
  </tr>
  <tr>
    <td>互联网厂商API利用工具。</td>
    <td>https://github.com/pykiller/API-T00L</td>
    <td>-</td>
  </tr>
  <tr>
    <td>混合盘APP - 网盘搜索、磁力搜索 - 搜索20个百度网盘、阿里网盘、夸克网盘以及磁力资源</td>
    <td>https://github.com/misiai/hunhepan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>云资产管理工具 目前工具定位是云安全相关工具，目前是两个模块 云存储工具、云服务工具， 云存储工具主要是针对oss存储、查看、删除、上传、下载、预览等等 云服务工具主要是针对rds、服务器的管理，查看、执行命令、接管等等</td>
    <td>https://github.com/dark-kingA/cloudTools</td>
    <td>-</td>
  </tr>
</table>

## 数据库利用工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>MDUT 2.0 数据库利用工具</td>
    <td>https://github.com/SafeGroceryStore/MDUT</td>
    <td>-</td>
  </tr>
  <tr>
    <td>数据库综合利用工具</td>
    <td>https://github.com/Ryze-T/Sylas</td>
    <td>-</td>
  </tr>
  <tr>
    <td>综合高危漏洞利用工具(包含各大数据库)</td>
    <td>https://github.com/Liqunkit/LiqunKit_</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款用Go语言编写的数据库自动化提权工具</td>
    <td>https://github.com/Hel10-Web/Databasetools</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Team IDE 工具 集成MySql、Oracle、金仓、达梦、神通等数据库、SSH、FTP、Redis、Zookeeper、Kafka、Elasticsearch等管理工具</td>
    <td>https://github.com/team-ide/</td>
    <td>-</td>
  </tr>
  <tr>
    <td>sqlserver利用工具，可上传下载文件，xp_cmdshell与sp_oacreate执行命令回显和clr加载程序集执行相应操作。</td>
    <td>https://github.com/uknowsec/SharpSQLTools</td>
    <td>-</td>
  </tr>
  <tr>
    <td>通过套接字重用通过受损的 Microsoft SQL Server  在受限环境中执行横向移动</td>
    <td>https://github.com/blackarrowsec/mssqlproxy</td>
    <td>-</td>
  </tr>
  <tr>
    <td>ODAT：Oracle 数据库攻击工具</td>
    <td>https://github.com/quentinhardy/odat</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Redis未授权访问漏洞利用工具</td>
    <td>https://github.com/n0b0dyCN/redis-rogue-server</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Redis未授权访问漏洞利用工具2</td>
    <td>https://github.com/Ridter/redis-rce</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Redis 漏洞利用工具</td>
    <td>https://github.com/yuyan-sec/RedisEXP</td>
    <td>-</td>
  </tr>
  <tr>
    <td>redis主从复制rce的go版本</td>
    <td>https://github.com/zyylhn/redis_rce</td>
    <td>-</td>
  </tr>
</table>

## 爆破利用工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>还是推荐fscan吧，还是还用，更新也快</td>
    <td>https://github.com/shadow1ng/fscan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>zombie主要为了解决需要全场景(外网、内网、云)的服务的口令爆破功能</td>
    <td>https://github.com/chainreactors/zombie</td>
    <td>-</td>
  </tr>
  <tr>
    <td>爆破神器，懂得都懂</td>
    <td>https://github.com/vanhauser-thc/thc-hydra</td>
    <td>-</td>
  </tr>
  <tr>
    <td>超级弱口令检查工具是一款Windows平台的弱口令审计工具</td>
    <td>https://github.com/shack2/SNETCracker</td>
    <td>-</td>
  </tr>
  <tr>
    <td>FTP,SSH,MYSQL,MSSQL等弱口令爆破工具</td>
    <td>https://github.com/BBD-YZZ/week-passwd</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款面向企业的渗透测试字典生成工具。</td>
    <td>https://github.com/ccc-f/Fdict</td>
    <td>-</td>
  </tr>
  <tr>
    <td>爆破Azure, ADFS, OWA, O365, Teams，smtp</td>
    <td>https://github.com/nodauf/GoMapEnum</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Boom 是一款基于无头浏览器的智能 Web 弱口令（后台密码）爆破工具</td>
    <td>https://github.com/Fly-Playgroud/Boom</td>
    <td>-</td>
  </tr>
</table>




## 全网字典收集

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>用户名密码字典生成工具(将中文汉字姓名转成14种格式的拼音、IP地址处理、网络设备密码生成)</td>
    <td>https://github.com/abc123info/UserNameDictTools</td>
    <td>-</td>
  </tr>
  <tr>
    <td>该工具是使用javaFX开发的基于信息收集进行组合生成密码字典的工具，可以快速组成密码字典。</td>
    <td>https://github.com/kkbo8005/dicttools</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个字典列表生成框架</td>
    <td>https://github.com/glitchedgitz/cook</td>
    <td>-</td>
  </tr>
  <tr>
    <td>渗透测试、SRC漏洞挖掘、爆破、Fuzzing等字典收集项目</td>
    <td>https://github.com/insightglacier/Dictionary-Of-Pentesting</td>
    <td>-</td>
  </tr>
  <tr>
    <td>1337 Wordlists for Bug Bounty Hunting</td>
    <td>https://github.com/0xPugazh/fuzz4bounty</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Fuzz 字典,一个就够了</td>
    <td>https://github.com/TheKingOfDuck/fuzzDicts</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Web 模糊测试字典与一些Payloads</td>
    <td>https://github.com/gh0stkey/Web-Fuzzing-Box</td>
    <td>-</td>
  </tr>
  <tr>
    <td>安全评估期间使用的多种类型列表的集合</td>
    <td>https://github.com/danielmiessler/SecLists</td>
    <td>-</td>
  </tr>
  <tr>
    <td>渗透测试仪和Bug赏金猎人的 Payload 库</td>
    <td>https://github.com/sh377c0d3/Payloads</td>
    <td>-</td>
  </tr>
  <tr>
    <td>基于实战沉淀下的各种弱口令字典</td>
    <td>https://github.com/fuzz-security/SuperWordlist</td>
    <td>-</td>
  </tr>
  <tr>
    <td>各类漏洞的 TOP25 参数字典</td>
    <td>https://github.com/lutfumertceylan/top25-parameter</td>
    <td>-</td>
  </tr>
  <tr>
    <td>提取收集以往泄露的密码中符合条件的强弱密码</td>
    <td>https://github.com/r35tart/RW_Password</td>
    <td>-</td>
  </tr>
  <tr>
    <td>实战沉淀字典</td>
    <td>https://github.com/SexyBeast233/SecDictionary</td>
    <td>-</td>
  </tr>
</table>

## 常规漏洞利用工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>Web 渗透测试 /CTF 的有用的payload大全</td>
    <td>https://github.com/swisskyrepo/PayloadsAllTheThings</td>
    <td>-</td>
  </tr>
  <tr>
    <td>您将在其中找到我在 CTF、现实生活应用程序以及阅读研究和新闻中学到的每一个技巧 / 技巧 / 任何东西。</td>
    <td>https://github.com/HackTricks-wiki/hacktricks</td>
    <td>-</td>
  </tr>
  <tr>
    <td>DalFox 是一款功能强大的开源 XSS 扫描工具和参数分析器、实用工具</td>
    <td>https://github.com/hahwul/dalfox</td>
    <td>-</td>
  </tr>
  <tr>
    <td>基于DOM的快速XSS漏洞扫描程序</td>
    <td>https://github.com/dwisiswant0/findom-xss</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款基于 Chromium的XSS检测工具</td>
    <td>https://github.com/v8blink/Chromium-based-XSS-Taint-Tracking</td>
    <td>-</td>
  </tr>
  <tr>
    <td>很常用的XSS平台</td>
    <td>https://github.com/beefproject/beef</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Fast CRLF injection scanning tool</td>
    <td>https://github.com/Nefcore/CRLFsuite</td>
    <td>-</td>
  </tr>
  <tr>
    <td>快速 CORS 错误配置漏洞扫描程序</td>
    <td>https://github.com/chenjj/CORScanner</td>
    <td>-</td>
  </tr>
  <tr>
    <td>xxe利用工具</td>
    <td>https://github.com/BuffaloWill/oxml_xxe</td>
    <td>-</td>
  </tr>
  <tr>
    <td>xxe利用工具2</td>
    <td>https://github.com/whitel1st/docem</td>
    <td>-</td>
  </tr>
  <tr>
    <td>UEditor编辑器批量GetShell / Code By:Tas9er</td>
    <td>https://github.com/Tas9er/UEditorGetShell</td>
    <td>-</td>
  </tr>
  <tr>
    <td>子域名接管工具</td>
    <td>https://github.com/michenriksen/aquatone</td>
    <td>-</td>
  </tr>
  <tr>
    <td>用于查找常见的Nginx错误配置和漏洞。</td>
    <td>https://github.com/stark0de/nginxpwner</td>
    <td>-</td>
  </tr>
  <tr>
    <td>文件包含自动化利用工具</td>
    <td>https://github.com/hansmach1ne/lfimap</td>
    <td>-</td>
  </tr>
  <tr>
    <td>文件包含利用工具</td>
    <td>https://github.com/mzfr/liffy</td>
    <td>-</td>
  </tr>
  <tr>
    <td>具有交互式界面的自动 SSTI 检测工具</td>
    <td>https://github.com/vladko312/SSTImap</td>
    <td>-</td>
  </tr>
  <tr>
    <td>A simple SSRF-testing sheriff written in Go</td>
    <td>https://github.com/teknogeek/ssrf-sheriff</td>
    <td>-</td>
  </tr>
  <tr>
    <td>SSRFmap，利用它可检测与利用 SSRF 漏洞， 同时它也整合了一些常用漏洞可以结合 SSRF 去利用</td>
    <td>https://github.com/swisskyrepo/SSRFmap</td>
    <td>-</td>
  </tr>
  <tr>
    <td>用于测试、调整和破解JSON Web令牌的工具包</td>
    <td>https://github.com/ticarpi/jwt_tool</td>
    <td>-</td>
  </tr>
  <tr>
    <td>jwt hack是jwt黑客/安全测试的工具。支持En/解码JWT，生成JWT攻击和非常快速破解的有效载荷（dict/brutefoce）</td>
    <td>https://github.com/hahwul/jwt-hack</td>
    <td>-</td>
  </tr>
  <tr>
    <td>XSS spider - 66/66 wavsep XSS detected</td>
    <td>https://github.com/DanMcInerney/xsscrapy</td>
    <td>-</td>
  </tr>
  <tr>
    <td>针对JWT渗透开发的漏洞验证/密钥爆破工具，针对CVE-2015-9235/空白密钥/未验证签名攻击/CVE-2016-10555/CVE-2018-0114/CVE-2020-28042的结果生成用于FUZZ，也可使用字典/字符枚举(包括JJWT)的方式进行爆破(JWT Crack)</td>
    <td>https://github.com/z-bool/Venom-JWT</td>
    <td>-</td>
  </tr>
</table>

## 反序列化利用工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>JYso是一个可以用于 jndi 注入攻击和生成反序列化数据流的工具。</td>
    <td>https://github.com/qi4L/JYso</td>
    <td>-</td>
  </tr>
  <tr>
    <td>生成 Java 反序列化负载的概念验证</td>
    <td>https://github.com/Whoopsunix/PPPYSO</td>
    <td>-</td>
  </tr>
  <tr>
    <td>项目为 ysoserial [su18] 专版，取名为 ysuserial ，在原项目 [ysoserial](https://github.com/frohoff/ysoserial) 基础上魔改而来</td>
    <td>https://github.com/su18/ysoserial/</td>
    <td>-</td>
  </tr>
  <tr>
    <td>图形化Java反序列化利用工具，集成Ysoserial</td>
    <td>https://github.com/0ofo/Deswing</td>
    <td>-</td>
  </tr>
  <tr>
    <td>jndi注入工具v1.4</td>
    <td>https://github.com/WhiteHSBG/JNDIExploit</td>
    <td>-</td>
  </tr>
  <tr>
    <td>JNDI服务利用工具 RMI/LDAP，支持部分场景回显、内存shell，高版本JDK场景下利用等，fastjson rce命令执行，log4j rce命令执行 漏洞检测辅助工具</td>
    <td>https://github.com/wyzxxz/jndi_tool</td>
    <td>-</td>
  </tr>
  <tr>
    <td>TopicsYsomap是一款适配于各类实际复杂环境的Java反序列化利用框架，可动态配置具备不同执行效果的Java反序列化利用链payload。</td>
    <td>https://github.com/wh1t3p1g/ysomap</td>
    <td>-</td>
  </tr>
  <tr>
    <td>原版反序列化利用工具</td>
    <td>https://github.com/frohoff/ysoserial</td>
    <td>-</td>
  </tr>
  <tr>
    <td>ysoserial修改版，着重修改`ysoserial.payloads.util.Gadgets.createTemplatesImpl`使其可以通过引入自定义class的形式来执行命令、内存马、反序列化回显</td>
    <td>https://github.com/Y4er/ysoserial</td>
    <td>-</td>
  </tr>
  <tr>
    <td>魔改版ysoserial，有更多方便的命令</td>
    <td>https://kgithub.com/woodpecker-framework/ysoserial-for-woodpecker</td>
    <td>-</td>
  </tr>
  <tr>
    <td>解决FastJson、Jackson、Log4j2、原生JNDI注入漏洞的高版本JDKBypass利用，探测本地可用反序列化gadget达到命令执行、回显命令执行、内存马注入</td>
    <td>https://github.com/exp1orer/JNDI-Inject-Exploit</td>
    <td>-</td>
  </tr>
  <tr>
    <td>MySQL Fake Server (纯Java实现，内置常见Java反序列化Payload，支持GUI版和命令行版，提供Dockerfile)</td>
    <td>https://github.com/4ra1n/mysql-fake-server</td>
    <td>-</td>
  </tr>
  <tr>
    <td>rmi打内存马工具，适用于目标用不了ldap的情况</td>
    <td>https://github.com/novysodope/RMI_Inj_MemShell</td>
    <td>-</td>
  </tr>
  <tr>
    <td>marshalsec是一款java反序列利用工具，其可以很方便的起一个ldap或rmi服务，通过这些服务来去访问攻击者准备好的恶意执行类来达到远程命令执行或入侵的目的。</td>
    <td>https://github.com/mbechler/marshalsec</td>
    <td>-</td>
  </tr>
  <tr>
    <td>使用 agent 实现反序列化 utf8 overlong</td>
    <td>https://github.com/Ar3h/utf8-overlong-agent</td>
    <td>-</td>
  </tr>
</table>

## 内存马注入工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>一款支持高度自定义的 Java 内存马生成工具</td>
    <td>https://github.com/pen4uin/java-memshell-generator-release</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Java内存马注入工具</td>
    <td>https://github.com/WisteriaTiger/JundeadShell</td>
    <td>-</td>
  </tr>
  <tr>
    <td>拿来即用的Tomcat内存马</td>
    <td>https://github.com/ce-automne/TomcatMemShell</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Memory WebShell Generator</td>
    <td>https://github.com/hosch3n/msmap</td>
    <td>-</td>
  </tr>
  <tr>
    <td>用Java agent实现内存马等功能</td>
    <td>https://github.com/ethushiroha/JavaAgentTools</td>
    <td>-</td>
  </tr>
  <tr>
    <td>多功能 java agent 内存马</td>
    <td>https://github.com/veo/vagent</td>
    <td>-</td>
  </tr>
</table>



## 代码审计辅助工具-通用

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>是一款基于正则表达式的代码安全审计工具，专为红队成员快速定位sink设计。它能够快速扫描目标代码库，定位潜在的漏洞 Sink 点，提升代码审计效率。</td>
    <td>https://github.com/guchangan1/CodeVulnScan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>源代码静态分析工具，支持Java、PHP、C#、Python、Go等27种编程语言，而且能够集成在IDE、Jenkins、Git等服务。</td>
    <td>https://www.sonarqube.org</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一种适用于 C++、C#、VB、PHP、Java、PL/SQL 和 COBOL 的自动化代码安全审查工具。</td>
    <td>https://sourceforge.net/projects/visualcodegrepp/</td>
    <td>-</td>
  </tr>
  <tr>
    <td>开源安全产品源码，IDS、IPS、WAF、蜜罐等</td>
    <td>https://github.com/birdhan/SecurityProduct</td>
    <td>-</td>
  </tr>
  <tr>
    <td>图形化的代码审计工具，支持对规则进行增删改查。可协助代码审计人员在日常代审中对于规则的积累。其中配置页面可配置：审计文件后缀、审计路径关键字、禁止审计路径关键字。支持 java php net项目审计。</td>
    <td>https://github.com/vsdwef/StarCodeSecurity</td>
    <td>-</td>
  </tr>
  <tr>
    <td>该工具目的为对大多数不完整的代码以及依赖快速进行Sink点匹配来帮助红队完成快速代码审计，开发该工具的初衷是以`Sink`到`Source`的思路来开发，为了将所有可疑的Sink点匹配出来并且凭借第六感进行快速漏洞挖掘，并且该工具开发可扩展性强，成本极低，目前工具支持的语言有PHP，Java</td>
    <td>https://github.com/Zjackky/CodeScan</td>
    <td>-</td>
  </tr>
</table>

  

## 代码审计辅助工具-java

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>一个用于分析Jar包的GUI工具，可以用多种方式搜索你想要的信息，自动构建方法调用关系，支持分析Spring框架（A Java GUI Tool for Analyzing Jar）</td>
    <td>https://github.com/4ra1n/jar-analyzer-gui</td>
    <td>-</td>
  </tr>
  <tr>
    <td>`SecurityInspector` 是一个静态代码扫描插件，内置了常见的`Java` 代码`Web`漏洞`sink` 点，高危组件调用`sink` 点，识别项目中可能存在的过滤器（如`XSS`过滤器、`SQLI`过滤器等<此功能存在较多`bug` ，将会于正式版上线>），并使用`IDEA`的`PSI` 和`Intercept`机制来对以上内容进行快速定位。</td>
    <td>https://github.com/SpringKill-team/SecurityInspector</td>
    <td>-</td>
  </tr>
  <tr>
    <td>JavaWeb漏洞审计工具，构建方法调用链并模拟栈帧进行分析</td>
    <td>https://github.com/4ra1n/code-inspector</td>
    <td>-</td>
  </tr>
  <tr>
    <td>闭源系统半自动漏洞挖掘工具，针对 jar/war/zip 进行静态代码分析，增加 LLM 大模型能力验证路径可达性，LLM 根据上下文代码环境给出该路径可信分数</td>
    <td>https://github.com/Phelaine/SinkFinder</td>
    <td>-</td>
  </tr>
  <tr>
    <td>开源的被动式交互式安全测试(IAST)产品</td>
    <td>https://github.com/HXSecurity/DongTai</td>
    <td>-</td>
  </tr>
  <tr>
    <td>CodeQLpy是一款基于CodeQL实现的半自动化代码审计工具，目前仅支持java语言。实现从源码反编译，数据库生成，脆弱性发现的全过程，可以辅助代码审计人员快速定位源码可能存在的漏洞。</td>
    <td>https://github.com/webraybtl/CodeQLpy</td>
    <td>-</td>
  </tr>
  <tr>
    <td>免费开源的语义代码分析引擎和查询工具</td>
    <td>https://github.com/github/codeql-cli-binaries</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Java Web应用安全漏洞自动化发现-idea插件</td>
    <td>https://github.com/find-sec-bugs/find-sec-bugs/wiki/IntelliJ-Tutorial</td>
    <td>-</td>
  </tr>
  <tr>
    <td>“铲子”是一款简单易用的JAVA SAST工具，旨在为安全工程师提供一款简单、好用、价格厚道的代码安全扫描产品，支持语言: java（Servlet、spring、dubbo、thirft、mybatis、jsp） ，采用轻量级污点分析，铲子会将java、xml（mybatis、dubbo）等统一构建数据流图，然后进行污点分析，无需编译，也可以反编译扫描jar或class，内置了 sql 注入、命令注入、文件上传、ssrf 等常见漏洞规则，用户可以自定义规则。</td>
    <td>https://github.com/Chanzi-keji/chanzi</td>
    <td>-</td>
  </tr>
  <tr>
    <td>IDEA依赖检查插件</td>
    <td>https://github.com/jeremylong/DependencyCheck</td>
    <td>-</td>
  </tr>
  <tr>
    <td>TABBY 是一个基于[Soot](https://github.com/soot-oss/soot)的 Java 代码分析工具。</td>
    <td>https://github.com/wh1t3p1g/tabby</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个静态代码脆弱性检测系统，支持java源码的审计</td>
    <td>https://github.com/zsdlove/Hades</td>
    <td>-</td>
  </tr>
  <tr>
    <td>IDEA静态代码安全审计及漏洞一键修复插件</td>
    <td>https://github.com/momosecurity/momo-code-sec-inspector-java</td>
    <td>-</td>
  </tr>
  <tr>
    <td>IDEA代码审计辅助插件（深信服深蓝实验室天威战队强力驱动）</td>
    <td>https://github.com/KimJun1010/inspector?tab=readme-ov-file</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款无需解压直接编辑修改jar包内文件的IDEA插件</td>
    <td>https://github.com/Liubsyy/JarEditor</td>
    <td>-</td>
  </tr>
  <tr>
    <td>JADX-GUI-AI 是一个在 JADX 基础上增强的智能反编译工具，集成了 AI 辅助功能，可以帮助开发者更好地理解和分析反编译后的代码</td>
    <td>https://github.com/cncsnet1/jadx-gui-ai</td>
    <td>-</td>
  </tr>
</table>

## 代码审计辅助工具-php

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>Seay源代码审计系统</td>
    <td>https://github.com/f1tz/cnseay</td>
    <td>-</td>
  </tr>
  <tr>
    <td>查找PHP代码漏洞工具</td>
    <td>https://github.com/ecriminal/phpvuln</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款不错的静态源代码分析工具，主要用来挖掘PHP程序的漏洞。</td>
    <td>[http://rips-scanner.sourceforge.net](http://rips-scanner.sourceforge.net/)</td>
    <td>-</td>
  </tr>
  <tr>
    <td>X-SAST 替代Seay的多语言、轻量、快速、代码审计工具</td>
    <td>https://github.com/winezer0/X-SAST-PUBLIC</td>
    <td>-</td>
  </tr>
</table>



## 代码审计辅助工具-dotNET

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>NETReactorSlayer一款反混淆神器，适用于Eziriz .NET Reactor工具混淆后的代码，最新版本6.4</td>
    <td>https://github.com/SychicBoy/NETReactorSlayer</td>
    <td>-</td>
  </tr>
</table>

  

## 通用型WAF绕过

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>绕过瑞数waf的动态验证机制，实现请求包重放，可针对不同网站使用。</td>
    <td>https://github.com/R0A1NG/Botgate_bypass</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个基于fuzz的waf绕过测试工具，当前支持命令执行、SQL注入绕过。</td>
    <td>https://github.com/leveryd/x-waf</td>
    <td>-</td>
  </tr>
</table>



# 内网渗透工具

## 后渗透辅助工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>一款轻量级的杀软在线识别的项目</td>
    <td>https://github.com/Aabyss-Team/Antivirus-Scan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>在线 Windows 操作系统常见杀软进程/办公软件/shell终端等识别，输入 tasklist /SVC 将内容粘贴</td>
    <td>https://forum.ywhack.com/bountytips.php?process</td>
    <td>-</td>
  </tr>
  <tr>
    <td>杀软在线对比</td>
    <td>http://bypass.tidesec.com/bycms</td>
    <td>-</td>
  </tr>
  <tr>
    <td>高价值系统的后利用工具</td>
    <td>https://github.com/0linlin0/XPost</td>
    <td>-</td>
  </tr>
</table>


## webshell管理工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>哥斯拉</td>
    <td>https://github.com/BeichenDream/Godzilla</td>
    <td>-</td>
  </tr>
  <tr>
    <td>“冰蝎”动态二进制加密网站管理客户端</td>
    <td>https://github.com/rebeyond/Behinder</td>
    <td>-</td>
  </tr>
  <tr>
    <td>中国蚁剑是一款开源的跨平台网站管理工具</td>
    <td>https://github.com/AntSwordProject/antSword</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一句话WEB端管理工具</td>
    <td>https://github.com/boy-hack/WebshellManager</td>
    <td>-</td>
  </tr>
  <tr>
    <td>跨平台版中国菜刀</td>
    <td>https://github.com/Chora10/Cknife</td>
    <td>-</td>
  </tr>
  <tr>
    <td>用于生成各类免杀webshell</td>
    <td>https://github.com/cseroad/Webshell_Generate</td>
    <td>-</td>
  </tr>
  <tr>
    <td>从零学习Webshell免杀手册</td>
    <td>https://github.com/AabyssZG/WebShell-Bypass-Guide</td>
    <td>-</td>
  </tr>
  <tr>
    <td>webshell收集项目，项目涵盖各种常用脚本</td>
    <td>https://github.com/tennc/webshell</td>
    <td>-</td>
  </tr>
</table>



## c2管理工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>cs4.4修改去特征狗狗版(美化ui,去除特征,自带bypass核晶截图等..)</td>
    <td>https://github.com/TryGOTry/DogCs4.4/tree/dogcs_v2.1</td>
    <td>-</td>
  </tr>
  <tr>
    <td>跨平台重构了Cobaltstrike Beacon，目前实现的功能具备免杀性，可过Defender、360核晶、卡巴斯基（除内存操作外，如注入原生cs的dll）、火绒</td>
    <td>https://github.com/H4de5-7/geacon_pro</td>
    <td>-</td>
  </tr>
  <tr>
    <td>类似于cs</td>
    <td>https://github.com/t3l3machus/Villain</td>
    <td>-</td>
  </tr>
  <tr>
    <td>是一个 C2前流控制工具，可以避免蓝队，AVs，EDR 检查</td>
    <td>https://github.com/wikiZ/RedGuard</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款可以在不出网的环境下进行反向代理及cs上线的工具</td>
    <td>https://github.com/Daybr4ak/C2ReverseProxy</td>
    <td>-</td>
  </tr>
  <tr>
    <td>该工具易于使用，它生成自己的 PowerShell 有效负载并支持加密 (ssl)。</td>
    <td>https://github.com/t3l3machus/hoaxshell</td>
    <td>-</td>
  </tr>
  <tr>
    <td>反弹shell就用这个</td>
    <td>https://github.com/WangYihang/Platypus</td>
    <td>-</td>
  </tr>
  <tr>
    <td>PingRAT使用ICMP有效载荷通过防火墙秘密传递C2流量。</td>
    <td>https://github.com/umutcamliyurt/PingRAT</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Empire 是一个后利用和对手模拟框架，用于帮助红队和渗透测试人员。</td>
    <td>https://github.com/BC-SECURITY/Empire</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Metasploit（MSF）是一个免费的、可下载的框架，通过它可以很容易地获取、开发并对计算机软件漏洞实施攻击。</td>
    <td>https://github.com/rapid7/metasploit-framework</td>
    <td>-</td>
  </tr>
</table>




## 提权项目

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>Linux自动提权</td>
    <td>https://github.com/liamg/traitor</td>
    <td>-</td>
  </tr>
  <tr>
    <td>提权辅助页</td>
    <td>https://i.hacking8.com/tiquan/</td>
    <td>-</td>
  </tr>
  <tr>
    <td>全平台系统提权辅助工具</td>
    <td>https://github.com/carlospolop/PEASS-ng</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个聚合了linux、windows、macOS的提权漏洞合集，带复现过程</td>
    <td>https://github.com/Ascotbe/Kernelhub</td>
    <td>-</td>
  </tr>
</table>

## 内网扫描工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>Fscan 一款内网综合扫描工具，方便一键自动化、全方位漏扫扫描。</td>
    <td>https://github.com/shadow1ng/fscan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款快速探测内网可达网段工具（深信服深蓝实验室天威战队强力驱动）</td>
    <td>https://github.com/shmilylty/netspy</td>
    <td>-</td>
  </tr>
  <tr>
    <td>下一代RedTeam启发式内网扫描</td>
    <td>https://github.com/1n7erface/Template</td>
    <td>-</td>
  </tr>
  <tr>
    <td>内网资产收集、探测主机存活、端口扫描、域控定位、文件搜索、各种服务爆破（SSH、SMB、MsSQL等）、Socks代理，一键自动化+无文件落地扫描</td>
    <td>https://github.com/INotGreen/SharpScan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个速度极快的内网扫描器，具备端口扫描、协议检测、指纹识别，暴力破解，漏洞探测等功能。支持协议1200+，协议指纹10000+，应用指纹20000+，暴力破解协议10余种</td>
    <td>https://github.com/qi4L/qscan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款更高、更快、更强的全方位内网扫描工具</td>
    <td>https://github.com/P001water/P1soda</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Ladon一款用于大型网络渗透的多线程插件化综合扫描神器</td>
    <td>https://github.com/k8gege/Ladon</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款快速探测内网主机信息工具（深信服深蓝实验室天威战队强力驱动）</td>
    <td>https://github.com/shmilylty/SharpHostInfo</td>
    <td>-</td>
  </tr>
  <tr>
    <td>红队小工具 ，利用DCERPC协议获取Windows机器主机信息和多网卡信息</td>
    <td>https://github.com/Y0-kan/HostInfoScan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>ATAttack是一款后渗透半自动化侦察工具，它从进攻性和防御性安全角度执行许多面向安全性的主机调查“安全检查”。</td>
    <td>https://github.com/c1y2m3/ATAttack</td>
    <td>-</td>
  </tr>
  <tr>
    <td>集权设施扫描器</td>
    <td>https://github.com/Amulab/CAudit</td>
    <td>-</td>
  </tr>
</table>




## 本机收集工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>GodInfo 是一个功能全面的后渗透信息和凭据收集工具，旨在帮助安全测试人员在获得授权访问权限后，快速收集目标系统的信息和凭据。</td>
    <td>https://github.com/Conan924/GodInfo</td>
    <td>-</td>
  </tr>
  <tr>
    <td>支持自动化一键 Hunting 主机各类关键信息和凭据，降低后渗透阶段操作的割裂感，有效拓宽后渗透攻击面</td>
    <td>https://github.com/lintstar/SharpHunter</td>
    <td>-</td>
  </tr>
  <tr>
    <td>该工具主要用于后渗透方面</td>
    <td>https://github.com/eeeeeeeeee-code/e0e1-config</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Pillager是一个适用于后渗透期间的信息收集工具，可以收集目标机器上敏感信息，方便下一步渗透工作的进行。</td>
    <td>https://github.com/qwqdanchun/Pillager</td>
    <td>-</td>
  </tr>
  <tr>
    <td>强大的敏感信息搜索工具</td>
    <td>https://github.com/Naturehi666/searchall</td>
    <td>-</td>
  </tr>
  <tr>
    <td>通用的数据库连接配置信息提取工具</td>
    <td>https://github.com/corener/JavaPassDump</td>
    <td>-</td>
  </tr>
</table>

 

## 横向移动工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>横向impacket工具包</td>
    <td>https://github.com/fortra/impacket</td>
    <td>-</td>
  </tr>
  <tr>
    <td>基于impacket的免杀横向渗透远程命令执行工具（推荐）。</td>
    <td>https://github.com/XiaoliChan/wmiexec-Pro</td>
    <td>-</td>
  </tr>
  <tr>
    <td>WMIHACKER是一款免杀横向渗透远程命令执行工具。</td>
    <td>https://github.com/rootclay/WMIHACKER</td>
    <td>-</td>
  </tr>
  <tr>
    <td>基于golang实现的impacket</td>
    <td>https://github.com/Amzza0x00/go-impacket</td>
    <td>-</td>
  </tr>
  <tr>
    <td>工具基于 CrackMapExec,针对大型Windows活动目录(AD)的后渗透工具</td>
    <td>https://github.com/Pennyw0rth/NetExec</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款比较好的CS后渗透模块插件</td>
    <td>https://github.com/pandasec888/taowu-cobalt-strike</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款CS后渗透模块插件，让大家使用一款插件就够了</td>
    <td>https://github.com/d3ckx1/OLa</td>
    <td>-</td>
  </tr>
  <tr>
    <td>常见横向移动与域控权限维持方法</td>
    <td>https://xz.aliyun.com/t/9382</td>
    <td>-</td>
  </tr>
  <tr>
    <td>绕过虚拟机登录验证屏幕的工具</td>
    <td>https://github.com/hzphreak/VMInjector</td>
    <td>-</td>
  </tr>
</table>

  

## 域渗透工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>检测域环境内，域机器的本地管理组成员是否存在弱口令和通用口令，对域用户的权限分配以及域内委派查询</td>
    <td>https://github.com/0x727/ShuiYing_0x727</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个强大的内网域渗透分析工具，构建于 Linkurious 之上</td>
    <td>https://github.com/BloodHoundAD/BloodHound</td>
    <td>-</td>
  </tr>
  <tr>
    <td>域内自动化信息搜集利用工具</td>
    <td>https://github.com/wjlab/Darksteel</td>
    <td>-</td>
  </tr>
</table>

  

## 密码提取工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>Mimikatz  Windows 密码抓取神器</td>
    <td>https://github.com/gentilkiwi/mimikatz</td>
    <td>-</td>
  </tr>
  <tr>
    <td>各种密码提取</td>
    <td>https://github.com/kerbyj/goLazagne</td>
    <td>-</td>
  </tr>
  <tr>
    <td>用于读取常用程序密码，如Navicat、TeamViewer、FileZilla、WinSCP等</td>
    <td>https://github.com/RowTeam/SharpDecryptPwd</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Xshell，Xftp密码解密工具</td>
    <td>https://github.com/JDArmy/SharpXDecrypt</td>
    <td>-</td>
  </tr>
  <tr>
    <td>解密浏览器数据（密码\</td>
    <td>历史记录\</td>
    <td>书签 \</td>
  </tr>
  <tr>
    <td>HackBrowserData的偏手动版，用于绕过特定情况下edr的限制</td>
    <td>https://github.com/Z3ratu1/HackBrowserDataManual</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款针对向日葵的识别码和验证码提取工具</td>
    <td>https://github.com/wafinfo/Sunflower_get_Password</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一键辅助抓取360安全浏览器密码的CobaltStrike脚本以及解密小工具</td>
    <td>https://github.com/hayasec/360SafeBrowsergetpass</td>
    <td>-</td>
  </tr>
  <tr>
    <td>BrowserGhost  抓取浏览器密码的工具</td>
    <td>https://github.com/QAX-A-Team/BrowserGhost</td>
    <td>-</td>
  </tr>
  <tr>
    <td>win-brute-logon  无需权限破解任何 Microsoft Windows 用户密码</td>
    <td>https://github.com/DarkCoderSc/win-brute-logon</td>
    <td>-</td>
  </tr>
  <tr>
    <td>TeamViewer：Bypass杀软 获取 Teamview 密码的工具</td>
    <td>https://github.com/wafinfo/TeamViewer</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Xdecrypt Xshell  Xftp 密码解密</td>
    <td>https://github.com/dzxs/Xdecrypt</td>
    <td>-</td>
  </tr>
  <tr>
    <td>微信客户端取证，可获取用户个人信息(昵称/账号/手机/邮箱/数据库密钥(用来解密聊天记录))；支持获取多用户信息</td>
    <td>https://github.com/AdminTest0/SharpWxDump</td>
    <td>-</td>
  </tr>
  <tr>
    <td>FakeLogonScreen 是一个伪造 Windows 登录屏幕以获取用户密码的实用程序。输入的密码将根据 Active Directory 或本地计算机进行验证，以确保其正确，然后显示到控制台或保存到磁盘。</td>
    <td>https://github.com/bitsadmin/fakelogonscreen</td>
    <td>-</td>
  </tr>
  <tr>
    <td>提取微信聊天记录，将其导出成HTML、Word、CSV文档永久保存，对聊天记录进行分析生成年度聊天报告</td>
    <td>https://github.com/LC044/WeChatMsg</td>
    <td>-</td>
  </tr>
</table>

  

## 隧道代理工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>全平台代理工具，支持多种socks协议</td>
    <td>https://www.proxifier.com/</td>
    <td>-</td>
  </tr>
  <tr>
    <td>开源的跨平台对手仿真/红队框架</td>
    <td>https://github.com/BishopFox/sliver</td>
    <td>-</td>
  </tr>
  <tr>
    <td>专注于内网穿透的高性能的反向代理应用</td>
    <td>https://github.com/fatedier/frp</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Erfrp-frp二开-免杀与隐藏</td>
    <td>https://github.com/Goqi/Erfrp</td>
    <td>-</td>
  </tr>
  <tr>
    <td>基于frp-0.58.1魔改二开，随机化socks5账户密码及端口、钉钉上线下线通知、配置文件oss加密读取、域前置防止溯源、源码替换/编译混淆等</td>
    <td>https://github.com/CodeSecurityTeam/frp</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款golang写的支持http与socks5的端口复用小工具，并且可以开启socks5代理。</td>
    <td>https://github.com/TryGOTry/multiplexing_port_socks5</td>
    <td>-</td>
  </tr>
  <tr>
    <td>修改frp支持域前置与配置文件自删除</td>
    <td>https://github.com/uknowsec/frpModify</td>
    <td>-</td>
  </tr>
  <tr>
    <td>轻量级、高性能、功能强大的内网穿透代理服务器</td>
    <td>https://github.com/ehang-io/nps</td>
    <td>-</td>
  </tr>
  <tr>
    <td>改进的reGeorg版本</td>
    <td>https://github.com/L-codes/Neo-reGeorg</td>
    <td>-</td>
  </tr>
  <tr>
    <td>是一款利用dns协议传输tcp数据的工具</td>
    <td>https://github.com/alex-sector/dns2tcp</td>
    <td>-</td>
  </tr>
  <tr>
    <td>是一个DNS隧道工具</td>
    <td>https://github.com/iagox86/dnscat2</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个简单的 reverse ICMP shell</td>
    <td>https://github.com/inquisb/icmpsh</td>
    <td>-</td>
  </tr>
  <tr>
    <td>pingtunnel 是把 tcp/udp/sock5 流量伪装成 icmp  流量进行转发的工具</td>
    <td>https://github.com/esrrhs/pingtunnel</td>
    <td>-</td>
  </tr>
  <tr>
    <td>正/反向代理，内网穿透，端口转发</td>
    <td>https://github.com/inconshreveable/ngrok</td>
    <td>-</td>
  </tr>
  <tr>
    <td>pystinger - 一款使用webshell进行流量转发的出网工具</td>
    <td>https://github.com/FunnyWolf/pystinger</td>
    <td>-</td>
  </tr>
  <tr>
    <td>goproxy 一款轻量级、功能强大、高性能的多种代理工具</td>
    <td>https://github.com/snail007/goproxy</td>
    <td>-</td>
  </tr>
  <tr>
    <td>内网渗透代理、端口转发工具</td>
    <td>http://rootkiter.com/Termite/</td>
    <td>-</td>
  </tr>
  <tr>
    <td>golang 实现的windows and linux 端口复用工具。</td>
    <td>https://github.com/p1d3er/port_reuse</td>
    <td>-</td>
  </tr>
  <tr>
    <td>grs内网穿透工具通过reality协议隐藏特征</td>
    <td>https://github.com/howmp/reality</td>
    <td>-</td>
  </tr>
</table>




## 优秀免杀项目

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>免杀shellcode加载器，使用go实现，免杀bypass火绒、360、核晶、def等主流杀软</td>
    <td>https://github.com/Pizz33/GobypassAV-shellcode</td>
    <td>-</td>
  </tr>
  <tr>
    <td>重写免杀版Gh0st远控、大灰狼远控免杀，目前可免杀360、火绒、腾讯电脑管家等主流杀软。</td>
    <td>https://github.com/SecurityNo1/Gh0st2023</td>
    <td>-</td>
  </tr>
  <tr>
    <td>TideSec团队整理的远控免杀系列文章及配套工具，汇总测试了互联网上的几十种免杀工具。</td>
    <td>https://github.com/TideSec/BypassAntiVirus</td>
    <td>-</td>
  </tr>
  <tr>
    <td>跟杀软和免杀有关的资料，当前包括200+工具和1300+文章  --Thanks:小雨</td>
    <td>https://github.com/alphaSeclab/anti-av</td>
    <td>-</td>
  </tr>
  <tr>
    <td>借助Win-PS2EXE项目编写cna脚本方便快速生成免杀可执行文件</td>
    <td>https://github.com/cseroad/bypassAV</td>
    <td>-</td>
  </tr>
  <tr>
    <td>在线免杀平台</td>
    <td>http://bypass.tidesec.com/web/</td>
    <td>-</td>
  </tr>
  <tr>
    <td>掩日 - 免杀执行器生成工具 用于快速生成免杀的 EXE 可执行文件</td>
    <td>https://github.com/1y0n/AV_Evasion_Tool</td>
    <td>-</td>
  </tr>
  <tr>
    <td>自动化生成 EDR 软件 Bypass Payload 的工具,一键化签名免杀</td>
    <td>https://github.com/optiv/ScareCrow</td>
    <td>-</td>
  </tr>
  <tr>
    <td>梅花K战队写的Nim一键免杀源码 使用nim语言进行shellcode加载</td>
    <td>https://github.com/M-Kings/BypassAv-web</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一键窃取文件的图标、资源信息、版本信息、修改时间、数字签名，降低程序熵值</td>
    <td>https://github.com/INotGreen/SharpThief</td>
    <td>-</td>
  </tr>
  <tr>
    <td>助力每一位RT队员，快速生成免杀木马</td>
    <td>https://github.com/wangfly-me/LoaderFly</td>
    <td>-</td>
  </tr>
  <tr>
    <td>自动化找白文件，用于扫描 EXE 文件的导入表，列出导入的DLL文件，并筛选出非系统DLL，符合条件的文件将被复制到特定的 X64 或 X86 文件夹</td>
    <td>https://github.com/ImCoriander/ZeroEye</td>
    <td>-</td>
  </tr>
</table>

## 权限维持工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>创建隐藏计划任务，权限维持，Bypass AV</td>
    <td>https://github.com/0x727/SchTask_0x727</td>
    <td>-</td>
  </tr>
  <tr>
    <td>进行克隆用户、添加用户等账户防护安全检测的轻巧工具</td>
    <td>https://github.com/0x727/CloneX_0x727</td>
    <td>-</td>
  </tr>
  <tr>
    <td>ridhijack是一款通过C/C++实现的RID劫持、影子账户、账户克隆工具。</td>
    <td>https://github.com/yanghaoi/ridhijack</td>
    <td>-</td>
  </tr>
</table>




# 基础设施搭建

## 攻防环境部署

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>Windows11 Penetration Suite Toolkit 一个开箱即用的windows渗透测试环境</td>
    <td>https://github.com/arch3rPro/Pentest-Windows</td>
    <td>-</td>
  </tr>
  <tr>
    <td>CoNote作为一个多功能信息安全测试套件，支持反连、Web文件服务器、URL缩短器、DNS Rebinding、临时邮箱、XSS平台</td>
    <td>https://conote.vulhub.org/</td>
    <td>-</td>
  </tr>
  <tr>
    <td>红/蓝队环境自动化部署工具</td>
    <td>https://github.com/ffffffff0x/f8x</td>
    <td>-</td>
  </tr>
  <tr>
    <td>适合每个人的动态基础设施框架，轻松分配许多不同扫描工具的工作量，包括nmap、ffuf、masscan、核、meg等！</td>
    <td>https://github.com/pry0cc/axiom</td>
    <td>-</td>
  </tr>
  <tr>
    <td>DNSLOG平台 golang 一键启动版</td>
    <td>https://github.com/yumusb/DNSLog-Platform-Golang</td>
    <td>-</td>
  </tr>
  <tr>
    <td>反连助手：发现可以映射本地端口的互联网IP，本工具可从hunter、quake、fofa等网络空间测绘平台，收集、探测互联网IP，并通过配置文件中的端口映射关系，把本地端口映射到互联网IP指定的端口，以便反弹shell等场景下使用。</td>
    <td>https://github.com/thinkoaa/Dlam</td>
    <td>-</td>
  </tr>
</table>




## 代理池

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>一款功能强大的代理检查和IP地址轮转工具</td>
    <td>https://github.com/kitabisa/mubeng</td>
    <td>-</td>
  </tr>
  <tr>
    <td>deadpool代理池工具，可从hunter、quake、fofa等网络空间测绘平台取高质量socks5代理，或本地导入socks5代理，轮询使用代理进行流量转发。</td>
    <td>https://github.com/thinkoaa/Deadpool</td>
    <td>-</td>
  </tr>
  <tr>
    <td>利用fofa搜索socks5开放代理进行代理池轮切的工具</td>
    <td>https://github.com/akkuman/rotateproxy</td>
    <td>-</td>
  </tr>
  <tr>
    <td>利用IP地址池进行自动切换Http代理，防止IP封禁。</td>
    <td>https://github.com/Mustard404/Auto_proxy</td>
    <td>-</td>
  </tr>
  <tr>
    <td>命令行全局代理--跨平台通用</td>
    <td>https://github.com/rofl0r/proxychains-ng</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Python爬虫代理IP池(proxy pool)</td>
    <td>https://github.com/jhao104/proxy_pool</td>
    <td>-</td>
  </tr>
</table>

  

  

  



## 靶场清单

通用漏洞类：

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>在线靶场</td>
    <td>https://hackmyvm.eu/anon/</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Vulfocus 是一个漏洞集成平台，将漏洞环境 docker 镜像，放入即可使用，开箱即用。</td>
    <td>https://github.com/fofapro/vulfocus</td>
    <td>-</td>
  </tr>
  <tr>
    <td>基于 Docker-Compose 的预建易受攻击环境</td>
    <td>https://github.com/vulhub/vulhub</td>
    <td>-</td>
  </tr>
  <tr>
    <td>*LingJing* 是一款专为复杂网络环境渗透测试量身打造的桌面级本地网络安全靶场平台。</td>
    <td>https://github.com/414aaj/LingJing</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Spring Boot 相关漏洞学习资料，利用方法和技巧合</td>
    <td>https://github.com/LandGrey/SpringBootVulExploit</td>
    <td>-</td>
  </tr>
  <tr>
    <td>TerraformGoat 是一个支持多云的云场景漏洞靶场搭建工具，目前支持阿里云、腾讯云、华为云、Amazon Web Services、Google Cloud Platform、Microsoft Azure 六个云厂商的云场景漏洞搭建。</td>
    <td>https://github.com/HXSecurity/TerraformGoat</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Metarget的名称来源于`meta-`（元）加`target`（目标，靶机），是一个脆弱基础设施自动化构建框架，主要用于快速、自动化搭建从简单到复杂的脆弱云原生靶机环境。</td>
    <td>https://github.com/Metarget/metarget</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个故意易受攻击的CI/CD环境。通过多种挑战学习CI/CD安全性。</td>
    <td>https://github.com/cider-security-research/cicd-goat</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个免费的云本地安全学习实验室列表，包括 CTF、自主研讨会、指导漏洞实验室和研究实验室。</td>
    <td>https://github.com/iknowjason/Awesome-CloudSec-Labs</td>
    <td>-</td>
  </tr>
  <tr>
    <td>GOAD是一个渗透测试活动目录实验室项目。该实验室的目的是为pentesters提供一个易受攻击的活动目录环境，以便用于练习通常的攻击技术。</td>
    <td>https://github.com/Orange-Cyberdefense/GOAD</td>
    <td>-</td>
  </tr>
  <tr>
    <td>`vulntarget`靶场涵盖Web漏洞、主机漏洞、域漏洞、工控漏洞、应急响应等。</td>
    <td>https://github.com/crow821/vulntarget</td>
    <td>-</td>
  </tr>
  <tr>
    <td>学习CTF的免费开源平台和题库</td>
    <td>https://github.com/GZTimeWalker/GZCTF</td>
    <td>-</td>
  </tr>
  <tr>
    <td>实时靶机，适合练习渗透测试和漏洞利用。</td>
    <td>https://www.hackthebox.com/</td>
    <td>-</td>
  </tr>
</table>




基础漏洞类：

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>FastJson全版本Docker漏洞环境(涵盖1.2.47/1.2.68/1.2.80等版本)，主要包括JNDI注入及高版本绕过、waf绕过、文件读写、原生反序列化、利用链探测绕过、不出网利用等。从黑盒的角度覆盖FastJson深入利用</td>
    <td>https://github.com/lemono0/FastJsonParty</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个覆盖常见 PHP 代码审计知识点的本地靶场。参考 DVWA / Pikachu 的组织方式，含安装向导与通关教程。</td>
    <td>https://github.com/duckpigdog/PHP-Code-Sec</td>
    <td>-</td>
  </tr>
  <tr>
    <td>经典php搭建的基础漏洞靶场</td>
    <td>https://github.com/digininja/DVWA</td>
    <td>-</td>
  </tr>
  <tr>
    <td>WebGoat是由OWASP维护的一个网络安全靶场，旨在教授网络应用安全课程。</td>
    <td>https://github.com/WebGoat/WebGoat</td>
    <td>-</td>
  </tr>
  <tr>
    <td>常见的web漏洞</td>
    <td>https://www.pentesterlab.com/exercises/web_for_pentester/course</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Java漏洞平台</td>
    <td>https://github.com/j3ers3/Hello-Java-Sec</td>
    <td>-</td>
  </tr>
  <tr>
    <td>JAVA 漏洞靶场</td>
    <td>https://github.com/tangxiaofeng7/SecExample</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个想帮你总结所有类型的上传漏洞的靶场</td>
    <td>https://github.com/c0ny1/upload-labs</td>
    <td>-</td>
  </tr>
  <tr>
    <td>SQLI 实验室测试基于错误、基于布尔值、基于时间。</td>
    <td>https://github.com/Audi-1/sqli-labs</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个包含php,java,python,C#等各种语言版本的XXE漏洞Demo</td>
    <td>https://github.com/c0ny1/xxe-lab</td>
    <td>-</td>
  </tr>
  <tr>
    <td>OWASP WebGoat.NET</td>
    <td>https://github.com/jerryhoff/WebGoat.NET</td>
    <td>-</td>
  </tr>
  <tr>
    <td>国光ssrf-内网靶场</td>
    <td>https://github.com/sqlsec/ssrf-vuls</td>
    <td>-</td>
  </tr>
</table>



## 漏洞订阅&安全推送

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>一个高价值漏洞采集与推送服务</td>
    <td>collect valueable vulnerability and push ithttps://github.com/zema1/watchvuln</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个基于✨HOOK机制的微信机器人，支持🌱安全新闻定时推送【FreeBuf，先知，安全客，奇安信攻防社区】</td>
    <td>https://github.com/ngc660sec/NGCBot</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个方便安全研究人员获取每日安全日报的爬虫和推送程序，目前爬取范围包括先知社区、安全客、Seebug Paper、跳跳糖、奇安信攻防社区、棱角社区以及绿盟、腾讯玄武、天融信、360等实验室博客，持续更新中。</td>
    <td>https://github.com/Le0nsec/SecCrawler</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Security-related Slide Presentation & Security Research Report（大安全各领域各公司各会议分享的PPT以及各类安全研究报告）</td>
    <td>https://github.com/FeeiCN/Security-PPT</td>
    <td>-</td>
  </tr>
  <tr>
    <td>实现对网络安全信息聚合，将安全相关的文章，数据，以及历届安全大会演讲的pptx,pdf进行了全文索引，方便检索。</td>
    <td>https://i.hacking8.com/forums/</td>
    <td>-</td>
  </tr>
  <tr>
    <td>网络安全相关的RSS订阅，帮助建立个人情报来源和日常知识库更新 更新频率: 每2个月一次</td>
    <td>https://github.com/zer0yu/CyberSecurityRSS</td>
    <td>-</td>
  </tr>
  <tr>
    <td>记录了个人用到的一些获取国内安全资讯的RSS地址。均为中文，方便自己抓取关键字。还有部分大佬的博客。均不分前后。</td>
    <td>https://github.com/zhengjim/Chinese-Security-RSS/</td>
    <td>-</td>
  </tr>
  <tr>
    <td>2024-至今 1Day 漏洞 PoC 深度研究与复现归档。涵盖 OA、ERP、安防、数通、大模型及容器等 高价值资产漏洞，实战导向，助力安全研究与合规检测。</td>
    <td>https://github.com/SourByte05/Vulnerability-Wiki-PoC</td>
    <td>-</td>
  </tr>
  <tr>
    <td>这个仓库收集了所有在 GitHub 上能找到的 CVE 漏洞利用工具。</td>
    <td>https://github.com/XiaomingX/data-cve-poc</td>
    <td>-</td>
  </tr>
</table>



# 运维&甲方&防守方工具

## 安全运营防护

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>用于记录企业安全规划，建设，运营，攻防的相关资源</td>
    <td>https://github.com/AnyeDuke/Enterprise-Security-Skill</td>
    <td>-</td>
  </tr>
  <tr>
    <td>暗网中文网监控爬虫(DEEPMIX)</td>
    <td>https://github.com/s045pd/DarkNet_ChineseTrading</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款开源的HIDS主机入侵检测系统</td>
    <td>https://wazuh.com/install/</td>
    <td>-</td>
  </tr>
  <tr>
    <td>`seckit`提供多种安全防护功能，帮助开发者防范常见的安全漏洞。该SDK通过`SecurityUtil`类提供统一的入口，支持JDBC连接串过滤、SSRF攻击防护、XXE攻击防护等核心安全功能。</td>
    <td>https://github.com/alibaba/seckit</td>
    <td>-</td>
  </tr>
</table>

## 应急响应笔记

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>NOP-TEAM出品的Windows 应急响应手册</td>
    <td>https://github.com/Just-Hack-For-Fun/Windows-INCIDENT-RESPONSE-COOKBOOK</td>
    <td>-</td>
  </tr>
  <tr>
    <td>NOP-TEAM出品的Liniux 应急响应手册</td>
    <td>https://github.com/Just-Hack-For-Fun/Linux-INCIDENT-RESPONSE-COOKBOOK</td>
    <td>-</td>
  </tr>
  <tr>
    <td>应急响应实战笔记，一个安全工程师的自我修养</td>
    <td>https://github.com/Bypass007/Emergency-Response-Notes</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Linux/Windows/应急响应个人笔记</td>
    <td>https://github.com/wpsec/Emergency-response-notes</td>
    <td>-</td>
  </tr>
  <tr>
    <td>应急响应指南 / emergency response checklist</td>
    <td>https://github.com/theLSA/emergency-response-checklist</td>
    <td>-</td>
  </tr>
</table>




## Linux应急响应工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>linux信息收集/应急响应/常见后门/挖矿检测/webshell检测脚本</td>
    <td>https://github.com/al0ne/LinuxCheck</td>
    <td>-</td>
  </tr>
  <tr>
    <td>主机侧Checklist的自动全面化检测脚本</td>
    <td>https://github.com/grayddq/GScan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>uroboros-一个GNU/Linux监视和概要分析工具，专注于单个进程</td>
    <td>https://github.com/evilsocket/uroboros</td>
    <td>-</td>
  </tr>
  <tr>
    <td>whohk linux下一款强大的应急响应工具</td>
    <td>https://github.com/heikanet/whohk</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Rootkit Hunter Rootkit猎手</td>
    <td>http://rkhunter.sourceforge.net/</td>
    <td>-</td>
  </tr>
</table>




## Windows应急响应工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>QDoctor是一款非传统意义上的ARK(Anti RootKit)工具。</td>
    <td>https://github.com/QAX-Anti-Virus/QDoctor</td>
    <td>-</td>
  </tr>
  <tr>
    <td>OpenArk是一款Windows平台上的开源Ark工具。</td>
    <td>https://github.com/BlackINT3/OpenArk</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个类似于PChunter的多功能分析工具（PChunter已无法适用于最新版windwos）</td>
    <td>https://github.com/ClownQq/YDArk/</td>
    <td>-</td>
  </tr>
  <tr>
    <td>包含一系列免费的系统分析工具，如Process Explorer、启动项分析工具 AutoRuns等。</td>
    <td>https://docs.microsoft.com/zh-cn/sysinternals/downloads/</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一个免费，功能强大的多功能工具，可帮助您监视系统资源，调试软件和检测恶意软件。</td>
    <td>https://processhacker.sourceforge.io/</td>
    <td>-</td>
  </tr>
  <tr>
    <td>微软公司出品的日志分析工具，它功能强大，使用简单。</td>
    <td>https://www.microsoft.com/en-us/download/details.aspx?id=24659</td>
    <td>-</td>
  </tr>
  <tr>
    <td>火麒麟-网络安全应急响应工具(系统痕迹采集)</td>
    <td>https://github.com/MountCloud/FireKylin</td>
    <td>-</td>
  </tr>
  <tr>
    <td>APT-Hunter Windows日志事件应急工具</td>
    <td>https://github.com/ahmedkhlief/APT-Hunter</td>
    <td>-</td>
  </tr>
  <tr>
    <td>基于Go编写的windows日志分析工具</td>
    <td>https://github.com/Fheidt12/Windows_Log</td>
    <td>-</td>
  </tr>
  <tr>
    <td>基于Memprocfs和Volatility的可视化内存取证工具</td>
    <td>https://github.com/Tokeii0/LovelyMem</td>
    <td>-</td>
  </tr>
</table>




## webshell查杀工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>webshell查杀工具</td>
    <td>http://www.shelldetector.com/</td>
    <td>-</td>
  </tr>
  <tr>
    <td>河马webshell查杀</td>
    <td>https://www.shellpub.com/</td>
    <td>-</td>
  </tr>
  <tr>
    <td>kunwu是新一代webshell检测引擎，使用了内置了模糊规则、污点分析模拟执行、机器学习三种高效的检测策略</td>
    <td>https://github.com/kunwu2023/kunwu</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一句话免疫,主动后门拦截,SESSION保护,防WEB嗅探,防CC,防篡改,注入防御,防XSS,防提权,上传防御,未知0day防御,异形脚本防御等等。</td>
    <td>https://www.d99net.net/</td>
    <td>-</td>
  </tr>
</table>




## 内存马查杀工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>Alibaba Java诊断利器Arthas</td>
    <td>https://github.com/alibaba/arthas</td>
    <td>-</td>
  </tr>
  <tr>
    <td>检测绝大部分所谓的内存免杀马</td>
    <td>https://github.com/huoji120/DuckMemoryScan</td>
    <td>-</td>
  </tr>
  <tr>
    <td>通过jsp脚本扫描java web Filter/Servlet型内存马</td>
    <td>https://github.com/c0ny1/java-memshell-scanner</td>
    <td>-</td>
  </tr>
  <tr>
    <td>A java memory web shell extracting tool</td>
    <td>https://github.com/LandGrey/copagent</td>
    <td>-</td>
  </tr>
  <tr>
    <td>杀内存马的小工具</td>
    <td>https://github.com/r00t4dm/aLIEz</td>
    <td>-</td>
  </tr>
</table>




## 防守辅助分析工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>蓝队分析研判工具箱</td>
    <td>https://github.com/abc123info/BlueTeamTools</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款基于 IP 信誉度信息实现的实时检测 Web 恶意流量的工具</td>
    <td>https://github.com/CRED-CLUB/ARTIF</td>
    <td>-</td>
  </tr>
  <tr>
    <td>勒索病毒解密工具汇总</td>
    <td>https://github.com/jiansiting/Decryption-Tools/</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Shiro-Cookie解密小工具</td>
    <td>https://github.com/r00tuser111/SerializationDumper-Shiro</td>
    <td>-</td>
  </tr>
  <tr>
    <td>这款工具是一款功能强大的网络安全综合工具，旨在为安全从业者、红蓝对抗人员和网络安全爱好者提供全面的网络安全解决方案。它集成了多种实用功能，包括解密、分析、扫描、溯源等，为用户提供了便捷的操作界面和丰富的功能选择。</td>
    <td>https://github.com/HotBoy-java/PotatoTool</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Malwoverview是一款用于威胁追踪的应急响应工具，能够从Virus Total、Hybrid Analysis、URLHaus、Polyswarm、Malshare、Alien Vault、Malpedia、Malware Bazaar、ThreatFox、Triage、InQuest、VxExchange和IPInfo等平台获取情报信息，并支持通过VT对安卓设备进行扫描。</td>
    <td>https://github.com/alexandreborges/malwoverview</td>
    <td>-</td>
  </tr>
  <tr>
    <td>CTF-NetA是一款专门针对CTF比赛的网络流量分析工具，可以对常见的网络流量进行分析，快速自动获取flag。</td>
    <td>https://github.com/Arinue/CTF-NetA</td>
    <td>-</td>
  </tr>
</table>


## 溯源反制工具

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>伪造Myslq服务端,并利用Mysql逻辑漏洞来获取客户端的任意文件反击攻击者</td>
    <td>https://github.com/BeichenDream/MysqlT</td>
    <td>-</td>
  </tr>
  <tr>
    <td>检测目标Mysql数据库是不是蜜罐</td>
    <td>https://github.com/BeichenDream/WhetherMysqlSham</td>
    <td>-</td>
  </tr>
  <tr>
    <td>安全、快捷、高交互、企业级的蜜罐管理系统，护网；支持多种协议蜜罐、蜜签、诱饵等功能。</td>
    <td>https://github.com/seccome/Ehoney</td>
    <td>-</td>
  </tr>
</table>

  

# 其他安全资料整理

## JAVA安全研究

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>【三万字原创】完全零基础从0到1掌握Java内存马，公众号：追梦信安</td>
    <td>https://github.com/W01fh4cker/LearnJavaMemshellFromZero</td>
    <td>-</td>
  </tr>
  <tr>
    <td>该项目旨在竭尽所能的以简洁清晰的方式分享`Java安全`相关技术，将某些复杂的技术问题简单化，让更多的人能够学会`Java安全`。</td>
    <td>https://github.com/javaweb-sec/javaweb-sec</td>
    <td>-</td>
  </tr>
  <tr>
    <td>抽离出 utf-8-overlong-encoding 的序列化逻辑，实现 2 3 字节加密序列化数组</td>
    <td>https://github.com/Whoopsunix/utf-8-overlong-encoding</td>
    <td>-</td>
  </tr>
  <tr>
    <td>A list for Web Security and Code Audit</td>
    <td>https://github.com/ax1sX/SecurityList</td>
    <td>-</td>
  </tr>
  <tr>
    <td>实战场景较通用的 Java Rce 相关漏洞的利用方式</td>
    <td>https://github.com/Whoopsunix/JavaRce</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Web-Security-Learning</td>
    <td>https://github.com/CHYbeta/Web-Security-Learning</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一款更利于全面学习内存马的注入工具</td>
    <td>https://github.com/ReaJason/MemShellParty</td>
    <td>-</td>
  </tr>
</table>

## AI-LLM相关资料

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>大模型学习导航</td>
    <td>https://github.com/Y4tacker/LLM-Navigation</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Ai迷思录（应用与安全指南）</td>
    <td>https://github.com/Acmesec/theAIMythbook</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Prompt越狱手册</td>
    <td>https://github.com/Acmesec/PromptJailbreakManual/</td>
    <td>-</td>
  </tr>
  <tr>
    <td>通过各厂商大模型应用中已公开的信息挖掘潜在的安全问题并公开一些技术细节</td>
    <td>https://github.com/LLM-Red-Team</td>
    <td>-</td>
  </tr>
  <tr>
    <td>一本系统化的企业安全指南，覆盖架构设计、方法论框架、实践落地。系统化提出 AiSecOps 方法论框架，将 AI 能力深度融入企业安全体系。</td>
    <td>https://github.com/cybermaxluo/AI-ESA</td>
    <td>-</td>
  </tr>
  <tr>
    <td>AIGC 求职面经、必备基础知识、提示词工程、ChatGPT、Stable Diffusion、Prompt、Embedding、Fintune 等 AIGC 求职你所需要知道的一切~</td>
    <td>https://github.com/EmbraceAGI/AIGC_Interview</td>
    <td>-</td>
  </tr>
  <tr>
    <td>《AI 研发提效：构建 AI 辅助编码助手》</td>
    <td>https://github.com/unit-mesh/build-your-ai-coding-assistant</td>
    <td>-</td>
  </tr>
  <tr>
    <td>MCP-SecurityTools 是一个专注于收录和更新网络安全领域 MCP 的开源项目，旨在汇总、整理和优化各类与 MCP 相关的安全工具、技术及实战经验。</td>
    <td>https://github.com/Ta0ing/MCP-SecurityTools</td>
    <td>-</td>
  </tr>
  <tr>
    <td>面向基于MCP的AI工具的综合安全检查清单。由SlowMist构建，以保障大语言模型插件生态系统的安全。</td>
    <td>https://github.com/slowmist/MCP-Security-Checklist</td>
    <td>-</td>
  </tr>
  <tr>
    <td>AI 驱动的开源渗透测试神器，解锁安全新可能</td>
    <td>https://github.com/vxcontrol/pentagi</td>
    <td>-</td>
  </tr>
  <tr>
    <td>提示词优化</td>
    <td>https://github.com/linshenkx/prompt-optimizer</td>
    <td>-</td>
  </tr>
  <tr>
    <td>《开源大模型食用指南》针对中国宝宝量身打造的基于Linux环境快速微调（全参数/Lora）、部署国内外开源大模型（LLM）/多模态大模型（MLLM）教程</td>
    <td>https://github.com/datawhalechina/self-llm</td>
    <td>-</td>
  </tr>
</table>
## 安全面试

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>一个2023届毕业生在毕业前持续更新、收集的安全岗面试题及面试经验分享~</td>
    <td>https://github.com/vvmdx/Sec-Interview-4-2023</td>
    <td>-</td>
  </tr>
  <tr>
    <td>网络信息安全从业者面试指南</td>
    <td>https://github.com/FeeiCN/SecurityInterviewGuide</td>
    <td>-</td>
  </tr>
  <tr>
    <td>安全方向知识点(包含web攻防、java攻防、企业安全、内网/域、提权、免杀)</td>
    <td>https://github.com/just0rg/Security-Interview</td>
    <td>-</td>
  </tr>



## 实战红蓝资料集锦

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>红蓝对抗以及护网相关工具和资料，内存shellcode（cs+msf）和内存马查杀工具</td>
    <td>https://github.com/Mr-xn/RedTeam_BlueTeam_HW</td>
    <td>-</td>
  </tr>
  <tr>
    <td>重生之我是赏金猎人系列，分享自己和团队在SRC、项目实战漏洞测试过程中的有趣案例</td>
    <td>https://github.com/J0o1ey/BountyHunterInChina</td>
    <td>-</td>
  </tr>
  <tr>
    <td>国外蓝队攻防知识库</td>
    <td>https://github.com/Purp1eW0lf/Blue-Team-Notes</td>
    <td>-</td>
  </tr>




## 云安全资料

<table>
  <tr>
    <th width="60%">项目简介</th>
    <th width="25%">项目地址</th>
    <th width="15%">最近更新</th>
  </tr>
  <tr>
    <td>也许这是国内第一个云安全知识文库</td>
    <td>https://wiki.teamssix.com/About/</td>
    <td>-</td>
  </tr>
  <tr>
    <td>从零开始的Kubernetes攻防</td>
    <td>https://github.com/neargle/my-re0-k8s-security</td>
    <td>-</td>
  </tr>
  <tr>
    <td>KubeHound 是一个专为 Kubernetes 设计的工具，它通过自动化的方式计算集群内资源之间的潜在攻击路径。这一工具的核心价值在于其能够提供全面的集群扫描，生成直观的攻击图，并提出针对性的保护策略。</td>
    <td>https://github.com/DataDog/KubeHound</td>
    <td>-</td>
  </tr>
  <tr>
    <td>CDK是一款为容器环境定制的渗透测试工具，在已攻陷的容器内部提供零依赖的常用命令及PoC/EXP。集成Docker/K8s场景特有的 逃逸、横向移动、持久化利用方式，插件化管理</td>
    <td>https://github.com/cdk-team/CDK</td>
    <td>-</td>
  </tr>
  <tr>
    <td>云资产管理工具 目前工具定位是云安全相关工具，目前是两个模块 云存储工具、云服务工具， 云存储工具主要是针对oss存储、查看、删除、上传、下载、预览等等 云服务工具主要是针对rds、服务器的管理，查看、执行命令、接管等等</td>
    <td>https://github.com/dark-kingA/cloudTools</td>
    <td>-</td>
  </tr>
  <tr>
    <td>六大云存储，泄露利用检测工具</td>
    <td>https://github.com/UzJu/Cloud-Bucket-Leak-Detection-Tools</td>
    <td>-</td>
  </tr>
  <tr>
    <td>云环境利用框架 Cloud Exploitation Framework 方便红队人员在获得 AK 的后续工作</td>
    <td>https://github.com/teamssix/cf</td>
    <td>-</td>
  </tr>
  <tr>
    <td>云漏洞扫描工具</td>
    <td>https://github.com/Rnalter/ThunderCloud</td>
    <td>-</td>
  </tr>
  <tr>
    <td>云渗透测试工具包</td>
    <td>https://github.com/404tk/cloudtoolkit</td>
    <td>-</td>
  </tr>
</table>

------
如果你有更好的提议或者其他想法，欢迎联系。

by--L0una(guchangan1)



