
Table of Contents
=================

   * [Table of Contents](#table-of-contents)
   * [Purpose](#purpose)
   * [Airflow Docker](#airflow-docker)
      * [Install Docker CE](#install-docker-ce)
      * [Install Docker-Compose](#install-docker-compose)
      * [Docker Pull](#docker-pull)
      * [Docker Delopy Airflow CeleryExecutor Mode](#docker-delopy-airflow-celeryexecutor-mode)
         * [Update Dockerfile](#update-dockerfile)
         * [Update docker-compose-CeleryExecutor.yml](#update-docker-compose-celeryexecutoryml)
         * [Update Airflow config](#update-airflow-config)
   * [Airflow tutorial](#airflow-tutorial)
      * [Setup](#setup)
      * [DGA](#dga)
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
[Airflow with Docker 容器部署 — part 2](https://medium.com/@cchangleo/airflow-with-docker-%E5%AE%B9%E5%99%A8%E9%83%A8%E7%BD%B2-part2-8ddb83dc2d4a)

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
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

#給予執行權限
sudo chmod +x /usr/local/bin/docker-composesudo pip install docker-compose  

#檢查版本
docker-compose version
```

## Docker Pull
```
docker pull puckel/docker-airflow

#or 

get from gitgit clone https://github.com/puckel/docker-airflow.git
```

## Docker Delopy Airflow CeleryExecutor Mode

### Update Dockerfile


### Update docker-compose-CeleryExecutor.yml 
```

```

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


[一段 Airflow 與資料工程的故事：談如何用 Python 追漫畫連載 2018-08-21(Tue)](https://leemeng.tw/a-story-about-airflow-and-data-engineering-using-how-to-use-python-to-catch-up-with-latest-comics-as-an-example.html)

# Airflow tutorial
[airflowのチュートリアルをしてみた updated at 2019-05-19](https://qiita.com/raqwel/items/37052d8d7d3fb1b7780b)

## Setup
```
git clone git@github.com:puckel/docker-airflow.git
```

```
docker build --rm --build-arg AIRFLOW_DEPS="datadog,dask" --build-arg PYTHON_DEPS="flask_oauthlib>=0.9" -t puckel/docker-airflow .
```

```
docker run -d -p 8080:8080 puckel/docker-airflow webserver
```
<img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F100993%2Ff506b702-5532-4f0b-9eb3-df9764071c40.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=1c72ce2863bc9a0c7a467f58abe14db4" width="800" height="400">

## DGA
<img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F100993%2F53f814ca-3c05-77a9-6e0e-392ae42a74f6.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=1bc15fa50f8bd631f6f501371e2eceb2" width="800" height="400">

[Airflow をさわってみた - Docker でのチュートリアルの実行 (Mac OSX 環境) posted at 2019-08-03](https://qiita.com/smatsumt/items/fe156936121185a7db0e)

[Airflow を単体の docker container で立ち上げる posted at 2019-02-15](https://qiita.com/kysnm/items/feda7b8cca44bb7389ac)

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

