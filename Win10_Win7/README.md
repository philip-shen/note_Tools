Table of Contents
=================

   * [Table of Contents](#table-of-contents)
   * [Notes of Tools](#notes-of-tools)
   * [01. OpenSSH Server and Client on Windows 10](#01-openssh-server-and-client-on-windows-10)
      * [サーバとクライアントの構成](#サーバとクライアントの構成)
      * [1. sshを入れる](#1-sshを入れる)
      * [2. ポート開放](#2-ポート開放)
      * [3. sshdを起動](#3-sshdを起動)
      * [4. 接続](#4-接続)
      * [5. 鍵認証方式](#5-鍵認証方式)
      * [感想](#感想)
   * [Public, Private or Domain Network on Windows 10](#public-private-or-domain-network-on-windows-10)
      * [Network Tyep](#network-tyep)
         * [Public Network](#public-network)
         * [Private Network](#private-network)
         * [Domain Network](#domain-network)
      * [What is the current network type of your computer?](#what-is-the-current-network-type-of-your-computer)
      * [Ways to change network types in Windows 10](#ways-to-change-network-types-in-windows-10)
         * [1- Using Windows Settings](#1--using-windows-settings)
         * [2- Setting network type using Windows Registry](#2--setting-network-type-using-windows-registry)
   * [02 NTP on Windows 10](#02-ntp-on-windows-10)
      * [使用するOS](#使用するos)
      * [レジストリ](#レジストリ)
         * [regedit](#regedit)
         * [NTP Server Enable](#ntp-server-enable)
         * [W32Time](#w32time)
      * [regedit閉じる](#regedit閉じる)
      * [NTPサーバ　起動](#ntpサーバ起動)
      * [Widows10でNTP同期](#widows10でntp同期)
   * [03. WindowsのWiFi操作をコマンドプロンプトから行う](#03-windowsのwifi操作をコマンドプロンプトから行う)
      * [既知のネットワーク詳細をパスワード含めて表示する](#既知のネットワーク詳細をパスワード含めて表示する)
      * [XMLファイルからインポートする](#xmlファイルからインポートする)
      * [レポートをHTML形式で生成する](#レポートをhtml形式で生成する)
   * [04. Ping can't work on Windows8](#04-ping-cant-work-on-windows8)
   * [Enable Control Panel on Windows8](#enable-control-panel-on-windows8)
      * [アプリ一覧から開く場合](#アプリ一覧から開く場合)
      * [メニューから開く場合](#メニューから開く場合)
   * [05. Chinese is garbled in Japanese Display Interface on Win 10](#05-chinese-is-garbled-in-japanese-display-interface-on-win-10)
   * [06. Find windows OS version from command line](#06-find-windows-os-version-from-command-line)
   * [07. Remote Desktop Windows 10 Home](#07-remote-desktop-windows-10-home)
      * [RDP Wrapper Libraryが突然使えなくなった！](#rdp-wrapper-libraryが突然使えなくなった)
         * [ビルド番号10.0.17134.706(KB4493464)](#ビルド番号10017134706kb4493464)
         * [ビルド番号10.0.18362.267(KB4505903)](#ビルド番号10018362267kb4505903)
         * [Check RDP port number](#check-rdp-port-number)
         * [RDP Conf](#rdp-conf)
      * [RDP Wrapper導入メモ Aug 13, 2019](#rdp-wrapper導入メモ-aug-13-2019)
         * [手順](#手順)
         * [設定（任意）](#設定任意)
      * [Files in release package:](#files-in-release-package)
      * [Windows 10 version 10.0.18362.267 not supported](#windows-10-version-10018362267-not-supported)
      * [Known issues: Listener is not listening on Win 10 Home (build 14997 )](#known-issues-listener-is-not-listening-on-win-10-home-build-14997)
      * [What's 「TrustedInstaller」?](#whats-trustedinstaller)
      * [How to Remote Desktop Windows 10 Home?](#how-to-remote-desktop-windows-10-home)
      * [There are a few things to note before you invite someone to remotely connect with your PC:](#there-are-a-few-things-to-note-before-you-invite-someone-to-remotely-connect-with-your-pc)
      * [Remote Desktop Command Line](#remote-desktop-command-line)
      * [さらに RDP Wrapper Library が使えなくなって fork先に変更した。](#さらに-rdp-wrapper-library-が使えなくなって-fork先に変更した)
   * [08. Windows 內建的遠端桌面連線工具設定與使用教學](#08-windows-內建的遠端桌面連線工具設定與使用教學)
      * [被控端電腦的設定](#被控端電腦的設定)
      * [主控端電腦的設定](#主控端電腦的設定)
   * [09. Account added on Windows 10 for Remote Desktop login](#09-account-added-on-windows-10-for-remote-desktop-login)
      * [Select Accounts icon to add](#select-accounts-icon-to-add)
      * [Add accounts](#add-accounts)
      * [Finally,](#finally)
   * [10. Windows Remote CLI](#10-windows-remote-cli)
      * [PsTools Setup on Windows 10](#pstools-setup-on-windows-10)
         * [01. Open TCP#445 Firewall](#01-open-tcp445-firewall)
         * [02. Open Remote Login Authority](#02-open-remote-login-authority)
      * [PsExec Execution](#psexec-execution)
         * [リモート端末での準備](#リモート端末での準備)
   * [11. How to fix ‘No internet connection’ on Windows 10 mobile hotspot](#11-how-to-fix-no-internet-connection-on-windows-10-mobile-hotspot)
      * [Enable devices &amp; update drivers](#enable-devices--update-drivers)
      * [Enable connection sharing](#enable-connection-sharing)
   * [Enable Win10 inbuild hotspot by cmd/batch/powershell](#enable-win10-inbuild-hotspot-by-cmdbatchpowershell)
   * [12. Set up and Add a VPN Connection in Windows 10](#12-set-up-and-add-a-vpn-connection-in-windows-10)
      * [To Add a VPN Connection in PowerShell](#to-add-a-vpn-connection-in-powershell)
      * [Add-VpnConnection - Microsoft Windows IT Center](#add-vpnconnection---microsoft-windows-it-center)
         * [Parameters](#parameters)
   * [13. VPN Dailup Automatically](#13-vpn-dailup-automatically)
      * [VPN(L2TP/IPsec)自動接続バッチプログラム](#vpnl2tpipsec自動接続バッチプログラム)
         * [バッチプログラム保存先](#バッチプログラム保存先)
         * [クラウドファイルサーバーの例](#クラウドファイルサーバーの例)
      * [To Connect to a VPN by Command Prompt in Windows 10](#to-connect-to-a-vpn-by-command-prompt-in-windows-10)
      * [To Disconnect a VPN in Command Prompt](#to-disconnect-a-vpn-in-command-prompt)
   * [14. Turn On or Off Network Discovery in Windows 10](#14-turn-on-or-off-network-discovery-in-windows-10)
      * [To Turn On or Off Network Discovery for All Network Profiles in Command Prompt](#to-turn-on-or-off-network-discovery-for-all-network-profiles-in-command-prompt)
   * [15. Start, Stop, and Disable Services in Windows 10](#15-start-stop-and-disable-services-in-windows-10)
      * [To Start, Stop, and Disable Services using Sc Command](#to-start-stop-and-disable-services-using-sc-command)
      * [To Check Status of Services in PowerShell](#to-check-status-of-services-in-powershell)
      * [To Start, Stop, Restart, Disable, and Enable Services in PowerShell](#to-start-stop-restart-disable-and-enable-services-in-powershell)
   * [16. CPU and Memory Usage](#16-cpu-and-memory-usage)
      * [やっておくと便利なこと](#やっておくと便利なこと)
      * [今回は、ディスクの使用率もとれるようにした。](#今回はディスクの使用率もとれるようにした)
   * [17. Windows WMIC](#17-windows-wmic)
      * [CPU Utilization by powershell](#cpu-utilization-by-powershell)
      * [wmic process](#wmic-process)
   * [18. SMB 1.0](#18-smb-10)
      * [SMB 1.0有効化の背景](#smb-10有効化の背景)
      * [SMB 1.0/CIFS ファイル共有のサポート（コマンド）](#smb-10cifs-ファイル共有のサポートコマンド)
      * [GUIで有効化,無効化する方法](#guiで有効化無効化する方法)
      * [CLIで有効化,無効化する方法](#cliで有効化無効化する方法)
         * [SMB 1.0/CIFS File Sharing Supportの有効化](#smb-10cifs-file-sharing-supportの有効化)
         * [SMB 1.0/CIFS Clientの有効化](#smb-10cifs-clientの有効化)
         * [SMB 1.0/CIFS File Sharing SupportとSMB 1.0/CIFS Clientの無効化](#smb-10cifs-file-sharing-supportとsmb-10cifs-clientの無効化)
         * [有効なのか、無効なのかの確認方法](#有効なのか無効なのかの確認方法)
   * [98. Fix Unable to contact your DHCP Server error on Windows  7, 8, 10](#98-fix-unable-to-contact-your-dhcp-server-error-on-windows--7-8-10)
   * [99. Win 7 區域網路分享 –– 共用資料夾](#99-win-7-區域網路分享--共用資料夾)
   * [Troubleshooting](#troubleshooting)
   * [Reference](#reference)
   * [h1 size](#h1-size)
      * [h2 size](#h2-size)
         * [h3 size](#h3-size)
            * [h4 size](#h4-size)
               * [h5 size](#h5-size)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)

# Notes of Tools
Take a note of Win10 or Win7 various utilitization.

# 01. OpenSSH Server and Client on Windows 10  
[Windows10でsshする 2019-04-13](https://qiita.com/TukamotoRyuzo/items/7bd4ff6810421bdc9924) 

## サーバとクライアントの構成  
* サーバOS  
* クライアントOS  
  Windows10 Home

## 1. sshを入れる  
* sshがデフォルトで入っている場合
    何もしなくてよいがsshサーバ機能はデフォルトでは有効になっていないはず
```
        Windowsでoptionで検索
            オプション機能を追加する
            機能の追加
            OpenSSHサーバを追加
```

* sshがデフォルトで入っていない場合
```
        こっちはあんまり今回想定してないよ
        以下のURLからダウンロードするらしいことは書いておく
        https://github.com/PowerShell/Win32-OpenSSH/releases
```

* サーバとクライアント両方にいれる

## 2. ポート開放  
* 管理者権限でPowerShell起動
```
    これ実行
            netsh advfirewall firewall add rule name="sshd" dir=in action=allow protocol=TCP localport=22
```
* サーバとクライアント両方でやる

## 3. sshdを起動  
* サーバ側設定
```
     サービスに登録
            sshd install
        サービス起動
            Start-Service sshd
        自動起動設定
            Set-Service sshd -StartupType Automatic
```
* この辺で一回再起動した方が良いかも

## 4. 接続  
* ssh ユーザ名@サーバIPもしくはホスト名
    ホスト名はhostsファイルを編集してくれ
    ```

        C:\Windows\System32\drivers\etc\hosts
    ```

    パスワード設定してないのにパスワード聞かれて詰む場合
    ```
        パスワード設定しておけ
    ```

    ユーザ名がわからないんだけど
        サーバでwhoamiコマンド実行
            ~\の前がユーザ名だから
            →\の後がユーザ名でした。ozraruさんご指摘ありがとうございます。

* 接続がタイムアウトする場合
```
    ファイアウォールが原因か、サーバ側でポート開放できてない
    ウィルスセキュリティソフトが原因かも
     それ以外ならお手上げ
```

* 接続できることを確認

## 5. 鍵認証方式  
* いちいちパスワード入力してたらめんどくさい  
* スクリプトで自動的にログインして何かしたいときに困る

* なのでサーバでパスワード聞くのやめる
```
    C:\Windows\System32\OpenSSHの中にsshd_configを作る
    sshd_config_defaultをコピーしてつくる
    PubkeyAuthentication yesのコメントを外せ
    sshdを再起動
        Restart-Service sshd
```

* クライアントでキーを作る
```
    鍵の名前はmykeyという名前にしようか
    ssh-keygen -t rsa -f mykey
```

* クライアントのキーはどこでもいいけど.ssh/においておこう
```
    mv mykey ~/.ssh/mykey
```

* 公開鍵をサーバに配置
```
    scp mykey.pub ユーザ名@ホスト名もしくはip:
    これでサーバの~にmykey.pubが置かれているはず
```

* サーバの公開鍵の名前を変更
```
    すでに~/.ssh/authorized_keyがある場合
        cat mykey.pub > ~/.ssh/authorized_key
    ない場合
        mv mykey.pub ~/.ssh/authorized_key
```

* ログインしよう
```
    ssh -i 秘密鍵のパス ユーザ名@ホスト名もしくはip
    パスワード聞かれなければOK
```

## 感想  
一番時間がかかったのはsshd_configの置き場所。
ここに置くってどこに書いてあるんだろ。

# Public, Private or Domain Network on Windows 10  
[4 Ways To Change Network Type In Windows 10 (Public, Private or Domain) October 20, 2015](https://www.itechtics.com/change-network-type-windows-10/)  
```
    1 Network Types
        1.1 Public Network
        1.2 Private Network
        1.3 Domain Network
    2 What is the current network type of your computer?
    3 Ways to change network types in Windows 10
        3.1 1- Using Windows Settings
        3.2 2- Setting network type using Windows Registry
        3.3 3- Change network type using Local Security Policy
        3.4 4- Setting network type using PowerShell
```
## Network Tyep  
### Public Network  
```
A public network is the default network type. If no network type is selected, Windows will configure Windows Firewall using the Public network type rules. In public network, Windows Firewall rules will be the most restrictive. The firewall will block most of the apps from connecting from the Internet and disabling some features like file and printer sharing, network discovery and automatic setup of network devices etc.

You should use this type of network when you have only one computer and do not want to communicate with any other network device.
```
###  Private Network  
```
The private network can be a home network or work network. This type of network will enable most networking features of Windows 10 like file sharing, network device setup, network discovery etc.

Use this network type if you trust the network you are connecting to.
```
###  Domain Network  
```
The domain network is automatically detected when your computer is a member of Active Directory domain network. Windows should automatically detect this type of network and configure Windows Firewall accordingly. This type of network gives more control to the network administrator and the admin can apply different network security configurations using Active Directory group policies.

In this article, we will be more interested in changing the network type from public to private and vice versa as the domain network is automatically detected by Windows 10 and we don’t need to change anything.
```
## What is the current network type of your computer?  
```
Go to Control Panel –> Network and Internet –> View Network status and tasks
You will see the network type under each connected network
```
![alt tag](https://www.itechtics.com/wp-content/uploads/2015/10/Network-and-Sharing-Center-670x330.jpg?ezimgfmt=ng:webp/ngcb2)  

## Ways to change network types in Windows 10  
### 1- Using Windows Settings  
```
To change the network type using Windows Control Panel settings, follow the steps below:

    Go to Control Panel –> Network and Internet –> HomeGroup
    Click on Change Network Location link.
    This will open a charms dialog asking you “Do you want to allow your PC to be discoverable by other PCs and devices on this network”.
    Press the Yes button if you want your network to be set to Home or Work and No button if you want to be in public network.

You can configure each type of these networks in more detail by clicking on the link “Change advanced sharing settings…”.
```
![alt tag](https://www.itechtics.com/wp-content/uploads/2015/10/HomeGroup-settings-for-changing-network-type.jpg)   

### 2- Setting network type using Windows Registry
```
If you are an advanced user and are comfortable with editing Windows Registry, this method will be easier for you to change the network type especially when you want it to be done on multiple PCs using just a single registry file.

    Go to Run –> regedit
    Go to the following key:
    HKEY_LOCAL_MACHINE –> SOFTWARE –> Microsoft –> Windows NT –> CurrentVersion –> NetworkList –> Profiles
    Under the Profiles key, you will find some sub-keys with different GUIDs. This corresponds to the no. of network cards you’re using with your computer.
    Select each sub-key of the Profiles and look for the ProfileName key in the right hand pane. This will give you the name of the network so that you can easily recognize which network you want to change.
    After identifying the right sub-key, you can change the Category DWORD value in the right hand pane to change the network type of that particular network.
    Value data can be 0 for Public network, 1 for Private network and 2 for Domain network.
```
![alt tag](https://www.itechtics.com/wp-content/uploads/2015/10/Registry-key-to-change-network-type-670x239.jpg?ezimgfmt=ng:webp/ngcb2)   


# 02 NTP on Windows 10  
[【備忘録】Windows を NTP Server として使う 2018-08-06](https://qiita.com/HLDC-FJ/items/b3346f5721d6b2e9e6b6)  
## 使用するOS  
Windows 10 HOME  
## レジストリ  
### regedit  
「ファイル名を指定して実行」を選択し「regedit」と入力、「OK」をクリック  
![alt tag](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F214132%2Ff083b548-0a9d-4c4e-f28b-146ead7295f3.png?ixlib=rb-1.2.2&auto=compress%2Cformat&gif-q=60&w=1400&fit=max&s=7b8efd3dc59bac1906d5b897f7818c9d)   
### NTP Server Enable  
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders\NtpServerを選択し、
[Enabled]の項目を１へ変更し"OK"をクリック  
![alt tag](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F214132%2F01574bf0-27a1-2977-d7a6-6538422447fc.png?ixlib=rb-1.2.2&auto=compress%2Cformat&gif-q=60&s=98c592aca6659a9a13e643086f5efa94)   
### W32Time  
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Config] の [AnnounceFlags] を開き "5"へ変更しOKをクリック  
※なぜ"5"なのかは不明....  
![alt tag](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F214132%2F480b3b38-8417-a053-3f05-8c83b5267b6a.png?ixlib=rb-1.2.2&auto=compress%2Cformat&gif-q=60&s=4979cf7b7d1238a7ceb8fae71465acb8) 
## regedit閉じる  
設定は以上で完了。  
## NTPサーバ　起動  
```
”コマンドプロンプト（管理者）”を開く
net stop w32time と入力しEnter
NTPサーバが起動していない場合は以下のような表示となる。
```
![alt tag](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F214132%2F1fb42004-b4b7-28ea-b96a-206566b38c46.png?ixlib=rb-1.2.2&auto=compress%2Cformat&gif-q=60&s=781f71973f98e2b8bad483f6cc85116e)   

```
net start w32time と入力しEnter
NTP サーバが起動する
```
![alt tag](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F214132%2F8a9e3ba8-e1a7-2a43-c807-4c111d5fd32f.png?ixlib=rb-1.2.2&auto=compress%2Cformat&gif-q=60&s=f21bf150dda862f969008ccf0abcd62c)   
```
これで正常にWindows上にて NTP サーバが起動。
他の端末からサーバが起動している端末へNTP接続を行えば時計同期が行える。
セキュリティソフトなどを使用している場合は必要に応じてルール変更が必要。
```
## Widows10でNTP同期  
[Windows10でNTP 2019-08-29](https://qiita.com/koyayashi/items/8b990f03d476c1c7d591)  
```
タスクバーにtimedate.cplと入力して実行
```
![alt tag](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F488658%2F3e5b7fb7-0c3f-d4bf-5ae1-816ed9518714.png?ixlib=rb-1.2.2&auto=compress%2Cformat&gif-q=60&s=b632601c127b04c42adc89166e565455)   

[台灣慣用公開時間伺服器(NTP.Server) 04 August 2019](https://note.chiatse.com/2019/08/04/tai-wan-guan-yong-shi-jian-si-fu-qi-ntp-server/)  

Item | Server 
------------------------------------ | ---------------------------------------------
Cloudflare - NTP Server(2019/08上線) | time.cloudflare.com
Apple - NTP Server (亞洲) | time.asia.apple.com
Apple - NTP Server (美洲) | time.apple.com 
Apple - NTP Server (歐洲) | time.euro.apple.com 
Google - NTP Server | time.google.com
國家時間與頻率標準實驗室 - NTP Server | 1. time.stdtime.gov.tw
國家時間與頻率標準實驗室 - NTP Server | 2. tock.stdtime.gov.tw
國家時間與頻率標準實驗室 - NTP Server | 3. watch.stdtime.gov.tw
國家時間與頻率標準實驗室 - NTP Server | 4. clock.stdtime.gov.tw
國家時間與頻率標準實驗室 - NTP Server | 5. tick.stdtime.gov.tw

# 03. WindowsのWiFi操作をコマンドプロンプトから行う  
[WindowsのWiFi操作をコマンドプロンプトから行う 2019-09-03](https://qiita.com/mindwood/items/22e0895473578c4e0c7e)  
```
netsh wlan show interface
```

```
netsh wlan show profiles
```

## 既知のネットワーク詳細をパスワード含めて表示する  
```
netsh wlan show profiles name="SSID" key=clear
```

```
netsh wlan delete profile name="SSID"
```

```
netsh wlan connect name="SSID"
```
```
netsh wlan disconnect
```

```
netsh wlan export profile
```

```
netsh wlan export profile name="SSID" folder="C:tmp"
```

## XMLファイルからインポートする  
```
netsh wlan add profile filename="ファイル名"
```
```
netsh wlan set profileparameter name="SSID" nonBroadcast='ステルス可否' keymaterial='パスワード' connectionmode='接続の自動/手動'
```

## レポートをHTML形式で生成する  
```
netsh wlan show wlanreport
```

# 04. Ping can't work on Windows8  
[Windows8.1のping応答の設定 | Windowsサポート Feb 10, 2017](https://www.windows8-help.net/windows/windows81ping/)  
１、コントロールパネルを起動する。  
※[Windows8.1でコントロールパネルを開く方法](https://www.windows8-help.net/windows/windows81comp/)  

２、システムとセキュリティを選択。   
![alt tag](https://www.windows8-help.net/windows/wp-content/uploads/sites/2/2016/12/k2-300x171.jpg)  

３、Windowsファイアウォールを選択。  
![alt tag](https://www.windows8-help.net/windows/wp-content/uploads/sites/2/2016/12/k3-300x137.jpg)  

４、詳細設定を選択。  
![alt tag](https://www.windows8-help.net/windows/wp-content/uploads/sites/2/2016/12/k4.jpg)  

５、受信の規則を選択し、ファイルとプリンターの共有（エコー要求）で該当するものを選択し、右クリックします。※（v4、v6） の選択と、ネットワークのプロファイル（ドメイン、プライベート、パブリック）の選択。
![alt tag](https://www.windows8-help.net/windows/wp-content/uploads/sites/2/2016/12/k5-300x127.jpg)  

６、規則の有効化を選択。※無効にする場合は無効と表示されます  
![alt tag](https://www.windows8-help.net/windows/wp-content/uploads/sites/2/2016/12/k6.jpg)  

# Enable Control Panel on Windows8  

## アプリ一覧から開く場合  
１、デスクトップ左下のWindowアイコン（スタート）をクリックする。  
![alt tag](https://www.windows8-help.net/windows/wp-content/uploads/sites/2/2016/12/k12-1.jpg)  

２、スタートメニューが開くので、画面下に下矢印のアイコンが表示されるのでクリックする。  
![alt tag](２、スタートメニューが開くので、画面下に下矢印のアイコンが表示されるのでクリックする。)  

３、右側の方にコントロールパネルがあるので、それをクリックするとコントロールパネルが開く。 
![alt tag](https://www.windows8-help.net/windows/wp-content/uploads/sites/2/2016/12/k22-1.jpg)  
![alt tag](https://www.windows8-help.net/windows/wp-content/uploads/sites/2/2016/12/k23.jpg)  

## メニューから開く場合  
１、デスクトップ左下のWindowアイコン（スタート）を右クリックをする。  
![alt tag](https://www.windows8-help.net/windows/wp-content/uploads/sites/2/2016/12/k12-1.jpg)  

２、メニュー一覧が表示されるので、コントロールパネルを選択すると、コントロールパネルが開く。  
![alt tag](https://www.windows8-help.net/windows/wp-content/uploads/sites/2/2016/12/k24.jpg)  

![alt tag](https://www.windows8-help.net/windows/wp-content/uploads/sites/2/2016/12/k23.jpg)  

# 05. Chinese is garbled in Japanese Display Interface on Win 10  
[WIN10日文界面下中文显示异常（大小形状怪异）2019/3/6](https://answers.microsoft.com/zh-hans/windows/forum/all/win10%E6%97%A5%E6%96%87%E7%95%8C%E9%9D%A2%E4%B8%8B/ec6880ba-fcdf-4f32-b7a1-dfd271344c78)  
```
您好,我是独立技术顾问(Independent Advisor)Dexter,请让我来帮助您.

这个问题的根源是Windows中日语字体的优先级高于中文字体，因此当中文内容出现时，其中日语字体有的部分会用日语字体显示，剩下的再用中文字体。

建议您可以参考我附图中的设置尝试操作,看是否可以正常显示中文字体.

希望以上信息可以帮得到您,如果还有什么疑问的话,请不要客气随时可以继续提问,我将帮您直到问题解决.
```
![alt tag](https://filestore.community.support.microsoft.com/api/images/731e45ce-1fce-4788-a55a-ffca30a7b9aa?upload=true)  

[Win10亂碼問題排除方法之一(非unicode程式的語言) 2017-10-05](https://www.mobile01.com/topicdetail.php?f=300&t=5282401)  

# 

# 06. Find windows OS version from command line  
[Find windows OS version from command line](https://www.windows-commandline.com/find-windows-os-version-from-command/)  
```
λ systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
OS Name:                   Microsoft Windows 10 Home
OS Version:                10.0.18362 N/A Build 18362
```

```
 λ systeminfo | findstr /C:"OS"
OS Name:                   Microsoft Windows 10 Home
OS Version:                10.0.18362 N/A Build 18362
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Workstation
OS Build Type:             Multiprocessor Free
BIOS Version:              American Megatrends Inc. X411UAS.300, 4/17/2019
```

```
λ wmic os get version
Version
10.0.18362
```

# 07. Remote Desktop Windows 10 Home  

## RDP Wrapper Libraryが突然使えなくなった！   
[RDP Wrapper Libraryが突然使えなくなった！ May 16, 2019](https://qiita.com/murashi/items/2d497193a2224a7fdacf) 

### ビルド番号10.0.17134.706(KB4493464)  
[ビルド番号10.0.17134.706(KB4493464)](https://qiita.com/murashi/items/2d497193a2224a7fdacf#%E3%83%93%E3%83%AB%E3%83%89%E7%95%AA%E5%8F%B710017134706kb4493464)  


### ビルド番号10.0.18362.267(KB4505903)   
[ビルド番号10.0.18362.267(KB4505903)](https://qiita.com/murashi/items/2d497193a2224a7fdacf#%E3%83%93%E3%83%AB%E3%83%89%E7%95%AA%E5%8F%B710018362267kb4505903)  

![alt tag](https://i.imgur.com/XkV9amO.jpg)  

[GitHubのissues](https://github.com/stascorp/rdpwrap/issues/795)で解決方法が記載されています。設定ファイルを更新してくれるバッチファイルを作成した方がいます。詳細な説明は省きます。

1. 上記のIssueページから rdpwrap_ini_updater_(02_August_2019).zip をダウンロード。  
2. uninstall.bat実行  
3. install.bat実行  
4. ダウンロードファイル展開後の「rdpwrap_ini_updater.bat」と「re-install.bat」を「%ProgramFiles%/RDP Wrapper」にコピー  
5. セキュリティソフトの除外フォルダに「%ProgramFiles%/RDP Wrapper」を追加  
6. 管理者権限で「re-install.bat」を実行  

[ icekingcy commented on 30 May](https://github.com/stascorp/rdpwrap/issues/795#issuecomment-497288624)
```
    1903 18362 succeeded
    step:

        Execute install.bat
        Copy RDPWInst.exe and rdpwrap_ini_updater.bat to C:\Program Files\RDP Wrapper\
        Execute rdpwrap_ini_updater.bat
        Success

Work！

Thanks！
```

### Check RDP port number  
```
λ netstat -a | findstr "3389"
```
![alt tag](https://i.imgur.com/e66z8QH.jpg)  

### RDP Conf  
![alt tag](https://i.imgur.com/g5Mpz5I.jpg)  

[Windowsでファイルのアクセス権変更 2019-05-15](https://qiita.com/murashi/items/708acd6b37aaf46b4fec)
![alt tag](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F326185%2Ff338c9dd-4b9f-f566-575d-ff77eadf9223.png?ixlib=rb-1.2.2&auto=compress%2Cformat&gif-q=60&s=b6a1cfb3db316758039aeb8c69153ee6)    


## RDP Wrapper導入メモ Aug 13, 2019   
[RDP Wrapper導入メモ Aug 13, 2019](https://qiita.com/it_araisan/items/67368a659251d480bd73)  
### 手順  
1. GitHubのRDP WrapperのRelease からRDPWrap-v1.6.2.zipをダウンロードする1。  
2. Issue #795からrdpwrap_ini_updater_(02_August_2019).zipをダウンロードする。  
3. C:\Program FilesにRDP Wrapperという名前でフォルダを作成して、2つの圧縮ファイルを展開する。  
4. re-install.batを管理者権限で実行する。  
### 設定（任意）  
1. RDPConf.exeを起動しAuthentication ModeをDefault RDP Authenticationにする。  

[RDP Wrapper Library by Stas'M](https://github.com/stascorp/rdpwrap)  
```
The goal of this project is to enable Remote Desktop Host support and 
concurrent RDP sessions on reduced functionality systems for home usage.

RDP Wrapper works as a layer between Service Control Manager and Terminal Services, 
so the original termsrv.dll file remains untouched. Also this method is very strong against Windows Update.
```
## Files in release package:  
[Files in release package:](https://github.com/stascorp/rdpwrap#files-in-release-package)  

File name | Description
------------------------------------ | ---------------------------------------------
RDPWInst.exe | RDP Wrapper Library installer/uninstaller
RDPCheck.exe | Local RDP Checker (you can check the RDP is working)
RDPConf.exe | RDP Wrapper Configuration
install.bat | Quick install batch file
uninstall.bat | Quick uninstall batch file
update.bat | Quick update batch file

## Windows 10 version 10.0.18362.267 not supported  
[Windows 10 version 10.0.18362.267 not supported](https://github.com/stascorp/rdpwrap/issues/848)  
```
 graphixillusion commented on 29 Jul
```
```
1. net stop termservice
2. unistall rdpwrap
3. reboot pc
4. install rdpwrap
5. add this in the ini with notepad++
```
```
[10.0.18362.267]
LocalOnlyPatch.x64=1
LocalOnlyOffset.x64=82FB5
LocalOnlyCode.x64=jmpshort
SingleUserPatch.x64=1
SingleUserOffset.x64=0DBFC
SingleUserCode.x64=Zero
DefPolicyPatch.x64=1
DefPolicyOffset.x64=1FE15
DefPolicyCode.x64=CDefPolicy_Query_eax_rcx
SLInitHook.x64=1
SLInitOffset.x64=22DDC
SLInitFunc.x64=New_CSLQuery_Initialize

[10.0.18362.267-SLInit]
bInitialized.x64 =F6A8C
bServerSku.x64 =F6A90
lMaxUserSessions.x64 =F6A94
bAppServerAllowed.x64 =F6A9C
bRemoteConnAllowed.x64=F6AA0
bMultimonAllowed.x64 =F6AA4
ulMaxDebugSessions.x64=F6AA8
bFUSEnabled.x64 =F6AAC
```
```
6. Save and exit (as administrator)
7. net stop termservice
8. net start termservice
9. in the option set default rdp or gui auth only

and try again.
```
[rdpwrap.zip](https://github.com/stascorp/rdpwrap/files/3448151/rdpwrap.zip)  

```
raphaelmachado commented on 3 Sep
```
```
   stop the service running CMD as administrator

   net stop termservice
   Replace rdpwrap.ini in C:\Program Files\RDP Wrapper
   net start termservice
   Reboot your PC
   rdpwrap_10.0.18362.267_x64.zip
   
   Yes! It Worked!!! Thanks (-_-*)
```
[rdpwrap_10.0.18362.267_x64.zip](https://github.com/stascorp/rdpwrap/files/3439496/rdpwrap_10.0.18362.267_x64.zip)
  
## Known issues: Listener is not listening on Win 10 Home (build 14997+)   
![alt tag](https://user-images.githubusercontent.com/34800596/34323062-191acfa0-e7fe-11e7-9742-b10f1e040cc5.PNG)  

[Known issues:](https://github.com/stascorp/rdpwrap/#known-issues)  
* Beginning with the Creators Update for Windows 10 Home, RDP Wrapper will no longer work, claiming that the listener is [not listening] because of rfxvmt.dll is missing - [more info](https://github.com/stascorp/rdpwrap/issues/194#issuecomment-323564111), [download links](https://github.com/stascorp/rdpwrap/issues/194#issuecomment-325627235)  

[You can try my dlls](https://github.com/stascorp/rdpwrap/files/1545652/dlls.zip)

[rfxvmt.dll of 64-bit Windows 10](https://github.com/stascorp/rdpwrap/files/1236856/rfxvmt.zip)  
[rfxvmt.dll of 32-bit Windows](https://github.com/stascorp/rdpwrap/files/1238499/rfxvmt.zip)  


[Listener is not listening on Win 10 Home (build 14997+) ](https://github.com/stascorp/rdpwrap/issues/194)  

## What's 「TrustedInstaller」?  
[【遠端桌面】Windows 8.1 多人遠端桌面連線修改 - 我也想要一機多用 Oct 15 Thu 2015](http://kuang1984tw.pixnet.net/blog/post/144501199)  
```
簡單說就是鑒於過去很多電腦被感染病毒，或者是重要系統檔案遭竄改刪除，
主要原因就是這些惡意程式取得了最高權限的帳號密碼，才能對電腦恣意的發動攻擊，
所以從 Windows Vista 開始 TrustedInstaller 就誕生了，
他是一個 Windows 的 Services，服務名稱為「Windows Modules Installer」，
他的工作是模擬一個虛擬的權限，對於重要的系統檔，不管是 System 或 Administrator 帳號，
只賦予讀取的功能，而完整的控制功能，則交給「TrustedInstaller」這個虛擬帳號。
```
![alt tag](https://pic.pimg.tw/kuang1984tw/1444896183-583824440.jpg)  

```
這時候你將「C:\Windows\System32」底下的「termsrv.dll」檔案給他按下右鍵，
點選名為「取得權限：TrustedInstaller」的功能，然後再丟一次檔案你就會發現可以取代原有檔案囉！灑花～
```
![alt tag](https://pic.pimg.tw/kuang1984tw/1444906615-3065834291.jpg)  

[◤ TrustedInstaller：TrustedInstaller權限.reg](https://mega.nz/#!l5QBHACI!HfQyYetdYp07jFMPqPA01enoh9GeISwNhWXVwzTCd_g)
```
＊ 解壓密碼：kuang1984tw.pixnet.net/blog
```


[【遠端桌面】Windows 10 多人遠端桌面連線修改- 新增支援 Threshold 2 Oct 15, 2019](http://kuang1984tw.pixnet.net/blog/post/144954046)  
```
如果你因為安全因素不想變動「termsrv.dll」原始檔案的話，我們有另外一種方法來達成：
使用「RDP Wrapper」充當 Terminal Services 和 Service Control Manager 之間的仲介。
```

[【遠端桌面】Windows 8.1 多人遠端桌面連線修改 - 我也想要一機多用 Oct 15 Thu 2015](http://kuang1984tw.pixnet.net/blog/post/144501199)  
【下載連結】  

[How To Enable Remote Desktop In Windows 10 Home (RDP) October 4, 2019](https://www.itechtics.com/remote-desktop-windows-10-home/#How_to_Remote_Desktop_Windows_10_Home)  

## How to Remote Desktop Windows 10 Home?  
1. Download RDP Wrapper Library from here. The specific filename is RDPWInst-v1.6.2.msi for automatic installation. Or you can also download the zip file RDPWrap-v1.6.2.zip for manual installation.  
2. Extract the .zip archive to a folder and open the folder.  
3. Open install.bat and then update.bat ‘as admin’. Wait for it execute in command prompt.  
![alt tag](https://www.itechtics.com/wp-content/uploads/2019/10/Install-RDP-Wrapper-library.jpg?ezimgfmt=ng:webp/ngcb2)  
4. Congrats! You have enabled RDP or remote desktop protocol and as a result, Windows Remote Desktop is now available on your Windows 10 Home PC.  
5. To view/change the configuration parameters of this wrapper, run RDPConf.bat from the folder. It should look similar to the screenshot below.   
![alt tag](https://www.itechtics.com/wp-content/uploads/2019/10/RDP-Wrapper-Configuration.jpg?ezimgfmt=ng:webp/ngcb2)  
6. You can now test RDP access to your machine or do a localhost RDP connection test by launching RDPCheck.exe.  

## There are a few things to note before you invite someone to remotely connect with your PC:  
1. Add a tick mark beside “Enable Remote Desktop” in System Properties. To go to this setting directly, go to Run –> systempropertiesremote.   
![alt tag](https://www.itechtics.com/wp-content/uploads/2019/10/System-Properties-Remote-477x500.jpg?ezimgfmt=ng:webp/ngcb2)  

2. Make sure your Windows firewall allows TCP and UDP port 3389, which will be used by the RDP server as the default port.  
3. Although this method isn’t illegal, you will still be in breach with Microsoft Windows EULA (End User Licensing Agreement). You should avoid it in commercial settings.  
4. Only give remote access of your PC to people whom you trust or those bounded by a contractual or legal obligation.  
5. You can use the same username and password which you use to login to your system to log in through RDP.  

## Remote Desktop Command Line  
[リモートデスクトップ接続](https://qiita.com/onoenter/items/a61508d8149dc06c68e9#%E3%83%AA%E3%83%A2%E3%83%BC%E3%83%88%E3%83%87%E3%82%B9%E3%82%AF%E3%83%88%E3%83%83%E3%83%97%E6%8E%A5%E7%B6%9A)  
```
@echo off
Set SERVER=XXX.XXX.XXX.XXX
Set USERNAME=user
Set PASSWORD=pass

Cmdkey /generic:TERMSRV/%SERVER% /user:%USERNAME% /pass:%PASSWORD%
Start mstsc /v:%SERVER%
Timeout 2
Cmdkey /delete:TERMSRV/%SERVER%
```
これも、パスワードなどが丸見えなので、  
```
@echo off
Set SERVER=XXX.XXX.XXX.XXX
Set /P USERNAME="Username："
Set /P PASSWORD="Password："

Cmdkey /generic:TERMSRV/%SERVER% /user:%USERNAME% /pass:%PASSWORD%
Start mstsc /v:%SERVER%
Timeout 2
Cmdkey /delete:TERMSRV/%SERVER%
```
「/P」で設定して入力できるようにしてしまえばいいんではないかと思います。

```
e:\project\note_Tools\Win10_Win7>RD_ironmanexcelsior.bat
```
![alt tag](https://i.imgur.com/01YFKKI.png)  

## さらに RDP Wrapper Library が使えなくなって fork先に変更した。  
[さらに RDP Wrapper Library が使えなくなって fork先に変更した。](#https://qiita.com/shooskay/items/3c0e28581097de7bb401)
```
2020/02/19 最近のupdateで 動かなかくなったようです。
つかうのやめようかなぁ・・
べんりだったんだけどなぁ。
ケチらないで Proにupdateする時期なのかも

windows10homeでRDPサービスを実現するのに 利用していた RDP Wrapper Libraryが 
windowupdate で ライブラリが 更新されると 使えなくなることが相次いだ。
今回は termsrv.dll Ver.10.0.17763.437に更新された。
```
![alt tag](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F125882%2Ff813007d-dc89-8186-c9ca-31bf4afd4943.png?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&w=1400&fit=max&s=61129a536cc72dcdab22dfdfcfe56a06)


# 08. Windows 內建的遠端桌面連線工具設定與使用教學   
[Windows 內建的遠端桌面連線工具設定與使用教學 2019/05/18](https://www.kjnotes.com/windows/31?page=0%2C3)  
## 被控端電腦的設定  
[被控端電腦的設定](https://www.kjnotes.com/windows/31?page=0%2C3#toc--) 
Step 1：按下鍵盤『windows鍵+R』，開啟『執行』對話框，輸入『systempropertiesremote』，並點選『確定』開啟遠端設定視窗。  
![alt tag](https://www.kjnotes.com/sites/default/files/contentimg/31/rds031.png)  

Step 2：在遠端設定視窗中，因為筆者此台電腦是要被控制的電腦，所以只需設定遠端桌面那部分就可以了，選擇『允許遠端連線到此電腦』後，這時會跳出視窗，大約說明是通知你說這台電腦目前的電源選項如果在不使用電腦時，是會進入睡眠或休眠狀態，Windows要你記得到電源選項設定中將其改成永不的睡眠狀態，以免電腦進入睡眠狀態後，而導致你無法遠端連線到此台電腦，關於電源管理部分，我們稍後在進行設定。  
![alt tag](https://www.kjnotes.com/sites/default/files/contentimg/31/rds032.png)  

Step 3：取消勾選『僅允許來自執行含有網路層級驗證之遠端桌面的電腦進行連線』，完成之後點選『確定』，被控端的遠端設定部分就設定完成了，接下來我們繼續設定Windows防火牆，以免因為防火牆阻擋到遠端桌面連線的問題，而導致主控端電腦無法連線到此台電腦。  
![alt tag](https://www.kjnotes.com/sites/default/files/contentimg/31/rds033.png)  

Step 4：按下鍵盤『windows鍵+R』，開啟『執行』對話框，輸入『firewall.cpl』，並點選『確定』開啟Windows防火牆。  
![alt tag](https://www.kjnotes.com/sites/default/files/contentimg/31/rds041.png)  

Step 5：在Windows防火牆中，如下圖所示點選『允許應用程式或功能通過Windows防火牆』。  
![alt tag](https://www.kjnotes.com/sites/default/files/contentimg/31/rds042.png)  

Step 6：在允許應用程式透過Windows防火牆通訊這邊，開始設定時需要先點擊『變更設定』。  
![alt tag](https://www.kjnotes.com/sites/default/files/contentimg/31/rds043.png)  

Step 7：在應用程式與功能列表中，找到『遠端桌面』功能，筆者在設定時，預設是都已經勾選好了，假如你電腦是沒有勾選的，那就勾選上去吧，如果有變更到防火牆設定，不要忘記要點選『確定』，儲存你的變更。  
![alt tag](https://www.kjnotes.com/sites/default/files/contentimg/31/rds044.png)  

Step 8：接下來要來查看被控端電腦的實體IP位址，按下鍵盤『windows鍵+R』，開啟『執行』對話框，輸入『cmd』，並點選『確定』開啟命令提示字元視窗。  

Step 9：開啟命令提示字元視窗後，輸入指令『ipconfig』  


## 主控端電腦的設定  
[主控端電腦的設定](https://www.kjnotes.com/windows/31?page=0%2C3#toc---2)  

Step 1：在主控端電腦這邊按下鍵盤『windows鍵+R』，開啟『執行』對話框，輸入『mstsc』，並點選『確定』開啟遠端桌面連線視窗。  
![alt tag](https://www.kjnotes.com/sites/default/files/contentimg/31/rds101.png)  

Step 2：輸入被控端電腦的IP位址，如下圖所示筆者剛剛在被控端電腦查到的IPv4位址是『114.41.XXX.XXX』，那就將IP位址輸入至欄位中，輸入好後點選『連線』。  
![alt tag](https://www.kjnotes.com/sites/default/files/contentimg/31/rds102.png)  

Step 3：如下圖所示輸入被控端電腦的密碼，假如你要讓主控端電腦記住此次的連線，那可以勾選『記住我的認證』，然後點選『確定』。
![alt tag](https://www.kjnotes.com/sites/default/files/contentimg/31/rds103.png)  

Step 4：首次遠端連線到不一樣的IP位址或不同電腦時，可能會有憑證錯誤的問題  
![alt tag](https://www.kjnotes.com/sites/default/files/contentimg/31/rds104.png)    

Step 5：如下圖所示筆者已成功遠端連線了。  
![alt tag](https://www.kjnotes.com/sites/default/files/contentimg/31/rds106.png)  


# 09. Account added on Windows 10 for Remote Desktop login  
##  Select Accounts icon to add  
![alt tag](https://i.imgur.com/98ygiFo.jpg)  
## Add accounts
![alt tag](https://i.imgur.com/nbskYJD.jpg)  
## Finally,  
![alt tag](https://i.imgur.com/y2EhAe5.jpg)  


# 10. Windows Remote CLI  

## PsTools Setup on Windows 10  
[PsTools 於Windows 10 的環境設定 Nov 1, 2019](http://pejslin.blogspot.com/2019/11/pstools-windows-10.html)  
[PsTools 下載](https://docs.microsoft.com/en-us/sysinternals/downloads/pstools)  

### 01. Open TCP#445 Firewall  
```
Win+R--->firewall.cpl
```
![alt tag](https://i.imgur.com/xdy26wY.jpg)
```
>netstat -a | findstr 445
  TCP    0.0.0.0:445            DESKTOP-7EDV2HB:0      LISTENING
  TCP    [::]:445               DESKTOP-7EDV2HB:0      LISTENING
```

### 02. Open Remote Login Authority  
```
1. excute regedit

2. 
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\policies\system

3.新增一個「DWORD 值」，並把它命名為「LocalAccountTokenFilterPolicy」，然後再把他的值設定成「1」
```

```
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\system /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f
```

```
>net use \\192.168.1.106 /user:username passwd

>psexec64 \\192.168.1.106 -u username -p passwd ipconfig
```
![alt tag](https://i.imgur.com/dAV2qsd.jpg)

[開啟Windows 10 的遠端指令權 Jun 9, 2017](https://kheresy.wordpress.com/2017/06/09/windows-10-remote-command/)

## PsExec Execution  
[別端末(Windows)のプログラムを標準機能でリモート起動する方法まとめ Dec 07, 2016](https://qiita.com/0829/items/5518256b348521ac358c)  
[方法７：PsExec Dec 07, 2016](https://qiita.com/0829/items/5518256b348521ac358c#%E6%96%B9%E6%B3%95%EF%BC%97psexec)

### リモート端末での準備  
```
    135/tcp（RPCエンドポイント・マッパー）
    445/tcp（ダイレクト・ホスティングSMB）
    1025～65535/tcp（RPC動的ポート）
```
```
> netsh advfirewall firewall add rule name=PsExec dir=in action=allow localport=rpc-epmap protocol=tcp program= %windir%\system32\svchost.exe  

> netsh advfirewall firewall add rule name=PsExec dir=in action=allow localport=445 protocol=tcp

> netsh advfirewall firewall add rule name=PsExec dir=in action=allow localport=rpc protocol=tcp program=%SystemRoot%\system32\services.exe
```
```
netsh advfirewall firewall set rule name=PsExec new enable=no
```

```
> PsExec.exe -u <user> -p <pass> \\192.168.100.101 C:\Remote\run_batch.bat

PsExec v2.2 - Execute processes remotely
Copyright (C) 2001-2016 Mark Russinovich
Sysinternals - www.sysinternals.com

C:\Windows\system32>echo Complete  1>C:\Remote\run.log
C:\Remote\run_batch.bat exited on 192.168.100.101 with error code 0.
```

[PsExec vs. the PowerShell remoting cmdlets Invoke-Command and Enter-PSSession Apr 14 2017](https://4sysops.com/archives/psexec-vs-the-powershell-remoting-cmdlets-invoke-command-and-enter-pssession/)  
[Using PsTools to Control Other PCs from the Command Line April 30, 2019](https://www.howtogeek.com/school/sysinternals-pro/lesson8/)  


# 11. How to fix ‘No internet connection’ on Windows 10 mobile hotspot  
[How to fix ‘No internet connection’ on Windows 10 mobile hotspot Aug 7, 2019](https://www.addictivetips.com/windows-tips/fix-no-internet-connection-on-windows-10-mobile-hotspot/)  
## Enable devices & update drivers  
![alt tag](https://cloud.addictivetips.com/wp-content/uploads/2019/08/Enable-devices-update-drivers.jpg.webp)  

## Enable connection sharing  
![alt tag](https://cloud.addictivetips.com/wp-content/uploads/2019/08/win-10-network-connections.webp)  
![alt tag](https://cloud.addictivetips.com/wp-content/uploads/2019/08/mobile-hotspot-LAN-1.jpg.webp)  
![alt tag](https://cloud.addictivetips.com/wp-content/uploads/2019/08/network-sharing-center-win-10.jpg.webp)  
![alt tag](https://cloud.addictivetips.com/wp-content/uploads/2019/08/ethernet-properties-win-10.jpg.webp)  

# Enable Win10 inbuild hotspot by cmd/batch/powershell  
[enable Win10 inbuild hotspot by cmd/batch/powershell Aug 23 2017](https://stackoverflow.com/questions/45833873/enable-win10-inbuild-hotspot-by-cmd-batch-powershell)  
```
The Hosted Network (which can be configured using the netsh wlan set hostednetwork ... command) 
and the "new" Mobile Hotspot use different technologies under the hood.
```
```
There's a WinRT API to control and configure the "new" mobile hotspot you're referring to. 
You can call it from PowerShell:
```
[Ben N.'s await function for IAsyncOperation and IAsyncAction in PowerShell, which can be found here.](https://superuser.com/a/1342416)  

```
$connectionProfile = [Windows.Networking.Connectivity.NetworkInformation,Windows.Networking.Connectivity,ContentType=WindowsRuntime]::GetInternetConnectionProfile()
$tetheringManager = [Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager,Windows.Networking.NetworkOperators,ContentType=WindowsRuntime]::CreateFromConnectionProfile($connectionProfile)

# Be sure to include Ben N.'s await for IAsyncOperation:
# https://superuser.com/questions/1341997/using-a-uwp-api-namespace-in-powershell

# Check whether Mobile Hotspot is enabled
$tetheringManager.TetheringOperationalState

# Start Mobile Hotspot
Await ($tetheringManager.StartTetheringAsync()) ([Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult])

# Stop Mobile Hotspot
Await ($tetheringManager.StopTetheringAsync()) ([Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult])
```


# 12. Set up and Add a VPN Connection in Windows 10  
[Set up and Add a VPN Connection in Windows 10 22 Nov 2019](https://www.tenforums.com/tutorials/90305-set-up-add-vpn-connection-windows-10-a.html#option3)  

## To Add a VPN Connection in PowerShell  

1 Open PowerShell.  

2 Type the command below you want to use into PowerShell, and press Enter. (see screenshot below)  

```
(Without remember my credentials)
Add-VpnConnection -Name "Connection Name" -ServerAddress "Server name or address" -Force -PassThru

OR

(With remember my credentials)
Add-VpnConnection -Name "Connection Name" -ServerAddress "Server name or address" -RememberCredential 
-Force -PassThru
```

```
Substitute Connection Name in the command above with the actual connection name for the VPN (ex: "MPN"). 
Usually this can be any name you want, but some VPN providers may require a specific name.

Substitute Server name or address in the command above with the actual server name or address 
(ex: "fre.mypn.co") required by your VPN provider (ex: "My Private Network").

For example: Add-VpnConnection -Name "MPN" -ServerAddress "fre.mypn.co" -RememberCredential 
-Force -PassThru
```
![alt tag](https://www.tenforums.com/attachments/tutorials/146591d1501598288-set-up-add-vpn-connection-windows-10-a-add_vpn_connection_powershell.jpg)

3 When finished, you can connect to the VPN when you want. You will be prompted for your user name and password for the VPN the first time you connect to the VPN.


## Add-VpnConnection - Microsoft Windows IT Center  
[Add-VpnConnection - Microsoft Windows IT Center](https://docs.microsoft.com/en-us/powershell/module/vpnclient/add-vpnconnection?redirectedfrom=MSDN&view=win10-ps#syntax)  

```
Add-VpnConnection
   [-Name] <String>
   [-ServerAddress] <String>
   [-RememberCredential]
   [-SplitTunneling]
   [-Force]
   [-PassThru]
   [-ServerList <CimInstance[]>]
   [-DnsSuffix <String>]
   [-IdleDisconnectSeconds <UInt32>]
   [-PlugInApplicationID] <String>
   -CustomConfiguration <XmlDocument>
   [-CimSession <CimSession[]>]
   [-ThrottleLimit <Int32>]
   [-AsJob]
   [-WhatIf]
   [-Confirm]
   [<CommonParameters>]
```

```
Add-VpnConnection
   [-Name] <String>
   [-ServerAddress] <String>
   [[-TunnelType] <String>]
   [-AllUserConnection]
   [-RememberCredential]
   [-SplitTunneling]
   [-Force]
   [-PassThru]
   [[-L2tpPsk] <String>]
   [-UseWinlogonCredential]
   [-ServerList <CimInstance[]>]
   [-DnsSuffix <String>]
   [-IdleDisconnectSeconds <UInt32>]
   [[-EapConfigXmlStream] <XmlDocument>]
   [[-AuthenticationMethod] <String[]>]
   [[-EncryptionLevel] <String>]
   [-MachineCertificateIssuerFilter <X509Certificate2>]
   [-MachineCertificateEKUFilter <String[]>]
   [-CimSession <CimSession[]>]
   [-ThrottleLimit <Int32>]
   [-AsJob]
   [-WhatIf]
   [-Confirm]
   [<CommonParameters>]
```

Example 2: Add a VPN connection with an alternate authentication method  
```
Add-VpnConnection -Name "Test3" -ServerAddress "10.1.1.1" -TunnelType "Pptp" 
-EncryptionLevel "Required" -AuthenticationMethod MSChapv2 -UseWinlogonCredential 
-SplitTunneling -AllUserConnection -RememberCredential -PassThru

Name                  : Test3 
ServerAddress         : 10.1.1.1 
AllUserConnection     : True 
Guid                  : {76746D4E-D72A-467D-A11F-3D4D9075F50D} 
TunnelType            : Pptp 
AuthenticationMethod  : {MsChapv2} 
EncryptionLevel       : Required 
L2tpIPsecAuth         : 
UseWinlogonCredential : True 
EapConfigXmlStream    : 
ConnectionStatus      : Disconnected 
NapState              : NotConnected 
RememberCredential    : True 
SplitTunneling        : True
```

Example 3: Add a VPN connection that uses EAP authentication  
```
Add-VpnConnection -Name "Test4" -ServerAddress "10.1.1.1" -TunnelType "L2tp" 
-EncryptionLevel "Required" -AuthenticationMethod Eap -SplitTunneling 
-AllUserConnection -L2tpPsk "password" -Force -RememberCredential -PassThru

Name                  : Test4 
ServerAddress         : 10.1.1.1 
AllUserConnection     : True 
Guid                  : {1D423FF3-E3D4-404A-B052-DB9130656D29} 
TunnelType            : L2tp 
AuthenticationMethod  : {Eap} 
EncryptionLevel       : Required 
L2tpIPsecAuth         : Psk 
UseWinlogonCredential : False 
EapConfigXmlStream    : #document 
ConnectionStatus      : Disconnected 
NapState              : NotConnected 
RememberCredential    : True 
SplitTunneling        : True
```

### Parameters  
-AllUserConnection

Indicates that the cmdlet adds the VPN connection to the global phone book entries.  

-AuthenticationMethod

Specifies the authentication method to use for the VPN connection. The acceptable values for this parameter are:
```
    PAP
    CHAP
    MSCHAPv2
    EAP
    MachineCertificate
```

-EncryptionLevel

Specifies the encryption level for the VPN connection. The acceptable values for this parameter are:

```
    NoEncryption
    Optional
    Required
    Maximum
    Custom
```

-Force

Indicates that the pre-shared key (PSK) value is supplied over an insecure channel, if L2TP is used.  

-L2tpPsk

Specifies the value of the PSK to be used for L2TP authentication. If this parameter is not specified, a certificate is used for L2TP.  

-PassThru

Returns an object representing the item with which you are working. By default, this cmdlet does not generate any output.  

-TunnelType

Specifies the type of tunnel used for the VPN connection. The acceptable values for this parameter are:
```
    PPTP
    L2TP
    SSTP
    IKEv2
    Automatic
```




# 13. VPN Dailup Automatically  
[WindowsクライアントPCからのVPN（L2TP/IPsec)接続を自動化しました Jan 22, 2016](https://qiita.com/Mitsu-Murakita/items/f8776157e9f8db72656d)  
```
本投稿で使用している "TIMEPUT"コマンドは、クライアントPCのOSが「VISTA」以降でないと動作しません。
「XP」の場合は、"SLEEP"コマンドをお使いください。
"SLEEP"コマンドは、「Windows Server 2003 Resource Kit Tools」に含まれます。
https://www.microsoft.com/en-us/download/confirmation.aspx?id=17657
```

## VPN(L2TP/IPsec)自動接続バッチプログラム  
[VPN(L2TP/IPsec)自動接続バッチプログラム](https://qiita.com/Mitsu-Murakita/items/f8776157e9f8db72656d#2-vpnl2tpipsec%E8%87%AA%E5%8B%95%E6%8E%A5%E7%B6%9A%E3%83%90%E3%83%83%E3%83%81%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0)  

```
 VPNConnect.bat

TIMEOUT /T 20
rasdial “VPN-L2TP接続” /disconnect
TIMEOUT /T 10
rasdial "VPN-L2TP接続" UserID Password
```

```
(1) TIMEOUT /T 20
Windows起動後、ネットワーク環境が安定するまで20秒待ちます。
（各クライアントPC環境により時間調整してください。）
```

```
(2) rasdial “VPN-L2TP接続” /disconnect
VPN(L2TP/UPsec)は未接続ですが二重接続操作を防ぐ目的で、切断操作を実行します。
```

```
(3) TIMEOUT /T 10
10秒待ちます。
（各クライアントPC環境により時間調整してください。）
```

```
(4) rasdial "VP-L2TP接続" UserID Password
VPN(L2TP/IPsec)を接続します。
・"VPN-L2TP接続"----- クライアントPC側で登録した、VPN接続名
・UserID --------------- VPN(L2TP/IPsec)サーバーで登録したユーザーID
・Password ------------ VPN(L2TP/IPsec)サーバーで登録したパスワード
```

### バッチプログラム保存先  
クライアントPCの下記スタートアップフォルダーに保存します。
```
Cドライブ
　　　└ユーザー
　　　　└（ユーザー名）
　　　　　└AppData
　　　　　　└Roaming
　　　　　　　└Microsoft
　　　　　　　　└Windows
　　　　　　　　　└スタートメニュー
　　　　　　　　　　└プログラム
　　　　　　　　　　　└スタートアップ
```

### クラウドファイルサーバーの例  
```
 VPNConnectFS.bat

TIMEOUT /T 20
rasdial “VPN-L2TP接続” /disconnect
TIMEOUT /T 10
rasdial "VPN-L2TP接続" UserID Password
net use x: \\xxx.xxx.xxx.xxx\共有フォルダー /user:FSUserID FSUser /persistent:no
```

```
net use p: \xxx.xxx.xxx.xxx\共有フォルダー /user:FSUserID FSPassword /persistent:no
・p: ---------------------- ネットワークドライブ
・xxx.xxx.xxx.xxx.xxx ----- Windowsサーバーのプライベートアドレス
・FSUserID -------------- WindowsユーザーID
・FSPassword ----------- Windowsパスワード
・/persistent:no --------- 次回ログオン時に再接続しない。
(/persistent:yesだと、Windows起動後はVPN未接続のため、「ドライブアサインできない」ダイアログが表示される。)
```

## To Connect to a VPN by Command Prompt in Windows 10  
[Connect to VPN in Windows 10 23 Dec 2019](https://www.tenforums.com/tutorials/90313-connect-vpn-windows-10-a.html)  

1 Open a command prompt.  

2 Copy and paste the PowerShell Get-VpnConnection command into the command prompt, and press Enter to see all available [added VPN connections.](https://www.tenforums.com/tutorials/90305-set-up-add-vpn-connection-windows-10-a.html#option2) (see screenshot below)  

```
Make note of the Name (ex: "MPN") of the VPN you want to connect to.

Make note if RememberCredential for the VPN is True or False.

* If True, then you may not need to enter your user name and password for the VPN in the command.
* If False, then you will need to enter your user name and password for the VPN in the command.
```
![alt tag](https://www.tenforums.com/attachments/tutorials/146622d1501607064-connect-vpn-windows-10-a-get_vpn_command-1.png?s=0248cef71d42efdc988ac2c2e6c7b52e)  

3 Enter the command below you need to use into the command prompt, and press Enter. (see screenshot below)  
```
(Without user name and password credentials)
rasdial "Name"

OR

(With user name and password credentials)
rasdial "Name" "User name" "Password"
```

![alt tag](https://www.tenforums.com/attachments/tutorials/146612d1501605749-connect-vpn-windows-10-a-connect_to_vpn_command.jpg?s=0248cef71d42efdc988ac2c2e6c7b52e)  

4 When completed successfully, you can close the command prompt if you like.


## To Disconnect a VPN in Command Prompt  
[To Disconnect a VPN in Command Prompt 02 Aug 2017](https://www.tenforums.com/tutorials/90324-disconnect-vpn-windows-10-a.html#option4)  

1. Open a command prompt.

2. Enter the command below into the command prompt, and press Enter to see details about all available added VPN connections. (see screenshots below)

```
PowerShell Get-VpnConnection
```

![alt tag](https://www.tenforums.com/attachments/tutorials/146644d1501607064-disconnect-vpn-windows-10-a-get_vpn_command-1.png)  

![alt tag](https://www.tenforums.com/attachments/tutorials/146639d1501612227-disconnect-vpn-windows-10-a-get_vpn_command-2.png)  

3. Enter the command below you want to use into the command prompt, and press Enter. 
(see screenshots below)  

```
rasdial "MPN" /disconnect

OR

rasphone -H "MPN"
```

![alt tag](https://www.tenforums.com/attachments/tutorials/146640d1501612227-disconnect-vpn-windows-10-a-disconnect_vpn_command.png)   

![alt tag](https://www.tenforums.com/attachments/tutorials/146659d1501614637-disconnect-vpn-windows-10-a-disconnect_vpn_command-2.png)   


# 14. Turn On or Off Network Discovery in Windows 10  

## To Turn On or Off Network Discovery for All Network Profiles in Command Prompt  
[To Turn On or Off Network Discovery for All Network Profiles in Command Prompt 21 Oct 2019](https://www.tenforums.com/tutorials/49652-turn-off-network-discovery-windows-10-a.html#option3)  

Discovery State | Description 
------------------------------------ | --------------------------------------------- 
On | This state allows your computer to see other network computers and devices and allows people on other network computers to see your computer. This makes it easier to share files and printers.
Off | This state prevents your computer from seeing other network computers and devices and prevents people on other network computers from seeing your computer.
Custom | This is a mixed state in which some settings related to network discovery are enabled, but not all of them. For example, network discovery could be turned on, but you or your system administrator might have changed firewall settings that affect network discovery.

1. Open an elevated command prompt.  

2. Do step 3 (on) or step 4 (off) below for what you want to do.  

3. To Turn On Network Discovery for All Network Profiles  
```

netsh advfirewall firewall set rule group="Network Discovery" new enable=Yes
```
![alt tag](https://www.tenforums.com/attachments/tutorials/78786d1462732159-turn-off-network-discovery-windows-10-a-turn_on_network_discovery_command.png)  

4. To Turn Off Network Discovery for All Network Profiles
```
netsh advfirewall firewall set rule group="Network Discovery" new enable=No
```
![alt tag](https://www.tenforums.com/attachments/tutorials/78785d1462732159-turn-off-network-discovery-windows-10-a-turn_off_network_discovery_command.png)  


# 15. Start, Stop, and Disable Services in Windows 10  
[Start, Stop, and Disable Services in Windows 10 06 Jan 2020](https://www.tenforums.com/tutorials/4499-start-stop-disable-services-windows-10-a.html)  

## To Start, Stop, and Disable Services using Sc Command  
[To Start, Stop, and Disable Services using Sc Command](https://www.tenforums.com/tutorials/4499-start-stop-disable-services-windows-10-a.html#option3)  

1. Open an elevated command prompt, and do step 2 (stop), step 3 (disable), step 4 (enable), or step 5 (start) below for what you would like to do.  

2. To Stop a Service using "Sc Stop" Command in Command Prompt  

A) Type the command below into the elevated command prompt, press Enter, and go to step 6 below.  
```
sc stop "service name"
```

![alt tag](https://www.tenforums.com/attachments/tutorials/13867d1485949973-start-stop-disable-services-windows-10-a-service_name.png)  

![alt tag](https://www.tenforums.com/attachments/tutorials/13866d1425680557-start-stop-disable-services-windows-10-a-sc_stop.png)  

3. To Disable a Service using "Sc Config" Command in Command Prompt  

A) Do step 2 above to stop the service, and return to continue with step 3B below.  
B) Type the command below into the elevated command prompt, press Enter, and go to step 6 below.  
```

If I wanted to disable the HomeGroup Listener service, I would type the command below using the HomeGroupListener (service name) exactly in the command prompt, and press Enter.

sc config "HomeGroupListener" start=disabled
```
![alt tag](https://www.tenforums.com/attachments/tutorials/13862d1425680538-start-stop-disable-services-windows-10-a-sc_config-1.png)  

4. To Enable a Service using "Sc Config" Commands   

A) If the Startup type of the service is set to Disabled, then in the elevated command prompt, type the command below using the startup type you want to set instead, and press Enter.  

"Startup Type" for Service  

Startup Type | Description 
------------------------------------ | --------------------------------------------- 
Manual (demand) | Manual mode allows Windows to start a service when needed. However, very few services will start up when required in Manual mode. If you find you need a service, place it into Automatic.
Automatic (auto) | With a service in this state, it will start at boot time. Some services, when no longer required, will also automatically stop when not needed. If you find you do not need a service, place it into Manual or Disabled.
Automatic (Delayed Start) (delayed-auto) | With a service in this state, it will start just after boot time. Some services, when no longer required, will also automatically stop when not needed. If you find you do not need a service, place it into Manual or Disabled.

```
If I wanted to set the startup type for the HomeGroup Listener service to Manual, I would type the command below using the HomeGroupListener (service name) exactly in the command prompt, and press Enter.

sc config "HomeGroupListener" start=demand
```
![alt tag](https://www.tenforums.com/attachments/tutorials/13863d1425680538-start-stop-disable-services-windows-10-a-sc_config-2.png)  

 5. To Start a Service using "Sc Start" Command  

A) If not already, you will need to enable the service using step 4 above first.  
B) Type the command below into the elevated command prompt, press Enter, and go to step 6 below.  
```
sc start "HomeGroupListener"
```
![alt tag](https://www.tenforums.com/attachments/tutorials/13864d1485949973t-start-stop-disable-services-windows-10-a-sc_start.png)  

## To Check Status of Services in PowerShell  
[To Check Status of Services in PowerShell](https://www.tenforums.com/tutorials/4499-start-stop-disable-services-windows-10-a.html#option6)  

```
Get-Service -Name "HomeGroupListener" | Format-Table -Auto

OR

Get-Service -DisplayName "HomeGroup Listener" | Format-Table -Auto
```

![alt tag](https://www.tenforums.com/attachments/tutorials/144822d1500567947-start-stop-disable-services-windows-10-a-get_status_of_service_in_powershell.png)  

4. To Check Status of All Services  
```
Get-Service | Format-Table -Auto
```
![alt tag](https://www.tenforums.com/attachments/tutorials/144821d1500567619t-start-stop-disable-services-windows-10-a-get_status_of_all_services_in_powershell.png)  


## To Start, Stop, Restart, Disable, and Enable Services in PowerShell  
[To Start, Stop, Restart, Disable, and Enable Services in PowerShell](https://www.tenforums.com/tutorials/4499-start-stop-disable-services-windows-10-a.html#option7)  

1. Open an elevated PowerShell.

2. Do step 3 (start), step 4 (stop), step 4 (restart), step 6 (disable), or step 7 (enable) below for what you would like to do.  

3. To Start a Service
```
Set-Service -Name "HomeGroupListener" -Status Running

Set-Service -DisplayName "HomeGroup Listener" -Status Running

OR

Start-Service -Name "HomeGroupListener"

Start-Service -DisplayName "HomeGroup Listener"
```
![alt tag](https://www.tenforums.com/attachments/tutorials/144826d1500568855-start-stop-disable-services-windows-10-a-start_service_in_powershell.png)  

![alt tag](https://www.tenforums.com/attachments/tutorials/144827d1500568855-start-stop-disable-services-windows-10-a-start_service2_in_powershell.png)  

4. To Stop a Service  
```
Set-Service -Name "HomeGroupListener" -Status Stopped

Set-Service -DisplayName "HomeGroup Listener" -Status Stopped

OR

Stop-Service -Force -Name "HomeGroupListener"

Stop-Service -Force -DisplayName "HomeGroup Listener"
```
![alt tag](https://www.tenforums.com/attachments/tutorials/144828d1500568855-start-stop-disable-services-windows-10-a-stop_service_in_powershell.png)  

![alt tag](https://www.tenforums.com/attachments/tutorials/144829d1500568855-start-stop-disable-services-windows-10-a-stop_service2_in_powershell.png)  

5. To Restart a Service  
```
Restart-Service -Force -Name "HomeGroupListener"

OR

Restart-Service -Force -DisplayName "HomeGroup Listener"
```
![alt tag](https://www.tenforums.com/attachments/tutorials/144830d1500568855-start-stop-disable-services-windows-10-a-restart_service_in_powershell.png)  

6. To Stop and Disable a Service  
```
Set-Service -Name "HomeGroupListener" -StartupType Disabled -Status Stopped

OR

Set-Service -DisplayName "HomeGroup Listener" -StartupType Disabled -Status Stopped
```
![alt tag](https://www.tenforums.com/attachments/tutorials/144831d1500568867-start-stop-disable-services-windows-10-a-disable_service_in_powershell.png)  

7. To Enable a Service  
```
"Startup Type" for Service

Manual - Manual mode allows Windows to start a service when needed. However, very few services will start up when required in Manual mode. If you find you need a service, place it into Automatic.

Automatic - With a service in this state, it will start at boot time. Some services, when no longer required, will also automatically stop when not needed. If you find you do not need a service, place it into Manual or Disabled.

Set-Service -Name "HomeGroupListener" -StartupType Manual

Set-Service -DisplayName "HomeGroup Listener" -StartupType Manual

OR

Set-Service -Name "HomeGroupListener" -StartupType Automatic

Set-Service -DisplayName "HomeGroup Listener" -StartupType Automatic
```
![alt tag](https://www.tenforums.com/attachments/tutorials/144838d1500571663-start-stop-disable-services-windows-10-a-set_service_startup_type_in_powershell.png)  

8. When finished, you can close PowerShell if you like.  


# 16. CPU and Memory Usage  
[]()  
[【第2回】pythonでCPUとメモリの使用率を取得する updated at 2020-01-13](https://qiita.com/hokke_mirin/items/47b6787f2c25caa40452)
```
    windows10 1909
    mac catalina
```

```
#!/usr/bin/env python
import psutil as psu
import tkinter as tk
import sys
import os
import datetime

# tkinterでwindowの作成とタイトルを作る
# windowサイズの指定
root = tk.Tk()
root.title(u"CPU&メモリ使用率")
root.geometry("600x300")

# cpu用ラベル
Static1 = tk.Label(text=u'CPU:')
Static1.pack()
# CPUの取得した値を表示する
txtcpu = tk.Entry(width=20)
txtcpu.pack()

# memory用ラベル
Static2 = tk.Label(text=u'memory:')
Static2.pack()

# memoryの取得した値を表示する
txtmem = tk.Entry(width=20)
txtmem.pack()


log = './cpumem.log'


def btn_click():
    # テキストボックスをクリア
    txtcpu.delete(0, tk.END)
    txtmem.delete(0, tk.END)
    if(os.path.exists(log)):
        with open(log, mode='a', encoding="utf-8") as f:
            # 時間の取得
            dt_now = datetime.datetime.now()
            # 日時のフォーマット修正
            dt = dt_now.strftime('%Y/%m/%d %H:%M:%S')
            # メモリの利用情報を取得
            memory = psu.virtual_memory()
            txtcpu.insert(0, memory.percent)
            cpu_percent = psu.cpu_percent(interval=1)
            txtmem.insert(0, cpu_percent)
            cpulog = txtcpu.get()
            memorylog = txtmem.get()
            f.write(dt + " " + cpulog + " , " + memorylog + "\n")
    else:
        with open(log, mode='w', encoding="utf-8") as f:
            # 時間の取得
            dt_now = datetime.datetime.now()
            # 日時のフォーマット修正
            dt = dt_now.strftime('%Y/%m/%d %H:%M:%S')
            # メモリの利用情報を取得
            memory = psu.virtual_memory()
            txtcpu.insert(0, memory.percent)
            cpu_percent = psu.cpu_percent(interval=1)
            txtmem.insert(0, cpu_percent)
            cpulog = txtcpu.get()
            memorylog = txtmem.get()
            f.write(dt + " " + cpulog + " , " + memorylog + "\n")


# ボタンの生成
Button = tk.Button(root, text='使用率取得', command=btn_click)
Button.pack()

root.mainloop()
```


[【第3回】pythonでCPUとメモリの使用率を取得する posted at 2020-01-29](https://qiita.com/hokke_mirin/items/ddf8e3c0c9ffa69cabbf)  

## やっておくと便利なこと  
```
$ pyinstaller xxxx.py --onefile --noconsole
```

## 今回は、ディスクの使用率もとれるようにした。  
```
#!/usr/bin/env python
import psutil as psu
import tkinter as tk
import sys
import os
import datetime

# tkinterでwindowの作成とタイトルを作る
# windowサイズの指定
root = tk.Tk()
root.title(u"CPU使用率&メモリ使用率&ディスク使用率")
root.geometry("600x100")

# cpu用ラベル
Static1 = tk.Label(text=u'CPU:')
Static1.pack(side='left')

# CPUの取得した使用率を表示する
txtcpu = tk.Entry(width=20)
txtcpu.pack(side='left', padx=0)

# memory用ラベル
Static2 = tk.Label(text=u'memory:')
Static2.pack(side='left')

# memoryの取得した使用率を表示する
txtmem = tk.Entry(width=20)
txtmem.pack(side='left', padx=0)

# disk用ラベル
Static3 = tk.Label(text=u'disk:')
Static3.pack(side='left')

# diskの取得した使用率を表示する
txtdsk = tk.Entry(width=20)
txtdsk.pack(side='left', padx=0)


log = './cpumem.log'


def btn_click():
    # テキストボックスをクリア
    txtcpu.delete(0, tk.END)
    txtmem.delete(0, tk.END)
    txtdsk.delete(0, tk.END)

    if os.path.exists(log):
        # logファイルがある場合
        with open(log, mode='a', encoding="utf-8") as f:
            # 時間の取得
            dt_now = datetime.datetime.now()
            # 日時のフォーマット修正
            dt = dt_now.strftime('%Y/%m/%d %H:%M:%S')
            # メモリの利用情報を取得
            memory = psu.virtual_memory()
            txtmem.insert(0, memory.percent)
            # CPUの使用率を取得
            cpu_percent = psu.cpu_percent(interval=1)
            txtcpu.insert(0, cpu_percent)
            # diskの使用率
            disk_percent = psu.disk_usage(path='/').percent
            txtdsk.insert(0, disk_percent)

            # textboxの値を取得
            cpulog = txtcpu.get()
            memorylog = txtmem.get()
            disklog = txtdsk.get()

            # ログに出力するフォーマット(日付 時間 cpu使用率 メモリ使用率 disk使用率)
            f.write(dt + " " + cpulog + " , " +
                    memorylog + " , " + disklog + "\n")
    else:
        # logファイルがない場合
        with open(log, mode='w', encoding="utf-8") as f:
            # 時間の取得
            dt_now = datetime.datetime.now()
            # 日時のフォーマット修正
            dt = dt_now.strftime('%Y/%m/%d %H:%M:%S')
            # メモリの利用情報を取得
            memory = psu.virtual_memory()
            txtmem.insert(0, memory.percent)
            # CPUの使用率を取得
            cpu_percent = psu.cpu_percent(interval=1)
            txtcpu.insert(0, cpu_percent)
            # diskの使用率
            disk_percent = psu.disk_usage(path='/').percent
            txtdsk.insert(0, disk_percent)
            # textboxの値を取得
            cpulog = txtcpu.get()
            memorylog = txtmem.get()
            disklog = txtdsk.get()
            # ログに出力するフォーマット(日付 時間 cpu使用率 メモリ使用率 disk使用率)
            f.write(dt + " " + cpulog + " , " +
                    memorylog + " , " + disklog + "\n")


# ボタンの生成
Button = tk.Button(root, text='使用率取得', command=btn_click)
Button.pack(fill='x', side='left', padx=0)

root.mainloop()
```

[様子をチェック！Windows10でCPU・メモリ使用率を確認する方法 ](https://nurgle77.com/1203.html)  
![alt tag](https://nurgle77.com/wp-content/uploads/2015/11/4cac4e97714c28d68969297902b5eed0.jpg)

# 17. Windows WMIC    
[Windows がなんか重いときにコマンドで調べる（WMIC PROCESS）May 15, 2015](https://qiita.com/qtwi/items/914021a8df608ab7792f)  

## CPU Utilization by powershell  
```
WMIC PATH Win32_PerfFormattedData_PerfProc_Process WHERE "PercentUserTime > 10" GET Name,IDProcess,PercentUserTime /FORMAT:LIST
```

## wmic process  
[Windowsのプロセスを、プロセス名・プロセスID以外の条件で停止する。 Jan 24, 2018](https://qiita.com/fjtm/items/7d3587b17cc403f52253)  

```
start mstsc
start mstsc /help

timeout 1

REM mstsc.exeの中で、コマンドラインの中に"help"という文字列を含むプロセスを停止する
wmic process where "name = 'mstsc.exe' and commandline like '%%help%%'" delete
```

```
wmic process where "name = 'mstsc.exe' and commandline like '%help%'" get name,commandline 
```

```
wmic process  get * /format:csv
```


# 18. SMB 1.0  
[Windows10 1709 Fall Creator Update以降のSMB v1.0有効化  Nov 09, 2019]()  

## SMB 1.0有効化の背景  
```
Windows10 1709 Fall Creator Updateより、Windowsファイル共通に使われる通信プロトコルの古いバージョンSMB v1.0が無効化されました。
```

[Windows 10 Fall Creators Update と Windows Server バージョン 1709 以降のバージョンの既定では SMBv1 はインストールされません](https://docs.microsoft.com/ja-jp/windows-server/storage/file-server/troubleshoot/smbv1-not-installed-by-default-in-windows)

```
重要度の低いファイルを保存した一部の古いNASが、SMB v1.0を利用しているようで、
Windows10の大型アップデートを適用した端末がファイルサーバーへ繋がらないという症状が出たことがきっかけで気づきました。

ping自体は通るので、初めは原因が分からずおかしいなぁと思っていました。

本来ならば、NAS側のソフトウェアまたはファームウェアをSMB v2.02以降の新しいバージョンをサポートする更新プログラムで対応するのですが、

古いNASの場合はメーカー側もそこまでサポートしてくれない場合もありますので、今回はクライアントPC側のプロコトルバージョンを下げて対応してみます。
```

## SMB 1.0/CIFS ファイル共有のサポート（コマンド）  
[SMB 1.0/CIFS ファイル共有のサポート（コマンド）](https://qiita.com/aa_ha1uhik0/items/b84ee3f1d52e8867ec39#smb-10cifs-%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E5%85%B1%E6%9C%89%E3%81%AE%E3%82%B5%E3%83%9D%E3%83%BC%E3%83%88%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89)  
```
echo SMB 1.0/CIFS ファイル共有のサポート：有効化
dism /online /Enable-Feature /FeatureName:SMB1Protocol /NoRestart
rem echo SMB 1.0/CIFS クライアント：無効化
rem ※今回はクライアントPCでSMBv1を利用するためコメントアウト化。
rem dism /online /Enable-Feature /FeatureName:SMB1Protocol-Client /NoRestart
echo SMB 1.0/CIFS サーバー：無効化
dism /online /Disable-Feature /FeatureName:SMB1Protocol-Server /NoRestart
echo SMB 1.0/CIFS 自動削除：無効化　バージョンによって自動削除が実装されていない場合があります。
dism /online /Disable-Feature /FeatureName:SMB1Protocol-Deprecation /NoRestart
echo このあとPCを再起動してください。
PAUSE
```

[Windows 10でSMB1.0を有効化する方法（PowerShellで有効化/無効化する） Jan 29, 2020](https://qiita.com/xus/items/3c30c0841c0736689d5b)  

## GUIで有効化,無効化する方法  
<img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F403714%2F8235edd8-31b9-0ac3-8fb8-3719056dea05.png?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&s=b894359efcbfe4f0a43ca2c4c65221f9" width="300" height="400">

## CLIで有効化,無効化する方法  
<img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F403714%2F4221cd8d-6ffa-8f63-2bac-044f7959041c.png?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&s=858a4ad917b596d028895ea0480e9781" width="200" height="300">

### SMB 1.0/CIFS File Sharing Supportの有効化  
```
Enable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol -NoRestart
```

### SMB 1.0/CIFS Clientの有効化   
```
Enable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol-Client -NoRestart
```

### SMB 1.0/CIFS File Sharing SupportとSMB 1.0/CIFS Clientの無効化  
```
Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol -NoRestart
Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol-Client -NoRestart
```

```
-NoRestartを付与すると再起動をする旨のYes/Noが問われない。
ActiveDirectoryグループポリシーのスタートアップスクリプトやシャットダウンスクリプトでは必須オプションと思う。
Yes/Noで停止してしまうとスクリプト同期の場合、
ログイン後デスクトップが表示されないことやシャットダウンがいつまで経っても終わらないという悲劇に見舞われる。
```

### 有効なのか、無効なのかの確認方法  
```
Get-WindowsOptionalFeature -Online -FeatureName SMB1Protocol
Get-WindowsOptionalFeature -Online -FeatureName SMB1Protocol-Client
```


# 98. Fix Unable to contact your DHCP Server error on Windows  7, 8, 10  
[Fix: Unable to Contact your DHCP Server Error on Windows 7, 8, 10 Aug 18, 2018](https://appuals.com/fix-unable-to-contact-your-dhcp-server-error-on-windows-7-8-10/)  
Solution 1: Update or Roll Back Your Network Drivers  
![alt tag](https://cdn.appuals.com/wp-content/uploads/2018/08/1-116.jpg)  

Update the Driver:  
![alt tag](https://cdn.appuals.com/wp-content/uploads/2018/08/1-117.jpg)  

Rolling Back the Driver:  
![alt tag](https://cdn.appuals.com/wp-content/uploads/2018/08/1-119.jpg)  

Solution 2: Disable the VirtualBox Related Driver  
![alt tag](https://cdn.appuals.com/wp-content/uploads/2018/08/1-120.jpg)  

Solution 3: Try a Simple Command  
![alt tag](https://cdn.appuals.com/wp-content/uploads/2018/08/1-121.jpg)  
```
ipconfig /registerdns
```

Solution 4: Disable IPv6 on Your Active Connection  
![alt tag](https://cdn.appuals.com/wp-content/uploads/2018/08/1-120.jpg)  

![alt tag](https://cdn.appuals.com/wp-content/uploads/2018/08/1-122.jpg)  

Solution 5: (Re)start Your DHCP Client Service  
![alt tag](https://cdn.appuals.com/wp-content/uploads/2018/08/1-123.jpg)  

Solution 6: Replace the Antivirus Program You are Using  
![alt tag](https://cdn.appuals.com/wp-content/uploads/2018/08/1-124.jpg)  


[Fix Unable to contact your DHCP Server error on Windows 10 Apr 27, 2019](https://www.thewindowsclub.com/unable-to-contact-your-dhcp-server)  

1] Update the Network drivers  
```
Press Win + R to open the Run window and type the command devmgmt.msc. Press Enter to open the Device Manager.
```
![alt tag](https://thewindowsclub-thewindowsclubco.netdna-ssl.com/wp-content/uploads/2019/04/Update-Network-drivers.png)  

2] Run the Network Adapter troubleshooter  
![alt tag](https://thewindowsclub-thewindowsclubco.netdna-ssl.com/wp-content/uploads/2018/11/Network-Adapter-troubleshooter.png)  

3] Disable IPv6 on the connection which is active   
```
At times, if IPv6 is enabled for active connections and that causes the problem. 
Thus, you could disable IPv6 as follows:

Press Win + R to open the Run window and type the command ncpa.cpl. 
Press Enter to open the Network Connections window. 
Right-click on the active Internet connection and select Properties.
```
![alt tag](https://thewindowsclub-thewindowsclubco.netdna-ssl.com/wp-content/uploads/2019/04/Network-properties.png)  

![alt tag](https://thewindowsclub-thewindowsclubco.netdna-ssl.com/wp-content/uploads/2019/04/Internet-protocol-version-6.png)  

4] Start/Restart the DHCP client service  
```
In case the DHCP client service is stopped or inactive, 
you could start/restart it from the Services Manager.

Press Win + R to open the Run window and type the command services.msc. 
Press Enter to open the Services Manager window.

In the list of services (which is arranged in alphabetical order), 
right-click on the service DHCP client and select Start/Restart.
```
![alt tag](https://thewindowsclub-thewindowsclubco.netdna-ssl.com/wp-content/uploads/2019/04/Restart-DHCP-client-service.png)  


# 99. Win 7 區域網路分享 –– 共用資料夾
[【教學】區域網路分享 –– 共用資料夾 Aug 28 2015](https://ofeyhong.pixnet.net/blog/post/95362789-%E3%80%90%E6%95%99%E5%AD%B8%E3%80%91%E5%8D%80%E5%9F%9F%E7%B6%B2%E8%B7%AF%E5%88%86%E4%BA%AB-%E2%80%93%E2%80%93-%E5%85%B1%E7%94%A8%E8%B3%87%E6%96%99%E5%A4%BE)  
![alt tag](https://pic.pimg.tw/ofeyhong/1440498039-529935486.jpg)  
![alt tag](https://pic.pimg.tw/ofeyhong/1440720890-522212512.jpg)  
![alt tag](https://pic.pimg.tw/ofeyhong/1440722917-797141263.jpg)  

![alt tag](https://pic.pimg.tw/ofeyhong/1440723061-2791256063.jpg)  
![alt tag](https://pic.pimg.tw/ofeyhong/1440723544-4209539621.jpg)  
![alt tag](https://pic.pimg.tw/ofeyhong/1440723771-886726308.jpg)  
![alt tag](https://pic.pimg.tw/ofeyhong/1440723950-84115144.jpg)  

# Troubleshooting  


# Reference
```

```


* []()  
![alt tag]()   
<img src="" width="400" height="500">

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





