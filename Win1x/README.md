Table of Contents
=================

   * [Table of Contents](#table-of-contents)
   * [Purpose](#purpose)
   * [話題沸騰中の Windows11(Insider Preview版) をHyper-Vにインストールする方法](#話題沸騰中の-windows11insider-preview版-をhyper-vにインストールする方法)
      * [必要なもの](#必要なもの)
      * [事前準備1 Hyper-Vをインストールする](#事前準備1-hyper-vをインストールする)
      * [事前準備2 Windows Insider Program に登録する](#事前準備2-windows-insider-program-に登録する)
      * [ISOをダウンロード](#isoをダウンロード)
      * [仮想マシンの作成](#仮想マシンの作成)
      * [Windows10をインストール](#windows10をインストール)
      * [Windows11に更新](#windows11に更新)
   * [Troubleshooting](#troubleshooting)
   * [Reference](#reference)
   * [h1 size](#h1-size)
      * [h2 size](#h2-size)
         * [h3 size](#h3-size)
            * [h4 size](#h4-size)
               * [h5 size](#h5-size)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)

# Purpose
Take a note of Win11 stuffs.


# 話題沸騰中の Windows11(Insider Preview版) をHyper-Vにインストールする方法
[話題沸騰中の Windows11(Insider Preview版) をHyper-Vにインストールする方法](https://qiita.com/TiggeZaki/items/6f1d70d345a4e02ab27b#%E4%BA%8B%E5%89%8D%E6%BA%96%E5%82%991-hyper-v%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B)

## 必要なもの  
```
    Windows10がインストール済みのPC（ホストOS用）
    Windows10のライセンス（ゲストOS用）　ぶっちゃけアプリの動作確認程度の目的だったら必要ない
    Hyper-V（インストールしてない場合は事前準備1）
    Windows Insider Programに登録済みのMSアカウント（持ってない場合は事前準備2）
```

## 事前準備1 Hyper-Vをインストールする  
```
nable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
```

```
インストールできたらWindows10を再起動してください。
（この記事ではWindows10 Pro前提で書いていますが一応Windows10 Homeでもこれとは違う方法でHyper-Vをインストールすることはできます。）
```

## 事前準備2 Windows Insider Program に登録する  
[Windows Insider Program](https://insider.windows.com/ja-jp/getting-started)
```
上のリンクからWindows Insider Programに登録してください。
これはあくまでもWindows Insider Previewの Dev チャネルのISOファイルをダウンロードするための登録なので
MicrosoftアカウントとWindows 10のアカウントを関連付ける必要はありません。
```

## ISOをダウンロード  

## 仮想マシンの作成  
<img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F807403%2F64628a07-e68c-c7fe-69ee-a01682cd6d45.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=0ebc5da3ba3cecefa1c43d98a6f29819" width="300" height="300">  
```
```


<img src="https://camo.qiitausercontent.com/a55c8e00fc8f2e1ed0927650d2f39d0f3ba00f6b/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e61702d6e6f727468656173742d312e616d617a6f6e6177732e636f6d2f302f3830373430332f38613964356531372d396463312d343161302d373063322d6665616465363535383632642e706e67" width="700" height="500">  
```
```

<img src="https://camo.qiitausercontent.com/55a70f6e9d569dacff43c362e148e204a690b193/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e61702d6e6f727468656173742d312e616d617a6f6e6177732e636f6d2f302f3830373430332f63613238303339382d613536302d393761612d663637652d6636663039333535623862382e706e67" width="700" height="500">  
```
```


## Windows10をインストール  
<img src="" width="400" height="500">  


## Windows11に更新  
```
Windows10のインストールが完了できたら後は簡単です。
Windows+Iキーを押して設定（コントロール パネルではない方）を開き
[更新とセキュリティ]->[Windows Update]から更新プログラムをチェックを押してください。
上手く行っていればWindows 11 Insider Previewが降ってくるはずです。
```

<img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F807403%2F95ba4369-a2c1-07f0-05b9-4835dea0f1b0.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=e989150f8d8de1ea040bce2639263fd9" width="700" height="500">  

# Troubleshooting


# Reference

 


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


