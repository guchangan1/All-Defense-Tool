# All-Defense-Tool
​	 首先恭喜你发现了宝藏。本项目集成了全网优秀的开源攻防武器项目，包含信息收集工具（自动化利用工具、资产发现工具、目录扫描工具、子域名收集工具、指纹识别工具、端口扫描工具、各种插件....etc...），漏洞利用工具（各大CMS利用工具、中间件利用工具等项目........），内网渗透工具（隧道代理、密码提取.....）、应急响应工具、甲方运维工具、等其他安全攻防资料整理，供攻防双方使用。如果你有更好的建议，欢迎提出请求。

## 免责声明

**重点提醒：本项目工具来源于互联网，是否含带木马及后门请自行甄别！！Hvv来即，请大家提高警惕！！！**

1. `本项目所有内容,仅供学习和研究使用,请勿使用项目的技术手段用于非法用途,任何人造成的任何负面影响,与本人无关.`
2. `本文档所有内容、新闻皆不代表本人态度、立场,如果有建议或方案,欢迎提交 issues`
3. `不会收取任何广告费用,展示的所有工具链接与本人无任何利害关系`

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
  * [常用小工具](#常用小工具)
* [漏洞利用工具](#漏洞利用工具)
  * [漏洞扫描框架/工具](#漏洞扫描框架工具)
  * [中间件漏洞利用工具](#中间件漏洞利用工具)
  * [重点cms利用工具](#重点cms利用工具)
  * [信息泄露利用工具](#信息泄露利用工具)
  * [数据库利用工具](#数据库利用工具)
  * [爆破利用工具](#爆破利用工具)
  * [全网字典收集](#全网字典收集)
  * [常规漏洞利用工具](#常规漏洞利用工具)
  * [反序列化利用工具](#反序列化利用工具)
  * [代码审计辅助工具](#代码审计辅助工具)
* [内网渗透工具](#内网渗透工具)
  * [提权项目](#提权项目)
  * [横向移动工具](#横向移动工具)
  * [shell托管工具](#shell托管工具)
  * [密码提取工具](#密码提取工具)
  * [隧道代理工具](#隧道代理工具)
  * [优秀免杀项目](#优秀免杀项目)
  * [权限维持工具](#权限维持工具)
* [运维&amp;甲方&amp;防守方工具](#运维甲方防守方工具)
  * [Linux应急响应工具](#linux应急响应工具)
  * [Windows应急响应工具](#windows应急响应工具)
  * [内存马查杀工具](#内存马查杀工具)
  * [xxxx](#xxxx)
  * [溯源反制工具](#溯源反制工具)
* [安全资料整理](#安全资料整理)
  * [红蓝资料集锦](#红蓝资料集锦)
  * [云安全资料](#云安全资料)
  * [靶场清单](#靶场清单)
  * [基础设施及环境搭建](#基础设施及环境搭建)

温馨提醒：不要沉迷于攻防而忘了吃饭喔~

- 程序员在家做饭方法指南。https://github.com/Anduin2017/HowToCook

# 半/全自动化利用工具

| 项目简介                                                     | 项目地址                                       | 项目名称      |
| ------------------------------------------------------------ | ---------------------------------------------- | ------------- |
| 一条龙服务，只需要输入根域名即可全方位收集相关资产，并检测漏洞。也可以输入多个域名、C段IP等，具体案例见下文。 | https://github.com/0x727/ShuiZe_0x727          | ShuiZe_0x727  |
| 单兵作战武器库，你值得拥有                                   | https://github.com/yaklang/yakit               | yakit         |
| 自动化巡航扫描框架（可用于红队打点评估）                     | https://github.com/b0bac/ApolloScanner         | ApolloScanner |
| 可针对指定IP段、资产清单、存活网段自动化进行端口扫描以及TCP指纹识别和Banner抓取 | https://github.com/lcvvvv/kscan                | kscan         |
| 一款尚未被发掘的脆弱性扫描工具                               | https://github.com/broken5/bscan               | bscan         |
| 一个漏洞扫描器粘合剂,添加目标后30款工具自动调用              | https://github.com/78778443/QingScan           | QingScan      |
| 分布式资产信息收集和漏洞扫描平台                             | https://github.com/1in9e/gosint                | gosint        |
| 一个辅助平常渗透测试项目或者攻防项目快速打点的综合工具       | https://github.com/P1-Team/AlliN               | AlliN         |
| nemo_go自动化信息收集                                        | https://github.com/hanc00l/nemo_go             | nemo_go       |
| 从子域名、端口服务、漏洞、爬虫等一体化的资产管理系统         | https://github.com/CTF-MissFeng/bayonet        | bayonet       |
| 一个高度可定制Web自动化扫描框架                              | https://github.com/r3curs1v3-pr0xy/vajra       | vajra         |
| reconFTW 集成了30个工具的信息收集利器                        | https://github.com/six2dez/reconftw            | reconftw      |
| 自动化侦查框架                                               | https://github.com/yogeshojha/rengine          | rengine       |
| GUI界面的自动化工具                                          | https://github.com/lz520520/railgun            | Railgun       |
| 在线cms识别\|信息泄露\|工控\|系统\|物联网安全\|cms漏洞扫描\|nmap端口扫描\|子域名获取\|待续.. | https://github.com/iceyhexman/onlinetools      | 在线工具集    |
| Acunetix Web漏洞扫描程序 GUI版本]                            | https://github.com/x364e3ab6/AWVS-13-SCAN-PLUS | AWVS-GUI      |

# 信息收集工具

## 资产发现工具

| 项目简介                                                     | 项目地址                                     | 项目名称        |
| ------------------------------------------------------------ | -------------------------------------------- | --------------- |
| reconFTW 集成了30个工具的信息收集利器                        | https://github.com/six2dez/reconftw          | reconftw        |
| 资产无限巡航扫描系统                                         | https://github.com/awake1t/linglong          | linglong        |
| SRC子域名资产监控                                            | https://github.com/LangziFun/LangSrcCurise   | LangSrcCurise   |
| 快速侦察与目标关联的互联网资产，构建基础资产信息库。         | https://github.com/TophantTechnology/ARL     | ARL(灯塔)       |
| 移动端(Android、iOS、WEB、H5、静态网站)信息收集扫描工具      | https://github.com/kelvinBen/AppInfoScanner  | AppInfoScanner  |
| 集成GoogleHacking语法来进行信息收集                          | https://github.com/TebbaaX/GRecon            | Grecon          |
| 从第三方平台获取目标网页内容                                 | https://github.com/tomnomnom/waybackurls     | waybackurls     |
| 从多个网站提取目标相关信息                                   | https://github.com/lc/gau                    | gau             |
| 集合了多个网络测绘平台，可以快速在多个网络测绘平台搜索信息并且合并展示及导出。 | https://github.com/ExpLangcn/InfoSearchAll   | InfoSearchAll   |
| 调用ZoomEye的官方api---GUI界面                               | https://github.com/xzajyjs/ThunderSearch     | ThunderSearch   |
| 一个简单实用的FOFA客户端 By flashine                         | https://github.com/wgpsec/fofa_viewer        | fofa_viewer     |
| icp备案查询、企业资产快速收集工具                            | https://github.com/SiJiDo/IEyes              | IEyes           |
| 一款基于各大企业信息API的工具                                | https://github.com/wgpsec/ENScan_GO          | ENScan_GO       |
| 基于斗象灯塔ARL修改后的版本。相比原版，增加了OneForAll、中央数据库，修改了altDns | https://github.com/ki9mu/ARL-plus-docker     | ARL-plus-docker |
| 灯塔（最新版）指纹添加脚本！                                 | https://github.com/loecho-sec/ARL-Finger-ADD | ARL-Finger-ADD  |
| apk爬虫工具可提取包内url等信息                               | https://github.com/dwisiswant0/apkleaks      | apkleaks        |
|                                                              |                                              |                 |
|                                                              |                                              |                 |

## 子域名收集工具

| 项目简介                                 | 项目地址                                        | 项目名称          |
| ---------------------------------------- | ----------------------------------------------- | ----------------- |
| 在线子域名收集                           | https://rapiddns.io/subdomain                   | 在线收集          |
| ksubdomain 无状态子域名爆破工具          | https://github.com/knownsec/ksubdomain          | ksubdomain        |
| 一款功能强大的子域收集工具               | https://github.com/shmilylty/OneForAll          | oneforall         |
| 通过使用被动在线资源来发现网站的有效子域 | https://github.com/projectdiscovery/subfinder   | subfinder         |
| src子域名监控                            | https://github.com/LangziFun/LangSrcCurise      | LangSrcCurise     |
| 从 github 上发现子域名                   | https://github.com/gwen001/github-subdomains    | github-subdomains |
| Layer子域名挖掘机                        | https://github.com/euphrat1ca/LayerDomainFinder | Layer             |
| 好用且强大的子域名扫描工具               | https://github.com/yunxu1/dnsub                 | dnsub             |
|                                          |                                                 |                   |
|                                          |                                                 |                   |

## 目录扫描工具

| 项目简介                                   | 项目地址                                          | 项目名称    |
| ------------------------------------------ | ------------------------------------------------- | ----------- |
| Web path scanner  目录扫描工具             | https://github.com/maurosoria/dirsearch           | dirsearch   |
| 用Rust编写的快速，简单，递归的内容发现工具 | https://github.com/epi052/feroxbuster             | feroxbuster |
| 用Go编写的模糊测试工具                     | https://github.com/ffuf/ffuf                      | ffuf        |
| 一个高级web目录、文件扫描工具              | https://github.com/H4ckForJob/dirmap              | dirmap      |
| 网站的敏感目录发掘工具                     | https://github.com/deibit/cansina                 | cansina     |
| 御剑后台扫描工具珍藏版                     | https://www.fujieace.com/hacker/tools/yujian.html | 御剑        |
| 使用GoLang开发的目录/子域扫描器            | https://github.com/ReddyyZ/urlbrute               | urlbrute    |
| 御剑目录扫描专业版                         | https://github.com/foryujian/yjdirscan            | yjdirscan   |
| web目录快速扫描工具，够用                  | https://github.com/hunyaio/yuhScan                | yuhScan     |
| 类似JSFinder的golang实现，更快更全更舒服   | https://github.com/pingc0y/URLFinder              | URLFinder   |
| 爬虫 可以发现搜索引擎发现不了的目录        | https://github.com/jaeles-project/gospider        | gospider    |
|                                            |                                                   |             |
|                                            |                                                   |             |

## 指纹识别工具

| 项目简介                                                 | 项目地址                                         | 项目名称       |
| -------------------------------------------------------- | ------------------------------------------------ | -------------- |
| 红队重点攻击系统指纹探测工具                             | https://github.com/EdgeSecurityTeam/EHole        | EHole(棱洞)2.0 |
| Golang实现Wappalyzer 指纹识别                            | https://github.com/projectdiscovery/wappalyzergo | wappalyzergo   |
| 功能齐全的Web指纹识别和分享平台，内置了一万多条互联网开源的指纹信息。|https://github.com/b1ackc4t/14Finger  |        14Finger        |
| 一个web应用程序指纹识别工具                              | https://github.com/urbanadventurer/WhatWeb       | Whatweb        |
| 一款红队在大量的资产中存活探测与重点攻击系统指纹探测工具 | https://github.com/EASY233/Finger                | Finger         |
| Glass是一款针对资产列表的快速指纹识别工具                | https://github.com/s7ckTeam/Glass                | Glass          |
|  |  |  |



## 端口扫描工具

| 项目简介                                                  | 项目地址                                              | 项目名称   |
| --------------------------------------------------------- | ----------------------------------------------------- | ---------- |
| naabu 用 go 编写的快速端口扫描器                          | https://github.com/projectdiscovery/naabu             | naabu      |
| TXPortMap 实用型的端口扫描、服务识别工具                  | https://github.com/4dogs-cn/TXPortMap                 | TXPortMap  |
| 使用Golang开发的高并发网络扫描、服务探测工具              | https://github.com/Adminisme/ServerScan               | serverScan |
| masnmapscan 一款端口扫描器。整合了masscan和nmap两款扫描器 | https://github.com/hellogoldsnakeman/masnmapscan-V1.0 | 整合扫描器 |
| gonmap是一个go语言的nmap端口扫描库                        | https://github.com/lcvvvv/gonmap                      | gonmap     |
| 光速扫描                                                  | http://pan.baidu.com/s/1pLjaQKF                       | 小米范     |
| 在线端口扫描1                                             | http://coolaf.com/tool/port                           | 在线工具   |
| 在线端口扫描2                                             | http://tool.cc/port/                                  | 在线工具2  |
|                                                           |                                                       |            |
|                                                           |                                                       |            |

## Burp插件

| 项目简介                                                     | 项目地址                                             | 项目名称                |
| ------------------------------------------------------------ | ---------------------------------------------------- | ----------------------- |
| 有关burpsuite的插件(非商店),文章以及使用技巧的收集           | https://github.com/Mr-xn/BurpSuite-collections       | BurpSuite-collections   |
| 一款基于BurpSuite的被动式shiro检测插件                       | https://github.com/pmiaowu/BurpShiroPassiveScan      | BurpShiroPassiveScan    |
| 一款基于BurpSuite的被动式FastJson检测插件                    | https://github.com/pmiaowu/BurpFastJsonScan          | BurpFastJsonScan        |
| fastjson漏洞burp插件，检测fastjson小于1.2.68基于dnslog       | https://github.com/zilong3033/fastjsonScan           | fastjsonScan            |
| HaE 请求高亮标记与信息提取的辅助型 BurpSuite 插件            | https://github.com/gh0stkey/HaE                      | HaE                     |
| domain_hunter_pro 一个资产管理类的Burp插件                   | https://github.com/bit4woo/domain_hunter_pro         | domain_hunter_pro       |
| 新一代子域名主/被动收集工具                                  | https://github.com/Acmesec/Sylas                     | Sylas                   |
| GadgetProbe Burp插件 用来爆破远程类查找Java反序列化          | https://github.com/BishopFox/GadgetProbe             | GadgetProbe             |
| HopLa 自动补全 Payload 的 BurpSuite插件                      | https://github.com/synacktiv/HopLa                   | HopLa                   |
| 验证码识别                                                   | https://github.com/f0ng/captcha-killer-modified      | captcha-killer-modified |
| 一款支持多种加密算法、或直接执行浏览器JS代码的BurpSuite插件。 | https://github.com/whwlsfb/BurpCrypto                | BurpCrypto              |
| 根据自定义来达到对数据包的处理（适用于加解密、爆破等），类似mitmproxy，不同点在于经过了burp中转 | https://github.com/f0ng/autoDecoder                  | autoDecoder             |
| 伪造ip地址                                                   | https://github.com/TheKingOfDuck/burpFakeIP          | burpFakeIP              |
| 自动发送请求                                                 | https://github.com/nccgroup/AutoRepeater             | AutoRepeater            |
| 自动探测请求走私漏洞                                         | https://github.com/portswigger/http-request-smuggler | http-request-smuggler   |
|                                                              |                                                      |                         |

## 浏览器插件

| 项目简介                                        | 项目地址                                                     | 项目名称                          |
| ----------------------------------------------- | ------------------------------------------------------------ | --------------------------------- |
| Hack-Tools  适用于红队的浏览器扩展插件          | https://github.com/LasCC/Hack-Tools                          | Hack-Tools                        |
| SwitchyOmega 浏览器的代理插件                   | https://github.com/FelisCatus/SwitchyOmega                   | SwitchyOmega                      |
| Chrome插件.使用DevTools查找DOM XSS              | https://github.com/filedescriptor/untrusted-types            | untrusted-types                   |
| FOFA Pro view 是一款FOFA Pro 资产展示浏览器插件 | https://github.com/fofapro/fofa_view                         | fofa_view                         |
| mitaka 用于 OSINT 搜索的Chrome和Firefox扩展     | https://github.com/ninoseki/mitaka                           | mitaka                            |
| Git History 查看git存储库文件的历史记录         | https://githistory.xyz/                                      | Git History                       |
| 一款可以检测WEB蜜罐并阻断请求的Chrome插件       | https://github.com/cnrstar/anti-honeypot                     | anti-honeypot                     |
| 一款基于 Chromium的XSS检测工具                  | https://github.com/v8blink/Chromium-based-XSS-Taint-Tracking | Chromium-based-XSS-Taint-Tracking |
|                                                 |                                                              |                                   |

## 邮箱&钓鱼

| 项目简介                                       | 项目地址                                      | 项目名称              |
| ---------------------------------------------- | --------------------------------------------- | --------------------- |
| 邮箱自动化收集爬取                             | https://github.com/Taonn/EmailAll             | EmailAll              |
| 通过搜索引擎爬取电子邮件                       | https://github.com/Josue87/EmailFinder        | EmailFinder           |
| 批量检查邮箱账密有效的  Python 脚本            | https://github.com/rm1984/IMAPLoginTester     | IMAPLoginTester       |
| Coremail邮件系统组织通讯录导出脚本             | https://github.com/dpu/coremail-address-book  | coremail-address-book |
| 拥有在线模板设计、发送诱骗广告等功能的钓鱼系统 | https://github.com/gophish/gophish            | gophish               |
| Swaks SMTP界的瑞士军刀                         | https://github.com/jetmore/swaks              | swaks                 |
| 一个在线的任意发件人发送Email邮件网站          | http://tool.chacuo.net/mailanonymous          | mailanonymous         |
| EwoMail是基于Linux的企业邮箱服务器             | https://github.com/gyxuehu/EwoMail            | EwoMail               |
| 批量发送钓鱼邮箱                               | https://github.com/Yang0615777/sendMail       | sendMail              |
| 免杀宏生成器                                   | https://github.com/Inf0secRabbit/BadAssMacros | BadAssMacros          |

## 社工个人信息收集类

| 项目简介                                               | 项目地址                                                     | 项目名称            |
| ------------------------------------------------------ | ------------------------------------------------------------ | ------------------- |
| 从大量站点中收集用户个人信息                           | https://github.com/soxoj/maigret                             | maigret             |
| 根据邮箱自动搜索泄漏的密码信息                         | https://github.com/D4Vinci/Cr3dOv3r                          | Cr3dOv3r            |
| 密码泄露搜集                                           | https://archive.org/search.php?query=                        | archive             |
| 从部分站点中收集个人信息                               | https://github.com/n0tr00t/Sreg                              | Sreg                |
| 输入人名或邮箱地址, 自动从互联网爬取关于此人的信息     | https://github.com/famavott/osint-scraper                    | osint-scraper       |
| 通过脉脉用户猜测企业邮箱                               | https://github.com/Ridter/Mailget                            | Mailget             |
| 社工字典密码生成                                       | https://github.com/Mebus/cupp                                | cupp                |
| 社会工程学密码生成器，是一个利用个人信息生成密码的工具 | https://github.com/zgjx6/SocialEngineeringDictionaryGenerator | DictionaryGenerator |
| 在线密码生成器                                         | https://zzzteph.github.io/weakpass/                          | weakpass            |
|                                                        |                                                              |                     |

## 常用小工具

| 项目简介                           | 项目地址                               | 项目名称  |
| ---------------------------------- | -------------------------------------- | --------- |
| 好用的去重对比工具                 | https://github.com/tomnomnom/anew      | anew      |
| 视觉侦查工具，用于信息收集屏幕截图 | https://github.com/sensepost/gowitness | gowitness |
|                                    |                                        |           |

# 漏洞利用工具

## 漏洞扫描框架/工具

| 项目简介                                                   | 项目地址                                                     | 项目名称                |
| ---------------------------------------------------------- | ------------------------------------------------------------ | ----------------------- |
| 高危漏洞精准检测与深度利用框架                             | https://github.com/woodpecker-framework/woodpecker-framwork-release | woodpecker-framwork     |
| Web漏洞攻击框架                                            | https://github.com/Anonymous-ghost/AttackWebFrameworkTools   | AttackWebFrameworkTools |
| 基于简单 YAML 的 DSL 的快速且可定制的漏洞扫描器。          | https://github.com/projectdiscovery/nuclei                   | nuclei                  |
| afrog 是一款性能卓越、快速稳定、PoC 可定制化的漏洞扫描工具 | https://github.com/zan8in/afrog                              | afrog                   |
| 一款功能强大的安全评估工具                                 | https://github.com/chaitin/xray                              | Xray                    |
| 网络安全测试工具                                           | https://github.com/gobysec/Goby                              | Goby                    |
| 开源的远程漏洞测试框架                                     | https://github.com/knownsec/pocsuite3                        | pocsuite3               |
| 全新的开源在线 poc 测试框架                                | https://github.com/jweny/pocassist                           | pocassist               |
| 是一款 web 漏洞扫描和验证工具                              | https://github.com/zhzyker/vulmap                            | Vulmap                  |
|                                                            |                                                              |                         |
|                                                            |                                                              |                         |

## 中间件漏洞利用工具

| 项目简介                                                     | 项目地址                                                     | 项目名称                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------ |
| 综合高危漏洞利用工具                                         | https://github.com/Liqunkit/LiqunKit_                        | LiqunKit                 |
| 使用JAVAFX图形化界面检测对HVV中常见的重点CMS系统和OA系统的已公开的漏洞进行验证。 | https://github.com/ExpLangcn/HVVExploitApply                 | HVVExploitApply          |
| Spring系列漏洞利用工具                                       | https://github.com/SummerSec/SpringExploit                   | SpringExploit            |
| shiro 反序列 命令执行辅助检测工具                            | https://github.com/wyzxxz/shiro_rce_tool                     | shiro_rce_tool           |
| shiro反序列化漏洞综合利用,包含（回显执行命令/注入内存马）修复原版中NoCC的问题 | https://github.com/SummerSec/ShiroAttack2                    | ShiroAttack2             |
| shiro反序列化漏洞综合利用,包含（回显执行命令/注入内存马）    | https://github.com/j1anFen/shiro_attack                      | shiro_attack             |
| FastjonExploit \| Fastjson漏洞快速利用框架                   | https://github.com/c0ny1/FastjsonExploit                     | FastjsonExploit          |
| fastjson_rce_tool fastjson命令执行自动化利用工具             | https://github.com/wyzxxz/fastjson_rce_tool                  | fastjson_rce_tool        |
| fastjson一键命令执行                                         | https://github.com/mrknow001/fastjson_rec_exploit            | fastjson_rec_exploit     |
| Jboss（和 Java 反序列化漏洞）验证和利用工具                  | https://github.com/joaomatosf/jexboss                        | exBoss                   |
| Weblogic漏洞利用图形化工具 支持注入内存马、一键上传webshell、命令执行 | https://github.com/sp4zcmd/WeblogicExploit-GUI               | WeblogicExploit-GUI      |
| Weblogic一键漏洞检测工具，V1.5，更新时间：20200730           | https://github.com/rabbitmask/WeblogicScan                   | WeblogicScan             |
| weblogic 漏洞扫描工具。包含2020                              | https://github.com/0xn0ne/weblogicScanner                    | weblogicScanner          |
| weblogic利用工具weblogic-framework                           | https://github.com/0nise/weblogic-framework                  | weblogic-framework       |
| woodpecker框架weblogic信息探测插件                           | https://github.com/woodpecker-appstore/weblogic-infodetector | weblogic-infodetector    |
| Dubbo反序列化一键快速攻击测试工具                            | https://github.com/threedr3am/dubbo-exp                      | dubbo-exp                |
| jenkins-attack-framework 针对 Jenkins 的攻击框架             | https://github.com/Accenture                                 | jenkins-attack-framework |
| Jiraffe 是为利用 Jira 实例而编写的半自动安全工具。           | https://github.com/0x48piraj/Jiraffe                         | Jiraffe                  |
| STS2G Struts2漏洞扫描利用工具 - Golang版                     | https://github.com/xwuyi/STS2G                               | STS2G                    |
| Struts2-Scan Struts2全漏洞扫描利用工具                       | https://github.com/HatBoy/Struts2-Scan                       | Struts2-Scan             |
| log4j漏洞利用工具                                            | https://github.com/kozmer/log4j-shell-poc                    | log4j-shell-poc          |
| Confluence-OGNL一键注入内存shell                             | https://github.com/BeichenDream/CVE-2022-26134-Godzilla-MEMSHELL | Confluence               |

## 重点cms利用工具

| 项目简介                                                     | 项目地址                                                 | 项目名称                    |
| ------------------------------------------------------------ | -------------------------------------------------------- | --------------------------- |
| 综合高危漏洞利用工具                                         | https://github.com/Liqunkit/LiqunKit_                    | LiqunKit                    |
| 致远OA综合利用工具                                           | https://github.com/Summer177/seeyon_exp                  | seeyon_exp                  |
| 致远OA综合利用工具GUI-V1.0                                   | https://github.com/God-Ok/SeeyonExploit-GUI              | SeeyonExploit-GUI           |
| 通达OA综合利用工具                                           | https://github.com/xinyu2428/TDOA_RCE                    | TDOA_RCE                    |
| 蓝凌OA漏洞利用工具/前台无条件RCE/文件写入                    | https://github.com/yuanhaiGreg/LandrayExploit            | LandrayExploit              |
| 泛微OA漏洞综合利用脚本                                       | https://github.com/z1un/weaver_exp                       | weaver_exp                  |
| 锐捷网络EG易网关RCE批量安全检测                              | https://github.com/Tas9er/EgGateWayGetShell              | EgGateWayGetShell           |
| CMSmap 针对流行CMS进行安全扫描的工具                         | https://github.com/Dionach/CMSmap                        | CMSmap                      |
| 使用Go开发的WordPress漏洞扫描工具                            | https://github.com/blackbinn/wprecon                     | wprecon                     |
| 一个 Ruby 框架，旨在帮助对 WordPress 系统进行渗透测试        | https://github.com/rastating/wordpress-exploit-framework | wordpress-exploit-framework |
| WPScan WordPress 安全扫描器                                  | https://github.com/wpscanteam/wpscan                     | wpscan                      |
| WPForce Wordpress 攻击套件                                   | https://github.com/n00py/WPForce                         | WPForce                     |
| 漏洞POC基本适用ThinkPHP全版本漏洞                            | https://github.com/zangcc/Aazhen-v3.1                    | Aazhen-v3.1                 |
| Thinkphp(GUI)漏洞利用工具，支持各版本TP漏洞检测，命令执行，getshell。 | https://github.com/Lotus6/ThinkphpGUI                    | ThinkphpGUI                 |
| ThinkPHP 漏洞 综合利用工具, 图形化界面, 命令执行, 一键getshell, 批量检测, 日志遍历, session包含, 宝塔绕过 | https://github.com/bewhale/thinkphp_gui_tools            | thinkphp_gui_tools          |
|                                                              |                                                          |                             |
|                                                              |                                                          |                             |

## 信息泄露利用工具

| 项目简介                                                     | 项目地址                                                  | 项目名称                          |
| ------------------------------------------------------------ | --------------------------------------------------------- | --------------------------------- |
| 六大云存储，泄露利用检测工具                                 | https://github.com/UzJu/Cloud-Bucket-Leak-Detection-Tools | Cloud-Bucket-Leak-Detection-Tools |
| AK资源管理工具，阿里云/腾讯云 AccessKey AccessKeySecret      | https://github.com/wyzxxz/aksk_tool                       | aksk_tool                         |
| swagger-exp Swagger  REST API 信息泄露利用工具               | https://github.com/lijiejie/swagger-exp                   | swagger-exp                       |
| swagger-hack 自动化爬取并测试所有swagger-ui.html接口         | https://github.com/jayus0821/swagger-hack                 | swagger-hack                      |
| heapdump敏感信息查询工具                                     | https://github.com/wyzxxz/heapdump_tool                   | heapdump_tool                     |
| Packer Fuzzer  针对Webpack等前端打包工具所构造的网站进行检测的扫描工具 | https://github.com/rtcatc/Packer-Fuzzer                   | Packer-Fuzzer                     |
| .git源代码泄露利用工具                                       | https://github.com/BugScanTeam/GitHack                    | GitHack                           |
| .cvs源代码泄露利用工具                                       | https://github.com/kost/dvcs-ripper.git                   | dvcs-ripper                       |
| .DS_store文件泄露利用工具                                    | https://github.com/lijiejie/ds_store_exp                  | ds_store_exp                      |
| SvnExploit支持SVN源代码泄露全版本Dump源码                    | https://github.com/admintony/svnExploit                   | svnExploit                        |
| git-dumper 从网站转储git存储库的工具                         | https://github.com/arthaud/git-dumper                     | git-dumper                        |
| GitDorker  通过使用大型的dorks库来从GitHub抓取敏感信息       | https://github.com/obheda12/GitDorker                     | GitDorker                         |
| 从JavaScript文件中提取敏感信息                               | https://github.com/m4ll0k/SecretFinder                    | SecretFinder                      |
| 功能比较多的一个JavaScript侦查自动化脚本                     | https://github.com/KathanP19/JSFScan.sh                   | JSFScan                           |
| 子域名接管漏洞检测工具，支持30+云服务托管检测                | https://github.com/Ice3man543/SubOver                     | SubOver                           |

## 数据库利用工具

| 项目简介                                                     | 项目地址                                       | 项目名称           |
| ------------------------------------------------------------ | ---------------------------------------------- | ------------------ |
| MDUT 2.0 数据库利用工具                                      | https://github.com/SafeGroceryStore/MDUT       | MDUT               |
| 综合高危漏洞利用工具(包含各大数据库)                         | https://github.com/Liqunkit/LiqunKit_          | LiqunKit           |
| sqlserver利用工具                                            | https://github.com/uknowsec/SharpSQLTools      | SharpSQLTools      |
| 通过套接字重用通过受损的 Microsoft SQL Server  在受限环境中执行横向移动 | https://github.com/blackarrowsec/mssqlproxy    | mssqlproxy         |
| ODAT：Oracle 数据库攻击工具                                  | https://github.com/quentinhardy/odat           | ODAT               |
| Redis未授权访问漏洞利用工具                                  | https://github.com/n0b0dyCN/redis-rogue-server | redis-rogue-server |
| Redis未授权访问漏洞利用工具2                                 | https://github.com/Ridter/redis-rce            | redis-rce          |
| Redis 漏洞利用工具                                           | https://github.com/yuyan-sec/RedisEXP          | RedisEXP           |
| redis主从复制rce的go版本                                     | https://github.com/zyylhn/redis_rce            | redis_rce          |
|                                                              |                                                |                    |

## 爆破利用工具

| 项目简介                                            | 项目地址                                   | 项目名称   |
| --------------------------------------------------- | ------------------------------------------ | ---------- |
| 还是推荐fscan吧，还是还用，更新也快                 | https://github.com/shadow1ng/fscan         | fscan      |
| 爆破神器，懂得都懂                                  | https://github.com/vanhauser-thc/thc-hydra | hydra      |
| 超级弱口令检查工具是一款Windows平台的弱口令审计工具 | https://github.com/shack2/SNETCracker      | 超级弱口令 |
| 集合了fscan和kscan等优秀工具功能的扫描爆破工具。    | https://github.com/i11us0ry/goon           | goon       |
|                                                     |                                            |            |
|                                                     |                                            |            |
|                                                     |                                            |            |
|                                                     |                                            |            |
|                                                     |                                            |            |

## 全网字典收集

| 项目简介                                           | 项目地址                                                   | 项目名称                 |
| -------------------------------------------------- | ---------------------------------------------------------- | ------------------------ |
|                                                    |                                                            |                          |
|                                                    |                                                            |                          |
| 渗透测试、SRC漏洞挖掘、爆破、Fuzzing等字典收集项目 | https://github.com/insightglacier/Dictionary-Of-Pentesting | Dictionary-Of-Pentesting |
| Fuzz 字典,一个就够了                               | https://github.com/TheKingOfDuck/fuzzDicts                 | Web Pentesting           |
| Web 模糊测试字典与一些Payloads                     | https://github.com/gh0stkey/Web-Fuzzing-Box                | Web Fuzzing Box          |
| 上传漏洞fuzz字典生成脚本                           | https://github.com/c0ny1/upload-fuzz-dic-builder           | upload-fuzz-dic-builder  |
| 安全评估期间使用的多种类型列表的集合               | https://github.com/danielmiessler/SecLists                 | SecLists                 |
| 渗透测试仪和Bug赏金猎人的 Payload 库               | https://github.com/sh377c0d3/Payloads                      | Payloads                 |
| 基于实战沉淀下的各种弱口令字典                     | https://github.com/fuzz-security/SuperWordlist             | SuperWordlist            |
| 各类漏洞的 TOP25 参数字典                          | https://github.com/lutfumertceylan/top25-parameter         | top25-parameter          |
| 提取收集以往泄露的密码中符合条件的强弱密码         | https://github.com/r35tart/RW_Password                     | RW_Password              |
|                                                    |                                                            |                          |

## 常规漏洞利用工具

| 项目简介                                                     | 项目地址                                  | 项目名称   |
| ------------------------------------------------------------ | ----------------------------------------- | ---------- |
| DalFox 是一款功能强大的开源 XSS 扫描工具和参数分析器、实用工具 | https://github.com/hahwul/dalfox          | dalfox     |
| 基于DOM的快速XSS漏洞扫描程序                                 | https://github.com/dwisiswant0/findom-xss | findom-xss |
| 很常用的XSS平台                                              | https://github.com/beefproject/beef       | beef       |
| Fast CRLF injection scanning tool                            | https://github.com/Nefcore/CRLFsuite      | CRLFsuite  |
|                                                              |                                           |            |
|                                                              |                                           |            |
|                                                              |                                           |            |
|                                                              |                                           |            |
|                                                              |                                           |            |

## 反序列化利用工具

| 项目简介                                                     | 项目地址                                 | 项目名称        |
| ------------------------------------------------------------ | ---------------------------------------- | --------------- |
| jndi注入工具v1.4                                             | https://github.com/WhiteHSBG/JNDIExploit | JNDIExploit     |
| JNDI服务利用工具 RMI/LDAP，支持部分场景回显、内存shell，高版本JDK场景下利用等 | https://github.com/wyzxxz/jndi_tool      | jndi_tool       |
| 反序列化利用工具                                             | https://github.com/frohoff/ysoserial     | ysoserial       |
| 项目为 ysoserial [su18] 专版，取名为 ysuserial ，在原项目 [ysoserial](https://github.com/frohoff/ysoserial) 基础上魔改而来 | https://github.com/su18/ysoserial/       | ysuserial       |
| ysoserial修改版，着重修改`ysoserial.payloads.util.Gadgets.createTemplatesImpl`使其可以通过引入自定义class的形式来执行命令、内存马、反序列化回显 | https://github.com/Y4er/ysoserial        | ysoserial修改版 |

## 代码审计辅助工具

| 项目简介                                                     | 项目地址                                                     | 项目名称               |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------- |
| 开源的被动式交互式安全测试(IAST)产品                         | https://github.com/HXSecurity/DongTai                        | DongTai                |
| TABBY 是一个基于[Soot](https://github.com/soot-oss/soot)的 Java 代码分析工具。 | https://github.com/wh1t3p1g/tabby                            | tabby                  |
| IDEA依赖检查插件                                             | https://github.com/jeremylong/DependencyCheck                | DependencyCheck        |
| Java Web应用安全漏洞自动化发现                               | https://github.com/find-sec-bugs/find-sec-bugs/wiki/IntelliJ-Tutorial | FindSecBugs            |
| 查找PHP代码漏洞工具                                          | https://github.com/ecriminal/phpvuln                         | phpvuln                |
| 一款不错的静态源代码分析工具，主要用来挖掘PHP程序的漏洞。    | http://rips-scanner.sourceforge.net                          | RIPS                   |
| 源代码静态分析工具，支持Java、PHP、C#、Python、Go等27种编程语言，而且能够集成在IDE、Jenkins、Git等服务。 | https://www.sonarqube.org                                    | SonarQube              |
| 免费开源的语义代码分析引擎和查询工具                         | https://github.com/github/codeql-cli-binaries                | CodeQL                 |
| 一种适用于 C++、C#、VB、PHP、Java、PL/SQL 和 COBOL 的自动化代码安全审查工具。 | https://sourceforge.net/projects/visualcodegrepp/            | VCG(VisualCodeGrepper) |
| 一个专门用于查找Python代码中常见安全问题的工具。             | https://github.com/PyCQA/bandit                              | bandit                 |
| 一个静态代码脆弱性检测系统，支持java源码的审计               | https://github.com/zsdlove/Hades                             | Hades                  |

# 内网渗透工具

## 提权项目

| 项目简介      | 项目地址                         | 项目名称 |
| ------------- | -------------------------------- | -------- |
| Linux自动提权 | https://github.com/liamg/traitor | traitor  |



## 横向移动工具

| 项目简介                                                     | 项目地址                                           | 项目名称            |
| ------------------------------------------------------------ | -------------------------------------------------- | ------------------- |
| Fscan 一款内网综合扫描工具，方便一键自动化、全方位漏扫扫描。 | https://github.com/shadow1ng/fscan                 | fscan               |
| 可针对指定IP段、资产清单、存活网段自动化进行端口扫描以及TCP指纹识别和Banner抓取 | https://github.com/lcvvvv/kscan                    | kscan               |
| K8Cscan大型内网渗透自定义插件化扫描神器                      | https://github.com/k8gege/K8CScan                  | K8Cscan             |
| Ladon一款用于大型网络渗透的多线程插件化综合扫描神器          | https://github.com/k8gege/Ladon                    | Ladon               |
| 集合了fscan和kscan等优秀工具功能的扫描爆破工具。             | https://github.com/i11us0ry/goon                   | goon                |
| Mimikatz  Windows 密码抓取神器                               | https://github.com/gentilkiwi/mimikatz             | mimikatz            |
| 检测域环境内，域机器的本地管理组成员是否存在弱口令和通用口令，对域用户的权限分配以及域内委派查询 | https://github.com/0x727/ShuiYing_0x727            | SchTask_0x727       |
| sharpwmi基于rpc的横向移动工具，具有上传和执行命令功能        | https://github.com/QAX-A-Team/sharpwmi             | sharpwmi            |
| 绕过虚拟机登录验证屏幕的工具                                 | https://github.com/hzphreak/VMInjector             | VMInjector          |
| 常见横向移动与域控权限维持方法                               | https://xz.aliyun.com/t/9382                       | 方法论              |
| 一款比较好的CS后渗透模块插件                                 | https://github.com/pandasec888/taowu-cobalt-strike | taowu-cobalt-strike |
| 一款CS后渗透模块插件，让大家使用一款插件就够了               | https://github.com/d3ckx1/OLa                      | OLa                 |
|                                                              |                                                    |                     |

## shell托管工具

| 项目简介                               | 项目地址                                      | 项目名称        |
| -------------------------------------- | --------------------------------------------- | --------------- |
| 反弹shell就用这个，懂得都懂            | https://github.com/WangYihang/Platypus        | Platypus        |
| 哥斯拉                                 | https://github.com/BeichenDream/Godzilla      | Godzilla        |
| “冰蝎”动态二进制加密网站管理客户端     | https://github.com/rebeyond/Behinder          | Behinder        |
| 中国蚁剑是一款开源的跨平台网站管理工具 | https://github.com/AntSwordProject/antSword   | antSword        |
| 一句话WEB端管理工具                    | https://github.com/boy-hack/WebshellManager   | WebshellManager |
| 跨平台版中国菜刀                       | https://github.com/Chora10/Cknife             | Cknife          |
| Java内存马注入工具                     | https://github.com/WisteriaTiger/JundeadShell | JundeadShell    |
| 拿来即用的Tomcat内存马                 | https://github.com/ce-automne/TomcatMemShell  | TomcatMemShell  |
|                                        |                                               |                 |

## 密码提取工具

| 项目简介                                                     | 项目地址                                          | 项目名称               |
| ------------------------------------------------------------ | ------------------------------------------------- | ---------------------- |
| 各种密码提取                                                 | https://github.com/kerbyj/goLazagne               | goLazagne              |
| 用于读取常用程序密码，如Navicat、TeamViewer、FileZilla、WinSCP等 | https://github.com/RowTeam/SharpDecryptPwd        | SharpDecryptPwd        |
| Xshell，Xftp密码解密工具                                     | https://github.com/JDArmy/SharpXDecrypt           | SharpXDecrypt          |
| 解密浏览器数据（密码\|历史记录\|Cookie\|书签 \| 信用卡 \| 下载记录）的导出工具，支持全平台主流浏览器。 | https://github.com/moonD4rk/HackBrowserData/      | HackBrowserData        |
| 一款针对向日葵的识别码和验证码提取工具                       | https://github.com/wafinfo/Sunflower_get_Password | Sunflower_get_Password |
| 一键辅助抓取360安全浏览器密码的CobaltStrike脚本以及解密小工具 | https://github.com/hayasec/360SafeBrowsergetpass  | 360SafeBrowsergetpass  |
| BrowserGhost  抓取浏览器密码的工具                           | https://github.com/QAX-A-Team/BrowserGhost        | BrowserGhost           |
| win-brute-logon  无需权限破解任何 Microsoft Windows 用户密码 | https://github.com/DarkCoderSc/win-brute-logon    | win-brute-logon        |
| TeamViewer：Bypass杀软 获取 Teamview 密码的工具              | https://github.com/wafinfo/TeamViewer             | TeamViewer             |
| Xdecrypt Xshell  Xftp 密码解密                               | https://github.com/dzxs/Xdecrypt                  | Xdecrypt               |
|                                                              |                                                   |                        |
|                                                              |                                                   |                        |
|                                                              |                                                   |                        |
|                                                              |                                                   |                        |

## 隧道代理工具

| 项目简介                                                     | 项目地址                                   | 项目名称       |
| ------------------------------------------------------------ | ------------------------------------------ | -------------- |
| 全平台代理工具，支持多种socks协议                            | https://www.proxifier.com/                 | proxifier      |
| 专注于内网穿透的高性能的反向代理应用                         | https://github.com/fatedier/frp            | frp            |
| 轻量级、高性能、功能强大的内网穿透代理服务器                 | https://github.com/ehang-io/nps            | nps            |
| 改进的reGeorg版本                                            | https://github.com/L-codes/Neo-reGeorg     | Neo-reGeorg    |
| 是一款利用dns协议传输tcp数据的工具                           | https://github.com/alex-sector/dns2tcp     | dns2tcp        |
| 是一个DNS隧道工具                                            | https://github.com/iagox86/dnscat2         | dnscat2        |
| 内网渗透代理、端口转发工具                                   | http://rootkiter.com/Termite/              | Termite        |
| 一个简单的 reverse ICMP shell                                | https://github.com/inquisb/icmpsh          | icmpsh         |
| 正/反向代理，内网穿透，端口转发                              | https://github.com/inconshreveable/ngrok   | ngrok          |
| pingtunnel 是把 tcp/udp/sock5 流量伪装成 icmp  流量进行转发的工具 | https://github.com/esrrhs/pingtunnel       | pingtunnel     |
| pystinger - 一款使用webshell进行流量转发的出网工具           | https://github.com/FunnyWolf/pystinger     | pystinger      |
| goproxy 一款轻量级、功能强大、高性能的多种代理工具           | https://github.com/snail007/goproxy        | goproxy        |
| 一款可以在不出网的环境下进行反向代理及cs上线的工具           | https://github.com/Daybr4ak/C2ReverseProxy | C2ReverseProxy |

## 优秀免杀项目

| 项目简介                                                     | 项目地址                                           | 项目名称               |
| ------------------------------------------------------------ | -------------------------------------------------- | ---------------------- |
| TideSec团队整理的远控免杀系列文章及配套工具，汇总测试了互联网上的几十种免杀工具。 | https://github.com/TideSec/BypassAntiVirus         | BypassAntiVirus        |
| 跟杀软和免杀有关的资料，当前包括200+工具和1300+文章  --Thanks:小雨 | https://github.com/alphaSeclab/anti-av             | anti-av                |
| 用于快速生成免杀的 EXE 可执行文件，目前拥有三种免杀方法。    | https://github.com/lengjibo/FourEye                | FourEye                |
| 掩日 - 免杀执行器生成工具 用于快速生成免杀的 EXE 可执行文件  | https://github.com/1y0n/AV_Evasion_Tool            | AV_Evasion_Tool        |
| 自动化生成 EDR 软件 Bypass Payload 的工具,一键化签名免杀     | https://github.com/optiv/ScareCrow                 | ScareCrow              |
| 梅花K战队写的Nim一键免杀源码 使用nim语言进行shellcode加载    | https://github.com/M-Kings/BypassAv-web            | BypassAv-web           |
| CS免杀,包括python版\C版本\GO版本\powershell版本              | https://github.com/Gality369/CS-Loader             | CS-Loader              |
| 绕3环的shellcode免杀框架                                     | https://github.com/mai1zhi2/ShellCodeFramework     | ShellCodeFramework     |
| 生成完美Powershell Payload的自动化工具                       | https://github.com/GetRektBoy724/MeterPwrShell     | MeterPwrShell          |
| js免杀shellcode，绕过杀毒添加自启动                          | https://github.com/Hzllaga/JsLoader                | JsLoader               |
| PowerShell 模糊脚本 使用字符串替换和变量串联 Bypass  常见的检测签名 | https://github.com/tokyoneon/Chimera               | Chimera                |
| 一款利用加载器以及Python反序列化绕过AV的在线免杀工具         | https://github.com/yhy0/AVByPass                   | AVByPass               |
| 绕过专业工具检测的Webshell研究文章和免杀的Webshell源码       | https://github.com/LandGrey/webshell-detect-bypass | webshell-detect-bypass |
| 一种创建欺骗代码的证书签名工具以及对二进制文件和DLL文件进行签名的工具 | https://github.com/Tylous/Limelighter              | Limelighter            |
| Cobalt Strike插件，用于快速生成免杀的可执行文件              | https://github.com/hack2fun/BypassAV               | BypassAV               |
| 无落地文件的 Windows 证书导入导出工具                        | https://github.com/TheWover/CertStealer            | CertStealer            |
| 通过阻止入口点执行来绕过EDR主动防御的DLL                     | https://github.com/CCob/SharpBlock                 | SharpBlock             |
|                                                              |                                                    |                        |
|                                                              |                                                    |                        |

## 权限维持工具

| 项目简介                                           | 项目地址                               | 项目名称      |
| -------------------------------------------------- | -------------------------------------- | ------------- |
| 创建隐藏计划任务，权限维持，Bypass AV              | https://github.com/0x727/SchTask_0x727 | SchTask_0x727 |
| 进行克隆用户、添加用户等账户防护安全检测的轻巧工具 | https://github.com/0x727/CloneX_0x727  | CloneX_0x727  |
|                                                    |                                        |               |





# 运维&甲方&防守方工具

## Linux应急响应工具

| 项目简介                                                  | 项目地址                                              | 项目名称     |
| --------------------------------------------------------- | ----------------------------------------------------- | ------------ |
| 主机侧Checklist的自动全面化检测脚本                       | https://github.com/grayddq/GScan                      | Gscan        |
| 应急响应实战笔记，一个安全工程师的自我修养                | https://github.com/Bypass007/Emergency-Response-Notes | Bypass007    |
| linux信息收集/应急响应/常见后门/挖矿检测/webshell检测脚本 | https://github.com/al0ne/LinuxCheck                   | LinuxCheck   |
| uroboros-一个GNU/Linux监视和概要分析工具，专注于单个进程  | https://github.com/evilsocket/uroboros                | uroboros     |
| whohk linux下一款强大的应急响应工具                       | https://github.com/heikanet/whohk                     | whohk        |
| Malwoverview 是用于威胁搜寻的第一响应工具                 | https://github.com/alexandreborges/malwoverview       | malwoverview |
| Rootkit Hunter Rootkit猎手                                | http://rkhunter.sourceforge.net/                      | Rootkitr     |
|                                                           |                                                       |              |
|                                                           |                                                       |              |
|                                                           |                                                       |              |
|                                                           |                                                       |              |
|                                                           |                                                       |              |
|                                                           |                                                       |              |

## Windows应急响应工具

| 项目简介                                                     | 项目地址                                                     | 项目名称           |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------ |
| 包含一系列免费的系统分析工具，如Process Explorer、启动项分析工具 AutoRuns等。 | https://docs.microsoft.com/zh-cn/sysinternals/downloads/     | SysinternalsSuite  |
| 微软公司出品的日志分析工具，它功能强大，使用简单。           | https://www.microsoft.com/en-us/download/details.aspx?id=24659 | Log Parser         |
| 火麒麟-网络安全应急响应工具(系统痕迹采集)                    | https://github.com/MountCloud/FireKylin                      | FireKylin          |
| APT-Hunter Windows日志事件应急工具                           | https://github.com/ahmedkhlief/APT-Hunter                    | APT-Hunter         |
| webshell查杀工具                                             | http://www.shelldetector.com/                                | Web Shell Detector |
| 河马webshell查杀                                             | https://www.shellpub.com/                                    | 河马webshell       |
| 日志分析库,nuclei 的另一种用法                               | https://github.com/ffffffff0x/LOG-HUB                        | LOG-HUB            |
| 一个免费，功能强大的多功能工具，可帮助您监视系统资源，调试软件和检测恶意软件。 | https://processhacker.sourceforge.io/                        | Process Hacker     |
|                                                              |                                                              |                    |
|                                                              |                                                              |                    |
|                                                              |                                                              |                    |
|                                                              |                                                              |                    |
|                                                              |                                                              |                    |

## 内存马查杀工具

| 项目简介                                       | 项目地址                                       | 项目名称              |
| ---------------------------------------------- | ---------------------------------------------- | --------------------- |
| Alibaba Java诊断利器Arthas                     | https://github.com/alibaba/arthas              | arthas                |
| 检测绝大部分所谓的内存免杀马                   | https://github.com/huoji120/DuckMemoryScan     | DuckMemoryScan        |
| 通过jsp脚本扫描java web Filter/Servlet型内存马 | https://github.com/c0ny1/java-memshell-scanner | java-memshell-scanner |
| A java memory web shell extracting tool        | https://github.com/LandGrey/copagent           | copagent              |
| 杀内存马的小工具                               | https://github.com/r00t4dm/aLIEz               | aLIEz                 |
|                                                |                                                |                       |

## xxxx

| 项目简介                                                | 项目地址                                                 | 项目名称                  |
| ------------------------------------------------------- | -------------------------------------------------------- | ------------------------- |
| 一款基于 IP 信誉度信息实现的实时检测 Web 恶意流量的工具 | https://github.com/CRED-CLUB/ARTIF                       | ARTIF                     |
| 勒索病毒解密工具汇总                                    | https://github.com/jiansiting/Decryption-Tools/          | Decryption-Tools          |
| Shiro-Cookie解密小工具                                  | https://github.com/r00tuser111/SerializationDumper-Shiro | SerializationDumper-Shiro |

## 溯源反制工具

| 项目简介                                                     | 项目地址                                         | 项目名称         |
| ------------------------------------------------------------ | ------------------------------------------------ | ---------------- |
| 伪造Myslq服务端,并利用Mysql逻辑漏洞来获取客户端的任意文件反击攻击者 | https://github.com/BeichenDream/MysqlT           | MysqlT           |
| 检测目标Mysql数据库是不是蜜罐                                | https://github.com/BeichenDream/WhetherMysqlSham | WhetherMysqlSham |
| 安全、快捷、高交互、企业级的蜜罐管理系统，护网；支持多种协议蜜罐、蜜签、诱饵等功能。 | https://github.com/seccome/Ehoney                | Ehoney           |

# 安全资料整理

## 红蓝资料集锦

| 项目简介                                                     | 项目地址                                     | 项目名称            |
| ------------------------------------------------------------ | -------------------------------------------- | ------------------- |
| 红蓝对抗以及护网相关工具和资料，内存shellcode（cs+msf）和内存马查杀工具 | https://github.com/Mr-xn/RedTeam_BlueTeam_HW | RedTeam_BlueTeam_HW |
|                                                              |                                              |                     |

## 云安全资料

| 项目简介                                                     | 项目地址                                                  | 项目名称                          |
| ------------------------------------------------------------ | --------------------------------------------------------- | --------------------------------- |
| 也许这是国内第一个云安全知识文库                             | https://wiki.teamssix.com/About/                          | T Wiki                            |
| 从零开始的Kubernetes攻防                                     | https://github.com/neargle/my-re0-k8s-security            | my-re0-k8s-security               |
| 六大云存储，泄露利用检测工具                                 | https://github.com/UzJu/Cloud-Bucket-Leak-Detection-Tools | Cloud-Bucket-Leak-Detection-Tools |
| 云环境利用框架 Cloud Exploitation Framework 方便红队人员在获得 AK 的后续工作 | https://github.com/teamssix/cf                            | cf                                |

## 靶场清单

通用漏洞类：

| 项目简介                                                     | 项目地址                                         | 项目名称             |
| ------------------------------------------------------------ | ------------------------------------------------ | -------------------- |
| 在线靶场                                                     | https://hackmyvm.eu/anon/                        | hackmyvm             |
| Vulfocus 是一个漏洞集成平台，将漏洞环境 docker 镜像，放入即可使用，开箱即用。 | https://github.com/fofapro/vulfocus              | vulfocus             |
| 基于 Docker-Compose 的预建易受攻击环境                       | https://github.com/vulhub/vulhub                 | vulhub               |
| Spring Boot 相关漏洞学习资料，利用方法和技巧合               | https://github.com/LandGrey/SpringBootVulExploit | SpringBootVulExploit |
|                                                              |                                                  |                      |

基础漏洞类：

| 项目简介                                              | 项目地址                                                     | 项目名称       |
| ----------------------------------------------------- | ------------------------------------------------------------ | -------------- |
| 基础漏洞靶场                                          | https://dvwa.co.uk/                                          | dvwa           |
| 常见的web漏洞                                         | https://www.pentesterlab.com/exercises/web_for_pentester/course | pentesterlab   |
| Java漏洞平台                                          | https://github.com/j3ers3/Hello-Java-Sec                     | Hello-Java-Sec |
| JAVA 漏洞靶场                                         | https://github.com/tangxiaofeng7/SecExample                  | SecExample     |
| 一个想帮你总结所有类型的上传漏洞的靶场                | https://github.com/c0ny1/upload-labs                         | upload-labs    |
| SQLI 实验室测试基于错误、基于布尔值、基于时间。       | https://github.com/Audi-1/sqli-labs                          | sqli-labs      |
| 一个包含php,java,python,C#等各种语言版本的XXE漏洞Demo | https://github.com/c0ny1/xxe-lab                             | xxe-lab        |

## 基础设施及环境搭建

| 项目简介                                       | 项目地址                                 | 项目名称       |
| ---------------------------------------------- | ---------------------------------------- | -------------- |
| 红/蓝队环境自动化部署工具                      | https://github.com/ffffffff0x/f8x        | f8x            |
| Frps 一键安装脚本&管理脚本                     | https://github.com/MvsCode/frps-onekey   | frps-onekey    |
| 修改frp支持域前置与配置文件自删除              | https://github.com/uknowsec/frpModify    | frpModify      |
| 一款功能强大的代理检查和IP地址轮转工具         | https://github.com/kitabisa/mubeng       | mubeng         |
| 利用fofa搜索socks5开放代理进行代理池轮切的工具 | https://github.com/akkuman/rotateproxy   | rotateproxy    |
| 利用IP地址池进行自动切换Http代理，防止IP封禁。 | https://github.com/Mustard404/Auto_proxy | Auto_proxy     |
| 命令行全局代理--跨平台通用                     | https://github.com/rofl0r/proxychains-ng | proxychains-ng |
|                                                |                                          |                |

正在整理中………………

------
如果你有更好的提议或者其他想法，欢迎联系。

by--L0una(guchangan1)



