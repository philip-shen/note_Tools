Table of Contents
=================

   * [Table of Contents](#table-of-contents)
   * [Purpose](#purpose)
   * [Markdown ABC](#markdown-abc)
      * [Block](#block)
      * [Table](#table)
   * [Publish by Markdown](#publish-by-markdown)
   * [Markdown TOC](#markdown-toc)
      * [[步驟一] 點選擴充功能按鈕](#步驟一-點選擴充功能按鈕)
      * [[步驟二] 搜尋『Markdown Toc』，找到Markdown Toc，點選安裝。](#步驟二-搜尋markdown-toc找到markdown-toc點選安裝)
      * [[步驟三] 點選『重新載入』。](#步驟三-點選重新載入)
      * [生成目錄](#生成目錄)
      * [結果](#結果)
   * [Markdown TOC on GitHub - 01](#markdown-toc-on-github---01)
      * [Installation-Linux (manual installation)](#installation-linux-manual-installation)
      * [Usage](#usage)
         * [STDIN](#stdin)
         * [Local files](#local-files)
         * [Remote files](#remote-files)
   * [Markdown TOC on GitHub - 02](#markdown-toc-on-github---02)
      * [Usage](#usage-1)
   * [Markdown to PDF](#markdown-to-pdf)
      * [PlantUML](#plantuml)
      * [CSV](#csv)
      * [Prince 輸出PDF](#prince-輸出pdf)
   * [Markdown to CSV/TSV](#markdown-to-csvtsv)
      * [Markdown Convert](#markdown-convert)
   * [Troubleshooting](#troubleshooting)
   * [Reference](#reference)
   * [h1 size](#h1-size)
      * [h2 size](#h2-size)
         * [h3 size](#h3-size)
            * [h4 size](#h4-size)
               * [h5 size](#h5-size)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)


# Purpose  
Take note of Markdown  


# Markdown ABC  
[markdown風格· GIT教學 - kingofamani ](https://kingofamani.gitbooks.io/git-teach/content/chapter_6_gitbook/markdown.html)  

## Block  
小區塊用1個反引號(`)   

大區塊用3個反引號(```)    

`
小區塊
`

```
大區塊
```

多行區塊用大於符號(>)

## Table  
```
| Left-Aligned  | Center Aligned  | Right Aligned |
| :------------ |:---------------:| -----:|
| col 3 is      | some wordy text | $1600 |
| col 2 is      | centered        |   $12 |
| zebra stripes | are neat        |    $1 |
| test | 測試        |    $3333 |
```

| Left-Aligned  | Center Aligned  | Right Aligned |
| :------------ |:---------------:| -----:|
| col 3 is      | some wordy text | $1600 |
| col 2 is      | centered        |   $12 |
| zebra stripes | are neat        |    $1 |
| test | 測試        |    $3333 |


# Publish by Markdown  
[使用 Markdown 來發文章吧! Dec 01 Fri 2017](https://j796160836.pixnet.net/blog/post/45509889-%e4%bd%bf%e7%94%a8-markdown-%e4%be%86%e7%99%bc%e6%96%87%e7%ab%a0%e5%90%a7%21)

```
現在有一個新的流程 -- 使用 Markdown
用 MacDown 編寫 Markdown 文字內容，然後用 Export > HTML... 的方式，將 Markdown 文件轉成 HTML 語法（含預設的CSS）
然後在所見即所得 (WYSIWYG) 編輯器裡適時的加上圖片、設定文字顏色、超連結...等。

```
[MacDown 軟體下載](https://macdown.uranusjr.com/)


# Markdown TOC  
[[Markdown] 使用Markdown Toc生成目錄 Aug 7, 2018](https://dotblogs.com.tw/yitingblog/2018/08/07/144059)  
## [步驟一] 點選擴充功能按鈕  
![alt tag](https://dotblogsfile.blob.core.windows.net/user/yiting/0523ccc9-be64-4e51-b462-b28c65fe66e3/1533616010_07189.png)  

## [步驟二] 搜尋『Markdown Toc』，找到Markdown Toc，點選安裝。  
![alt tag](https://dotblogsfile.blob.core.windows.net/user/yiting/0523ccc9-be64-4e51-b462-b28c65fe66e3/1533621231_47384.png)  

## [步驟三] 點選『重新載入』。   
![alt tag](https://dotblogsfile.blob.core.windows.net/user/yiting/0523ccc9-be64-4e51-b462-b28c65fe66e3/1533623020_05707.png)  

## 生成目錄  
![alt tag](https://dotblogsfile.blob.core.windows.net/user/yiting/0523ccc9-be64-4e51-b462-b28c65fe66e3/1533623355_16844.png)  

## 結果  
![alt tag](https://dotblogsfile.blob.core.windows.net/user/yiting/0523ccc9-be64-4e51-b462-b28c65fe66e3/1533623447_01461.png)  


# Markdown TOC on GitHub - 01   
[ekalinin /github-markdown-toc](https://github.com/ekalinin/github-markdown-toc)  
## Installation-Linux (manual installation)    
```
$ wget https://raw.githubusercontent.com/ekalinin/github-markdown-toc/master/gh-md-toc
$ chmod a+x gh-md-toc
```
## Usage  
### STDIN  
```
➥ cat ~/projects/Dockerfile.vim/README.md | ./gh-md-toc -
  * [Dockerfile.vim](#dockerfilevim)
  * [Screenshot](#screenshot)
  * [Installation](#installation)
        * [OR using Pathogen:](#or-using-pathogen)
        * [OR using Vundle:](#or-using-vundle)
  * [License](#license)
```

### Local files  
```
➥ ./gh-md-toc ~/projects/Dockerfile.vim/README.md                                                                                                                                                Вс. марта 22 22:51:46 MSK 2015

Table of Contents
=================

  * [Dockerfile.vim](#dockerfilevim)
  * [Screenshot](#screenshot)
  * [Installation](#installation)
        * [OR using Pathogen:](#or-using-pathogen)
        * [OR using Vundle:](#or-using-vundle)
  * [License](#license)
```

### Remote files  
```
➥ ./gh-md-toc https://github.com/ekalinin/envirius/blob/master/README.md

Table of Contents
=================

  * [envirius](#envirius)
    * [Idea](#idea)
    * [Features](#features)
  * [Installation](#installation)
  * [Uninstallation](#uninstallation)
  * [Available plugins](#available-plugins)
  * [Usage](#usage)
    * [Check available plugins](#check-available-plugins)
    * [Check available versions for each plugin](#check-available-versions-for-each-plugin)
    * [Create an environment](#create-an-environment)
    * [Activate/deactivate environment](#activatedeactivate-environment)
      * [Activating in a new shell](#activating-in-a-new-shell)
      * [Activating in the same shell](#activating-in-the-same-shell)
    * [Get list of environments](#get-list-of-environments)
    * [Get current activated environment](#get-current-activated-environment)
    * [Do something in environment without enabling it](#do-something-in-environment-without-enabling-it)
    * [Get help](#get-help)
    * [Get help for a command](#get-help-for-a-command)
  * [How to add a plugin?](#how-to-add-a-plugin)
    * [Mandatory elements](#mandatory-elements)
      * [plug_list_versions](#plug_list_versions)
      * [plug_url_for_download](#plug_url_for_download)
      * [plug_build](#plug_build)
    * [Optional elements](#optional-elements)
      * [Variables](#variables)
      * [Functions](#functions)
    * [Examples](#examples)
  * [Example of the usage](#example-of-the-usage)
  * [Dependencies](#dependencies)
  * [Supported OS](#supported-os)
  * [Tests](#tests)
  * [Version History](#version-history)
  * [License](#license)
  * [README in another language](#readme-in-another-language)
```


# Markdown TOC on GitHub - 02  
[GitHub 上の Markdown が TOC(目次) を表示してくれないのでどうしようか → ツール自製したよって話 Jul 27, 2017](https://qiita.com/sta/items/9481c94e0fc36f27fa92)  
[stakiran /test_anchor_rendering](https://github.com/stakiran/test_anchor_rendering)  
[stakiran /intoc](https://github.com/stakiran/intoc/tree/d541b893f36fedf3f772fdbacdd6cd8c77891889)  
> Generate a markdown TOC for a README or any GFM files.  

> Requirement  
* Python 2.7
* Windows7+ 

## Usage  
```
$ python intoc.py -i intoc.md --indent-depth 4 --parse-depth 2
- [intoc](#intoc)
    - [Install](#install)
    - [CLI](#cli)
    - [Info](#info)
```





[GitHubのREADME.mdにシーケンス図を埋め込む May 22, 2019](https://qiita.com/takke/items/86a5ddf145cf9693b6e9)  
[Markdown に gist を参照するプロキシ URL を画像として埋め込む](https://qiita.com/takke/items/86a5ddf145cf9693b6e9#markdown-%E3%81%AB-gist-%E3%82%92%E5%8F%82%E7%85%A7%E3%81%99%E3%82%8B%E3%83%97%E3%83%AD%E3%82%AD%E3%82%B7-url-%E3%82%92%E7%94%BB%E5%83%8F%E3%81%A8%E3%81%97%E3%81%A6%E5%9F%8B%E3%82%81%E8%BE%BC%E3%82%80) 
> Markdown に下記のように記述します。  
```
![sequence dialog](http://www.plantuml.com/plantuml/proxy?src=https://gist.githubusercontent.com/takke/995d474a8ad72a724c8187cf21b1e238/raw)
https://gist.github.com/takke/995d474a8ad72a724c8187cf21b1e238
```
![alt tag](https://qiita-user-contents.imgix.net/http%3A%2F%2Fwww.plantuml.com%2Fplantuml%2Fproxy%3Fsrc%3Dhttps%3A%2F%2Fgist.githubusercontent.com%2Ftakke%2F995d474a8ad72a724c8187cf21b1e238%2Fraw?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&s=1cc14e918ab5d3e3cbcd978c69fe35eb)  


# Markdown to PDF  
[用筆記也可以管理專案(二)：Markdown Preview Enhanced 017/12/13](https://jonny-huang.github.io/projects/02_markdown_preview_enhanced/)  
[安裝 Markdown Preview Enhanced](https://jonny-huang.github.io/projects/02_markdown_preview_enhanced/#%E5%AE%89%E8%A3%9D-Markdown-Preview-Enhanced)  
[匯出 PDF](https://jonny-huang.github.io/projects/02_markdown_preview_enhanced/#%E5%8C%AF%E5%87%BA-PDF)  
## PlantUML  
[PlantUML](https://jonny-huang.github.io/projects/02_markdown_preview_enhanced/#PlantUML)  
```
但是筆者則採用 @import 方式將外部 UML 模型檔(.puml)嵌入進來，這樣 UML 模型就可以獨立維護。
```
![alt tag](https://jonny-huang.github.io/images/projects/markdown_preview_enhanced/mpe_43.png)  

![alt tag](https://jonny-huang.github.io/images/projects/markdown_preview_enhanced/mpe_44.png)  

## CSV  
[CSV](https://jonny-huang.github.io/projects/02_markdown_preview_enhanced/#CSV)  
![alt tag](https://jonny-huang.github.io/images/projects/markdown_preview_enhanced/mpe_47.png)  

```
要注意的是因為 Markdown 會轉換成 HTML，所以會將 csv 檔採用 UTF-8 方式編碼，但是透過 Excel 開啟預設便會出現亂碼。

但是如果是透過 LibreOffie 的 Calc 開啟時，只要先指定字元集為 UTF-8 便可正常開啟與編輯。
```
![alt tag](https://jonny-huang.github.io/images/projects/markdown_preview_enhanced/mpe_48.png)  

![alt tag](https://jonny-huang.github.io/images/projects/markdown_preview_enhanced/mpe_46.png)  


[安裝擴充功能：Excel Viewer (選擇性)](https://jonny-huang.github.io/projects/02_markdown_preview_enhanced/#%E5%AE%89%E8%A3%9D%E6%93%B4%E5%85%85%E5%8A%9F%E8%83%BD%EF%BC%9AExcel-Viewer-%E9%81%B8%E6%93%87%E6%80%A7)



[Visual Studio Code 寫文檔或文章必裝的外掛Markdown Preview Enhanced 2020年4月22日](https://aishuafei.com/markdown-preview-enhanced/)  
## Prince 輸出PDF  
```
1. 安裝 Prince

    下載 ：https://www.princexml.com/download/
    選擇你的電腦的位元安裝下載。

2. 設定環境變數
新增：C:\Program Files (x86)\Prince\engine\bin
```
![alt tag](https://i2.wp.com/aishuafei.com/wp-content/uploads/image-1587556618066.png?w=900&ssl=1)  

```
3.markdown設定輸出格式
在要輸出的md格式檔案開頭輸入，官方文檔說明
```
![alt tag](https://i2.wp.com/aishuafei.com/wp-content/uploads/image-1587556744869.png?w=900&ssl=1)  

```
4.輸出
對預覽的markdown文件右鍵選擇 PDF
```

# Markdown to CSV/TSV  
[(Multi)Markdown table to CSV/TSV ](https://stackoverflow.com/questions/15521912/multimarkdown-table-to-csv-tsv)  

ou can use [tomroy/mdtable2csv](https://github.com/tomroy/mdtable2csv).
```
$ mdtable2csv <filename>.md
```

## Markdown Convert  
[从一个表格中生成Markdown](https://markdown-convert.com/zh/tool/table)  
```
从Excel、CSV和SQL结果等表格格式中生成Markdown表。
```
 
# Troubleshooting


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


