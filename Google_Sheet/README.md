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


# Reference    
* [Google 試算表製作可執行 Apps Script 指令碼的(圖片)按鈕 Aug 11, 2018](https://www.wfublog.com/2018/08/google-spreadsheet-add-button-execute-apps-script.html)  


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
