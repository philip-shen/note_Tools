# Table of Contents
=================

   * [Table of Contents](#table-of-contents)
   * [Upgarde the Latest CMake on Ubuntu](#upgarde-the-latest-cmake-on-ubuntu)
      * [Use Snappyy](#use-snappyy)
      * [Install from source](#install-from-source)
      * [Reference](#reference)
   * [C/C++ Porject by CMake](#cc-porject-by-cmake)
      * [Reference](#reference-1)
   * [CMake for Cross Platform](#cmake-for-cross-platform)
      * [Reference](#reference-2)
   * [Reference](#reference-3)

# Upgarde the Latest CMake on Ubuntu  

## Use Snappyy  
Remove old version  
```
sudo apt remove --purge cmake
hash -r
```

```
sudo snap install cmake --classic

cmake --version
```

## Install from source  
```
sudo apt install build-essential libssl-dev
wget https://github.com/Kitware/CMake/releases/download/v3.20.2/cmake-3.20.2.tar.gz
tar -zxvf cmake-3.20.2.tar.gz
cd cmake-3.20.2
./bootstrap
make 
sudo make install 
```

## Reference  
[Installing the Latest CMake on Ubuntu Linux Aug 28, 2023](https://graspingtech.com/upgrade-cmake/)

# C/C++ Porject by CMake 

## Reference  
[建構屬於自己的C/C++專案 : 我的30天CMake學習之旅 2023-09-15](https://ithelp.ithome.com.tw/users/20162026/ironman/6715)


# CMake for Cross Platform  

## Reference  
[30 天 CMake 跨平台之旅 2023-09-01](https://ithelp.ithome.com.tw/users/20161950/ironman/6278?page=1)

# Reference 
[CMakeの使い方（その１）2022-03-25](https://qiita.com/shohirose/items/45fb49c6b429e8b204ac)  
[CMakeの使い方（その２）2022-03-27](https://qiita.com/shohirose/items/637f4b712893764a7ec1)  
[CMakeの使い方（その３）2022-03-27](https://qiita.com/shohirose/items/d2b9c595a37b27ece607)  
[【初心者向け】CMakeLists.txtを使ってビルドする。2023-06-13](https://qiita.com/hi_to_san/items/490f8320900617db9230)  
[【初心者向け】CMakeLists.txtを使ってincludeのpathを省略する 2023-06-13](https://qiita.com/hi_to_san/items/00a5e9a75a8876b39492)  
[【初心者向け】CMakeLists.txtを使ってlibraryをリンクする。2023-06-13](https://qiita.com/hi_to_san/items/2b44dd44d3e152594c53)  
