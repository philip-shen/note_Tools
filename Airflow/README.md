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
      * [Reference](#reference-1)
   * [Airflow tutorial](#airflow-tutorial)
      * [docker-compose Installation](#docker-compose-installation)
      * [Initialization](#initialization)
      * [DGA](#dga)
      * [Reference](#reference-2)
   * [Airflow-Learning-English-tool](#airflow-learning-english-tool)
      * [update docker-compose.yml by Airflow-Learning-English-tool/docker-compose.yaml](#update-docker-composeyml-by-airflow-learning-english-tooldocker-composeyaml)
   * [How to Upload Files to Google Drive using Airflow](#how-to-upload-files-to-google-drive-using-airflow)
      * [1. Configuring the Google Drive API and a creating service account on GCP](#1-configuring-the-google-drive-api-and-a-creating-service-account-on-gcp)
      * [2. Configuring Domain-wide Delegation on our Google Workspace](#2-configuring-domain-wide-delegation-on-our-google-workspace)
      * [3. Writing the code for our custom GoogleDriveOperator](#3-writing-the-code-for-our-custom-googledriveoperator)
      * [4. Testing a minimal DAG that uploads a text file to our Google Drive account](#4-testing-a-minimal-dag-that-uploads-a-text-file-to-our-google-drive-account)
      * [Reference](#reference-3)
   * [Airflow import local module](#airflow-import-local-module)
   * [Failed to import custom python module in Airflow](#failed-to-import-custom-python-module-in-airflow)
   * [Airflow, Docker and Data Analysis](#airflow-docker-and-data-analysis)
      * [imageを取得する](#imageを取得する)
      * [単体で動かす](#単体で動かす)
         * [webserver](#webserver)
         * [scheduler](#scheduler)
         * [worker](#worker)
   * [Troubleshooting](#troubleshooting)
   * [Reference](#reference-4)
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
~~sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose~~

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

## Reference  
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

設定連接 port，兩個 5432，代表 docker 容器外和容器內的 port  
<img src="https://ithelp.ithome.com.tw/upload/images/20231002/20135427TDeEEi3YzW.png" width="500" height="300">

重新 Build Postgres 的服務
```
docker-compose up -d --no-deps --build postgres
```

*Airflow CLI 設定* 
```
docker exec -it <container_id> bash

airflow connections add 'local-db-cli' \
--conn-uri 'postgres://airflow:airflow@host.docker.internal:5432/postgres'
```

*Docker Compose 設定*
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

[[day18] 急！在線等！求解20 點！Airflow 安裝 Python 模組 2023-10-03](https://ithelp.ithome.com.tw/articles/10333330)  
[[Day19] Airflow Scheduler 排程爬坑筆記(上) 2023-10-04](https://ithelp.ithome.com.tw/articles/10334198)  
[[Day20] Airflow Scheduler 排程爬坑筆記(下) 2023-10-05](https://ithelp.ithome.com.tw/articles/10334705)  


[一段 Airflow 與資料工程的故事：談如何用 Python 追漫畫連載 2018-08-21](https://leemeng.tw/a-story-about-airflow-and-data-engineering-using-how-to-use-python-to-catch-up-with-latest-comics-as-an-example.html)  

[Airflow with Docker 容器部署 — part 2 Mar 26, 2019](https://medium.com/@cchangleo/airflow-with-docker-%E5%AE%B9%E5%99%A8%E9%83%A8%E7%BD%B2-part2-8ddb83dc2d4a)  
[cchangleo/docker-airflow](https://github.com/cchangleo/docker-airflow)

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


