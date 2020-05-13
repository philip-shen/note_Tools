# Purpose
Take note of Ansible from Cyber.

# Table of Content
[Provisioning vs Deployment](https://github.com/philip-shen/note_Tools/tree/master/Ansible#provisioning-vs-deployment)  
[Microservice Prerequisites](https://github.com/philip-shen/note_Tools/tree/master/Ansible#microservice-prerequisites)  
[Definition](https://github.com/philip-shen/note_Tools/tree/master/Ansible#Definition)  
[Stage](https://github.com/philip-shen/note_Tools/tree/master/Ansible#Definition)  
[Tool Chains](https://github.com/philip-shen/note_Tools/tree/master/Ansible#tool-chains)  
[]()  

[Reference](https://github.com/philip-shen/note_Tools/tree/master/Ansible#reference) 

# Provisioning vs Deployment
[Resource Provisioning and DevOps 2017/02/11](https://rickhw.github.io/2017/02/11/AWS/Resource-Provisioning-and-DevOps/#)

# Microservice Prerequisites
[Microservice Prerequisites 28 August 2014](https://martinfowler.com/bliki/MicroservicePrerequisites.html)

* Rapid Provisioning
* Basic Monitoring
* Rapid Application Deployment

# Definition
> Deployment (部署) 是把開發好的應用程式 (.NET, Java 的 war, jar file) 放到 Application Server，把應用程式的 config (DB connection / Thirdparty API Key)，然後讓他可以上線服務。

> Provisioning 是部署之前，要準備好的相關資源以及設定，像是常見的 Route53 + ELB + ASG / Launch Config + AMI 的組合。

> 以傳統的 IT 單位來說，Provisioning 就是：開發單位下需求給 IT ，IT 進行設備採購 + 列管 + 把機器放到機房 + 把網路設定好 + 作業系統裝好 + 帳號設定好 + 預先安裝好管理工具，前面這段都是 Provisioning，最後給使用單位，使用單位自己去裝自己要用的東西。

# Stage

* Plan：需求分析、資源管理、技術評估、使用者 UI/UX、業務評估、市場預測 
* Development：開發主要的商務需求、功能 
* Testing：功能、系統、整合、E2E、效能等測試、回歸 
* Deployment：重點在於把開發好的應用程式放到線上的過程，需要 Provisioning 一起 co-work。
* Observation, Monitor and Controller：中文稱 監控，但其實只有 監視 (Monitor) ，不包含 控制 (Controller)，而且少了最重要的 觀測 (Observe)。重點在三件事情：

    - 1 Dashboard：系統資訊的呈現
    - 2 Alert：異常的通報
    - 3 Log：蒐集與儲存

* Provisioning：環境建置、資源管理、預算控管、重構系統架構 
* Collaboration：包含 Source Control、Project Management、CI/CD Pipeline … 等

# Tool Chains

* Anisble:
    - 適合部署應用程式，也可以做 Provisioning
    - module 命名有點亂，使用上有些雷， debug 要花一點時間
    - 沒有考慮實際應用的場景，像是 security group 只能建立，無法更新。
    - 功能不完整，像是 Auto Scaling 不支援 Scaling Policy，看來需要自幹 ….
* CloudFormation:
    - 適合：建立 AWS Infrastructure, Service 的 Provisioning，像是建立新的 VPC, 建立整個完整的 Service Stack, 包含 RDS, ELB, ASG, … 等介接
    - 不適合：安裝應用程式，像是執行 EC2 建立後的 userdata，理由是把 script 嵌入 yaml or json 很蠢、很噁心. 搞不懂為啥 AWS 為啥會這麼沒有設計概念，做出這麼爛的設計 …..
* Terraform:
    - 可以建立完整的 Infrastructure，但是狀態要記得進版控.
    - 是自己定義的 DSL，格式比較複雜 (相對於 Ansible)
* CodeDeploy: 為啥會提這個？他跟 Ansible 一樣都是作部署用途，不適合做 Provisioning，再次強調：Deployment and Provisioning 是兩件事。


# Reference
* [Ansibleで始める構成管理ツール_Part1 2019-02-08](https://qiita.com/legitwhiz/items/672b8c6aa569b118e7a5)
* [Ansibleで始める構成管理ツール Part2 2019-02-08](https://qiita.com/legitwhiz/items/0e8dd595d8548a058c77)
* [Resource Provisioning and DevOps 2017/02/11](https://rickhw.github.io/2017/02/11/AWS/Resource-Provisioning-and-DevOps/#)

* [ansible for windows Sep 15, 2015](https://qiita.com/h-imaoka/items/7e5707b08afb725801e0)
* [Windows10 に ゼロから Ansible をインストールする(Ansible for Windows) 2018-10-08](https://qiita.com/search?utf8=%E2%9C%93&sort=&q=ansible+windows)
---
Ansible稼働環境

    Windows 10 Pro (バージョン1803)
    PowerShell 5.1
    ActiveDirectory ドメインに属する
Windowsホスト上でAnsibleを設置するには、大きく２つの方法があります
1. Linux For Windows ＋ Ansible
2. Docker For Windows + LinuxOS Image + Ansible

今回は「2. Docker For Windows」の上にAnsibleを設定する方法を選択しました。
- Docker for Windows 18.06.1
こちらの記事が大変参考になりました。
「Docker for WindowsからAnsibleを使ってみました。」
http://blog.serverworks.co.jp/tech/2018/04/11/ansible-docker-for-windows/

---

* [WindowsServerをAnsibleでリモート管理するための第一歩(Ansible for Windows) 2018-10-08](https://qiita.com/Tkm_Kit/items/976587a086a08a0c613a)

* [IISにWebサイトを追加するplaybookサンプル 2018-10-08](https://qiita.com/Tkm_Kit/items/3d15656a337c3e497d85)

* [Ansibleで自作Windowsモジュールを作ってみる Jun 17, 2018](https://qiita.com/sky_jokerxx/items/03e83befb75bb9de685e)

* [番外篇：在 Windows 上也能使用 Ansible (13:48) ](https://school.soft-arch.net/courses/ansible/lectures/659421)
---
Ansible 1.7 之後，managed node（被管理的主機）可以是 Windows 了。相關資訊請見官方文件：http://www.ansible.com/windows

但 Ansible 的 control machine（管理主機；主控台）仍然需要是 Unix-like 系統。引述官方文件的說法： 

如果你一定要以 Windows 作為 control machine，有幾種可能的方法。（Disclaimer：以下方法可能都不盡完美，如有可能，還是盡可能找一台 Mac 或 Linux 當做 control machine 吧。） 

1. 比較建議的方法：透過虛擬機
---

* [用 Ansible 管理 Windows 2016-01-19](https://metavige.github.io/2016/01/19/ansible-windows-manage-start/)
---

---

* [[Day 09] 撰寫第一個 Ansible Role 2017-12-20](https://ithelp.ithome.com.tw/articles/10192364)


* [Ansible 自動化部署工具 Oct 12, 2016](https://medium.com/@chihsuan/ansible-%E8%87%AA%E5%8B%95%E5%8C%96%E9%83%A8%E7%BD%B2%E5%B7%A5%E5%85%B7-b2e8b8534a8d)

* [Ansible 筆記  2017-04-22](http://www.lawrencelin.info/2017/04/ansible-notes/)
---
Ansible 是屬於 push-based 的自動部署工具, 我們不需要在遠端機器上安裝任何 client 端的程式或是 agent, 只要確定好有安裝 python 2.6以上的版本就可以了. Ansible 主要是經由 SSH 來進行控制及設定遠端的機器, 經由這樣子的設計, 我們在使用 ansible 時, 所需要的前置作業就會少很多.

安裝 Ansible
Ansible 預設是經由 SSH protocol 來管理其它的遠端機器. 因此, 需要一台機器作為中央控管來操作 Ansible 的所有指令 , Ansible 稱為 ** Control Machine **, 而其它的遠端
機器則稱為 ** Managed Node **. 這些機器都需要安裝 Python 2.6 以上的版本.

---

* [解決問題 Ansible (1) Aug 14 2017](https://leoyeh.me/2017/08/14/%E8%A7%A3%E6%B1%BA%E5%95%8F%E9%A1%8C-Ansible-1/)
---
方式一
安裝 Virtualenv 套件
首先透過 Virtualenv 套件建立虛擬且獨立 Python 環境，主要可以讓我們在沒有權限的情況下安裝新套件，不同專案可以使用不同版本的相同套件和套件版本升級時不會影響其他專案。

---

* [解決問題 Ansible (2) Aug 14 2017](https://leoyeh.me/2017/08/14/%E8%A7%A3%E6%B1%BA%E5%95%8F%E9%A1%8C-Ansible-2/)
* [解決問題 Ansible (3) Aug 14 2017](https://leoyeh.me/2017/08/14/%E8%A7%A3%E6%B1%BA%E5%95%8F%E9%A1%8C-Ansible-3/)

* [透過 Ansible 快速部署 OpenShift 3.11(OKD) 叢集](https://yylin1.github.io/2019/08/12/openshift-ansible-v3-11/)

* []()
![alt tag]()

# h1 size

## h2 size

### h3 size

#### h4 size

##### h5 size

*strong*strong  
**strong**strong  

> quote  
> quote

- [ ] checklist1
- [x] checklist2

* 1
* 2
* 3

- 1
- 2
- 3