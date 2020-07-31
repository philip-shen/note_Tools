Table of Contents
=================

   * [Notes of Tools](#notes-of-tools)
   * [Purpose](#purpose)
   * [声優ラジオ録音環境](#声優ラジオ録音環境)
      * [録音ファイルのアップロード、アップロード完了通知の準備](#録音ファイルのアップロードアップロード完了通知の準備)
         * [Dropboxへのファイルアップロード準備](#dropboxへのファイルアップロード準備)
         * [LINEへの通知準備](#lineへの通知準備)
         * [slackで通知する](#slackで通知する)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)

# Purpose  
Take note of Raspberry_Pi  

# 声優ラジオ録音環境  
[ぼくの声優ラジオ録音環境（ラズパイ4で録音→Dropboxにアップ→LINEに通知まで） updated at 2020-06-15](https://qiita.com/kino15/items/32f8ceed4261ba18817f#windows10%E3%81%8B%E3%82%89ssh%E3%81%A7%E3%83%A9%E3%82%BA%E3%83%91%E3%82%A4%E3%81%AB%E6%8E%A5%E7%B6%9A%E3%81%97%E3%81%A6%E4%BD%9C%E6%A5%AD)

## 録音ファイルのアップロード、アップロード完了通知の準備  
### Dropboxへのファイルアップロード準備  
[【Dropbox】scriptを使用してのファイル転送処理](https://qiita.com/Dace_K/items/890e9f2fe93a66ec8e56)

### LINEへの通知準備  
[[超簡単]LINE notify を使ってみる](https://qiita.com/iitenkida7/items/576a8226ba6584864d95)
RThBFBKPPKa1lKyVv1mKURTRci4Mq4VZhOnUdoIefKp

通知先のルームです。 
![alt tag](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F21391%2F69fccdd0-58c1-6cfe-194e-8fa53aca8903.png?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&s=df5227f671c781ebd6336f437c86648b)  

![alt tag](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F21391%2Fcbd483ef-7300-9763-fc40-2dd33e3a3053.png?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&s=5a359371a5342f5484fe258515e75c96)  

![alt tag](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F21391%2F6e6024af-565f-3a9f-cf9c-4316f463d01d.png?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&s=76049c30a5bbed504e40b2f7a8776a64)  

通知してくれるbotくん（LINE notify）を設定したルームに招待してあげてください  
![alt tag](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F21391%2F95155252-dcc0-7b26-555d-c74cec44c41c.jpeg?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&s=abe1174e1ae6ae1f644fbb1cb4c4074b)  

```
curl -X POST -H "Authorization: Bearer ACCESS_TOKEN" -F "message=ABC" https://notify-api.line.me/api/notify
```



[上手 LINE Notify 不求人：一行代碼都不用寫的推播通知方法 2020/02/17](https://blog.miniasp.com/post/2020/02/17/Go-Through-LINE-Notify-Without-Any-Code)  
```
如果想得知目前 Access Token 的 API Rate Limit 相關資訊，可以改用以下命令查詢：

curl -D - -H "Authorization: Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" https://notify-api.line.me/api/status
```
```
其中的 X-RateLimit-Remaining 就是你這個 Token 在這一個小時內還能用幾次。

還有 X-RateLimit-Reset 代表著下次 Reset 用量限制的時間點，這是 UTC epoch seconds 單位。
```

### slackで通知する  
[Slack APIを使用してメッセージを送信する](https://qiita.com/kou_pg_0131/items/56dd81f2f4716ca292ef)

* []()
![alt tag]()  

# h1 size

## h2 size

### h3 size

#### h4 size

##### h5 size

*strong*strong  
**strong**strong  

