
Table of Contents
=================

   * [Table of Contents](#table-of-contents)
   * [Purpose](#purpose)
   * [雙系統 Win10/11   Ubuntu 22.04 LTS 雙系統安裝（GPT UEFI）](#雙系統-win1011--ubuntu-2204-lts-雙系統安裝gptuefi)
      * [Step1 : 因為要開安裝雙系統，先確認電腦已存在Win10/11(這是廢話)。](#step1--因為要開安裝雙系統先確認電腦已存在win1011這是廢話)
      * [Step2 : 先確認舊筆電硬體規格 VS Ubuntu 配備需求是否可支援(很重要，不然就做白工。)](#step2--先確認舊筆電硬體規格-vs-ubuntu-配備需求是否可支援很重要不然就做白工)
      * [Step3 : 因為HDD有1TB夠大分出足夠的硬碟給Ubuntu系統(安裝磁碟分割至少需要 20 GB以上的磁碟空間)，本實作上預留了120G。](#step3--因為hdd有1tb夠大分出足夠的硬碟給ubuntu系統安裝磁碟分割至少需要-20-gb以上的磁碟空間本實作上預留了120g)
      * [Step4 : 關閉Win10/11 快速啟動功能( 重要，不關這個會影響雙系統啟動時的系統選擇) 關閉**【windows快速啟動】**](#step4--關閉win1011-快速啟動功能-重要不關這個會影響雙系統啟動時的系統選擇-關閉windows快速啟動)
      * [Step5 : 下載 ubuntu-22.04.1-desktop-amd64.iso](#step5--下載-ubuntu-22041-desktop-amd64iso)
      * [Step6 : 使用Rufus 製作 UBUNTU 開機USB，找一只4GB以上的隨身碟(建議16GB)](#step6--使用rufus-製作-ubuntu-開機usb找一只4gb以上的隨身碟建議16gb)
      * [Step7 : 每個電腦製造商開機時要進入 BOIS 開機選單的按鍵都不太一樣，下方幫大家整理常見的開機選單按鈕：](#step7--每個電腦製造商開機時要進入-bois-開機選單的按鍵都不太一樣下方幫大家整理常見的開機選單按鈕)
      * [Step8 : 再次啟動時，下一次啟動 老戴(Dell)是按F12開機進入BIOS，開啟一次性開機功能表。使用游標/方向鍵選取您的開機方式，然後按下 ENTER 鍵到 Secure boot/ 將【Secure Boot Enabled】 關閉後，下一次重啟進入USB開機安裝ubuntu install。](#step8--再次啟動時下一次啟動-老戴dell是按f12開機進入bios開啟一次性開機功能表使用游標方向鍵選取您的開機方式然後按下-enter-鍵到-secure-boot-將secure-boot-enabled-關閉後下一次重啟進入usb開機安裝ubuntu-install)
      * [Step9: 使用進行 UBUNTU 開機USB進行安裝與設定](#step9-使用進行-ubuntu-開機usb進行安裝與設定)
         * [1. 設定開機時，請選擇試用 Ubuntu 選項。此選項會檢查 Ubuntu 是否判斷您的硬體正常。](#1-設定開機時請選擇試用-ubuntu-選項此選項會檢查-ubuntu-是否判斷您的硬體正常)
         * [2. 當您準備好繼續時，請按一下安裝 Ubuntu 按鈕。安裝精靈隨即出現，並提示您進行某些選擇。](#2-當您準備好繼續時請按一下安裝-ubuntu-按鈕安裝精靈隨即出現並提示您進行某些選擇)
         * [3. 選取您的安裝語言，然後按一下繼續。](#3-選取您的安裝語言然後按一下繼續)
         * [4. 隨即會顯示keybord layout 鍵盤配置視窗。](#4-隨即會顯示keybord-layout-鍵盤配置視窗)
         * [5. 為電腦選取的配置 english (建議)or chinese(路徑會變成中文容易有問題)，然後按一下「繼續」。](#5-為電腦選取的配置-english-建議or-chinese路徑會變成中文容易有問題然後按一下繼續)
         * [6. 如沒有插入有線，則安裝會引導設定無線 Wi-Fi 連線與密碼。](#6-如沒有插入有線則安裝會引導設定無線-wi-fi-連線與密碼)
         * [7. 安裝精靈隨即出現/Install畫面/Installation type 選擇 something else。](#7-安裝精靈隨即出現install畫面installation-type-選擇-something-else)
      * [Step10:使用 Ubuntu 安裝程式建立多個自訂磁碟分割](#step10使用-ubuntu-安裝程式建立多個自訂磁碟分割)
      * [Step11: 選取地圖上最接近您的位置，或在文字方塊內輸入，然後按一下繼續。可以偵測鍵盤設定取得協助。](#step11-選取地圖上最接近您的位置或在文字方塊內輸入然後按一下繼續可以偵測鍵盤設定取得協助)
      * [Step12: Who are you ? 畫面視窗 隨即出現。需要輸入您的資訊。](#step12-who-are-you--畫面視窗-隨即出現需要輸入您的資訊)
      * [Step13: 安裝精靈完成後，您會看到安裝已完成訊息視窗。按一下右上角 立即重新開機。](#step13-安裝精靈完成後您會看到安裝已完成訊息視窗按一下右上角-立即重新開機)
      * [Step14: 設定開機順序](#step14-設定開機順序)
         * [1. 預設開機作業系統為 Ubuntu。這表示如果您按下 Enter 鍵或等待 10 秒，系統會直接開機至 Ubuntu。](#1-預設開機作業系統為-ubuntu這表示如果您按下-enter-鍵或等待-10-秒系統會直接開機至-ubuntu)
         * [2. 如果您要變更為 Windows 安裝，請重新開機電腦，然後從 GRUB 功能表選擇 Windows 磁碟分割。](#2-如果您要變更為-windows-安裝請重新開機電腦然後從-grub-功能表選擇-windows-磁碟分割)
   * [Reference](#reference)
      * [UEFI 安裝需要哪些 BIOS 設定？](#uefi-安裝需要哪些-bios-設定)
         * [在啟動時按下 F2 鍵進入 BIOS。確定 BIOS 設為 UEFI，並停用傳統選項 ROM，亦停用安全開機。](#在啟動時按下-f2-鍵進入-bios確定-bios-設為-uefi並停用傳統選項-rom亦停用安全開機)
   * [h1 size](#h1-size)
      * [h2 size](#h2-size)
         * [h3 size](#h3-size)
            * [h4 size](#h4-size)
               * [h5 size](#h5-size)
   * [Table of Contents](#table-of-contents-1)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)


# Purpose  
Take note of either Windows or Linux boots OS

# 雙系統 Win10/11 + Ubuntu 22.04 LTS 雙系統安裝（GPT+UEFI）   
[JT技術筆記-讓舊筆電變廢為寶-雙系統 Win11 與 Linux ubuntu desktop  2022-09-16](https://ithelp.ithome.com.tw/articles/10289644)  

## Step1 : 因為要開安裝雙系統，先確認電腦已存在Win10/11(這是廢話)。  

## Step2 : 先確認舊筆電硬體規格 VS Ubuntu 配備需求是否可支援(很重要，不然就做白工。)

```
以下是安裝Ubuntu基本的配備需求：

    2GHz以上的x86處理器。
    512MB以上的系統記憶體。
    5G以上的磁碟空間。
    Linux相容的顯示卡。
```

## Step3 : 因為HDD有1TB夠大分出足夠的硬碟給Ubuntu系統(安裝磁碟分割至少需要 20 GB以上的磁碟空間)，本實作上預留了120G。

## Step4 : 關閉Win10/11 快速啟動功能( 重要，不關這個會影響雙系統啟動時的系統選擇) 關閉**【windows快速啟動】**

## Step5 : 下載 ubuntu-22.04.1-desktop-amd64.iso  

## Step6 : 使用Rufus 製作 UBUNTU 開機USB，找一只4GB以上的隨身碟(建議16GB)  

```
插入U盤，開啟Rufus軟體，
   1.選擇你自己下載的iso檔案
   2.資料分割配置 : GPT
   3.目標系統 : UEFI
   4.然後點選【執行】。
```

<img src="https://ithelp.ithome.com.tw/upload/images/20220916/20127129i8NWCZIifq.png" width="400" height="500">

<img src="https://ithelp.ithome.com.tw/upload/images/20220916/20127129i8NWCZIifq.png" width="400" height="500">

## Step7 : 每個電腦製造商開機時要進入 BOIS 開機選單的按鍵都不太一樣，下方幫大家整理常見的開機選單按鈕：  

<img src="https://ithelp.ithome.com.tw/upload/images/20220916/20127129UNRONE0CJE.png" width="500" height="500">

## Step8 : 再次啟動時，下一次啟動 老戴(Dell)是按F12開機進入BIOS，開啟一次性開機功能表。使用游標/方向鍵選取您的開機方式，然後按下 ENTER 鍵到 Secure boot/ 將【Secure Boot Enabled】 關閉後，下一次重啟進入USB開機安裝ubuntu install。

**注意 :【Secure Boot Enabled】 關閉(設定變更會需要微軟恢復金鑰) ，請小心服用 **

## Step9: 使用進行 UBUNTU 開機USB進行安裝與設定

### 1. 設定開機時，請選擇試用 Ubuntu 選項。此選項會檢查 Ubuntu 是否判斷您的硬體正常。
### 2. 當您準備好繼續時，請按一下安裝 Ubuntu 按鈕。安裝精靈隨即出現，並提示您進行某些選擇。
### 3. 選取您的安裝語言，然後按一下繼續。
### 4. 隨即會顯示keybord layout 鍵盤配置視窗。
### 5. 為電腦選取的配置 english (建議)or chinese(路徑會變成中文容易有問題)，然後按一下「繼續」。
### 6. 如沒有插入有線，則安裝會引導設定無線 Wi-Fi 連線與密碼。
### 7. 安裝精靈隨即出現/Install畫面/Installation type 選擇 something else。

## Step10:使用 Ubuntu 安裝程式建立多個自訂磁碟分割 
[How to Install Ubuntu with Multiple Custom Partitions on Your Dell Computer](https://www.dell.com/support/kbdoc/zh-tw/000131391/how-to-install-ubuntu-with-multiple-custom-partitions-on-your-dell-pc)

<img src="https://ithelp.ithome.com.tw/upload/images/20220916/20127129MHHjCamQFs.jpg" width="600" height="400">

<img src="https://ithelp.ithome.com.tw/upload/images/20220916/20127129VBdZGt2SSF.jpg" width="600" height="400">

<img src="https://ithelp.ithome.com.tw/upload/images/20220916/201271292neSSiz7s5.jpg" width="600" height="400">

## Step11: 選取地圖上最接近您的位置，或在文字方塊內輸入，然後按一下繼續。可以偵測鍵盤設定取得協助。

## Step12: Who are you ? 畫面視窗 隨即出現。需要輸入您的資訊。

<img src="https://ithelp.ithome.com.tw/upload/images/20220916/20127129NIXRT5LDXe.jpg" width="600" height="400">

## Step13: 安裝精靈完成後，您會看到安裝已完成訊息視窗。按一下右上角 立即重新開機。

<img src="https://ithelp.ithome.com.tw/upload/images/20220916/20127129zecWQMVsxo.jpg" width="600" height="400">

## Step14: 設定開機順序

### 1. 預設開機作業系統為 Ubuntu。這表示如果您按下 Enter 鍵或等待 10 秒，系統會直接開機至 Ubuntu。
### 2. 如果您要變更為 Windows 安裝，請重新開機電腦，然後從 GRUB 功能表選擇 Windows 磁碟分割。

# Reference
[如何透過 Windows 11 為您的 Dell 電腦以雙重開機安裝 Ubuntu 和 Windows 8](https://www.dell.com/support/kbdoc/zh-tw/000131253/%E5%A6%82%E4%BD%95-%E7%82%BA-%E6%82%A8%E7%9A%84-dell-%E9%9B%BB%E8%85%A6-%E4%BB%A5-%E9%9B%99%E9%87%8D%E9%96%8B%E6%A9%9F-%E5%AE%89%E8%A3%9D-ubuntu-%E5%92%8C-windows-8-%E6%88%96-10?lang=tw)

## UEFI 安裝需要哪些 BIOS 設定？  

### 在啟動時按下 F2 鍵進入 BIOS。確定 BIOS 設為 UEFI，並停用傳統選項 ROM，亦停用安全開機。

<img src="https://supportkb.dell.com/img/ka06P000000Xxo6QAC/ka06P000000Xxo6QAC_zh_TW_4.jpeg" width="500" height="400">

<img src="https://supportkb.dell.com/img/ka06P000000Xxo6QAC/ka06P000000Xxo6QAC_zh_TW_5.jpeg" width="500" height="400">

<img src="https://supportkb.dell.com/img/ka06P000000Xxo6QAC/ka06P000000Xxo6QAC_zh_TW_6.jpeg" width="500" height="400">


* []()

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


