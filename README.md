# All-Defense-Tool
 首先恭喜你发现了宝藏。本项目集成了全网优秀的攻防武器项目，包含信息收集工具（自动化利用工具、资产发现工具、目录扫描工具、子域名收集工具....etc...），漏洞利用工具（各大CMS利用工具、中间件利用工具等项目），内网渗透工具、应急响应工具、甲方运维工具、等其他安全资料项目，供攻防双方使用。如果你有更好的建议，欢迎提出请求，本文收录全网优秀工具，欢迎大佬提交。
# 目录

* [信息收集工具](#信息收集工具)
  * [半/全自动化利用工具](#半全自动化利用工具)
  * [资产发现工具](#资产发现工具)
  * [子域名收集工具](#子域名收集工具)
  * [目录扫描工具](#目录扫描工具)
  * [指纹识别工具](#指纹识别工具)
  * [端口扫描工具](#端口扫描工具)
  * [Burp\+浏览器插件](#burp浏览器插件)
* [漏洞利用工具](#漏洞利用工具)
  * [信息泄露利用工具](#信息泄露利用工具)
  * [漏洞扫描框架/工具](#漏洞扫描框架工具)
  * [中间件漏洞利用工具](#中间件漏洞利用工具)
  * [重点cms利用工具](#重点cms利用工具)
  * [常规漏洞利用工具](#常规漏洞利用工具)
  * [数据库利用工具](#数据库利用工具)
  * [爆破工具](#爆破工具)
  * [字典收集](#字典收集)
* [内网渗透工具](#内网渗透工具)
  * [webshell托管工具](#webshell托管工具)
  * [密码提取工具](#密码提取工具)
  * [横向移动工具](#横向移动工具)
  * [隧道代理工具](#隧道代理工具)
* [运维&amp;甲方&amp;防守方工具](#运维甲方防守方工具)
  * [应急响应工具](#应急响应工具)
* [安全资料整理](#安全资料整理)

## 半/全自动化利用工具

| 项目名称      | 项目地址                                       | 项目简介                                                     |
| ------------- | ---------------------------------------------- | ------------------------------------------------------------ |
| ShuiZe_0x727  | https://github.com/0x727/ShuiZe_0x727          | 一条龙服务，只需要输入根域名即可全方位收集相关资产，并检测漏洞。也可以输入多个域名、C段IP等，具体案例见下文。 |
| nemo_go       | https://github.com/hanc00l/nemo_go             | nemo_go自动化信息收集                                        |
| gosint        | https://github.com/1in9e/gosint                | 分布式资产信息收集和漏洞扫描平台                       |
| ApolloScanner | https://github.com/b0bac/ApolloScanner         | 自动化巡航扫描框架（可用于红队打点评估）                     |
|               |                                                |                                                              |
| rengine       | https://github.com/yogeshojha/rengine          | 自动化侦查框架                                               |
| Railgun       | https://github.com/lz520520/railgun            | GUI界面的自动化工具                                          |
| 在线工具集    | https://github.com/iceyhexman/onlinetools      | 在线cms识别\|信息泄露\|工控\|系统\|物联网安全\|cms漏洞扫描\|nmap端口扫描\|子域名获取\|待续.. |
| AlliN         | https://github.com/P1-Team/AlliN               | 一个辅助平常渗透测试项目或者攻防项目快速打点的综合工具       |
| AWVS-GUI      | https://github.com/x364e3ab6/AWVS-13-SCAN-PLUS | Acunetix Web漏洞扫描程序 GUI版本]                            |
| vajra         | https://github.com/r3curs1v3-pr0xy/vajra       | 一个高度可定制Web自动化扫描框架            |
| bayonet       | https://github.com/CTF-MissFeng/bayonet        | 从子域名、端口服务、漏洞、爬虫等一体化的资产管理系统         |
| kscan         | https://github.com/lcvvvv/kscan                | 可针对指定IP段、资产清单、存活网段自动化进行端口扫描以及TCP指纹识别和Banner抓取 |

## 资产发现工具

| 项目名称                            | 项目地址                                    | 项目简介                                                |
| ----------------------------------- | ------------------------------------------- | ------------------------------------------------------- |
| linglong                            | https://github.com/awake1t/linglong         | 资产无限巡航扫描系统                                    |
| LangSrcCurise                       | https://github.com/LangziFun/LangSrcCurise  | SRC子域名资产监控                                       |
| ARL(灯塔)                           | https://github.com/TophantTechnology/ARL    | 快速侦察与目标关联的互联网资产，构建基础资产信息库。    |
| AppInfoScanner                      | https://github.com/kelvinBen/AppInfoScanner | 移动端(Android、iOS、WEB、H5、静态网站)信息收集扫描工具 |
| 集成GoogleHacking语法来进行信息收集 | https://github.com/TebbaaX/GRecon           | Grecon                                                  |
|                                     |                                             |                                                         |
|                                     |                                             |                                                         |

## 子域名收集工具

| 项目简介                                 | 项目地址                                        | 项目名称      |
| ---------------------------------------- | ----------------------------------------------- | ------------- |
| 在线子域名收集                           | https://rapiddns.io/subdomain                   | 在线收集      |
| ssl证书扫域名                            | [https://myssl.com/ ](https://myssl.com/)       | myssl         |
| 一款功能强大的子域收集工具               | https://github.com/shmilylty/OneForAll          | oneforall     |
| ksubdomain 无状态子域名爆破工具          | https://github.com/knownsec/ksubdomain          | ksubdomain    |
| 好用且强大的子域名扫描工具               | https://github.com/yunxu1/dnsub                 | dnsub         |
| Layer子域名挖掘机                        | https://github.com/euphrat1ca/LayerDomainFinder | Layer         |
| src子域名监控                            | https://github.com/LangziFun/LangSrcCurise      | LangSrcCurise |
| 通过使用被动在线资源来发现网站的有效子域 | https://github.com/projectdiscovery/subfinder   | subfinder     |
|                                          |                                                 |               |

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
|                                            |                                                   |             |
|                                            |                                                   |             |

## 指纹识别工具

| 项目简介                                                 | 项目地址                                         | 项目名称       |
| -------------------------------------------------------- | ------------------------------------------------ | -------------- |
| 红队重点攻击系统指纹探测工具                             | https://github.com/EdgeSecurityTeam/EHole        | EHole(棱洞)2.0 |
| 功能齐全的Web指纹识别和分享平台，内置了一万多条互联网开源的指纹信息。|https://github.com/b1ackc4t/14Finger  |        14Finger        |
| 一个web应用程序指纹识别工具                              | https://github.com/urbanadventurer/WhatWeb       | Whatweb        |
| Golang实现Wappalyzer 指纹识别                            | https://github.com/projectdiscovery/wappalyzergo | wappalyzergo   |
| 一款红队在大量的资产中存活探测与重点攻击系统指纹探测工具 | https://github.com/EASY233/Finger                | Finger         |
| Glass是一款针对资产列表的快速指纹识别工具                | https://github.com/s7ckTeam/Glass                | Glass          |



## 端口扫描工具

| 项目简介                                                  | 项目地址                                              | 项目名称   |
| --------------------------------------------------------- | ----------------------------------------------------- | ---------- |
| TXPortMap 实用型的端口扫描、服务识别工具                  | https://github.com/4dogs-cn/TXPortMap                 | TXPortMap  |
| 使用Golang开发的高并发网络扫描、服务探测工具              | https://github.com/Adminisme/ServerScan               | serverScan |
| naabu 用 go 编写的快速端口扫描器                          | https://github.com/projectdiscovery/naabu             | naabu      |
| masnmapscan 一款端口扫描器。整合了masscan和nmap两款扫描器 | https://github.com/hellogoldsnakeman/masnmapscan-V1.0 | 整合扫描器 |
| gonmap是一个go语言的nmap端口扫描库                        | https://github.com/lcvvvv/gonmap                      | gonmap     |
| 在线端口扫描1                                             | http://coolaf.com/tool/port                           | 在线工具   |
| 在线端口扫描2                                             | http://tool.cc/port/                                  | 在线工具2  |
|                                                           |                                                       | 小米范     |
|                                                           |                                                       |            |
|                                                           |                                                       |            |

## Burp+浏览器插件

| 项目简介                                               | 项目地址                                          | 项目名称                |
| ------------------------------------------------------ | ------------------------------------------------- | ----------------------- |
| 有关burpsuite的插件(非商店),文章以及使用技巧的收集     | https://github.com/Mr-xn/BurpSuite-collections    | BurpSuite-collections   |
| 一款基于BurpSuite的被动式shiro检测插件                 | https://github.com/pmiaowu/BurpShiroPassiveScan   | BurpShiroPassiveScan    |
| 一款基于BurpSuite的被动式FastJson检测插件              | https://github.com/pmiaowu/BurpFastJsonScan       | BurpFastJsonScan        |
| fastjson漏洞burp插件，检测fastjson小于1.2.68基于dnslog | https://github.com/zilong3033/fastjsonScan        | fastjsonScan            |
| HaE 请求高亮标记与信息提取的辅助型 BurpSuite 插件      | https://github.com/gh0stkey/HaE                   | HaE                     |
| domain_hunter_pro 一个资产管理类的Burp插件             | https://github.com/bit4woo/domain_hunter_pro      | domain_hunter_pro       |
| GadgetProbe Burp插件 用来爆破远程类查找Java反序列化    | https://github.com/BishopFox/GadgetProbe          | GadgetProbe             |
| HopLa 自动补全 Payload 的 BurpSuite插件                | https://github.com/synacktiv/HopLa                | HopLa                   |
| 验证码识别                                             | https://github.com/f0ng/captcha-killer-modified   | captcha-killer-modified |
| 伪造ip地址                                             | https://github.com/TheKingOfDuck/burpFakeIP       | burpFakeIP              |
| 自动发送请求                                           | https://github.com/nccgroup/AutoRepeater          | AutoRepeater            |
|                                                        |                                                   |                         |
| Hack-Tools  适用于红队的浏览器扩展插件                 | https://github.com/LasCC/Hack-Tools               | Hack-Tools              |
| SwitchyOmega 浏览器的代理插件                          | https://github.com/FelisCatus/SwitchyOmega        | SwitchyOmega            |
| Chrome插件.使用DevTools查找DOM XSS                     | https://github.com/filedescriptor/untrusted-types | untrusted-types         |
| FOFA Pro view 是一款FOFA Pro 资产展示浏览器插件        | https://github.com/fofapro/fofa_view              | fofa_view               |
| mitaka 用于 OSINT 搜索的Chrome和Firefox扩展            | https://github.com/ninoseki/mitaka                | mitaka                  |
| Git History 查看git存储库文件的历史记录                | https://githistory.xyz/                           | Git History             |

# 漏洞利用工具

## 信息泄露利用工具

| 项目简介                                                     | 项目地址                                  | 项目名称      |
| ------------------------------------------------------------ | ----------------------------------------- | ------------- |
| swagger-exp Swagger  REST API 信息泄露利用工具               | https://github.com/lijiejie/swagger-exp   | swagger-exp   |
| swagger-hack 自动化爬取并测试所有swagger-ui.html接口         | https://github.com/jayus0821/swagger-hack | swagger-hack  |
| Packer Fuzzer  针对Webpack等前端打包工具所构造的网站进行检测的扫描工具 | https://github.com/rtcatc/Packer-Fuzzer   | Packer-Fuzzer |
| SvnExploit支持SVN源代码泄露全版本Dump源码                    | https://github.com/admintony/svnExploit   | svnExploit    |
| git-dumper 从网站转储git存储库的工具                         | https://github.com/arthaud/git-dumper     | git-dumper    |
| GitDorker  通过使用大型的dorks库来从GitHub抓取敏感信息       | https://github.com/obheda12/GitDorker     | GitDorker     |
| 从JavaScript文件中提取敏感信息                               | https://github.com/m4ll0k/SecretFinder    | SecretFinder  |
| 功能比较多的一个JavaScript侦查自动化脚本                     | https://github.com/KathanP19/JSFScan.sh   | JSFScan       |
|                                                              |                                           |               |

## 漏洞扫描框架/工具

| 项目简介                       | 项目地址                                                     | 项目名称                |
| ------------------------------ | ------------------------------------------------------------ | ----------------------- |
|                                |                                                              |                         |
| 高危漏洞精准检测与深度利用框架 | https://github.com/woodpecker-framework/woodpecker-framwork-release | woodpecker-framwork     |
| Web漏洞攻击框架                | https://github.com/Anonymous-ghost/AttackWebFrameworkTools   | AttackWebFrameworkTools |
| 开源的远程漏洞测试框架         | https://github.com/knownsec/pocsuite3                        | pocsuite3               |
| 全新的开源在线 poc 测试框架    | https://github.com/jweny/pocassist                           | pocassist               |
| 一款功能强大的安全评估工具     | https://github.com/chaitin/xray                              | Xray                    |
| 网络安全测试工具               | https://github.com/gobysec/Goby                              | Goby                    |
| 是一款 web 漏洞扫描和验证工具  | https://github.com/zhzyker/vulmap                            | Vulmap                  |

## 中间件漏洞利用工具

| 项目简介                                                     | 项目地址                                                     | 项目名称                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------ |
| 综合高危漏洞利用工具                                         | https://github.com/Liqunkit/LiqunKit_                        | LiqunKit                 |
| Spring系列漏洞利用工具                                       | https://github.com/SummerSec/SpringExploit                   | SpringExploit            |
| shiro反序列化漏洞综合利用,包含（回显执行命令/注入内存马）修复原版中NoCC的问题 | https://github.com/SummerSec/ShiroAttack2                    | ShiroAttack2             |
| shiro反序列化漏洞综合利用,包含（回显执行命令/注入内存马）    | https://github.com/j1anFen/shiro_attack                      | shiro_attack             |
| FastjonExploit \| Fastjson漏洞快速利用框架                   | https://github.com/c0ny1/FastjsonExploit                     | FastjsonExploit          |
| fastjson_rce_tool fastjson命令执行自动化利用工具             | https://github.com/wyzxxz/fastjson_rce_tool                  | fastjson_rce_tool        |
| fastjson一键命令执行                                         | https://github.com/mrknow001/fastjson_rec_exploit            | fastjson_rec_exploit     |
| Jboss（和 Java 反序列化漏洞）验证和利用工具                  | https://github.com/joaomatosf/jexboss                        | exBoss                   |
| weblogic利用工具weblogic-framework                           | https://github.com/0nise/weblogic-framework                  | weblogic-framework       |
| woodpecker框架weblogic信息探测插件                           | https://github.com/woodpecker-appstore/weblogic-infodetector | weblogic-infodetector    |
| Dubbo反序列化一键快速攻击测试工具                            | https://github.com/threedr3am/dubbo-exp                      | dubbo-exp                |
| jenkins-attack-framework 针对 Jenkins 的攻击框架             | https://github.com/Accenture                                 | jenkins-attack-framework |
| Jiraffe 是为利用 Jira 实例而编写的半自动安全工具。           | https://github.com/0x48piraj/Jiraffe                         | Jiraffe                  |
| STS2G Struts2漏洞扫描利用工具 - Golang版                     | https://github.com/xwuyi/STS2G                               | STS2G                    |
| Struts2-Scan Struts2全漏洞扫描利用工具                       | https://github.com/HatBoy/Struts2-Scan                       | Struts2-Scan             |
| spring boot Fat Jar 任意写文件漏洞到稳定 RCE 利用技巧        | https://github.com/LandGrey/spring-boot-upload-file-lead-to-rce-tricks | Fat Jar                  |

## 重点cms利用工具

| 项目简介                                              | 项目地址                                                 | 项目名称                    |
| ----------------------------------------------------- | -------------------------------------------------------- | --------------------------- |
| 致远OA综合利用工具                                    | https://github.com/Summer177/seeyon_exp                  | seeyon_exp                  |
| 通达OA综合利用工具                                    | https://github.com/xinyu2428/TDOA_RCE                    | TDOA_RCE                    |
| 蓝凌OA漏洞利用工具/前台无条件RCE/文件写入             | https://github.com/yuanhaiGreg/LandrayExploit            | LandrayExploit              |
| 泛微OA漏洞综合利用脚本                                | https://github.com/z1un/weaver_exp                       | weaver_exp                  |
| 锐捷网络EG易网关RCE批量安全检测                       | https://github.com/Tas9er/EgGateWayGetShell              | EgGateWayGetShell           |
| CMSmap 针对流行CMS进行安全扫描的工具                  | https://github.com/Dionach/CMSmap                        | CMSmap                      |
| 使用Go开发的WordPress漏洞扫描工具                     | https://github.com/blackbinn/wprecon                     | wprecon                     |
| 一个 Ruby 框架，旨在帮助对 WordPress 系统进行渗透测试 | https://github.com/rastating/wordpress-exploit-framework | wordpress-exploit-framework |
| WPScan WordPress 安全扫描器                           | https://github.com/wpscanteam/wpscan                     | wpscan                      |
| WPForce Wordpress 攻击套件                            | https://github.com/n00py/WPForce                         | WPForce                     |
|                                                       |                                                          |                             |

## 常规漏洞利用工具

| 项目简介                     | 项目地址                                  | 项目名称   |
| ---------------------------- | ----------------------------------------- | ---------- |
| 基于DOM的快速XSS漏洞扫描程序 | https://github.com/dwisiswant0/findom-xss | findom-xss |
| 很常用的XSS平台              | https://github.com/beefproject/beef       | beef       |
|                              |                                           |            |
|                              |                                           |            |
|                              |                                           |            |
|                              |                                           |            |

## 数据库利用工具

| 项目简介                                                     | 项目地址                                    | 项目名称      |
| ------------------------------------------------------------ | ------------------------------------------- | ------------- |
| MDUT 2.0 数据库利用工具                                      | https://github.com/SafeGroceryStore/MDUT    | MDUT          |
| 综合高危漏洞利用工具(包含各大数据库)                         | https://github.com/Liqunkit/LiqunKit_       | LiqunKit      |
| sqlserver利用工具                                            | https://github.com/uknowsec/SharpSQLTools   | SharpSQLTools |
| 通过套接字重用通过受损的 Microsoft SQL Server  在受限环境中执行横向移动 | https://github.com/blackarrowsec/mssqlproxy | mssqlproxy    |
| ODAT：Oracle 数据库攻击工具                                  | https://github.com/quentinhardy/odat        | ODAT          |
|                                                              |                                             |               |

## 爆破工具

| 项目简介                                            | 项目地址                                                     | 项目名称              |
| --------------------------------------------------- | ------------------------------------------------------------ | --------------------- |
| 集合了fscan和kscan等优秀工具功能的扫描爆破工具。    | https://github.com/i11us0ry/goon                             | goon                  |
| 超级弱口令检查工具是一款Windows平台的弱口令审计工具 | https://github.com/shack2/SNETCracker                        | 超级弱口令检查工具    |
| Web-Brutator 中间件接口爆破                         | https://github.com/koutto/web-brutator                       | Web-Brutator          |
| WebCrack是一款web后台弱口令/万能密码批量检测工具    | https://github.com/yzddmr6/WebCrack                          | WebCrack              |
| zero-crack Web应用(webapps)暴力破解小工具           | https://github.com/0-sec/zero-crack                          | zero-crack            |
| WordPress 超级快速暴力破解工具                      | https://github.com/22XploiterCrew-Team/WordPress-Brute-Force | WordPress-Brute-Force |
| ssb 一种更快更简单的爆破SSH服务器的工具             | https://github.com/kitabisa/ssb                              | ssh爆破               |
| rsync弱密码扫描(爆破)                               | https://github.com/hi-unc1e/some_scripts/blob/master/EXPs/rsync_weakpass.py | rsync                 |
|                                                     |                                                              |                       |

## 字典收集

| 项目简介                                              | 项目地址                                                   | 项目名称                 |
| ----------------------------------------------------- | ---------------------------------------------------------- | ------------------------ |
| -  在线整理的一些常见默认设备/应用密码                | https://forum.ywhack.com/bountytips.php?password           | EdgeTeam                 |
| - 在线整理的一些华为系列设备默认密码表                | https://forum.ywhack.com/bountytips.php?huawei             | EdgeTeam                 |
| -  渗透测试、SRC漏洞挖掘、爆破、Fuzzing等字典收集项目 | https://github.com/insightglacier/Dictionary-Of-Pentesting | Dictionary-Of-Pentesting |
| Fuzz 字典,一个就够了                                  | https://github.com/TheKingOfDuck/fuzzDicts                 | Web Pentesting           |
| - Web 模糊测试字典与一些Payloads                      | https://github.com/gh0stkey/Web-Fuzzing-Box                | Web Fuzzing Box          |
| 上传漏洞fuzz字典生成脚本                              | https://github.com/c0ny1/upload-fuzz-dic-builder           | upload-fuzz-dic-builder  |
| 安全评估期间使用的多种类型列表的集合                  | https://github.com/danielmiessler/SecLists                 | SecLists                 |
| 渗透测试仪和Bug赏金猎人的 Payload 库                  | https://github.com/sh377c0d3/Payloads                      | Payloads                 |
| 基于实战沉淀下的各种弱口令字典                        | https://github.com/fuzz-security/SuperWordlist             | SuperWordlist            |
| 各类漏洞的 TOP25 参数字典                             | https://github.com/lutfumertceylan/top25-parameter         | top25-parameter          |
| 提取收集以往泄露的密码中符合条件的强弱密码            | https://github.com/r35tart/RW_Password                     | RW_Password              |
|                                                       |                                                            |                          |

# 内网渗透工具

## webshell托管工具

| 项目简介                               | 项目地址                                    | 项目名称        |
| -------------------------------------- | ------------------------------------------- | --------------- |
| 哥斯拉                                 | https://github.com/BeichenDream/Godzilla    | Godzilla        |
| “冰蝎”动态二进制加密网站管理客户端     | https://github.com/rebeyond/Behinder        | Behinder        |
| 中国蚁剑是一款开源的跨平台网站管理工具 | https://github.com/AntSwordProject/antSword | antSword        |
| 一句话WEB端管理工具                    | https://github.com/boy-hack/WebshellManager | WebshellManager |
| 跨平台版中国菜刀                       | https://github.com/Chora10/Cknife           | Cknife          |

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

## 横向移动工具

| 项目简介                                              | 项目地址                                         | 项目名称     |
| ----------------------------------------------------- | ------------------------------------------------ | ------------ |
| Mimikatz  Windows 密码抓取神器                        | https://github.com/gentilkiwi/mimikatz           | mimikatz     |
| sharpwmi基于rpc的横向移动工具，具有上传和执行命令功能 | https://github.com/QAX-A-Team/sharpwmi           | sharpwmi     |
| 文件下载命令快捷生成                                  | https://forum.ywhack.com/bountytips.php?download | 快捷命令     |
| 反弹Shell命令一键生成                                 | https://forum.ywhack.com/shell.php               | 反弹shell    |
| ATT&CK 横向移动总结技巧                               | https://attack.mitre.org/tactics/TA0008/         | attack       |
| 将哈希传递到命名管道以进行令牌模拟                    | https://github.com/S3cur3Th1sSh1t/NamedPipePTH   | NamedPipePTH |
| 常见横向移动与域控权限维持方法                        | https://xz.aliyun.com/t/9382                     | 方法论       |

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



# 运维&甲方&防守方工具

## 应急响应工具

| 项目简介                                                  | 项目地址                                              | 项目名称              |
| --------------------------------------------------------- | ----------------------------------------------------- | --------------------- |
| 主机侧Checklist的自动全面化检测脚本                       | https://github.com/grayddq/GScan                      | Gscan                 |
| 应急响应实战笔记，一个安全工程师的自我修养                | https://github.com/Bypass007/Emergency-Response-Notes | Bypass007             |
| linux信息收集/应急响应/常见后门/挖矿检测/webshell检测脚本 | https://github.com/al0ne/LinuxCheck                   | LinuxCheck            |
| APT-Hunter Windows日志事件应急工具                        | https://github.com/ahmedkhlief/APT-Hunter             | APT-Hunter            |
| uroboros-一个GNU/Linux监视和概要分析工具，专注于单个进程  | https://github.com/evilsocket/uroboros                | uroboros              |
| whohk linux下一款强大的应急响应工具                       | https://github.com/heikanet/whohk                     | whohk                 |
| Malwoverview 是用于威胁搜寻的第一响应工具                 | https://github.com/alexandreborges/malwoverview       | malwoverview          |
| Attack Surface Analyzer 可以帮助您分析操作系统的安全配置  | https://github.com/Microsoft/AttackSurfaceAnalyzer    | AttackSurfaceAnalyzer |
| 一款基于 IP 信誉度信息实现的实时检测 Web 恶意流量的工具   | https://github.com/CRED-CLUB/ARTIF                    | ARTIF                 |
| Rootkit Hunter Rootkit猎手                                | http://rkhunter.sourceforge.net/                      | Rootkit               |
| SHELLPUB.COM 专注查杀 河马webshell查杀                    | https://www.shellpub.com/                             | 河马webshell          |
| 火麒麟-网络安全应急响应工具(系统痕迹采集)                 | https://github.com/MountCloud/FireKylin               | FireKylin             |
| 日志分析库,nuclei 的另一种用法                            | https://github.com/ffffffff0x/LOG-HUB                 | LOG-HUB               |

# 安全资料整理

正在整理中………………

------
如果你有更好的提议或者其他想法，欢迎联系。

<img src="../../../../Library/Mobile%20Documents/com~apple~CloudDocs/%E7%AC%94%E8%AE%B0/img/image-20220519215338754.png" alt="image-20220519215338754" style="zoom: 25%;" />

​	by--L0una(guchangan1)



