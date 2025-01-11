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
   * [Airflow, Google Sheets](#airflow-google-sheets) 
      * [1. Service Account Configuration](#1-service-account-configuration)
      * [2. Airflow Configuration](#2-airflow-configuration)
      * [2.1 Adding Google Connection to your Airflow](#21-adding-google-connection-to-your-airflow)  
      * [2.2 Errors when testing the API connection](#22-errors-when-testing-the-api-connection)  
      * [3. DAG Creation](#3-dag-creation)  
      * [Reference](#reference-7)
   * [Airflow, Yahoo Finance](#airflow-yahoo-finance)
      * [1. Checking if Yahoo API is Available](#1-checking-if-yahoo-api-is-available)  
      * [2. Fetching Stock Prices](#2-fetching-stock-prices) 
      * [3. Storing Data in MinIO](#3-storing-data-in-minio)    
      * [4. Data Transformation with Spark](#4-data-transformation-with-spark)  
      * [5. Loading Data to Postgres](#5-loading-data-to-postgres)    
      * [6. Notifications via Slack](#6-notifications-via-slack)  
      * [Reference](#reference-8)
   * [Airflow, Docker and Data Analysis](#airflow-docker-and-data-analysis)
      * [imageを取得する](#imageを取得する)
      * [単体で動かす](#単体で動かす)
         * [webserver](#webserver)
         * [scheduler](#scheduler)
         * [worker](#worker)
   * [SSL on Airflow](#ssl-on-airflow)  
      * [Reference](#reference-9)       
   * [Airflow on Raspberry Pi](#airflow-on-raspberry-pi)  
      * [Reference](#reference-10)      
   * [Troubleshooting](#troubleshooting)
   * [Reference](#reference-11)
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
sudo curl -L "https://github.com/docker/compose/releases/download/v2.32.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

#給予執行權限
sudo chmod +x /usr/local/bin/docker-compose
sudo pip install docker-compose  

#檢查版本
docker-compose version
```

## troubleshooting  
```
TypeError: kwargs_from_env() got an unexpected keyword argument 'ssl_version'
```
*Update Docker-Compose to latest version*
```
$ pip list | grep docker
docker                7.1.0
docker-compose        1.29.2
docker-py             1.10.6
docker-pycreds        0.4.0
dockerpty             0.4.1
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

    Run docker compose down --volumes --remove-orphans 
    command in the directory you downloaded the docker-compose.yaml file
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
[gontcharovd/google-drive-operator](https://github.com/gontcharovd/google-drive-operator)  


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


# Airflow, Google Sheets  
## 1. Service Account Configuration  

## 2. Airflow Configuration  
Dockerfile
```
FROM apache/airflow:2.5.1

USER airflow

RUN pip install gspread
```
### 2.1 Adding Google Connection to your Airflow    
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*XiyFtX1fgXITcY1QOPDtOg.png" width="900" height="200">  

```
   * Connection Id: Here you will put the name you prefer for your connection
   
   * Connection Type: You should select the Google Cloud option
   
   * Project Id: You will enter the id of your project
   
   * Keyfile JSON: Here you will paste the credentials that you downloaded
   
   * Scopes: paste https://www.googleapis.com/auth/drive
```

<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*HLTCfpoXhSRWgbQm5P1lxA.png" width="900" height="400">

/*if your connection is ok:*/  
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*yfbeHT_AaFy6hl6cxy7FxA.png" width="900" height="400">

### 2.2 Errors when testing the API connection  
/*docker-compose.yml*/
```
volumes:    
  - /etc/timezone:/etc/timezone:ro
  - /etc/localtime:/etc/localtime:ro
```

## 3. DAG Creation  
```
data = {
            "products": ["product_1", "product_2", "product_3"],
            "price": [50, 40, 45],
        }

df = pd.DataFrame(data)
```

```
hook = GoogleBaseHook(gcp_conn_id="google_conn_id")
credentials = hook.get_credentials()
google_credentials = gspread.Client(auth=credentials)
```

```
sheet = google_credentials.open("Products - Data")

worksheet = sheet.worksheet("products-data")

worksheet.update([df.columns.values.tolist()] + df.values.tolist())
```

/*Errno 13 - Permission denied: '/opt/airflow/logs/scheduler*/
[Errno 13 - Permission denied: '/opt/airflow/logs/scheduler](https://github.com/helm/charts/issues/23589)  
```
 "chmod -R 777 /opt"
```

```
 mkdir -p dags logs plugins
 chown 50000:50000 dags logs plugins 
```

## Reference  
[Gspread in Airflow  Jul 15, 2023](https://medium.com/@camila-marquess/gspread-in-airflow-3728abe4b617)  

[camila-marquess/airflow-gspread-dag](https://github.com/camila-marquess/airflow-gspread-dag)  
[camila-marquess/estudos-airflow](https://github.com/camila-marquess/estudos-airflow)  

[How to connect Google Cloud Composer (Airflow) with Google Sheets and extract the info to Google Storage (bucket) Mar 30, 2022](https://stackoverflow.com/questions/71681902/how-to-connect-google-cloud-composer-airflow-with-google-sheets-and-extract-th)  

[How to ETL mongodb To Google Sheets using Airflow Jun 15, 2024](https://medium.com/@miller.yoon/how-to-etl-mongodb-to-google-sheets-using-airflow-b54c24484737)  
[ssssyyyoon/mongo_to_gspread](https://github.com/ssssyyyoon/mongo_to_gspread)  

[Airflow: FileNotFoundError: [Errno 2] No such file or directory:](https://www.reddit.com/r/docker/comments/ow3j8l/airflow_filenotfounderror_errno_2_no_such_file_or/?rdt=46398)  
[Volumes](https://docs.docker.com/engine/storage/volumes/) 
```
By design docker containers can't interact directly with the host machine's file system. 
For the container to be able to "see" this file you will have to use a volume.
https://docs.docker.com/storage/volumes/

I suggest putting the CSV file in a separate directory from the DAGs, say D:\airflow\data, 
then adding a volume to the list in the compose file you linked to, e.g.

volumes:
- ./dags:/opt/airflow/dags
- ./logs:/opt/airflow/logs
- ./plugins:/opt/airflow/plugins
- ./data:/opt/airflow/data

Then in your DAG code point to "/opt/airflow/data/data_2012.csv".
```

# Airflow, Yahoo Finance  
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*J41FiKV5PnO-4TqDCPvflw.jpeg" width="900" height="300">

## 1. Checking if Yahoo API is Available  

## 2. Fetching Stock Prices 

## 3. Storing Data in MinIO  

## 4. Data Transformation with Spark  

## 5. Loading Data to Postgres  

## 6. Notifications via Slack

## Reference  
[Automating Stock Market Data Pipeline with Apache Airflow, MinIO, Spark, and Postgres Sep 13, 2024](https://medium.com/@mehran1414/automating-stock-market-data-pipeline-with-apache-airflow-minio-spark-and-postgres-b67f7379566a)  
[Mehranmzn/stock_market_prices](https://github.com/Mehranmzn/stock_market_prices)  

[avilares-stack/airflow-google-sheets-data-loader Aug 16, 2023](https://github.com/avilares-stack/airflow-google-sheets-data-loader)  
[ashish1104/options_dat_yahoo_fin_airflow Sep 29, 2023](https://github.com/ashish1104/options_dat_yahoo_fin_airflow)  
[seepala98/Churn_Data_Enginering Jan 3, 2025](https://github.com/seepala98/Churn_Data_Enginering)  
```
Data Engineering for Churn Analysis Using Google Sheets, Airflow, Bigquery, GCS and Looker 
```
```
Setup Airflow environment.

This is the site used to setup the environment locally: https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

   Install Docker (https://docs.docker.com/desktop/setup/install/windows-install/)

   Install Airflow locally using Docker Compose (https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
```

```   
   SetUp steps:
      fetch docker-compose for airflow setup: curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.4/docker-compose.yaml'
      
      create necessary folders: mkdir ./dags ./logs ./plugins ./config
      
      setip environment variable: export AIRFLOW_UID=$(id -u)
      
      Initialize Airflow: docker-compose up airflow-init
      
      Docker compose to spin up the environment: docker-compose up -d
```

[sheoran19 /yahoo-airflow-data-engineering-project Mar 18, 2024](https://github.com/sheoran19/yahoo-airflow-data-engineering-project)  
```
Yahoo Data Pipeline using Airflow
```
```
.              
├── airflow  
|   └── airflow.cfg                           
│   └── dags 
|       └── yahoo_dag.py
│
├── app                                 
│   ├── main.py                            
│   ├── models.py                          
│   └── database.py 
│
├── docker    
│   ├── Dockerfile                        
│   └── docker-compose.yaml                           
│
├── etl                                 
|   └── yahoo_data_etl.py 
|
├── .env                               
├── README.md                          
├── application_default_credentials.json 
├── architecture_diagram.png            
├── market_codes.csv                  
├── requirements.txt     
```
<img src="https://github.com/sheoran19/yahoo-airflow-data-engineering-project/raw/main/architecture_diagram.png" width="900" height="300">

[Mapa0/airflow-amazonads-postgres-pipeline Dec 11, 2024](https://github.com/Mapa0/airflow-amazonads-postgres-pipeline)
```
ETL pipeline that extracts data from Amazon Ads API, transforms and loads it into Google Sheets. All orchastrated via Airflow.
```
[dodinovembri/airflow_google_sheets Jan 12, 2022](https://github.com/dodinovembri/airflow_google_sheets)  


[Airflow For Data Extraction Feb 23, 2022](https://medium.com/@digvijay-gaikwad/airflow-for-data-extraction-cf39415b5d50)  
[digvijay13873/airflow-docker](https://github.com/digvijay13873/airflow-docker) 

[[5/22] TIL - Airflow DAG 작성하기 2024/5/22](https://velog.io/@hjjwa1234/0522TIL)  
```
docker exec --user root -it [컨테이너ID] sh
```
[Yahoo Finance API DAG - 1](https://velog.io/@hjjwa1234/0522TIL#yahoo-finance-api-dag---1)  
[Source code](https://velog.io/@hjjwa1234/0522TIL#%EC%BD%94%EB%93%9C)

[Yahoo Finance API DAG - 2](https://velog.io/@hjjwa1234/0522TIL#yahoo-finance-api-dag---2)  
[Source code](https://velog.io/@hjjwa1234/0522TIL#%EC%BD%94%EB%93%9C-1)


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


# SSL on Airflow  
```
airflow-webserver:
    <<: *airflow-common
    command: webserver --ssl-cert domain.cer --ssl-key domain.key
    ports:
      - "8080:8080"
    healthcheck:
      test: ["CMD", "curl", "--fail", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 30s
    restart: always
    depends_on:
      <<: *airflow-common-depends-on
      airflow-init:
        condition: service_completed_successfully
```

## Reference  
[Airflow 2.5.3, unable to specify ssl key and cert for webserver in Docker based installation #31089](https://github.com/apache/airflow/discussions/31089)

[How to enable SSL on Apache Airflow?](https://stackoverflow.com/questions/47883769/how-to-enable-ssl-on-apache-airflow)

[Question Regarding SSL Errors Inside Container](https://www.reddit.com/r/docker/comments/jetrdn/question_regarding_ssl_errors_inside_container/)  


# Airflow on Raspberry Pi  

```
$ AIRFLOW_VERSION=2.1.2
$ PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
$ CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
$ sudo pip3 install "apache-airflow[async,postgres,redis,slack,discord]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
$ sudo apt-get install redis postgresql
```

```
$ mkdir ~/airflow
$ cd ~/airflow
$ mkdir dags
$ export AIRFLOW_HOME=$(pwd)
$ airflow db init
```

```
Open airflow.cfg with any text editor, then:* set your favorite executor in "executor = ..."
* replace "sql_alchemy_conn = sqlite:..." with "sql_alchemy_conn = postgresql+psycopg2://airflow:password@localhost:5432/airflow"
* replace "result_backend = ..." to "result_backend = db+postgresql+psycopg2://airflow:password@localhost:5432/airflow"
```

```
$ sudo -u postgres psqlpostgres=# CREATE USER airflow PASSWORD 'password';
postgres=# CREATE DATABASE airflow;
postgres=# GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO airflow;
postgres=# EXIT
```

```
$ cd ~/airflow
$ export AIRFLOW_HOME=$(pwd)
$ airflow db init
```

```
$ cd ~/airflow
$ export AIRFLOW_HOME=$(pwd)
$ airflow webserver
```

```
$ sudo su
# systemd-tmpfile --create
# systemctl daemon-reload
# systemctl enable .... # enable whatever service units as required
# systemctl start .... # start whatever service units as required
# systemctl status .... # check if the services is running 
```

<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*2_CWBNVt-RVr5i0NIlYTHw.png" width="900" height="300">

## Reference 
[Apache Airflow, Raspberry Pi OS & Systemd Aug 20, 2021](https://medium.com/@phutidus/apache-airflow-raspberry-pi-os-systemd-90ef3ed20a87)  

[Docker 多架構 image Part 2 (Docker multi-arch image — build on multiple physical machines) Feb 14, 2022](https://medium.com/@phutidus/docker-%E5%A4%9A%E6%9E%B6%E6%A7%8B-image-part-2-docker-multi-arch-image-build-on-multiple-physical-machines-d82828953015)  

[建立 Docker 多架構 image (Building Docker multi-arch image) Aug 4, 2021](https://medium.com/@phutidus/%E5%BB%BA%E7%AB%8B-docker-%E5%A4%9A%E6%9E%B6%E6%A7%8B-image-building-docker-multi-arch-image-9b79e611da7a)  

[資產價格走勢圖 HD Remaster Nov 6, 2022](https://medium.com/@phutidus/%E8%B3%87%E7%94%A2%E5%83%B9%E6%A0%BC%E8%B5%B0%E5%8B%A2%E5%9C%96-hd-remaster-f2c9f89a7b31) 

[Install Airflow 2 on a Raspberry Pi (using Python 3.x) July 21, 2021](https://pedromadruga.com/posts/airflow-install/)  

[Apache Airflow Running on a Raspberry PI Jul 7, 2020](https://medium.com/the-kickstarter/apache-airflow-running-on-a-raspberry-pi-2e061f6c3655)  

[Setting up airflow on a Raspberry Pi 4 (Part 1)](http://www.thecrustyengineer.com/home/post/setting_up_airflow_on_a_raspberry_pi_4_part_1)  

[Setting up airflow on a Raspberry Pi 4 (Part 2)](http://www.thecrustyengineer.com/post/setting_up_airflow_on_a_raspberry_pi_4_part_2)  

[justinwagg /docker-airflow-tutorial](https://github.com/justinwagg/docker-airflow-tutorial)  

[puckel /docker-airflow ](https://github.com/puckel/docker-airflow)  


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


