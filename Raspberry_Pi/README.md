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
   * [I2C](#i2c)         
   * [h1 size](#h1-size)
      * [h2 size](#h2-size)
         * [h3 size](#h3-size)
            * [h4 size](#h4-size)
               * [h5 size](#h5-size)

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


* []()
![alt tag]()  

# h1 size

## h2 size

### h3 size

#### h4 size

##### h5 size

*strong*strong  
**strong**strong  

