Table of Contents
=================

   * [Table of Contents](#table-of-contents)
   * [Purpose](#purpose)
   * [基本的な操作方法](#基本的な操作方法)
      * [Toolbar](#toolbar)
         * [Selection Tool](#selection-tool)
         * [Time Shift Tool](#time-shift-tool)
         * [選択範囲を少しずつだけ拡げれる--「SHIFT →」と「SHIFT ←」](#選択範囲を少しずつだけ拡げれる--shiftとshift)
         * [選択範囲を少しずつだけ狭めれる--「SHIFT Ctrl →」と「SHIFT Ctrl←」](#選択範囲を少しずつだけ狭めれる--shiftctrlとshiftctrl)
         * [First position of Seek Bar-- 「SHIFT J」](#first-position-of-seek-bar---shiftj)
         * [Last position of Seek Bar-- 「SHIFT K」](#last-position-of-seek-bar---shiftk)
   * [音源分割](#音源分割)
      * [Add Label at Selection-- 「Ctrl B」](#add-label-at-selection---ctrlb)
      * [Export Mulitple-- 「Ctrl Shift L」](#export-mulitple---ctrlshiftl)
      * [3Q_TimeShift_Label_Export-Multiple](#3q_timeshift_label_export-multiple)
   * [Clip Boundaries](#clip-boundaries)
      * [How to cut and move audio](#how-to-cut-and-move-audio)
      * [Removing silence](#removing-silence)
   * [Troubleshooting](#troubleshooting)
   * [Reference](#reference)
   * [h1 size](#h1-size)
      * [h2 size](#h2-size)
         * [h3 size](#h3-size)
            * [h4 size](#h4-size)
               * [h5 size](#h5-size)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)

# Purpose
Take note of Audacity  

# 基本的な操作方法  
[【Audacity】基本的な操作方法とメニュー等の説明②【初心者講座】 2016/5/28](http://audacity-mp3.xyz/menu-syousinnsya/)  
## Toolbar 
![alt tag](http://audacity-mp3.xyz/wp-content/uploads/2015/10/%E3%83%84%E3%83%BC%E3%83%AB%E3%83%90%E3%83%BC.png)  

### Selection Tool 
```
「選択範囲」を指定出来るツールです。カットしたりエフェクトをかけたりするのに使用します（かなり多用します）
```
![alt tag](http://audacity-mp3.xyz/wp-content/uploads/2015/10/%E9%81%B8%E6%8A%9E%E3%83%84%E3%83%BC%E3%83%AB.png)  
![alt tag](http://audacity-mp3.xyz/wp-content/uploads/2015/10/%E9%81%B8%E6%8A%9E%E3%83%84%E3%83%BC%E3%83%AB1.gif)  

### Time Shift Tool 
```
（タイムシフトツール）：クリップ（トラックを分割した際の1つ当たりの単位）を前後に移動する事が出来るツールです。
（かなり多用します）
```
![alt tag](http://audacity-mp3.xyz/wp-content/uploads/2015/10/%E3%82%BF%E3%82%A4%E3%83%A0%E3%82%B7%E3%83%95%E3%83%88%E3%83%84%E3%83%BC%E3%83%AB.png)  
![alt tag](http://audacity-mp3.xyz/wp-content/uploads/2015/10/%E3%82%BF%E3%82%A4%E3%83%A0%E3%82%B7%E3%83%95%E3%83%88%E3%83%84%E3%83%BC%E3%83%AB.gif)  

[【Audacity】不要な部分をカット･結合する方法④ 2016/5/28](https://audacity-mp3.xyz/katto-ketugou-huyou/)  
### 選択範囲を少しずつだけ拡げれる--「SHIFT+→」と「SHIFT+←」
```
「SHIFT+→」と「SHIFT+←」
```
![alt tag](http://audacity-mp3.xyz/wp-content/uploads/2015/10/%E9%81%B8%E6%8A%9E%E7%AF%84%E5%9B%B2%E3%82%92%E5%B0%91%E3%81%97%E3%81%9A%E3%81%A4%E3%81%A0%E3%81%91%E6%8B%A1%E3%81%92%E3%82%8B.gif)  

### 選択範囲を少しずつだけ狭めれる--「SHIFT+Ctrl+→」と「SHIFT+Ctrl←」
```
「SHIFT+Ctrl+→」と「SHIFT+Ctrl←」
```
![alt tag](http://audacity-mp3.xyz/wp-content/uploads/2015/10/%E9%81%B8%E6%8A%9E%E7%AF%84%E5%9B%B2%E3%82%92%E5%B0%91%E3%81%97%E3%81%9A%E3%81%A4%E3%81%A0%E3%81%91%E7%8B%AD%E3%82%81%E3%82%8B1.gif)  

### First position of Seek Bar-- 「SHIFT+J」 
```
「SHIFT+J」
```
![alt tag](http://audacity-mp3.xyz/wp-content/uploads/2015/10/%E3%82%B7%E3%83%BC%E3%82%AF%E3%83%90%E3%83%BC%E4%BD%8D%E7%BD%AE%E3%81%8B%E3%82%89%E6%9C%80%E5%88%9D%E3%81%BE%E3%81%A7%E6%8C%87%E5%AE%9A%EF%BC%9A%E3%80%8CSHIFT-J%E3%80%8D.gif)  

### Last position of Seek Bar-- 「SHIFT+K」    
```
「SHIFT+K」
```
![alt tag](http://audacity-mp3.xyz/wp-content/uploads/2015/10/%E3%82%B7%E3%83%BC%E3%82%AF%E3%83%90%E3%83%BC%E4%BD%8D%E7%BD%AE%E3%81%8B%E3%82%89%E6%9C%80%E5%BE%8C%E3%81%BE%E3%81%A7%E6%8C%87%E5%AE%9A%EF%BC%9A%E3%80%8CSHIFT-K%E3%80%8D.gif)  


# 音源分割  
[[カギ] Audacityで簡単に音源を分割してmp3にする方法 2014.05.11](http://usklog.net/archives/6041)  
```
1時間以上の長い時間録音した場合に”10分ごと”など一定時間で
細切れに分割する方法を探していたらヘルプページに分かり易い説明があった。
```
> やってみたら案外簡単だったのだけど、また忘れそうなのでメモ。

```
これで音源の頭(00h00m00s)から12分間が選択されている。
```
![alt tag](https://i2.wp.com/usklog.net/wp-content/uploads/2014/05/Audacity-03.png)  


```
次の12分間を選択したい場合には「選択開始」を00h12m00sに変更するだけ
(長さは00h12m00sのままなので12分目から次の12分間、
つまり24分目までが選択される)。
```
![alt tag](https://i1.wp.com/usklog.net/wp-content/uploads/2014/05/Audacity-04.png)  

![alt tag](https://i1.wp.com/usklog.net/wp-content/uploads/2014/05/Audacity-05.png)  

![alt tag](https://i1.wp.com/usklog.net/wp-content/uploads/2014/05/Audacity-06.png)  

![alt tag](https://i1.wp.com/usklog.net/wp-content/uploads/2014/05/Audacity-07.png)  
> 24分目から次の12分間が選択された  

```
この数値入力による対象選択と、さっきの複数トラックに分ける操作を組み合わせたら、
簡単に1つの長い音源ファイルを細切れにすることができる。
```
## Add Label at Selection-- 「Ctrl+B」   
![alt tag](https://i1.wp.com/usklog.net/wp-content/uploads/2014/05/Audacity-08.png)  
> 対象を選択したうえで「選択範囲にラベルを付ける」を選択  

![alt tag](https://i1.wp.com/usklog.net/wp-content/uploads/2014/05/Audacity-09.png)  
> “ラベルトラック”の帯が出て、名前を入力ができるようになる  

![alt tag](https://i1.wp.com/usklog.net/wp-content/uploads/2014/05/Audacity-10.png)  
> 単純に”01″と設定した  

![alt tag](https://i1.wp.com/usklog.net/wp-content/uploads/2014/05/Audacity-11.png)  
> 選択開始を00h12m00sに変えて2つ目の12分間を選択してラべリング

![alt tag](https://i1.wp.com/usklog.net/wp-content/uploads/2014/05/Audacity-12.png)  
> 真ん中を”終了”に変えて選択もできる  

![alt tag](https://i1.wp.com/usklog.net/wp-content/uploads/2014/05/Audacity-13.png)  
> 1時間12分目から12分間を選択したことと同じになる  

```
それぞれを選択してラべリングを終えたら「複数ファイルの書き出し」を選択するだけ。
```
## Export Mulitple-- 「Ctrl+Shift+L」   
![alt tag](https://i1.wp.com/usklog.net/wp-content/uploads/2014/05/Audacity-14.png)  
> 「複数ファイルの書き出し」を選択  

![alt tag](https://i1.wp.com/usklog.net/wp-content/uploads/2014/05/Audacity-15.png)  
> 書き出し形式などを設定して”書き出し”ボタンを押す  

## 3Q_TimeShift_Label_Export-Multiple  

Items  | start	actual | duration | Add Label at Selection-- 「Ctrl+B」 | Remark
------------------------------------ | --------------------------------------------- | ----------------------------------- | --------------------------------------------- | ----------------------------------- 
1 | 0:00:00 | 00:00:00.000 | 00:00:00.000	 |  
2 | 0:01:36 | 00:01:36.261 | 0:01:35 | Star and Length of Selection 
3 | 0:03:11 | 00:03:11.261 | 0:01:38 | Star and Length of Selection
4 | 0:04:49 | 00:04:48.921 | 0:01:38 | Star and Length of Selection
5 | 0:06:27 | 00:06:27.358 | 0:01:37 | Star and Length of Selection
6 | 0:08:04 | 00:08:04.336 | 0:01:38 | Star and Length of Selection
7 | 0:09:43 | 00:09:42.688 | 0:01:38 | Star and Length of Selection
8 | 0:11:20 | 00:11:20.382 | 0:01:37 | Star and Length of Selection
9 | 0:12:58 | 00:12:57.531 | 0:01:37 | Star and Length of Selection
10 | 0:14:35 | | | 

![alt tag](https://i.imgur.com/lt8LnHA.png)  

![alt tag](https://i.imgur.com/Kmg2aTC.png)  

![alt tag](https://i.imgur.com/tw6rjGx.png)  


# Macro  
[複数の音声ファイルをまとめて処理する（マクロ）2020.09.25](https://czmemo.com/audacity/#toc14)  
## １．ツールバーの[道具箱]にある[マクロ]を選択します。
<img src="https://czmemo.com/wp-content/uploads/2020/07/2020-07-12-21_03_56-min.png" width="200" height="100">

## ２．[新規ボタン]をクリックします。 
<img src="https://czmemo.com/wp-content/uploads/2020/07/85c7e3b0124f54767bd7f6006ff8f25a.png" width="400" height="500">

```
すると、以下のダイアログが表示されるので、今回は「無音部分の短縮」と入力し、[OKボタン]をクリックします。
```
<img src="https://czmemo.com/wp-content/uploads/2020/07/f7b1b719e2d685e09fbdab0816a16136.png" width="200" height="100">

## ３．今回追加したマクロを選択し、[挿入ボタン]をクリックします。
<img src="https://czmemo.com/wp-content/uploads/2020/07/2ab77dcd56e06fc73c0074db66ed35b5.png" width="600" height="400">

```
「無音の切り詰め」コマンドを選択し、[OKボタン]をクリックします。
```
<img src="https://czmemo.com/wp-content/uploads/2020/07/733af37f31551caefc878b1b93686eb8.png" width="400" height="500">

##  ４．編集ステップの「01 無音の切り詰め」を選択し、[編集ボタン]をクリックします。  
<img src="https://czmemo.com/wp-content/uploads/2020/07/dbc302aca595a55d7d44f9df028f6bb9.png" width="400" height="500">

```
下記のダイアログで切り詰め条件を設定します。設定したら[OKボタン]をクリックします。
```
<img src="https://czmemo.com/wp-content/uploads/2020/07/08b76dc37606c423b85d10b1381cbfd2.png" width="200" height="400"> 

##  ５．編集ステップの「02 – 終了 -」を選択し、[挿入ボタン]をクリックします。
<img src="https://czmemo.com/wp-content/uploads/2020/07/90b38c8e8422d457c4eea82b8cba33b7.png" width="600" height="300"> 

```
「MP3として書き出し」コマンドを選択し、[OKボタン]をクリックします。
```
<img src="https://czmemo.com/wp-content/uploads/2020/07/c8ea9cc9014abb86e02e90c93539ae7e.png" width="600" height="400"> 

##  ６．[OKボタン]をクリックで、マクロの作成が完了です！
<img src="https://czmemo.com/wp-content/uploads/2020/07/5c10e2e5ce6a2767d1a0607b846a24a0.png" width="600" height="400">  

##  ７．ここからマクロの実行になります。　ツールバーの[道具箱] > [マクロの適用] > [パレット]をクリックします。
<img src="https://czmemo.com/wp-content/uploads/2020/07/2020-07-12-21_43_51-Part1_1-min.png" width="400" height="200">  

##  ８．「無音部分の短縮」マクロを選択し、[ファイルボタン]をクリックします。
```
※ここで「先に現在のプロジェクトを保存して閉じてください。」とメッセージが出たら、
　　　今開いているファイルを全部閉じてから再実行してください。
```
<img src="https://czmemo.com/wp-content/uploads/2020/07/ed6f8e2b771a56ee5b1b81df7039a09d.png" width="200" height="400">

##  ９．処理を行いたいファイルをまとめて選択し、[開くボタン]をクリックします。
<img src="https://czmemo.com/wp-content/uploads/2020/07/fa77f2e05dbc101ec5ef5e0051646c3c.png" width="600" height="300">

##  １０．書き出しが始まるので、終わるまで待ちましょう。処理したファイルが「macro-output」フォルダに作られています。
<img src="https://czmemo.com/wp-content/uploads/2020/07/2020-07-12-21_46_21-Part1_3-min.png" width="200" height="200">

[2 mp3再生速度一括倍速変換の事前準備](https://affikatsu.com/mp3-double-speed-conversion-soft-7331/#mp3)  
```
01 変更:テンポの変更
02 MP3として書き出し
03 終了
```
<img src="https://affikatsu.com/wp-content/uploads/2015/09/7331-b01-Audacity%E3%81%AE%E9%81%93%E5%85%B7%E7%AE%B1%E3%81%AE%E3%83%9E%E3%82%AF%E3%83%AD.png" width="200" height="300">  

<img src="" width="400" height="500">

<img src="" width="400" height="500">

<img src="" width="400" height="500">

<img src="" width="400" height="500">

<img src="" width="400" height="500">

<img src="" width="400" height="500">


[3 mp3再生速度一括倍速変換](https://affikatsu.com/mp3-double-speed-conversion-soft-7331/#mp3-2)  


# Clip Boundaries  
[Audacity 2.0.3多重剪輯音樂 2013-08-18](https://blog.xuite.net/yh96301/blog/84507120-Audacity+2.0.3%E5%A4%9A%E9%87%8D%E5%89%AA%E8%BC%AF%E9%9F%B3%E6%A8%82)  

[How to Cut (Split) Music in Audacity ](https://www.mightyexpert.com/how-to-cut-music-audacity/)  

[Working with Tracks and Clips - Audio Editing with Audacity Oct 25, 2019](https://guides.vpl.ca/c.php?g=698610&p=4959737)  

[How to Edit Audio in Audacity Feb 27, 2020](https://www.sweetwater.com/sweetcare/articles/how-to-edit-audio-in-audacity/)  
## How to cut and move audio  
[How to split and move audio](https://www.sweetwater.com/sweetcare/articles/how-to-edit-audio-in-audacity/#how-to-split-and-move-tracks)  

## Removing silence  
[Removing silence](https://www.sweetwater.com/sweetcare/articles/how-to-edit-audio-in-audacity/#removing-silence)  


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


