# Table of Contents
=================

   * [Purpose](#purpose)
   * [OpenMediaVault](#openmediavault)
      * [Reference](#reference)
   * [TrueNAS](#truenas)
      * [Reference](#reference-1)
   * [Reference](#reference-2)

# Purpose  
Take a note of NAS.


# OpenMediaVault   

## Installation  
### 1. Raspberry Pi OS Lite(64bit) by Micro SD  
  Raspberry Pi Imager installation on Windows 
    
  <img src="https://camo.qiitausercontent.com/6cc2fc7d82d3526122024edbdd6cb651df31398d/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e61702d6e6f727468656173742d312e616d617a6f6e6177732e636f6d2f302f3235363931342f66366434373534632d346436332d373831352d313762642d6334396466313530333463622e706e67" width="600" height="400">  

### 2. config.txt Setup  
   ```
    #hdmi_safe=1
   ```

### 3. WiFi and SSH Setup  
  ```
    $touch boot/ssh
  ```

  ```
    $vi boot/wpa_supplicant.confg
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=JP

    network={
      ssid="<アクセスポイントのSSID>"
      psk="<パスワード>"
    }
  ```

### 4. OpenMediaVault Installation  
  ```
    sudo -i
    sudo apt update
    sudo apt upgrade
  ```

  ```
    cd /opt/
    wget -O - https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install | sudo bash
  ```

### 5. OpenMediaVault Setup from Browser on Windows

### 6. SSH Setup  
  ```
  Whats missing? SSH as different user

  Does the user have SSH permissions? In the web-gui at "user management" - "users" - "edit" check if the group "ssh" is checked ("sudo" is also useful).  
  ```
  [Whats missing? SSH as different user](https://www.reddit.com/r/OpenMediaVault/comments/pv0ksz/whats_missing_ssh_as_different_user/) 

## Reference  
[Raspberry Pi 4 + OpenMediaVaultでNASを構築する 2023/03/13](https://zenn.dev/oversleep/articles/3f9ad984a37aba)  
[Raspberry Pi 4が起動しない（モニタが映らない）場合の設定方法 2022-07-06](https://qiita.com/karaage0703/items/97808dfb957b3312b649)  

[RaspberryPI4をサーバーにして遊び倒す。その１ 2020-12-24](https://qiita.com/miyukiaizawa/items/99da331359eaf4c7eec7)
```
DockerとPortainerのインストール
```
[RaspberryPI4をサーバーにして遊び倒す。その２ 2020-12-20](https://qiita.com/miyukiaizawa/items/37d4d386150eddaaeddb)  

[New 2024 openmediavault getting started, omv extras and portainer  2024年1月29日](https://www.youtube.com/watch?v=2hU8e61UE9w)  
[*Link to my GitHub where you can find the portainer.yml file* ](https://github.com/robwithtech/homelab)  

[RaspberrypiでNASを作成する 2024-03-12](https://qiita.com/T3pp31/items/36a9ce18b0780ff04cd3)  

[PythonでRaspberryPiで撮影したカメラ映像をリアルタイム転送する 2023-01-27](https://qiita.com/Yurix/items/e3260da3d91451c5a60a)  

[Raspberry PiでRAID付きNASを構築する 2023-09-02](https://qiita.com/YaezakuraP/items/d0c41d6c5ee8438fecbb)

[Raspberry Piでprimary/2replica構成のMySQL serverを建てる 2024/05/1](https://zenn.dev/kumashun8/articles/ab8ef900613f7c)  

[OMV7.xをbookworm(Pi 4)へ新規インストールする方法 2024-03-09](https://raspida.com/omv7-bookworm-pi4)  
[初心者でもラズパイでNASサーバーを作ってみよう！ 2024-03-13](https://raspida.com/make-nas-rpi)  
[openmediavaultでexfatの外付けハードディスクを利用する 2023-05-03](https://raspida.com/omv-exfat/)  

[Raspberry pi 4 でNAS（openmediavault）を構築する方法 2020-10-20](https://qiita.com/zono_0/items/1eb877ad9c6e5ac12532#14-guiopenmediavault%E3%81%B8%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9)  

[【Raspberry Pi4】新OS「Bullseye」で自宅用NASを構築する-前編 OpennMediaVault6対応 2022.06.05](https://immedeep.com/raspberrypi4-omv-nas-1/364/)  
[【Raspberry Pi4】新OS「Bullseye」で自宅用NASを構築する-後編 OpennMediaVault6の導入とベンチマーク 2022.10.19](https://immedeep.com/raspberrypi4-omv-nas-2/454/)  

[【低成本 Raspberry Pi 家用伺服器】前置動作: 在 Raspberry pi 4 上安裝 Ubuntu Server 08292020](https://journal.travelhackfun.com/raspberry-pi-4-ubuntu/)  
[【低成本 Raspberry Pi 家用伺服器】之二 – Raspberry Pi NAS | 使用USB外接硬碟設定 RAID 1 09262023](https://journal.travelhackfun.com/raspberry-pi-nas/)  
[【低成本家用伺服器】之三 – 10分鐘在Raspberry Pi上架多個WordPress網站 10232023](https://journal.travelhackfun.com/multi-wordpress-raspberrypi/)  

[自己动手使用树莓派搭建家用NAS和流媒体服务器 2023-11-13](https://www.packetmania.net/2021/12/19/RPi-NAS-Plex/)  

[Installing OpenMediaVault to a Raspberry Pi Jun 11, 2022](https://pimylifeup.com/raspberry-pi-openmediavault/)  


# TrueNAS   

## Reference  

# Reference
[大画面テレビの録画用HDDの代わりにRasberry Pi4のUSB OTG機能を生かしてUSBtoLAN(NAS)なストレージゲートウェイを構成する 2020-03-13](https://qiita.com/kthrtty/items/7243d59bb418de50f732)  



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

