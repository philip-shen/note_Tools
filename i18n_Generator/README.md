Table of Contents
=================

   * [Purpose](#purpose)
   * [Original](#original)
   * [Google Sheet](#google-sheet)
   * [VS_Code antfu /i18n-ally](#vs_code-antfu-i18n-ally)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)


# Purpose
Take note of i18n Generator

# Original  
```
王智永

各位前端大大、行銷大大，大家好！
小弟想請教有關 i18n 有沒有好用的編輯器！
因為需要製作多國語言，因此我現在有「繁體中文」、「英文」、「越南文」三種語系
其中「英文」、「越南文」需要參照「繁體中文」給行銷進行翻譯，翻譯完成之後還需要能匯出 JSON 覆蓋回 source code
因此需要「專門處理 i18n 的編輯器」
那小弟我目前是使用 POEditor
可是 POEditor 有分方案，你頁面越多，翻譯越多，每個月要付的錢就越多！
小弟我目前是 Start Plan 每個月 15 美，因為我最近開發頁面越來越多，眼看每個月要付的錢可能越來越多，應該一下子就會到 Enterprise Plan 了
因此上來請教各位大大，有沒有好用推薦的 i18n 編輯器，能跟行銷完美配合，甚至又更便宜的呢？
謝謝各位大大！
```

```
可以考慮用 https://poedit.net？只是需要在 json 和 PO 之間做轉檔
```

```
有考慮自架的話，可以看看 weblate
```

# Google Sheet  

```
乃綠茶
Google 試算表 ，然後寫nodejs抓下來轉成json
行銷人員也不用重學，權限google也搞定10

王智永
作者
對呀，這應該最棒的方式了，還有版控和協作功能，我在跟同事討論看看好了！！

Neil Lin
我們 team 幾年前也改成這種方式
一份 google excel 轉出不同格式檔案,
用sheet分辨共用或不共用
前端.json
後端 properties 

陳典佑
我也都這樣做 缺點是沒有版本控制 比較麻煩
應該說不好跟隨環境版控
```
[i18n-generator](https://www.npmjs.com/package/i18n-generator?fbclid=IwAR1KpkTwc_msnaaoLpT8ERkLVtAZHnZ_EtglXHcpYkfr5g1aShAKkIjaJso)  

```
推這個 https://www.codeandweb.com/babeledit
```

```
Lokalise 推推！
功能蠻多的，可以很簡單的把不同語言的翻譯工作分配給多位翻譯人員。
另外可以接他們的 API 拉翻譯 ( json ) 下來，看是直接用 REST 請求或用他們的 Node API ( 支援 TypeScript )。
```
[Lokalise](https://lokalise.com/pricing)


```
Nathan Chang
願意自架的話，也可以參考一下這個幾年前的拙作: https://github.com/chejen/keys-translations-manager，
它除了可以管理翻譯外，也可以線上匯出 nested JSON, flat JSON, properties, CSV 等格式，也有支援 CLI 及基本的 rest api 可用 🙂
```

# VS_Code antfu /i18n-ally  

```
VS Code 有外掛可以支援你的需求 https://github.com/antfu/i18n-ally
```
[ antfu /i18n-ally ](https://github.com/antfu/i18n-ally)


* []()  

![alt tag]()  
![alt tag]()  

![alt tag]()  

![alt tag]()  

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