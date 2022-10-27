
Table of Contents
=================

   * [Table of Contents](#table-of-contents)
   * [Purpose](#purpose)
   * [Airflow Docker](#airflow-docker)
      * [Install Docker CE](#install-docker-ce)
      * [Install Docker-Compose](#install-docker-compose)
      * [Docker Pull Image](#docker-pull-image)
      * [Docker Delopy Airflow CeleryExecutor Mode](#docker-delopy-airflow-celeryexecutor-mode)
         * [Update Dockerfile](#update-dockerfile)
         * [Update docker-compose-CeleryExecutor.yml](#update-docker-compose-celeryexecutoryml)
         * [Update Airflow config](#update-airflow-config)
   * [Airflow tutorial](#airflow-tutorial)
      * [docker-compose Installation](#docker-compose-installation)
      * [Initialization](#initialization)
      * [DGA](#dga)
   * [How to Upload Files to Google Drive using Airflow](#how-to-upload-files-to-google-drive-using-airflow)
      * [1. Configuring the Google Drive API and a creating service account on GCP](#1-configuring-the-google-drive-api-and-a-creating-service-account-on-gcp)
      * [2. Configuring Domain-wide Delegation on our Google Workspace](#2-configuring-domain-wide-delegation-on-our-google-workspace)
      * [3. Writing the code for our custom GoogleDriveOperator](#3-writing-the-code-for-our-custom-googledriveoperator)
      * [4. Testing a minimal DAG that uploads a text file to our Google Drive account](#4-testing-a-minimal-dag-that-uploads-a-text-file-to-our-google-drive-account)
   * [Airflow import local module](#airflow-import-local-module)
   * [Failed to import custom python module in Airflow](#failed-to-import-custom-python-module-in-airflow)
   * [Airflow, Docker and Data Analysis](#airflow-docker-and-data-analysis)
      * [imageを取得する](#imageを取得する)
      * [単体で動かす](#単体で動かす)
         * [webserver](#webserver)
         * [scheduler](#scheduler)
         * [worker](#worker)
   * [Troubleshooting](#troubleshooting)
   * [Reference](#reference)
   * [h1 size](#h1-size)
      * [h2 size](#h2-size)
         * [h3 size](#h3-size)
            * [h4 size](#h4-size)
               * [h5 size](#h5-size)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)


# Purpose  
Take note of Airflow stuffs  

# Airflow Docker
[Airflow with Docker 容器部署 — part 2 Mar 26, 2019](https://medium.com/@cchangleo/airflow-with-docker-%E5%AE%B9%E5%99%A8%E9%83%A8%E7%BD%B2-part2-8ddb83dc2d4a)
[cchangleo/docker-airflow](https://github.com/cchangleo/docker-airflow)

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


[一段 Airflow 與資料工程的故事：談如何用 Python 追漫畫連載 2018-08-21](https://leemeng.tw/a-story-about-airflow-and-data-engineering-using-how-to-use-python-to-catch-up-with-latest-comics-as-an-example.html)

# Airflow tutorial
[ChickenBenny/Airflow-tutorial](https://github.com/ChickenBenny/Airflow-tutorial)

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


[Airflow を単体の docker container で立ち上げる posted at 2019-02-15](https://qiita.com/kysnm/items/feda7b8cca44bb7389ac)


# How to Upload Files to Google Drive using Airflow  
[How to Upload Files to Google Drive using Airflow Mar 26, 2021](https://towardsdatascience.com/how-to-upload-files-to-google-drive-using-airflow-73d961bbd22)

*A Google account with admin privileges on GCP and the Google Workspace it belongs to* 

*An Airflow 2.0.x installation*

## 1. Configuring the Google Drive API and a creating service account on GCP

## 2. Configuring Domain-wide Delegation on our Google Workspace

## 3. Writing the code for our custom GoogleDriveOperator

## 4. Testing a minimal DAG that uploads a text file to our Google Drive account


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


