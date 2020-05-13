# Purpose
Take note of Android CTS/VTS/GTS 

# Table of Contents  
[What's the difference between CTS and GTS?](#whats-the-difference-between-cts-and-gts)  
[VTS on Android8.0](#vts-on-android80)  

# What's the difference between CTS and GTS?  
[What's the difference between CTS and GTS? Jan 5, 2016](https://stackoverflow.com/questions/33543544/whats-the-difference-between-cts-and-gts)  

GTS is a list of requirements that the tablet must comply with in order for that tablet to be “Google Certified” and have permission to preload the Google Market Suite(“GMS”)  

Just read this links for in details. 
[GMS Testing and Certification with no hassle](http://www.hatchmfg.com/gms-testing-and-certification/)

[Compatibility Test Suite](https://source.android.com/compatibility/cts/index.html)  

# WindowsでAndroid CTSの実施方法  
[WindowsでAndroid CTSの実施方法 Dec 25, 2018](https://qiita.com/sacred-sanctuary/items/2a7f09f60a3b5c9cfdd1)  

## 6.android-cts/tools/cts-tradefedの修正  
[6.android-cts/tools/cts-tradefedの修正](https://qiita.com/sacred-sanctuary/items/2a7f09f60a3b5c9cfdd1#6android-ctstoolscts-tradefed%E3%81%AE%E4%BF%AE%E6%AD%A3)  

修正1  
```
# get OS
HOST=`uname`
if [ "$HOST" == "Linux" ]; then
    OS="linux-x86"
elif [ "$HOST" == "Darwin" ]; then
    OS="darwin-x86"
else
    echo "Unrecognized OS"
    #exit(※Windowではexitするためコメントアウト)
fi
```

修正2
```
# load any shared libraries for host-side executables
LIB_DIR=${CTS_ROOT}/android-cts/lib
if [ "$HOST" == "Linux" ]; then
    LD_LIBRARY_PATH=${LIB_DIR}:${LIB_DIR}64:${LD_LIBRARY_PATH}
    export LD_LIBRARY_PATH
elif [ "$HOST" == "Darwin" ]; then
    DYLD_LIBRARY_PATH=${LIB_DIR}:${LIB_DIR}64:${DYLD_LIBRARY_PATH}
    export DYLD_LIBRARY_PATH
### ここから　Windows(Cygwin上)でもLinuxと同じ設定をしたいためLD_LIBRARY_PATHを設定する
else
    LD_LIBRARY_PATH=${LIB_DIR}:${LIB_DIR}64:${LD_LIBRARY_PATH}
    export LD_LIBRARY_PATH
### ここまで
fi
```

## 7.CTSの解凍環境の変更  
どうもCドライブなどにあると上手く動かないようだ。そのためネットワーク上のフォルダなどに移動する必要がある。
もっとも簡単な方法は解凍したフォルダを共有設定する。

共有設定を行うとフォルダのプロパティでネットワークパスが表示されます。

ネットワーク上で実行すると

```
$ cd \\MyPcName\android-cts-9.0_r5-linux_x86-arm
$ ./android-cts/tools/cts-tradefed run cts
```

# VTS on Android8.0  
[你準備好了Android8.0的VTS測試嗎？2017-09-22](https://kknews.cc/code/xn8ezmo.html)  

二，VTS測試  
VTS（ Android Vendor Test Suite） 由一套測試框架和測試用例組成，目的是提高安卓系統(如，核心硬體抽象層HALs和庫libraries)和底層系統軟體（如，內核kernel，模塊moduls，固件firmware等）的健壯性，可依賴性和依從性。

點評：google此舉將Android Framework與HAL分開，對Vendor Interface測試確保兼容性。
![alt tag](https://i2.kknews.cc/SIG=phsi3h/3o11000345o9s23p5779.jpg)  

CTS測試，確保APP開發者編寫的同一款程序可以運行在不同系統版本（向前兼容）、不同硬體平台、不同廠商製造的不同設備上。VTS類似CTS，通過對Vendor Interface進行測試，確保同一個版本的Android Framework可以運行在不同HAL上，或不同Android Framework可以運行在同一個HAL上。

目前GMS認證包括CTS測試和GTS測試。後續GMS認證必須依賴VTS、CTS、GTS測試。


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
