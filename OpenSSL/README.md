Table of Contents
=================

   * [Table of Contents](#table-of-contents)
   * [Purpose](#purpose)
   * [Create a self-signed certificate using OpenSSL](#create-a-self-signed-certificate-using-openssl)
      * [Method #1: 直接生出一組 key &amp; certificate](#method-1-直接生出一組-key--certificate)
      * [Method #2: 用自己的 CA 簽自己的 Certificate](#method-2-用自己的-ca-簽自己的-certificate)
   * [SAN Certificate for Multi-Domain Certificate](#san-certificate-for-multi-domain-certificate)
      * [Wildcard certificate &amp; SAN](#wildcard-certificate--san)
   * [SANの設定（OpenSSL）](#sanの設定openssl)
      * [環境](#環境)
      * [手順](#手順)
   * [Troubleshooting](#troubleshooting)
   * [Reference](#reference)
   * [h1 size](#h1-size)
      * [h2 size](#h2-size)
         * [h3 size](#h3-size)
            * [h4 size](#h4-size)
               * [h5 size](#h5-size)
   * [Table of Contents](#table-of-contents-1)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)


# Purpose
Take note of OpenSSL

# Create a self-signed certificate using OpenSSL  
[Create a self-signed certificate using OpenSSL Feb 3, 2019](https://blog.cssuen.tw/create-a-self-signed-certificate-using-openssl-240c7b0579d3)

* certificate：指 SSL 證書
* key：指證書的私鑰
* CA：Certificate Authority，憑證頒發機構，負責簽憑證的
* CSR：Certificate Signing Request

## Method #1: 直接生出一組 key & certificate  
```
openssl req -x509 -newkey rsa:4096 -sha256 -nodes -keyout key.pem -out cert.pem -days 30
```

* req：Certificate Request(PKCS #10)
* x509：輸出 x509 的 certificate ，而不要輸出 certificate request
* newkey rsa:4096：建立一個新的 4096 bits 的 RSA key
* sha256：用 SHA256 做檢查碼（Digest）
* nodes：不要幫 key 加密
* keyout：輸出 key 的檔案
* out：輸出 certificate 的檔案
* days 365：憑證的有效日期

## Method #2: 用自己的 CA 簽自己的 Certificate  

* 1. 先幫自己的 CA 生一組 key & certificate
* 2. 幫自己的主機生一組 key & CSR
* 3. 用自己的主機簽 CSR 讓他變成 certificate

> 首先我們先幫 CA 生一組 key  
> 由於 CA 的 key 只有在簽 certificate 的時候會用到，不像 certificate 的 key 服務本身會用到，所以這邊可以加上 des3 ，會要你輸入一個密碼加密。  

```
openssl genrsa -des3 -out ca.key 4096
```

> 接下來我們幫 CA 生一組 certificate，通常這個天數會久不少。  

```
openssl genrsa -out host.key 4096
```

> 這組是主機上的服務要用的 key ，就不加密了。  

```
openssl req -new -key host.key -sha256 -out host.csr
```

> 產生一個 CSR ，會要求你輸入一些資訊，你也可以把他們弄成參數直接帶入，像下面這樣：

```
openssl req -new -key host.key -subj "/C=TW/ST=Taiwan/L=Taipei City/O=MyOrg/OU=MyUnit/CN=my.domain" -sha256 -out host.csr
```

> 最後來簽這個 CSR 產生 certificate

```
openssl x509 -req -in host.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out host.crt -days 30 -sha256
```

* in：輸入檔案，這邊是 CSR 檔
* out：輸出檔案，這邊是產生的 certificate
* CA：CA 自己的 certificate
* CAkey：CA 自己的 key
* CAcreateserial：建立一個 CA 的序號檔（.srl），這是用來記錄 CA 簽了多少 certificate 的，只有第一次需要，之後是直接用 CAserial 指定 srl 檔就可以了 

```
第二種方法的好處是你可以簽很多 certificate 出來，把自己的 CA 加入信任的 CA 之後就不會有錯誤訊息了。不過說真的，Certbot 跟 Let’s Encrypt 真的很方便，不試試嗎？
```
[Let’s Encrypt](https://letsencrypt.org/getting-started/)  


# SAN Certificate for Multi-Domain Certificate  
[用 SAN Certificate 做 Multi-Domain Certificate Feb 4, 2019](https://blog.cssuen.tw/%E7%94%A8-san-certificate-%E5%81%9A-multi-domain-certificate-c7403e05c697)  
```
SAN 的全名是 “Subject Alternative Name”，維基百科上翻譯的中文叫做「主題備用名稱」
（但我覺得這感覺像是丟翻譯軟體翻出來的，所以後面都直接用簡寫 SAN），
是前一篇提到的 X.509 的擴充（extension）之一。
```

## Wildcard certificate & SAN
```
一般在做多個 domain 的 certificate 的時候，除了幫每個 domain 各自簽自己的 certificate 之外，
我們也會用一張 certificate 給多個 domain 用的方式，來節省管理上和金錢上的各種成本。
其中常見的兩種方式一個是 Wildcard certificate（萬用字元憑證），另一個就是加上 SAN。
```

```
Wildcard certificate 的概念是在簽 certificate 的時候使用萬用字元（wildcard），
例如我們簽發 *.hs.ntnu.edu.tw 這個 certificate，
那不管是 www.hs.ntnu.edu.tw 或者是 mail.hs.ntnu.edu.tw 都可以使用這張 certificate。
對 Wildcard certificate 來說，只要一張就可以讓所有的子網域使用；
而且之後任何新增的子網域也不需要重新簽發憑證，因為也都符合 Wildcard 的規則。

```

```
而 SAN 則是我們在簽發的時候加上 SAN 的欄位，讓這張 certificate 可以符合多個獨立的網域。
例如我可以簽一張 certificate 給 cnmc.tw 跟 cnmc.club 一起用，不需要是同一個網域下面的子網域。
相對的，變更 SAN 需要進行重新簽發；另外 SAN 也有一個上限值，不能無限增加網域。
```

# SANの設定（OpenSSL）
[Docker Registry v2設定(TLS) updated at 2019-11-22](https://qiita.com/niiku-y/items/df3dbcb3453e6f529e07)
[SANの設定（OpenSSL）updated at 2019-11-22](https://qiita.com/niiku-y/items/df3dbcb3453e6f529e07#san%E3%81%AE%E8%A8%AD%E5%AE%9Aopenssl)  

## 環境  
* OS : Ubuntu 18.04
* Docker-ce : 19.03.5
* OpenSSL : 1.1.1 
* リバースプロキシ 

## 手順  
```
1. SANの設定（OpenSSL）
2. 自己署名証明書の作成
    1. 証明書、鍵ファイルの作成 : TLS通信のサーバ側の作業
    2. 証明書の配置、更新 : TLS通信のクライアント側の作業
    3. dockerエンジン再起動
3. Basic認証設定
    1. htpasswd（を含むパッケージ）インストール
    2. パスワードファイル作成
4. registry起動
    1. 起動用スクリプト準備
    2. registryコンテナの起動
5. 設定ファイルについて
```
[niiku-y/make_certs.sh](https://gist.github.com/niiku-y/feaf7a2d4b4111641480dd4e9f737212)  
[niiku-y/add_san.sh](https://gist.github.com/niiku-y/e4435d6d2f308cbf484940e20eff4946)  


# Troubleshooting


# Reference
[ Know about SAN Certificate and How to Create With OpenSSL Dec 2, 2018](https://geekflare.com/san-ssl-certificate/)  
[Provide subjectAltName to OpenSSL directly on the command line Dec 28, 2018](https://security.stackexchange.com/questions/74345/provide-subjectaltname-to-openssl-directly-on-the-command-line)  

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
