Table of Contents
=================

   * [Table of Contents](#table-of-contents)
   * [Notes of Google Sheet](#notes-of-google-sheet)
   * [Table of Content](#table-of-content)
   * [Dependent Drop-Down Lists in Google Sheets](#dependent-drop-down-lists-in-google-sheets)
      * [Step1 把分類打在一 分頁上](#step1-把分類打在一-分頁上)
      * [Step2](#step2)
      * [Step3](#step3)
      * [Step4](#step4)
      * [Step5](#step5)
      * [Step6](#step6)
      * [Step7](#step7)
      * [Step8](#step8)
      * [Step9](#step9)
      * [EXCEL 製作下拉式選單 教學－STEP1.定義名稱](#excel-製作下拉式選單-教學step1定義名稱)
      * [EXCEL 製作多層下拉式選單 教學－STEP2.產生選單](#excel-製作多層下拉式選單-教學step2產生選單)
         * [第一層下拉選單](#第一層下拉選單)
         * [第二層下拉式選單(Google 試算表版)](#第二層下拉式選單google-試算表版)
         * [第三層下拉式選單(Google 試算表版)](#第三層下拉式選單google-試算表版)
   * [如何統計Google表格中某列的出現次數？](#如何統計google表格中某列的出現次數)
   * [Google Sheet refers from Google Sheet](#google-sheet-refers-from-google-sheet)
      * [IMPORTRANGE使用方式](#importrange使用方式)
      * [步驟一：複製想要同步的主要試算表網址](#步驟一複製想要同步的主要試算表網址)
      * [步驟二：前往其他試算表輸入IMPORTRANGE公式](#步驟二前往其他試算表輸入importrange公式)
      * [步驟三：點擊允許存取](#步驟三點擊允許存取)
      * [如果要同步該試算表的特定分頁呢？](#如果要同步該試算表的特定分頁呢)
   * [Google Sheet 如何調整儲存格的最適欄寬及欄高？](#google-sheet-如何調整儲存格的最適欄寬及欄高)
      * [1](#1)
      * [2](#2)
      * [3](#3)
      * [4](#4)
      * [5](#5)
      * [6](#6)
   * [Reference](#reference)
   * [h1 size](#h1-size)
      * [h2 size](#h2-size)
         * [h3 size](#h3-size)
            * [h4 size](#h4-size)
               * [h5 size](#h5-size)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)


# Notes of Google Sheet
Take a note of Google Sheet

# Table of Content  
[Dependent Drop-Down Lists in Google Sheets](#dependent-drop-down-lists-in-google-sheets)   
[如何統計Google表格中某列的出現次數？](#%E5%A6%82%E4%BD%95%E7%B5%B1%E8%A8%88google%E8%A1%A8%E6%A0%BC%E4%B8%AD%E6%9F%90%E5%88%97%E7%9A%84%E5%87%BA%E7%8F%BE%E6%AC%A1%E6%95%B8)  

# Dependent Drop-Down Lists in Google Sheets  
[║Google試算表╠ 多層下拉選單 ╣ 要幾層就有幾層 ? Feb 19, 2019](https://eillen810123.pixnet.net/blog/post/457533353#comment-125439269)   
## Step1 把分類打在一 分頁上  
![alt tag](https://pic.pimg.tw/eillen810123/1487507456-555205031_n.png)
## Step2  
![alt tag](https://pic.pimg.tw/eillen810123/1487507458-1990448768_n.png)
## Step3   
![alt tag](https://pic.pimg.tw/eillen810123/1487507460-1303619108_n.png)
## Step4  
![alt tag](https://pic.pimg.tw/eillen810123/1487507461-3897717356_n.png)
## Step5  
![alt tag](https://pic.pimg.tw/eillen810123/1487507462-1235160736_n.png)
## Step6  
![alt tag](https://pic.pimg.tw/eillen810123/1487507465-415523979_n.png)
```
如果我下面這個指令只放一個，最多就是到兩層，如果多放一個，就會到第三層，依此類推...

    if (aColumn == 1 && aSheet.getName() == '範例檔') {
    var range = aSheet.getRange(aCell.getRow(), aColumn + 1);
    var sourceRange = SpreadsheetApp.getActiveSpreadsheet().getRangeByName(aCell.getValue());
    setDataValid_(range, sourceRange);
  }

```

## Step7  
![alt tag](https://pic.pimg.tw/eillen810123/1487507467-1865519817_n.png)
## Step8  
![alt tag](https://pic.pimg.tw/eillen810123/1487507472-3425474658_n.png)
## Step9  
![alt tag](https://pic.pimg.tw/eillen810123/1487507474-3528202300_n.png)


[製作Excel與Google試算表「下拉式選單」教學－單層&多層動態連動下拉選單。](https://www.pkstep.com/archives/16546)  
## EXCEL 製作下拉式選單 教學－STEP1.定義名稱  
(Google Excel試算表請到「資料」→「已命名範圍」)  

## EXCEL 製作多層下拉式選單 教學－STEP2.產生選單 
### 第一層下拉選單     
（Google Excel試算表請到「資料」→「驗證」→「範圍內的清單」）  
（Google Excel試算表輸入(EX.年級)）  
### 第二層下拉式選單(Google 試算表版)  
### 第三層下拉式選單(Google 試算表版)  

# 如何統計Google表格中某列的出現次數？  
[如何統計Google表格中某列的出現次數？](https://www.extendoffice.com/zh-TW/documents/excel/4707-google-sheets-count-number-of-occurrence.html)  
```
使用公式計算Google表格中某列的出現次數

您也可以應用以下公式來獲取結果。 請這樣做：

請輸入這個公式： = ArrayFormula（QUERY（A1：A16＆{“”，“”}，“select Col1，count（Col2）where Col1！=''col1 label count（Col2）'Count'”，1））） 放入要放置結果的空白單元格中，然後按 輸入 鍵，並且計算結果立即顯示，請參見截圖：

注意：在上面的公式中， A1：A16 是包含要計數的列標題的數據范圍。
```
![alt tag](https://www.extendoffice.com/images/stories/doc-excel/google-sheet/count-number-of-occurrence/xdoc-google-sheet-count-occurrence-4.png.pagespeed.ic.fMSoITL6Aw.png)

# Google Sheet refers from Google Sheet  
[別浪費時間複製貼上了！教你如何Google試算表同步於多個試算表資料 ](https://www.astralweb.com.tw/stop-wasting-your-time-on-copy-and-pasting-how-to-use-google-spreadsheet-to-sync-to-multiple-spreadsheets-tutorial/)  

## IMPORTRANGE使用方式  
[Google文件編輯器說明](https://support.google.com/docs/answer/3093340?hl=zh-Hant)  
<img src="https://www.astralweb.com.tw/wp-content/uploads/2020/03/image7-1.png" width="400" height="400">  

>講白了就是importrange(“試算表網址”, “資料範圍”)

```
要把A試算表同步到B,C,D試算表，就請在B,C,D試算表key入

=Importrange(“A試算表網址“,”資料範圍“)

重點：網址跟資料範圍都要用引號「 “ 」坐區隔，且兩者之間有一個逗點「 , 」

=importrange(“https://docs.google.com/spreadsheets/d/3345678rememberit3345678/edit#gid=0”,“A1:B5”)
```
## 步驟一：複製想要同步的主要試算表網址  
<img src="https://www.astralweb.com.tw/wp-content/uploads/2020/03/image8-2.png" width="500" height="400">  

## 步驟二：前往其他試算表輸入IMPORTRANGE公式  
```

    A試算表網址已複製起來 
    A試算表要同步的資料範圍為：A1:B5 

上面這兩個資料就足夠讓IMPORTRANGE知道，你要同步哪一個試算表（網址）以及哪一個範圍了（A1:B5）

所以前往B試算表再輸入欄位key入

=Importrange(“A試算表網址”,“資料範圍”）

=IMPORTRANGE(“https://docs.google.com/spreadsheets/d/1nokKrYrPj0wczZSyCVulX_FyreB9XvnRdyjv74-Gb9M/edit#gid=0″,”A1:B5“)

備註：網址是固定，請貼自己試算表的網址。
```
<img src="https://www.astralweb.com.tw/wp-content/uploads/2020/03/image5-1.png" width="500" height="400">  

## 步驟三：點擊允許存取  
```
在B試算表輸入IMPORTRANGE公式完成後，會看到#REF!的錯誤，請莫急莫慌莫害怕，你只要點擊允許存取，就會顯示A試算表的A1:B5的資料了。
```
<img src="https://www.astralweb.com.tw/wp-content/uploads/2020/03/image3-2.png" width="500" height="400">

```
這樣就設定完成囉，A試算表的A1:B5有任何更動，就會同步到Ｂ試算表。
```
<img src="https://www.astralweb.com.tw/wp-content/uploads/2020/03/image1-3.png" width="500" height="400">

```
後續只要依樣畫葫蘆，再把這段公式貼到其他試算表之後，只要A試算表的該欄位變更，其他試算表就會自動同步更新，是不是很方便呢？

請注意：要確保各個試算表都有取得權限，才能讓IMPORTRANGE做動。
```

## 如果要同步該試算表的特定分頁呢？ 
```
假設我要指定讓A試算表裡面的某一特定分頁的資料同步到別的試算表的話，只要在資料範圍做個調整就可以了

=Importrange(“A試算表網址”,“資料範圍”)

原本資料範圍我們是A1:B5，只要前面加分頁名稱與驚嘆號即可（分頁名稱是工作表3）
```
<img src="https://www.astralweb.com.tw/wp-content/uploads/2020/03/image2-2.png" width="300" height="200">

[Excel-Google試算表如何關聯到另一個試算表的內容 Apr 11 2016](https://isvincent.pixnet.net/blog/post/46090834-excel-google%E8%A9%A6%E7%AE%97%E8%A1%A8%E5%A6%82%E4%BD%95%E9%97%9C%E8%81%AF%E5%88%B0%E5%8F%A6%E4%B8%80%E5%80%8B%E8%A9%A6%E7%AE%97%E8%A1%A8%E7%9A%84%E5%85%A7)  
```
根據 Google 的說明：

https://support.google.com/docs/answer/3093340?hl=zh-Hant&rd=1

試算表必需明確取得權限，才能使用 IMPORTRANGE 函數自其他試算表擷取資料。
```
<img src="https://pic.pimg.tw/isvincent/1460381836-3067860420.png" width="500" height="500">

# Google Sheet 如何調整儲存格的最適欄寬及欄高？     
[【活用 Google試算表的技巧】如何調整儲存格的最適欄寬及欄高？ 2016年8月1日](https://www.techbang.com/posts/43775-tips-for-using-google-spreadsheet-how-to-adjust-the-optimal-column-width-of-the-cell-and-the-bar-higher)

## 1  
<img src="https://cdn2.techbang.com/system/images/349792/original/ca237101d62459a10ce126742c4e6c35.jpg?1464681485" width="400" height="300">  

## 2  
<img src="https://cdn0.techbang.com/system/images/349793/original/877ca06d0b63b58fb3bb1e72d99c3338.jpg?1464681485" width="400" height="300">  

## 3  
<img src="https://cdn0.techbang.com/system/images/349794/original/fd8ca8a57042f0d3e37679826a8d3ea7.jpg?1464681486" width="400" height="300">  

## 4  
<img src="https://cdn1.techbang.com/system/images/349795/original/38e8d1c0ad08b3d3930ba69feff5e06e.jpg?1464681486" width="400" height="300">  

## 5  
<img src="https://cdn0.techbang.com/system/images/349796/original/df489f8b44699c5d4044bd3b9819f9ce.jpg?1464681487" width="400" height="300">

## 6  
<img src="https://cdn2.techbang.com/system/images/349797/original/2ed42b93d887aa8b1c8d38ea29340382.jpg?1464681487" width="400" height="300">


# Reference    
* [Google 試算表製作可執行 Apps Script 指令碼的(圖片)按鈕 Aug 11, 2018](https://www.wfublog.com/2018/08/google-spreadsheet-add-button-execute-apps-script.html)  


* []()  
![alt tag]()
<img src="" width="500" height="500">

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


