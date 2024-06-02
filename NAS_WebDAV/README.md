# Table of Contents
=================

   * [Purpose](#purpose)
   * [WebDAV](#webdav)
      * [Reference](#reference)
   * [BT](#bt)
      * [1 htop](#1-htop)
      * [2 aria2 1.15.1](#2-aria2-1151)
      * [3 transmission 2.52](#3-transmission-252)

# Purpose  
Take a note of NAS.


# WebDAV  
```
λ wsgidav.exe  -h
usage: wsgidav [-h] [-p PORT] [-H HOST] [-r ROOT_PATH] [--auth {anonymous,nt,pam-login}] [--server {cheroot,ext-wsgiutils,gevent,gunicorn,paste,uvicorn,wsgiref}]
               [--ssl-adapter {builtin,pyopenssl}] [-v | -q] [-c CONFIG_FILE | --no-config] [--browse] [-V]

Run a WEBDAV server to share file system folders.

Examples:

  Share filesystem folder '/temp' for anonymous access (no config file used):
    wsgidav --port=80 --host=0.0.0.0 --root=/temp --auth=anonymous

  Run using a specific configuration file:
    wsgidav --port=80 --host=0.0.0.0 --config=~/my_wsgidav.yaml

  If no config file is specified, the application will look for a file named
  'wsgidav.yaml' in the current directory.
  See
    http://wsgidav.readthedocs.io/en/latest/run-configure.html
  for some explanation of the configuration file format.


options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  port to serve on (default: 8080)
  -H HOST, --host HOST  host to serve from (default: localhost). 'localhost' is only accessible from the local computer. Use 0.0.0.0 to make your application public
  -r ROOT_PATH, --root ROOT_PATH
                        path to a file system folder to publish as share '/'.
  --auth {anonymous,nt,pam-login}
                        quick configuration of a domain controller when no config file is used
  --server {cheroot,ext-wsgiutils,gevent,gunicorn,paste,uvicorn,wsgiref}
                        type of pre-installed WSGI server to use (default: cheroot).
  --ssl-adapter {builtin,pyopenssl}
                        used by 'cheroot' server if SSL certificates are configured (default: builtin).
  -v, --verbose         increment verbosity by one (default: 3, range: 0..5)
  -q, --quiet           decrement verbosity by one
  -c CONFIG_FILE, --config CONFIG_FILE
                        configuration file (default: ('wsgidav.yaml', 'wsgidav.json') in current directory)
  --no-config           do not try to load default ('wsgidav.yaml', 'wsgidav.json')
  --browse              open browser on start
  -V, --version         print version info and exit (may be combined with --verbose)

Licensed under the MIT license.
See https://github.com/mar10/wsgidav for additional information.
```

```
λ wsgidav.exe  --config=wsgidav.yaml
00:11:28.275 - WARNING : App wsgidav.mw.cors.Cors(None).is_disabled() returned True: skipping.
00:11:28.307 - INFO    : WsgiDAV/4.3.0 Python/3.11.1 Windows-10-10.0.22621
00:11:28.307 - INFO    : Lock manager:      LockManager(LockStorageDict)
00:11:28.307 - INFO    : Property manager:  None
00:11:28.307 - INFO    : Domain controller: SimpleDomainController()
00:11:28.307 - INFO    : Registered DAV providers by route:
00:11:28.307 - INFO    :   - '/:dir_browser': FilesystemProvider for path 'c:\\WsgiDAV\\lib\\wsgidav\\dir_browser\\htdocs' (Read-Only) (anonymous)
00:11:28.307 - INFO    :   - '/pub': FilesystemProvider for path 'D:\\tools' (Read-Only) (anonymous)
00:11:28.307 - INFO    :   - '/': FilesystemProvider for path 'D:\\tools' (Read-Write)
00:11:28.307 - WARNING : Basic authentication is enabled: It is highly recommended to enable SSL.
00:11:28.307 - WARNING : Share '/pub' will allow anonymous write access.
00:11:28.307 - WARNING : Share '/:dir_browser' will allow anonymous write access.
00:11:28.417 - INFO    : Running WsgiDAV/4.3.0 Cheroot/9.0.0 Python/3.11.1
00:11:28.417 - INFO    : Serving on http://0.0.0.0:8080 ...
```

[wsgidav.bat](wsgidav.bat)  
[wsgidav.yaml](wsgidav.yaml)  

## Reference  
[15 Open Source WebDAV Servers Oct 27, 2022](https://medevel.com/15-os-webdav-servers/)  

[mar10/wsgidav](https://github.com/mar10/wsgidav)   
[mar10/wsgidav MSI Installer](https://github.com/mar10/wsgidav/releases/latest)  

[Linuxで簡易WebDAVサーバ構築 Last updated at 2020-09-24](https://qiita.com/Brad-55/items/5b596b76ef7dc1be9a39)  


# BT
[WD My Cloud + Aria2](https://jojolization.blogspot.com/p/wd-my-cloud-ari.html)  

```
 以下僅支援WD My Cloud 4.x固件，不支持3.x，且4.x 暫無迅雷遠端下載的支援。

htop為top的的最佳替代品；aria2是一款支持http/https/ftp、bt、磁力鏈下載的工具，在國內常被用於百度雲離線、迅雷離線、QQ旋風離線下載；而transmission是一款專業的BT下載工具，常被用於PT。

首先訪問網頁 http://wdmycloud/UI ，在 設置 > 網路 中開啟ssh，用戶名：root，密碼：welc0me，並新建共用：Downloads。

以下通過ssh連接wdmycloud進行命令列操作，aria2 與 transmission 不以 root 方式運行。
```

## 1 htop  
```
#wget http://www.qiwu.org/uploads/2015/02/htop_1.0.1-1_armhf.deb
#dpkg -i htop_1.0.1-1_armhf.deb
```
 
## 2 aria2 1.15.1  
```
安裝：
#wget http://www.qiwu.org/uploads/2015/02/libc-ares2_1.9.1-3_armhf.deb
#dpkg -i libc-ares2_1.9.1-3_armhf.deb
#wget http://www.qiwu.org/uploads/2015/02/aria2_1.15.1-1_armhf.deb
#dpkg -i aria2_1.15.1-1_armhf.deb
配置：
#useradd -r aria2c -M -s /bin/false
#wget http://www.qiwu.org/uploads/2015/02/aria2.tar.gz
#tar zxvf aria2.tar.gz -C /
#touch /var/log/aria2.log
#chmod 644 /var/log/aria2.log
#chown aria2c:aria2c /var/log/aria2.log
#mkdir /DataVolume/shares/Downloads/aria2
#chmod 777 /DataVolume/shares/Downloads/aria2
啟動：
#/etc/init.d/aria2c start
用戶端：
Aria2cRemoteControl-0.1.1-win32.exe 及 yaaw-zh-hans-master.zip 
[下載](http://www.qiwu.org/uploads/2015/02/Aria2cRemoteControl.zip)
```

## 3 transmission 2.52  
```
安裝支援檔：
#wget http://www.qiwu.org/uploads/2015/02/libcurl3-gnutls_7.26.0-1_armhf.deb
#dpkg -i libcurl3-gnutls_7.26.0-1_armhf.deb
#wget http://www.qiwu.org/uploads/2015/02/libminiupnpc5_1.5-2_armhf.deb
#dpkg -i libminiupnpc5_1.5-2_armhf.deb
#wget http://www.qiwu.org/uploads/2015/02/libnatpmp1_20110808-3_armhf.deb
#dpkg -i libnatpmp1_20110808-3_armhf.deb
#useradd -r transmission -M -s /bin/false
安裝配置transmission:
#wget http://www.qiwu.org/uploads/2015/02/transmission_wd.tar.gz
#tar zxvf transmission_wd.tar.gz -C /
#mkdir /DataVolume/shares/Downloads/Transmission/
#chmod 777 /DataVolume/shares/Downloads/Transmission
#mkdir /DataVolume/shares/Downloads/Transmission/info
#cd /DataVolume/shares/Downloads/Transmission/info
#wget http://www.qiwu.org/uploads/2015/02/settings.json
#chown transmission:transmission -R/DataVolume/shares/Downloads/Transmission/info
#chmod 755 /DataVolume/shares/Downloads/Transmission/info
#chmod 600/DataVolume/shares/Downloads/Transmission/info/settings.json
#touch /var/log/transmission-daemon.log
#chmod 644 /var/log/transmission-daemon.log
#chown transmission:transmission /var/log/transmission-daemon.log
編輯設定檔：
#vi /DataVolume/shares/Downloads/Transmission/info/settings.json
查找
"rpc-whitelist": "127.0.0.1,192.168.*.*",
將 192.168.*.* 改為你目前的IP段.
啟動：
#/etc/init.d/transmission start
用戶端：
Transmission Remote GUI 5.0.1 for windows下載：
http://www.qiwu.org/uploads/2015/02/transgui-5.0.1-setup.zip

如需aria2、transmission開機自啟，執行：
#update-rc.d aria2c defaults
#update-rc.d transmission defaults
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

