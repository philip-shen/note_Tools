# Notes of NAS
Take a note of NAS.

# BT
[WD My Cloud + Aria2](https://jojolization.blogspot.com/p/wd-my-cloud-ari.html)  

```
 以下僅支援WD My Cloud 4.x固件，不支持3.x，且4.x 暫無迅雷遠端下載的支援。

htop為top的的最佳替代品；aria2是一款支持http/https/ftp、bt、磁力鏈下載的工具，在國內常被用於百度雲離線、迅雷離線、QQ旋風離線下載；而transmission是一款專業的BT下載工具，常被用於PT。

首先訪問網頁 http://wdmycloud/UI ，在 設置 > 網路 中開啟ssh，用戶名：root，密碼：welc0me，並新建共用：Downloads。

以下通過ssh連接wdmycloud進行命令列操作，aria2 與 transmission 不以 root 方式運行。
```

## 一：htop  
```
#wget http://www.qiwu.org/uploads/2015/02/htop_1.0.1-1_armhf.deb
#dpkg -i htop_1.0.1-1_armhf.deb
```
 
##  二：aria2 1.15.1  
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

## 三：transmission 2.52  
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

