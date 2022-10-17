
Table of Contents
=================

   * [Purpose](#purpose)
   * [Airflow tutorial](#airflow-tutorial)
      * [Setup](#setup)
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
   * [Table of Contents](#table-of-contents)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)
# Purpose  
Take note of Airflow stuffs  

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





