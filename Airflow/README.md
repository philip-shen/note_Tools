Table of Contents
=================

   * [Table of Contents](#table-of-contents)
   * [Purpose](#purpose)
   * [Airflow Environment Setup Pattern](#airflow-environment-setup-pattern)
      * [1. Installation Directly](#1-installation-directly)
      * [2. Installation Directly and Another Instance Execution](#2-installation-directly-and-another-instance-execution)
      * [3. Docker Compose Startup](#3-docker-compose-startup)
         * [Installation Procedures](#installation-procedures)
      * [4. Docker Compose Startup and Another Instance Execution](#4-docker-compose-startup-and-another-instance-execution)
      * [Reference](#reference)
   * [Airflow Docker](#airflow-docker)
      * [Install Docker CE](#install-docker-ce)
      * [Install Docker-Compose](#install-docker-compose)
      * [Docker Pull Image](#docker-pull-image)
      * [Docker Delopy Airflow CeleryExecutor Mode](#docker-delopy-airflow-celeryexecutor-mode)
         * [Update Dockerfile](#update-dockerfile)
         * [Update docker-compose-CeleryExecutor.yml](#update-docker-compose-celeryexecutoryml)
         * [Update Airflow config](#update-airflow-config)
      * [Airflow connects to Database](#airflow-connects-to-database)   
         * [Web UI 新增 Connections](#web-ui-新增-connections)
         * [Airflow CLI 設定](#airflow-cli-設定)
         * [Docker Compose 設定](#docker-compose-設定)
      * [Reference](#reference-1)
   * [Airflow on WSL](#airflow-on-wsl)
      * [Step 1: Search for Turn Windows Features On/Off](#step-1-search-for-turn-windows-features-onOff)
      * [Step 2: Check the Windows Subsystem for Linux](#step-2-check-the-windows-subsystem-for-linux)
      * [Step 3: Installing WSL](#step-3-installing-wsl)
      * [Step 4: Install Ubuntu Distribution](#step-4-install-ubuntu-distribution)
      * [Step 5: Configure Ubuntu](#step-5-configure-ubuntu)
      * [Step 6: Accessing Root User](#step-6-accessing-root-user)
      * [Step 7: Update and Install the packages](#step-7-update-and-install-the-packages)
      * [Step 8: Change User from root to your user](#step-8-change-user-from-root-to-your-user)
      * [Step 9: Create a virtual environment](#step-9-create-a-virtual-environment)
      * [Step 10: Create a folder called ‘airflow’](#step-10-create-a-folder-called-airflow)
      * [Step 11: Now activate your virtual env](#step-11-now-activate-your-virtual-env)
      * [Step 12: Installing airflow](#step-12-installing-airflow)
      * [Step 13: Configure Airflow Files](#step-13-configure-airflow-files)
      * [Step 14: Let’s run our Airflow Webserver and Scheduler](#step-14-lets-run-our-airflow-webserver-and-scheduler)
      * [Step 15: SSH Server Installation](#step-15-ssh-server-installation)
      * [Reference](#reference-2)
   * [Airflow on WSL Docker](#airflow-on-wsl-docker)
      * [Reference](#reference-3)
   * [Airflow tutorial](#airflow-tutorial)
      * [docker-compose Installation](#docker-compose-installation)
      * [Initialization](#initialization)
      * [DGA](#dga)
      * [Reference](#reference-4)
   * [Airflow-Learning-English-tool](#airflow-learning-english-tool)
      * [update docker-compose.yml by Airflow-Learning-English-tool/docker-compose.yaml](#update-docker-composeyml-by-airflow-learning-english-tooldocker-composeyaml)
   * [Airflow-scraping-ETL-tutorial](#airflow-scraping-etl-tutorial)
      * [Reference](#reference-5)
   * [How to Upload Files to Google Drive using Airflow](#how-to-upload-files-to-google-drive-using-airflow)
      * [1. Configuring the Google Drive API and a creating service account on GCP](#1-configuring-the-google-drive-api-and-a-creating-service-account-on-gcp)
      * [2. Configuring Domain-wide Delegation on our Google Workspace](#2-configuring-domain-wide-delegation-on-our-google-workspace)
      * [3. Writing the code for our custom GoogleDriveOperator](#3-writing-the-code-for-our-custom-googledriveoperator)
      * [4. Testing a minimal DAG that uploads a text file to our Google Drive account](#4-testing-a-minimal-dag-that-uploads-a-text-file-to-our-google-drive-account)
      * [Reference](#reference-6)
   * [Airflow import local module](#airflow-import-local-module)
   * [Failed to import custom python module in Airflow](#failed-to-import-custom-python-module-in-airflow)
   * [Airflow, Docker and Data Analysis](#airflow-docker-and-data-analysis)
      * [imageを取得する](#imageを取得する)
      * [単体で動かす](#単体で動かす)
         * [webserver](#webserver)
         * [scheduler](#scheduler)
         * [worker](#worker)
   * [Troubleshooting](#troubleshooting)
   * [Reference](#reference-7)
   * [h1 size](#h1-size)
      * [h2 size](#h2-size)
         * [h3 size](#h3-size)
            * [h4 size](#h4-size)
               * [h5 size](#h5-size)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)  


# Purpose  
Take note of Airflow stuffs  

# Airflow Environment Setup Pattern   

## 1. Installation Directly  
<img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F177076%2F0a93ee43-3525-d297-a561-1a8e03f88fe8.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=f048c3f85badaa459cdccece6e27d58e" width="600" height="500">  

## 2. Installation Directly and Another Instance Execution  
<img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F177076%2F4c718fd7-a2ff-2639-3b47-1eedac8c739d.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=88ebb4209c223070fdc7a89b28346068" width="600" height="400">  

## 3. Docker Compose Startup
<img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F177076%2F95b78171-b9f6-f502-c1fb-ecaff601f010.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=196edb249700d81ab6f36fa4fbc68d38" width="600" height="400">  

### Installation Procedures 
[Official docker-compose.yaml](https://airflow.apache.org/docs/apache-airflow/2.5.2/docker-compose.yaml)  
[Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#)  

```
今回の構成ではDBやRedisは既存の環境を利用するため不要です。
また、flowerやairflow-cliも使いません。

下記はdocker-compose.yamlのディレクトリ構成です。
mntにマウントするファイルを格納しています。
```

## 4. Docker Compose Startup and Another Instance Execution  
<img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F177076%2F68d6629c-a0be-22a8-705b-c9f69410f30f.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=00c70a3972aa1cff21056794d2e04443" width="600" height="400">  

## Reference  
[Airflow環境構築パターン&構築手順メモ　～その1～ Last updated at 2023-03-31](https://qiita.com/yuuman/items/a449bbe36710ad837df7)  
[家計簿アプリZaimデータの分析・可視化基盤を作った話 Posted at 2019-04-02](https://qiita.com/hassiweb/items/63374089edef63dc35b3)  


# Airflow Docker

## Install Docker CE
```
sudo apt-get update

sudo apt-get install docker-ce
#將當前用户加入docker組
sudo gpasswd -a ${USER} docker  
sudo systemcl enable docker 
sudo systemcl restart docker  
docker ps
```

## Install Docker-Compose
```
sudo curl -L "https://github.com/docker/compose/releases/download/v2.12.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

#給予執行權限
sudo chmod +x /usr/local/bin/docker-composesudo pip install docker-compose  

#檢查版本
docker-compose version
```

## Docker Pull Image
```
docker pull puckel/docker-airflow

#or 

get from gitgit clone https://github.com/puckel/docker-airflow.git
```

## Docker Delopy Airflow CeleryExecutor Mode

### Update Dockerfile
[gistfile1.txt](https://gist.github.com/cchangleo/ecc13e04424c75ac3028ada5fc1f421b#file-gistfile1-txt)

### Update docker-compose-CeleryExecutor.yml 
[gistfile1.txt](https://gist.github.com/cchangleo/e6b2d79866eaf29485958b42c3716dd6#file-gistfile1-txt)

### Update Airflow config  
```
cd config
vi airflow.cfg
```
<img src="https://miro.medium.com/max/720/1*4yQwYJ4ka9s1a6PfaLWCKQ.png" width="600" height="500">


## 
```
docker build --rm -t puckel/docker-airflow .

docker-compose -f docker-compose-CeleryExecutor.yml up -d
```
<img src="https://miro.medium.com/max/720/1*FGMV3URO8mHNJVb2qF5p5w.png" width="500" height="100">

```
# 啟動
docker-compose -f docker-compose-CeleryExecutor.yml up -d

# 停止
docker-compose -f ./docker-compose-CeleryExecutor.yml stop

# Celery and worker 擴展
docker-compose -f docker-compose-CeleryExecutor.yml scale worker=3 
docker-compose -f docker-compose-CeleryExecutor.yml scale scheduler=3
```
(default setting for browser is localhost:5555)

<img src="https://miro.medium.com/max/720/1*KbTBRPXn21XUJKsocetrBw.png" width="600" height="400">

## Airflow connects to Database  
設定連接 port，兩個 5432，代表 docker 容器外和容器內的 port  
<img src="https://ithelp.ithome.com.tw/upload/images/20231002/20135427TDeEEi3YzW.png" width="500" height="300">

重新 Build Postgres 的服務
```
docker-compose up -d --no-deps --build postgres
```

### Web UI 新增 Connections  
```
設定
   Connection Id(要在airflow中使用的id): localhost-db (可以自己設定)
   HOST(連接的主機): host.docker.internal
   Connection Type(連接的資料庫類型): Postgres
   Schema(連接的db名稱): postgres
   Login 和 Password 都是 airflow
```
<img src="https://ithelp.ithome.com.tw/upload/images/20231002/201354273InlHO6oFg.png" width="600" height="400">

```
設定完按save即可，想要測試可以直接跳到實作時間～
```

### Airflow CLI 設定  
```
docker exec -it <container_id> bash

airflow connections add 'local-db-cli' \
--conn-uri 'postgres://airflow:airflow@host.docker.internal:5432/postgres'
```

### Docker Compose 設定  
```
x-airflow-common:
    xxx
    environment:
        xxx
        AIRFLOW__API__AUTH_BACKENDS:
        AIRFLOW_CONN_LOCAL_DB=
                'postgres://airflow:airflow@host.docker.internal:5432/postgres'
```
```
Docker Compose 設定是比較推薦的方式，不會因為清空容器就要重新設定連接，
但還是盡量不要直接像上面一樣把帳號密碼放在設定中

成功連接 db 之後就趕緊實作一個 DAG 來看看能不能下 sql 來取得資料囉～
```

## Reference  
[Cleaning-up the environment](https://airflow.apache.org/docs/apache-airflow/2.8.4/howto/docker-compose/index.html#cleaning-up-the-environment)  
```
The best way to do this is to:

    Run docker compose down --volumes --remove-orphans command in the directory you downloaded the docker-compose.yaml file
```

[[Day16] 用 Docker Compose 建立 Airflow 環境 2023-10-01](https://ithelp.ithome.com.tw/articles/10331507)  
```
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml'
```
```
mkdir -p ./dags ./logs ./plugins ./config

docker-compose up airflow-init

docker ps -a

docker-compose up
```
[[Day17] Airflow 連接到 Database 的三種方法 2023-10-02](https://ithelp.ithome.com.tw/articles/10332967)  

[[day18] 急！在線等！求解20 點！Airflow 安裝 Python 模組 2023-10-03](https://ithelp.ithome.com.tw/articles/10333330)  
[[Day19] Airflow Scheduler 排程爬坑筆記(上) 2023-10-04](https://ithelp.ithome.com.tw/articles/10334198)  
[[Day20] Airflow Scheduler 排程爬坑筆記(下) 2023-10-05](https://ithelp.ithome.com.tw/articles/10334705)  

*Crontab 預設(preset)*  

Crontab  | 意思 | 等同 Cron 表達式
------------------------------------ | --------------------------------------------- | ----------------------------------- 
None | 不設定排程，可能是手動觸發或是外部觸發 | 
@once | 只執行唯一一次 | 
@continuous | 上一次執行完就接著執行 | 
@hourly | 每個小時結束時執行一次 | 0 * * * *
@daily | 每天半夜12點執行一次 | 0 0 * * *
@weekly | 每週星期天半夜12點執行一次 | 0 0 * * 0
@monthly | 每個月第一天半夜12點執行一次 | 0 0 1 * *
@quarterly | 每季第一天半夜12點執行一次 | 0 0 1 */3 *
@yearly | 每年1月1日半夜12點執行一次 | 0 0 1 1 *

*Cron 表達式(Expressions) 基本語法*  

```
┌───────────── 分鐘   (0 - 59)
| ┌─────────── 小時   (0 - 23)
│ │ ┌───────── 日期   (1 - 31)
│ │ │ ┌─────── 月份   (1 - 12)
│ │ │ │ ┌───── 星期幾 (0 - 7，0 和 7 都是週日，6 是週六，以此類推)
│ │ │ │ │
* * * * *
```

[Windows11でApache Airflowを起動するまで 2022-07-06](https://qiita.com/mizukyf/items/5489a0eef6db58ee7e5f)  
[Airflow での処理通知を Slack でなく Teams に送りたい 2021/09/26](https://zenn.dev/antyuntyun/articles/airflow_custom_notification)  

[Airflow with Docker 容器部署 — part 2 Mar 26, 2019](https://medium.com/@cchangleo/airflow-with-docker-%E5%AE%B9%E5%99%A8%E9%83%A8%E7%BD%B2-part2-8ddb83dc2d4a)  
[cchangleo/docker-airflow](https://github.com/cchangleo/docker-airflow)


# Airflow on WSL  
## Step 1: Search for Turn Windows Features On/Off   

## Step 2: Check the Windows Subsystem for Linux  

## Step 3: Installing WSL   
```
wsl --set-default-version 2
wsl --status
```

## Step 4: Install Ubuntu Distribution  
```
wsl --install -d ubuntu
```

## Step 5: Configure Ubuntu  

## Step 6: Accessing Root User  
```
sudo su
```

## Step 7: Update and Install the packages  
```
apt-get update

apt install python3.12-virtualenv
```

## Step 8: Change User from root to your user  
```
su "username"
```

## Step 9: Create a virtual environment  
```
mkdir ~/virtualenv
python3 -m venv ~/virtualenv/airflow_env
```

## Step 10: Create a folder called ‘airflow’  
```
mkdir ~/airflow
```

## Step 11: Now activate your virtual env  
```
source ~/virtualenv/airflow_env/bin/activate
```

## Step 12: Installing airflow  
```
pip install 'apache-airflow[crypto, slack]==2.10.2' \
 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.2/constraints-3.8.txt"
```

## Step 13: Configure Airflow Files  
```
a) Set the AIRFLOW_HOME environment variable with a folder name for our Airflow Project.
export AIRFLOW_HOME=~/airflow
cd airflow

b) Initialize Airflow Database
airflow db migrate    # Earlier it was airflow db init, now its not supported

c) Create a User for our Airflow UI with Admin Role
airflow users create --username <username> --firstname <firstname> 
--lastname <lastname> --role Admin --password <password> --email <email> 
 
d) Create a DAGS and PLUGINS folder in the same directory, which will be used to keep our DAGS and plugins files.
mkdir dags plugins
```

```
git clone https://github.com/leemengtaiwan/airflow-tutorials.git
cd airflow-tutorials
```
```
export AIRFLOW_HOME="$(pwd)"
airflow initdb
```
```
【2018/08/27 加註】如果沒有設定 export AIRFLOW_HOME="$(pwd)" 就執行 airflow initdb的話，
會讓 Airflow 使用作者當初測試時使用的路徑，而不是你 git clone 下來的 repo 的路徑而造成問題，務必記得設定。
```

## Step 14: Let’s run our Airflow Webserver and Scheduler  
```
Airflow Webserver:-
nohup airflow webserver -p 8080 >> airflow_webserver.out &

Airflow Scheduler:-
nohup airflow scheduler >> airflow_scheduler.out &
```
```
We have used the nohup utility, which is a command on Linux systems that keeps processes running even after exiting the shell or terminal. 
You can remove the nohup command if you don't need it.
```

## Step 15: SSH Server Installation  
```
#sshdのインストール

$ sudo apt install ssh -y
```

```
#sshd設定ファイルの変更

$ sudo vi /etc/ssh/sshd_config.d/sshd_ubuntu.conf
# 以下の2行を追加
Port 10022
PasswordAuthentication yes
```

```
#sshd再起動

$ sudo systemctl restart ssh

```

```
shdステータス確認

$ systemctl status ssh
● ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled)
     Active: active (running) since Sun 2023-04-23 11:58:01 JST; 4s ago
       Docs: man:sshd(8)
             man:sshd_config(5)
    Process: 1429 ExecStartPre=/usr/sbin/sshd -t (code=exited, status=0/SUCCESS)
   Main PID: 1430 (sshd)
      Tasks: 1 (limit: 19182)
     Memory: 1.7M
        CPU: 10ms
     CGroup: /system.slice/ssh.service
```

```
/etc/wsl.confの確認

$ cat /etc/wsl.conf
# 以下2行が存在することを確認する。
[boot]
systemd=true   
```

## Reference  
[Install Airflow on Windows without Docker or Virtual Box in 5 mins Mar 10, 2023](https://medium.com/@routr5953/installing-airflow-on-windows-without-docker-in-5-mins-21d16091ebc5)  



[一段 Airflow 與資料工程的故事：談如何用 Python 追漫畫連載 2018-08-21](https://leemeng.tw/a-story-about-airflow-and-data-engineering-using-how-to-use-python-to-catch-up-with-latest-comics-as-an-example.html)  


[【WSL2】WSL2のUbuntuでsshdの自動起動を有効にする【Ubuntu】2023-04-23](https://qiita.com/tmiki/items/022242af3853cd8e7a6a) 


# Airflow on WSL Docker   
[1. Introduction and Local Installation](https://www.youtube.com/watch?v=z7xyNOF8tak)  
[2. Get Airflow running in Docker](https://www.youtube.com/watch?v=J6azvFhndLg)  
[3. Airflow Core Concepts in 5 mins](https://www.youtube.com/watch?v=mtJHMdoi_Gg)  
[4. Airflow Task Lifecycle and Basic Architecture](https://www.youtube.com/watch?v=UFsCvWjQT4w)  
[5. Airflow DAG with BashOperator](https://www.youtube.com/watch?v=CLkzXrjrFKg)  
```
1. Remove all the airflow example dags
   
   docker-compose -f docker-compose_airflow.yaml down -v
   docker-compose -f docker-compose_airflow.yaml up airflow-init
   docker-compose -f docker-compose_airflow.yaml up -d
```

[6. Airflow DAG with PythonOperator and XComs](https://www.youtube.com/watch?v=IumQX-mm20Y)  
[7. Airflow TaskFlow API](https://www.youtube.com/watch?v=9y0mqWsok_4)  
[8. Airflow Catchup and Backfill](https://www.youtube.com/watch?v=OXOiUeHOQ-0)  
[9. Schedule Airflow DAG with Cron Expression](https://www.youtube.com/watch?v=tpuovQFUByk)  
[10. Airflow Connection and PostgresOperator](https://www.youtube.com/watch?v=S1eapG6gjLU)  
```
Conn Id: postgres_docker
Conn Type: Postgres
Host: host.docker.internal
Port: 5432 
```

[11. Add Python Dependencies via Airflow Docker Image Extending and Customizing](https://www.youtube.com/watch?v=0UepvC9X4HY)  
[12. AWS S3 Key Sensor Operator](https://www.youtube.com/watch?v=vuxrhipJMCk)  
[13. Airflow Hooks S3 PostgreSQL](https://www.youtube.com/watch?v=rcG4WNwi900)  

```
1. Clone this repo
2. Create dags, logs and plugins folder inside the project directory

mkdir ./dags ./logs ./plugins

3. Set user permissions for Airflow to your current user

echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

4. Install docker desktop application if you don't have docker running on your machine
```
[Download Docker Desktop Application for Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows)  
[Download Docker Desktop Application for Mac OS](https://hub.docker.com/editions/community/docker-ce-desktop-mac)  
```
If your admin account is different to your user account, you must add the user to the docker-users group:

 $ net localgroup docker-users <user> /add
```

```
5. Launch airflow by docker-compose

docker-compose up -d

6. Check the running containers

docker ps

7. Open browser and type http://http://172.27.181.205:8080 to launch the airflow webserver
```

## Reference  
[coder2j/airflow-docker](https://github.com/coder2j/airflow-docker)  

[https://stackoverflow.com/questions/70797971/docker-error-response-from-daemon-ports-are-not-available-listen-tcp-0-0-0-0](https://stackoverflow.com/questions/70797971/docker-error-response-from-daemon-ports-are-not-available-listen-tcp-0-0-0-0)  
```
docker run -p 5001:5000 flask_demo:v0

-p 5001:5000 basically means, bind port 5001 in my host machine with the port 5000 in the container. 
Since port 5000 already used in your host machine, then u can bind with another port example: port 5001
```

[DBeaver™ portable](https://portapps.io/app/dbeaver-portable/)  


# Airflow tutorial

## docker-compose Installation
```
$ sudo curl -L https://github.com/docker/compose/releases/download/v2.12.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

$ sudo chmod +x /usr/local/bin/docker-compose

$ sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

## Initialization
```
$ docker-compose up airflow-init
```
<img src="images/airflow_tutorial_docke-compose.png" width="900" height="200">

```
$ docker-compose -f docker-compose.yaml up -d
```
```
$ docker ps
```
<img src="images/airflow_tutorial_docke-compose_03.png" width="900" height="400">

## DGA
<img src="images/airflow_tutorial_docke-compose_02.png" width="900" height="400">

## Reference  
[Airflow を単体の docker container で立ち上げる posted at 2019-02-15](https://qiita.com/kysnm/items/feda7b8cca44bb7389ac)  
[用 Airflow & Flink 來開發 ETL 吧 系列](https://ithelp.ithome.com.tw/users/20161625/ironman/6233)  


# Airflow-Learning-English-tool
[ ChickenBenny/Airflow-Learning-English-tool ](https://github.com/ChickenBenny/Airflow-Learning-English-tool)

## update docker-compose.yml by Airflow-Learning-English-tool/docker-compose.yaml

<img src="images/airflow_learning_english_tool_01.jpg" width="900" height="300">


# Airflow-scraping-ETL-tutorial
[Airflow-scraping-ETL-tutorial](https://github.com/ChickenBenny/Airflow-scraping-ETL-tutorial?tab=readme-ov-file)  

<img src="https://camo.githubusercontent.com/2a5be8e536eb1118b089f1418fc9badf025f8f435ab923ae8a8ace0c61bf135a/68747470733a2f2f692e696d6775722e636f6d2f447448476f59742e706e67" width="900" height="200">

```
上證交所查看當日是否有交易紀錄

    股市有開盤
        Trigger爬蟲程式
        爬取交易資訊
        資料清洗
        存入資料庫 or csv file
        發送爬取消息
    股市沒開盤
        不做事
```
## Reference  
[Apache Airflow ile Telegram’a Bildirim Mesajı Gönderme Jun 18, 2024](https://kayademirs.medium.com/apache-airflow-ile-telegrama-bildirim-mesaj%C4%B1-g%C3%B6nderme-bf5fd99f65f2) 
[kayademirs /airflow-telegram-notifications](https://github.com/kayademirs/airflow-telegram-notifications)  
```
User Guide for Airflow Telegram Notifications
This GitHub repository contains a step-by-step guide for receiving notifications via Telegram using Apache Airflow. 
The guide covers the process from creating the Telegram bot to setting up the Airflow environment on Docker.
```

[Apache Airflow: ETL を容易にする](https://prohoster.info/ja/blog/administrirovanie/apache-airflow-delaem-etl-proshhe)  
[dmlogv/airflow-tutorial](https://github.com/dm-logv/airflow-tutorial)  

[tayonagithab/airflow_hw](https://github.com/tayonagithab/airflow_hw)  
[dmlogv/docker-airflow](https://github.com/dmlogv/docker-airflow)  


# How to Upload Files to Google Drive using Airflow  
[How to Upload Files to Google Drive using Airflow Mar 26, 2021](https://towardsdatascience.com/how-to-upload-files-to-google-drive-using-airflow-73d961bbd22)

*A Google account with admin privileges on GCP and the Google Workspace it belongs to* 

*An Airflow 2.0.x installation*

## 1. Configuring the Google Drive API and a creating service account on GCP

## 2. Configuring Domain-wide Delegation on our Google Workspace

## 3. Writing the code for our custom GoogleDriveOperator

## 4. Testing a minimal DAG that uploads a text file to our Google Drive account

## Reference  
[ChickenBenny/Airflow-tutorial](https://github.com/ChickenBenny/Airflow-tutorial)  

# Airflow import local module
[Importing local module (python script) in Airflow DAG  Jun 6, 2019](https://stackoverflow.com/questions/50150384/importing-local-module-python-script-in-airflow-dag)

```
In airflow.cfg, make sure the path in airflow_home is correctly set to the path 
the Airflow directory strucure is in.

Then Airflow scans all subfolders and populates them so that modules can be found.
```

Otherwise, just make sure the folder you are trying to import is in 
the Python path: How to use [PYTHONPATH](https://stackoverflow.com/questions/19917492/how-to-use-pythonpath)


# Failed to import custom python module in Airflow
[Failed to import custom python module in Airflow Jul 14, 2020](https://stackoverflow.com/questions/62868156/failed-to-import-custom-python-module-in-airflow)

So the Airflow folder structure looks like this:
```
airflow/  
    |_ dag/  
    |    |_ __init__.py  
    |    |_ my_first_DAG.py  
    |_ my_scripts/
    |    |_ __init__.py         
    |    |_  custom_script.py 
    |_ __init__.py 
```

Inside my_first_DAG.py I try:

```
from my_scripts import custom_script     
```

But I get the error: ModuleNotFoundError: No module named 'my_scripts'



The problem was that the PYTHONPATH was only getting set in local terminal, 
not for all programs. FIxed by adding it in

```
~/.bashrc

~/.profile

/etc/environment
```


# Airflow, Docker and Data Analysis
[AirflowとDockerで俺々データ分析基盤をつくってみた&Imageを公開してみた #kwskrb  2017-08-31](https://shinyorke.hatenablog.com/entry/airflow-docker#Production%E3%81%AA%E6%A7%8B%E6%88%90%E3%81%A7%E5%8B%95%E3%81%8B%E3%81%99%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AB)

## imageを取得する
```
$  docker pull shinyorke/airflow
```

## 単体で動かす
### webserver
```
$ docker run -p 8080:8080 --env-file=./env_example shinyorke/airflow webserver init
```

### scheduler
```
$  docker run --env-file=./env_example shinyorke/airflow scheduler init
```

### worker
```
$  docker run --env-file=./env_example shinyorke/airflow worker init
```


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


