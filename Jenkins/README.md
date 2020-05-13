# Purpose
Take notes of Jenkis  

# Table of Contents  


[Plug-In Installation of Jenkins](#plug-in-installation-of-jenkins)  
[01 dockerfile](#01-dockerfile)  
[02 Build docker image](#02-build-docker-image)  
[03 Run Jenkis Container](#03-run-jenkis-container)  
[04 Eneter Jekins Container to make sure Administrator password](#04-eneter-jekins-container-to-make-sure-administrator-password)  
[05 Administrator Login](#05-administrator-login)  
[06 Click "Select Plugins"](#06-click-select-plugins)  
[07 Select Plugins to plugin and then install](#07-select-plugins-to-plugin-and-then-install)  
[08 Plugins download](#08-plugins-download)  
[09 Save and Finsh](#09-save-and-finsh)  
[10 Start using Jenkins](#10-start-using-jenkins)  
[11 Try it and Enjoy](#11-try-it-and-enjoy)  
[12 Creat a Project](#12-creat-a-project)  
[13 Stop Jenkis Container](#13-stop-jenkis-container)  

[Reference](#reference)  
[Jenkinsを手探りで社内ローカルに立てて詰んだ話](#jenkins%E3%82%92%E6%89%8B%E6%8E%A2%E3%82%8A%E3%81%A7%E7%A4%BE%E5%86%85%E3%83%AD%E3%83%BC%E3%82%AB%E3%83%AB%E3%81%AB%E7%AB%8B%E3%81%A6%E3%81%A6%E8%A9%B0%E3%82%93%E3%81%A0%E8%A9%B1)  
[JenkinsとSeleniumを使ってWebコンテンツの自動UIテスト環境を作ろう！](#jenkins%E3%81%A8selenium%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6web%E3%82%B3%E3%83%B3%E3%83%86%E3%83%B3%E3%83%84%E3%81%AE%E8%87%AA%E5%8B%95ui%E3%83%86%E3%82%B9%E3%83%88%E7%92%B0%E5%A2%83%E3%82%92%E4%BD%9C%E3%82%8D%E3%81%86)  
[JenkinsでCI環境構築チュートリアル ～GitHubとの連携～](#jenkins%E3%81%A7ci%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89%E3%83%81%E3%83%A5%E3%83%BC%E3%83%88%E3%83%AA%E3%82%A2%E3%83%AB-github%E3%81%A8%E3%81%AE%E9%80%A3%E6%90%BA)  
[JenkinsでCI環境構築チュートリアル ～GitHubからWebサーバーへのデプロイ～](#jenkins%E3%81%A7ci%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89%E3%83%81%E3%83%A5%E3%83%BC%E3%83%88%E3%83%AA%E3%82%A2%E3%83%AB-github%E3%81%8B%E3%82%89web%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%81%B8%E3%81%AE%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4)  
[テスト自動化環境構築]()  

[dockerでjenkins構築（plugin install errorを出さない）](#docker%E3%81%A7jenkins%E6%A7%8B%E7%AF%89plugin-install-error%E3%82%92%E5%87%BA%E3%81%95%E3%81%AA%E3%81%84)  
[Jenkinsインストール(Ansible)](#jenkins%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%ABansible)  
[【Jenkins備忘録】Python自動テスト環境構築](#jenkins%E5%82%99%E5%BF%98%E9%8C%B2python%E8%87%AA%E5%8B%95%E3%83%86%E3%82%B9%E3%83%88%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89)  
[Dockerで動くJenkinsから他のコンテナを操作する（Docker outside of Docker）](#docker%E3%81%A7%E5%8B%95%E3%81%8Fjenkins%E3%81%8B%E3%82%89%E4%BB%96%E3%81%AE%E3%82%B3%E3%83%B3%E3%83%86%E3%83%8A%E3%82%92%E6%93%8D%E4%BD%9C%E3%81%99%E3%82%8Bdocker-outside-of-docker)  
[Dockerでjenkins(+SSL)](#docker%E3%81%A7jenkinsssl)  

[Jenkins CheatSheet — Know The Top Best Practices of Jenkins](#jenkins-cheatsheet--know-the-top-best-practices-of-jenkins)  

[Devops实践中的CICD工具]() 

# Plug-In Installation of Jenkins   
[プラグインインストール済のJenkins 構築 Docker編 その1 Feb 27, 2019](https://qiita.com/atmaru/items/3707b6f3fca7f4671498)   
* モチベーション  
```
パッとローカルのwin10 PCによく使うPlugin入りのJenkinsを構築したい。
みんなで使うJenkinsさんはあるんだけど、ちょっと周りに迷惑かけずに試したいことがある時に、その時だけ使ってあとは捨てる前提。
手段は大きく分けると2つ。

1.Docker Image作っておいて、必要な時だけコンテナ起動
2.Ansibleなどの構成管理ツールで、自動で構築

机上で考えても両者の優越つけられなかったので、両方やってみましょう。
今回は1.のDocker編です。
```
## 01 dockerfile  
```
FROM jenkins:2.19.4
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"

#COPY plugins.txt /usr/share/jenkins/ref/
#RUN /usr/local/bin/install-plugins.sh $(cat /usr/share/jenkins/ref/plugins.txt)
```

## 02 Build docker image  
```
λ docker build -t myjenkins:1 .
λ docker images
```
![alt tag](https://i.imgur.com/F6vP46M.jpg)  

## 03 Run Jenkis Container  
```
d:\project\Jenkis
λ cd home\
```

```
d:\project\Jenkis\home
λ docker run -it -d -v %cd%:/var/jenkins_home/ --name myjenkins-1 -p 8080:8080 myjenkins:1
2812257032b451156a2fe2960459b6a901d814b40fd2b5ecd85655ee80d7a40d

λ docker ps
```
![alt tag](https://i.imgur.com/BHi8eOB.jpg)  

### Remove Containers  if something wrong   
```
d:\project\Jenkis
λ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
490c90a45d61        myjenkins:1         "/bin/tini -- /usr/l…"   24 minutes ago      Exited (1) 24 minutes ago                       myjenkins-1
```
```
d:\project\Jenkis
λ docker rm myjenkins-1
myjenkins-1

d:\project\Jenkis
λ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

## 04 Eneter Jekins Container to make sure Administrator password  
```
λ docker exec -i -t myjenkins-1 bash
jenkins@2812257032b4:/$ cat /var/jenkins_home/secrets/initialAdminPassword
84ffb92f5d694099bef17de4fdb3e687
```
![alt tag](https://i.imgur.com/ItJVJnZ.jpg)  

### File directory on Windows 
![alt tag](https://i.imgur.com/vy3wivw.jpg)  
### "NETSTAT.EXE -a | findstr "8080"" on Windows 
```
d:\project\Jenkis\home
λ NETSTAT.EXE -a | findstr "8080"
  TCP    0.0.0.0:8080           DESKTOP-7EDV2HB:0      LISTENING
  TCP    [::1]:8080             DESKTOP-7EDV2HB:0      LISTENING
```

## 05 Administrator Login  
![alt tag](https://i.imgur.com/iMQ1RfK.jpg)  

## 06 Click "Select Plugins"
![alt tag](https://i.imgur.com/4CRSwFO.jpg)  

## 07 Select Plugins to plugin and then install  
![alt tag](https://i.imgur.com/nD3rAbQ.jpg)  

## 08 Plugins download  
![alt tag](https://i.imgur.com/gE7pfgn.jpg)  

## 09 Save and Finsh  
![alt tag](https://i.imgur.com/FMaRq3i.jpg)  

## 10 Start using Jenkins  
![alt tag](https://i.imgur.com/JqnhRBR.jpg)  

## 11 Try it and Enjoy  
![alt tag](https://i.imgur.com/OnVKD00.jpg) 

## 12 Creat a Project    
![alt tag](https://i.imgur.com/dzSNRzf.jpg)  

## 13 Stop Jenkis Container  
```
d:\project\Jenkis\home
λ docker stop myjenkins-1
myjenkins-1
```
![alt tag](https://i.imgur.com/GKI6YKU.jpg)  



[プラグインインストール済のJenkins 構築 Docker編 番外編 Feb 28, 2019](https://qiita.com/atmaru/items/eba33a407d12cb40f079)   
* 環境や前提条件  
```
windows10 pro 1803
PowerShell
Docker 18.09.0
jenkins:2.19.4
```

[プラグインインストール済のJenkins 構築 Docker編 その2  Mar 01, 2019](https://qiita.com/atmaru/items/1f57b79e4f32c9071b75)  
```
プラグインインストール済のJenkins 構築 Docker編 その1の続きです。
```

[プラグインインストール済のJenkins 構築 Docker編 その4 Mar 03, 2019](https://qiita.com/atmaru/items/25cbc07576e668350d8d)  
```
もともとローカルで動かすのが目的だったが、せっかくなのでAWS上で動かす練習しておく。
（表題と内容が合わないので、あとで表題は変える予定です。）
```

# Troubleshooting


# Reference  
## Jenkinsを手探りで社内ローカルに立てて詰んだ話  
[Jenkinsを手探りで社内ローカルに立てて詰んだ話 Dec 14, 2017](https://qiita.com/wryu/items/de3767f231e690fb4e7d)  

## JenkinsとSeleniumを使ってWebコンテンツの自動UIテスト環境を作ろう！  
[JenkinsとSeleniumを使ってWebコンテンツの自動UIテスト環境を作ろう！ 4/9, 2015](https://ics.media/entry/6031/)  

## JenkinsでCI環境構築チュートリアル ～GitHubとの連携～  
[JenkinsでCI環境構築チュートリアル ～GitHubとの連携～ 12/9, 2016](https://ics.media/entry/2869/)  

## JenkinsでCI環境構築チュートリアル ～GitHubからWebサーバーへのデプロイ～  
[JenkinsでCI環境構築チュートリアル ～GitHubからWebサーバーへのデプロイ～ 11/14, 2015](https://ics.media/entry/3283/)  

## テスト自動化環境構築  
[テスト自動化環境構築  Jul 14, 2018](https://qiita.com/jun2014/items/0c97f99e60109f9ec870)  

## dockerでjenkins構築（plugin install errorを出さない）  
[dockerでjenkins構築（plugin install errorを出さない） Jul 08, 2019](https://qiita.com/_ainosh_/items/04992adbab8502e2ed9e)  
* 1. 適当にjenkins試す用のディレクトリ作って、docker-compose.yml作成する
docker-compose.yml

```
version: "3"
services:
  master:
    container_name: master
    # (library/)jenkins:2.60.3（公式）だと依存プラグインの関係でインストールがエラるので、jenkins/jenkins使う
    image: jenkins/jenkins:lts
    ports:
      - 18080:8080
      - 50000:50000
    volumes:
      - ./jenkins_home:/var/jenkins_home
#    links:
#     - slave01
#
#  slave01:
#    container_name: slave01
#    image: jenkinsci/ssh-slave
#    environment:
#      - JENKINS_SLAVE_SSH_PUBKEY=ssh-rsa AAAxxxxxxxxxxxx
```

```
docker-compose up --build -d
```

```
docker logs master
```

* 2. master側のSSHキー作成  
```
docker exec -it master ssh-keygen -t rsa -C "" 
```


* 3. slaveを作成する  
docker-compose.yml

```

version: "3"
services:
  master:
    container_name: master
    # (library/)jenkins:2.60.3（公式）だと依存プラグインの関係でインストールがエラるので、jenkins/jenkins使う
    image: jenkins/jenkins:lts
    ports:
      - 18080:8080
      - 50000:50000
    volumes:
      - ./jenkins_home:/var/jenkins_home
    links:
     - slave01

  slave01:
    container_name: slave01
    image: jenkinsci/ssh-slave
    environment:
      - JENKINS_SLAVE_SSH_PUBKEY=ssh-rsa AAAAxxxxxxxxxxxxxxxx
```
```
docker-compose up --build -d
```

* 4. 適当にjenkinsの画面でポチポチ設定してください  
http://localhost:18080/

秘密鍵の入力を[Jenkinsのマスター上の~/.sshから]にしたいんですが、ないので直接入力しました。
![alt tag](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F455534%2F64551bb3-ae7d-caf7-abc0-592eff8a183e.png?ixlib=rb-1.2.2&auto=compress%2Cformat&gif-q=60&w=1400&fit=max&s=1c0de9750426a6584da9e338a7718474)  



[docker-composeを使って開発環境でjenkinsを動かせるようにする Oct 31, 2018](https://qiita.com/i_whammy_/items/84b71c56d70817803472)  

## Jenkinsインストール(Ansible)  
[Jenkinsインストール(Ansible) Oct 24, 2019](https://qiita.com/tz2i5i_ebinuma/items/c7cdb0520062a6c75685)  

## 【Jenkins備忘録】Python自動テスト環境構築  
[【Jenkins備忘録】Python自動テスト環境構築①Python準備編  Jun 09, 2018](https://qiita.com/Kento75/items/8558d9ddd2cb04c3e36d)  
[【Jenkins備忘録】Python自動テスト環境構築②テストコード準備編 Jun 09, 2018](https://qiita.com/Kento75/items/e4ebeb990449f447ce3f)  
[【Jenkins備忘録】Python自動テスト環境構築③jenkins準備編 Jun 09, 2018](https://qiita.com/Kento75/items/2ecd1f3251c9c344ca69)  

[【Jenkins備忘録】Python自動テスト環境構築④プロジェクト作成編 Jun 09, 2018](https://qiita.com/Kento75/items/f46b4c47a3a33de7ae5d)  

## Dockerで動くJenkinsから他のコンテナを操作する（Docker outside of Docker） 
* [Dockerで動くJenkinsから他のコンテナを操作する（Docker outside of Docker） Oct 26, 2019](https://qiita.com/quotto/items/61b44bdeef7dbb915970)  

## Dockerでjenkins(+SSL)  
* [Dockerでjenkins(+SSL) Sep 05, 2019](https://qiita.com/search?page=2&q=Jenkins)  

## Jenkins CheatSheet — Know The Top Best Practices of Jenkins  
[Jenkins CheatSheet — Know The Top Best Practices of Jenkins Aug 7, 2019](https://medium.com/edureka/jenkins-cheat-sheet-e0f7e25558a3)  
```
Different Types of Jenkins Jobs

Below are the types of jobs you can choose from:

    Freestyle

Freestyle build jobs are general-purpose build jobs, which provides maximum flexibility. It can be used for any type of project.

    Pipeline

This project runs the entire software development workflow as code. Instead of creating several jobs for each stage of software development, you can now run the entire workflow as one code.

    Multiconfiguration

The multiconfiguration project allows you to run the same build job on different environments. It is used for testing an application in different environments.

    Folder

This project allows users to create folders to organize and categorize similar jobs in one folder or subfolder.

    GitHub Organization

This project scans your entire GitHub organization and creates Pipeline jobs for each repository containing a Jenkinsfile

    Multibranch Pipeline

This project type lets you implement different Jenkinsfiles for different branches of the same project.
```

## Devops实践中的CICD工具  
[Devops实践中的CICD工具](https://mp.weixin.qq.com/s/r7CnMAIVJ_gMLL8WppWZbw)

* []()  
## 
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
