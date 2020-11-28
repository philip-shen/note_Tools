Table of Contents
=================

   * [Table of Contents](#table-of-contents)
   * [Purpose](#purpose)
   * [声優ラジオ録音環境](#声優ラジオ録音環境)
      * [録音ファイルのアップロード、アップロード完了通知の準備](#録音ファイルのアップロードアップロード完了通知の準備)
         * [Dropboxへのファイルアップロード準備](#dropboxへのファイルアップロード準備)
         * [LINEへの通知準備](#lineへの通知準備)
         * [slackで通知する](#slackで通知する)
   * [NFS](#nfs)
      * [NAS の設定変更する](#nas-の設定変更する)
      * [Raspberry Pi でマウント設定する](#raspberry-pi-でマウント設定する)
      * [Clinet Side](#clinet-side)
      * [Raspberry PiからNASボリュームMount](#raspberry-piからnasボリュームmount)
         * [/etc/fstabにNFSボリュームのマウント情報を記載](#etcfstabにnfsボリュームのマウント情報を記載)
         * [Raspberry PiのBootオプション変更（NASマウントタイミング変更）](#raspberry-piのbootオプション変更nasマウントタイミング変更)
         * [/etc/rc.localに３秒Sleep後マウント](#etcrclocalに３秒sleep後マウント)
         * [その他ブートシーケンスに関係すると](#その他ブートシーケンスに関係すると)
   * [樹莓派｜外接麥克風及喇叭設置](#樹莓派外接麥克風及喇叭設置)
      * [調整音量](#調整音量)
   * [Raspberrypi Connection by Windows](#raspberrypi-connection-by-windows)
      * [xrdpインストール](#xrdpインストール)
      * [日本語キーボードの配列を追加](#日本語キーボードの配列を追加)
      * [xrdpを再起動させる](#xrdpを再起動させる)
      * [Windowsから接続](#windowsから接続)
   * [Installing cryptography using pip on Raspbian Jessie image](#installing-cryptography-using-pip-on-raspbian-jessie-image)
   * [I2C](#i2c)
      * [I2C configraion on Rpi 4](#i2c-configraion-on-rpi-4)
      * [Raspberry PI Multiple I2C Devices](#raspberry-pi-multiple-i2c-devices)
   * [Raspberry Pi NAS](#raspberry-pi-nas)
      * [Step 01: Is NAS for you?](#step-01-is-nas-for-you)
      * [Step 02: Self-storage](#step-02-self-storage)
      * [Step 03: Prepare the OS](#step-03-prepare-the-os)
      * [Step 04: Add your storage](#step-04-add-your-storage)
      * [Step 05: Prepare the drives](#step-05-prepare-the-drives)
      * [Step 06: Create the RAID](#step-06-create-the-raid)
      * [Step 07: Mount the drive](#step-07-mount-the-drive)
      * [Step 08: Do the Samba!](#step-08-do-the-samba)
      * [Step 09: Granting access](#step-09-granting-access)
      * [Step 10: Create home directories](#step-10-create-home-directories)
      * [Step 11: Backup, backup, backup](#step-11-backup-backup-backup)
      * [Step 12: Don’t interrupt!](#step-12-dont-interrupt)
      * [Step 13: Add more features](#step-13-add-more-features)
   * [Transmission-daemon torrent-box](#transmission-daemon-torrent-box)
      * [１．transmission-daemonのインストール](#１transmission-daemonのインストール)
      * [２．transmission-daemonの設定](#２transmission-daemonの設定)
   * [Rpi Security](#rpi-security)
      * [１．rootユーザーのパスワード設定](#１rootユーザーのパスワード設定)
      * [２．piユーザーに代わる新たなユーザーの追加とpiの削除](#２piユーザーに代わる新たなユーザーの追加とpiの削除)
      * [３．SSHの設定見直し](#３sshの設定見直し)
      * [４．ファイアウォールの設定](#４ファイアウォールの設定)
      * [新規ユーザーの作成](#新規ユーザーの作成)
      * [SSHで公開鍵認証](#sshで公開鍵認証)
      * [ポート番号等の設定変更](#ポート番号等の設定変更)
      * [piユーザーの削除](#piユーザーの削除)
   * [h1 size](#h1-size)
      * [h2 size](#h2-size)
         * [h3 size](#h3-size)
            * [h4 size](#h4-size)
               * [h5 size](#h5-size)
   * [Table of Contents](#table-of-contents-1)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)

# Purpose  
Take note of Raspberry_Pi  

# 声優ラジオ録音環境  
[ぼくの声優ラジオ録音環境（ラズパイ4で録音→Dropboxにアップ→LINEに通知まで） updated at 2020-06-15](https://qiita.com/kino15/items/32f8ceed4261ba18817f#windows10%E3%81%8B%E3%82%89ssh%E3%81%A7%E3%83%A9%E3%82%BA%E3%83%91%E3%82%A4%E3%81%AB%E6%8E%A5%E7%B6%9A%E3%81%97%E3%81%A6%E4%BD%9C%E6%A5%AD)

## 録音ファイルのアップロード、アップロード完了通知の準備  
### Dropboxへのファイルアップロード準備  
[【Dropbox】scriptを使用してのファイル転送処理](https://qiita.com/Dace_K/items/890e9f2fe93a66ec8e56)

### LINEへの通知準備  
[[超簡単]LINE notify を使ってみる](https://qiita.com/iitenkida7/items/576a8226ba6584864d95)
RThBFBKPPKa1lKyVv1mKURTRci4Mq4VZhOnUdoIefKp

通知先のルームです。 
![alt tag](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F21391%2F69fccdd0-58c1-6cfe-194e-8fa53aca8903.png?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&s=df5227f671c781ebd6336f437c86648b)  

![alt tag](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F21391%2Fcbd483ef-7300-9763-fc40-2dd33e3a3053.png?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&s=5a359371a5342f5484fe258515e75c96)  

![alt tag](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F21391%2F6e6024af-565f-3a9f-cf9c-4316f463d01d.png?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&s=76049c30a5bbed504e40b2f7a8776a64)  

通知してくれるbotくん（LINE notify）を設定したルームに招待してあげてください  
![alt tag](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F21391%2F95155252-dcc0-7b26-555d-c74cec44c41c.jpeg?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&s=abe1174e1ae6ae1f644fbb1cb4c4074b)  

```
curl -X POST -H "Authorization: Bearer ACCESS_TOKEN" -F "message=ABC" https://notify-api.line.me/api/notify
```



[上手 LINE Notify 不求人：一行代碼都不用寫的推播通知方法 2020/02/17](https://blog.miniasp.com/post/2020/02/17/Go-Through-LINE-Notify-Without-Any-Code)  
```
如果想得知目前 Access Token 的 API Rate Limit 相關資訊，可以改用以下命令查詢：

curl -D - -H "Authorization: Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" https://notify-api.line.me/api/status
```
```
其中的 X-RateLimit-Remaining 就是你這個 Token 在這一個小時內還能用幾次。

還有 X-RateLimit-Reset 代表著下次 Reset 用量限制的時間點，這是 UTC epoch seconds 單位。
```

### slackで通知する  
[Slack APIを使用してメッセージを送信する](https://qiita.com/kou_pg_0131/items/56dd81f2f4716ca292ef)


# NFS  
[Raspberry Pi 4 と NAS で録画環境を整える 2020-01-02](https://kumak1.hatenablog.com/entry/2020/01/02/202308)  

## NAS の設定変更する  

## Raspberry Pi でマウント設定する  
```
pi@raspberrypi:~ $ sudo mkdir -p /mnt/nas
pi@raspberrypi:~ $ sudo chown pi /mnt/nas/
```

> /etc/fstab に以下を追記し、自動マウントさせる。  
```
192.168.10.2:/volume1/video /mnt/nas nfs rsize=8192,wsize=8192,timeo=14,intr
```

> 自動マウントしたら、保存先のディレクトリ作成と権限を付与しておく。
```
pi@raspberrypi:~ $ sudo mkdir -p /mnt/nas/recorded
pi@raspberrypi:~ $ sudo chown pi /mnt/nas/recorded 
pi@raspberrypi:~ $ sudo chown :video /mnt/nas/recorded 
```

## Clinet Side  
[ubuntu 16.04 or raspberry pi 3 でのNFSの設定 クライアント側 posted at 2016-10-25](https://qiita.com/hdoi/items/06e3aeca07efa1993555#%E3%82%AF%E3%83%A9%E3%82%A4%E3%82%A2%E3%83%B3%E3%83%88%E5%81%B4)
```
sudo apt-get install nfs-common
```

> 次に、/etc/fstabを編集します。  
```
sudo vi /etc/fstab
```

> また中身に以下を追加します。
```
192.168.1.1:/home /home nfs defaults,soft,intr,clientaddr=192.168.1.2
```

> 以下のコマンドで確認してください。
```
sudo service rpcbind start
sudo mount -a
```

## Raspberry PiからNASボリュームMount  
[Raspberry PiからSynology NAS volumeをnfs mountする 2019年7月21日](https://www.miki-ie.com/infrastructure/raspberry-pi-nfs-mount-synology-nas/)

### /etc/fstabにNFSボリュームのマウント情報を記載  
```
 $ cat /etc/fstab
proc /proc proc defaults 0 0
/dev/mmcblk0p6 /boot vfat defaults 0 2
/dev/mmcblk0p7 / ext4 defaults,noatime 0 1
# a swapfile is not a swap partition, no line here
# use dphys-swapfile swap[on|off] for that
192.168.0.100:/volume1/raspberry /mnt/synology nfs defaults,_netdev 0 0
```

### Raspberry PiのBootオプション変更（NASマウントタイミング変更）  
```
$ sudo raspi-config
```

```
1. 3 Boot Options Configure options for start-up　を選択
2. B2 Wait for Network at Boot Chose whether to wait for network connection　を選択
3. <Yes>　を選択
4. <Ok>　を選択
```
![alt tag](https://i0.wp.com/www.miki-ie.com/wp-content/uploads/2019/07/nas-mount1.png?resize=860%2C726&ssl=1)  

![alt tag](https://i0.wp.com/www.miki-ie.com/wp-content/uploads/2019/07/nas-mount2.png?resize=860%2C732&ssl=1)  

![alt tag](https://i0.wp.com/www.miki-ie.com/wp-content/uploads/2019/07/nas-mount3.png?resize=568%2C571&ssl=1)  

![alt tag](https://i0.wp.com/www.miki-ie.com/wp-content/uploads/2019/07/nas-mount4.png?resize=568%2C581&ssl=1)  

### /etc/rc.localに３秒Sleep後マウント  
```
よって、/etc/rc.localに３秒のスリープとマウントコマンドを追加しました。
sleep 3
sudo mount -t nfs 192.168.0.100:/volume1/raspberry /mnt/synology
```

### その他ブートシーケンスに関係すると  
```
$ sudo systemctl enable systemd-networkd

$ sudo systemctl enable systemd-networkd-wait-online
```


[Raspberry Pi 3+Chinachuで地デジ録画サーバー構築 updated at 2019-12-02](https://qiita.com/shotasano/items/3809b8f3e0b62d51d3c3)  
[Raspberry Pi でTVを見る録る！ updated at 2019-09-29](https://qiita.com/sigma7641/items/5b4946d2388ae0f5402d)  
[とりあえずRaspberryPiにChinachu γを導入できた件  2017-07-30](http://k-pi.hatenablog.com/entry/2017/07/30/151659)  

# 樹莓派｜外接麥克風及喇叭設置  
[IoT｜硬體｜樹莓派｜外接麥克風及喇叭設置 9月 26, 2017](http://agilego99.blogspot.com/2017/09/iot_26.html) 

## 調整音量  
```
我們直接用工具程式來調整。
alsamixer
```


# Raspberrypi Connection by Windows  
[Windowsパソコンからraspberrypi3にリモートデスクトップで接続する 2016/09/24](https://qiita.com/t114/items/bfac508504b9a6b7570d)  

## xrdpインストール  
```
  $ sudo apt-get update
  $ sudo apt-get install xrdp
```

## 日本語キーボードの配列を追加  
```
  $ cd /etc/xrdp/
  $ sudo wget http://w.vmeta.jp/temp/km-0411.ini
  $ sudo ln -s km-0411.ini km-e0010411.ini
  $ sudo ln -s km-0411.ini km-e0200411.ini
  $ sudo ln -s km-0411.ini km-e0210411.ini
```

## xrdpを再起動させる  
```
 $ sudo service xrdp restart
```

## Windowsから接続  
```
    win + R でファイル名を指定して実行画面表示する。
    mstsc を入力する。

    表示されたリモートデスクトップ接続画面でraspberrypi3のipアドレスを入力し接続する。 (raspberrypiのipアドレス固定方法はこちら)

    Moduleはそのまま（sesman-Xvnc）

    username：pi

    password：raspberry

    raspberrypiのデスクトップが表示されれば成功です。
```

# Installing cryptography using pip on Raspbian Jessie image   
[Installing cryptography using pip on Raspbian Jessie image asked Feb 22 '17](https://raspberrypi.stackexchange.com/questions/62364/installing-cryptography-using-pip-on-raspbian-jessie-image)  
```
sudo apt-get update  
sudo apt-get upgrade  
sudo apt-get install libffi-dev libssl-dev python-dev  
```
```
pip install cryptography
```
<img src="https://i.imgur.com/UGQQgHM.png" width="900" height="150">


# I2C  
[Alexaに部屋の温度と湿度を教えてもらう updated at 2019-02-14](https://qiita.com/yuppejp/items/f1d26b1852935d3b50cb)
```
$ sudo apt-get install i2c-tools
```

```
$ sudo raspi-config
```

```
$ sudo i2cdetect -r -y 1
```

## I2C configraion on Rpi 4 
[Raspberry Pi で I2C を利用するための設定 2019/06/03](https://www.qoosky.io/techs/2316d68b2e)  
[Raspberry Pi3 I2C baud rate setting Sat Aug 04, 2018](https://www.raspberrypi.org/forums/viewtopic.php?t=219675)  
[Raspberry PiのI2Cデータ転送速度と波形を見る　その2 2016.10.30](https://www.denshi.club/pc/raspi/raspberry-pii2c2.html)  
**1**  
```
sudo cat /etc/modules
i2c-dev
```
**2**  
```
sudo nano /boot/config.txt
```
<img src="https://i.imgur.com/xfIgfN1.jpg"  width="300" height="400">

**3**  
```
sudo reboot
```

## Raspberry PI Multiple I2C Devices  
[Raspberry PI Multiple I2C Devices](https://www.instructables.com/id/Raspberry-PI-Multiple-I2c-Devices/)  

[RPi4 and i2c; Has anyone used additional i2c buses? ](https://www.raspberrypi.org/forums/viewtopic.php?f=44&t=244947&sid=998d60c61c7909512716e9d4a60634c3)  

<img src="https://img.purch.com/1561671569116-png/w/755/aHR0cDovL21lZGlhLmJlc3RvZm1pY3JvLmNvbS8xLzAvODQzNzMyL29yaWdpbmFsLzE1NjE2NzE1NjkxMTYucG5n"  width="400" height="500">

# Raspberry Pi NAS  
[Build a Raspberry Pi NAS](https://magpi.raspberrypi.org/articles/build-a-raspberry-pi-nas) 
```
You'll need

    2 × External USB drives (minimum), e.g. these Seagate hard drives
    USB 3.0 powered hub
    Gigabit Ethernet (recommended)
    UPS (optional)
```
## Step 01: Is NAS for you?  
## Step 02: Self-storage  
## Step 03: Prepare the OS  
## Step 04: Add your storage  
## Step 05: Prepare the drives  
## Step 06: Create the RAID  
## Step 07: Mount the drive  
## Step 08: Do the Samba!  
## Step 09: Granting access  
## Step 10: Create home directories  
## Step 11: Backup, backup, backup 
## Step 12: Don’t interrupt!  
## Step 13: Add more features  
```
 For the more adventurous user, 
 Docker is an excellent way of making your NAS perform multiple functions without getting into a configuration nightmare. 
 Why not set up a DLNA streaming server or run multiple databases? 
 If you’ve enabled SSH, you’ve already got SFTP available; just connect using your favourite FTP client using /mnt/raid1/shared as the starting point.
```

[RaspberryPi4 サーバー構築03　ストレージ入替＆Samba共有編 2020年06月27日](http://devlife.blog.jp/archives/54771132.html)  


# Transmission-daemon torrent-box  
[Transmission-daemon@ラズパイでtorrent-box 2020年08月14日](http://devlife.blog.jp/archives/54915711.html)  
## １．transmission-daemonのインストール  
```
$ su - root
パスワード:
 
# apt update
# apt upgrade
# apt install transmission-daemon
```

## ２．transmission-daemonの設定  
```
# systemctl stop transmission-daemon
# cd /etc/transmission-daemon
# vim ./setting.json
 
:
"download-dir": "/data/torrent/downloads",      15行目当たり。ここをダウンロード先ディレクトリに変更。
:
"incomplete-dir": "/data/torrent/Downloads",    23行目当たり。ここもダウンロード先ディレクトリに変更。
:
"rpc-host-whitelist": "127.0.0.1,192.168.*.*",  48行目当たり。ラズパイ自身とラズパイにリモート接続する端末IPアドレス帯を許可しておく。
"rpc-host-whitelist-enabled": true,
"rpc-password": "Password!",                    とりあえず"Password!"で。transmission-daemonを起動すると平文から暗号化される。
"rpc-port": 9091,                               このポート番号は覚えておく。あとでファイアウォール許可します。
"rpc-url": "/transmission/",                    ブラウザからアクセスするためのURLの定義。http://[]ラズパイIPアドレス]:9091でアクセスするとURL後ろに/transmission/が補完される。
"rpc-username": "transmission",                 ブラウザからアクセスした時のBASIC認証のユーザー名
"rpc-whitelist": "127.0.0.1,192.168.*.*",       48行目のrpc-host-whitelistと同じにした。
"rpc-whitelist-enabled": true,
:
 
（上記変更して保存）
```

```
# mkdir -p /data/torrent/downloads
# mkdir -p /data/torrent/Downloads
# chown -R debian-transmission:debian-transmission /data/torrent/
# chmod -R g+w /data/torrent/
```

```
# usermod -aG debian-transmission [smb.confの"force user"に記載したユーザー名]
```

```
# ufw allow 9091
```

```
# systemctl start transmission-daemon
```

```
http://[]ラズパイIPアドレス]:9091
```

# Rpi Security  
[RaspberryPi4 サーバー構築06　セキュリティ対策編 2020年06月30日](http://devlife.blog.jp/archives/54778281.html) 

## １．rootユーザーのパスワード設定  
## ２．piユーザーに代わる新たなユーザーの追加とpiの削除  
## ３．SSHの設定見直し  
## ４．ファイアウォールの設定  

[ラズパイでやらなければいけない４つのセキュリティ対策！ 2020-06-11](https://qiita.com/nokonoko_1203/items/94a888444d5019f23a11) 

## 新規ユーザーの作成  
## SSHで公開鍵認証  
[公開鍵と秘密鍵を作成](https://qiita.com/nokonoko_1203/items/94a888444d5019f23a11#%E5%85%AC%E9%96%8B%E9%8D%B5%E3%81%A8%E7%A7%98%E5%AF%86%E9%8D%B5%E3%82%92%E4%BD%9C%E6%88%90)
## ポート番号等の設定変更  
[ラズパイとSSHの設定変更](https://qiita.com/nokonoko_1203/items/94a888444d5019f23a11#%E3%83%A9%E3%82%BA%E3%83%91%E3%82%A4%E3%81%A8ssh%E3%81%AE%E8%A8%AD%E5%AE%9A%E5%A4%89%E6%9B%B4)  
## piユーザーの削除

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

