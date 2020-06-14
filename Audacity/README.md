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


