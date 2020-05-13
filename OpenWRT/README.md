# Purpose
Take note of OpenWRT.

# Table of Content

# BT
[OpenWRT/DD-WRT路由器BT：不開電腦也可下載torrent 六月 23, 2013](https://upsangel.com/dd-wrt/openwrt-router-bt-bittorrent/)  
## 1. usb儲存裝置的準備  
```  

    ext2：速度快，但是單個文件不能超過2GB
    ext3：文件能超過2GB，但是journal功能一定開啟，會拖慢BT套件的讀寫
    ext4：可以關閉journal從而達到提高讀寫效率

顯而易見，我們要選擇ext3或ext4，BT電影輕易就超過2GB

如果你熟悉linux，可以用像這裡https://forum.openwrt.org/viewtopic.php?id=37165那樣關閉ext4的journalling

然後就要讓openwrt識別你的Usb設備：請根據http://wiki.openwrt.org/doc/howto/usb.storage中的Required Packages安裝你需要的套件，由於我是用SD卡+讀卡器+EXT4分區格式，我安裝的套件是：

kmod-usb-storage
kmod-usb-storage-extras
block-mount
kmod-fs-ext4
```  
![alt tag](https://farm8.staticflickr.com/7326/9115857058_085c0661ce.jpg)  

## 2. 安裝Transmission  

## 3. 設置Transmission  
![alt tag](https://farm8.staticflickr.com/7284/9113630667_429e5b947a.jpg)  

# Reference

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
