Table of Contents
=================

   * [Table of Contents](#table-of-contents)
   * [InfluxDB](#influxdb)
         * [Installation](#installation)               
           * [Reference](#reference)
         * [DataSet Insertation](#dataset-insertation)               
           * [Reference](#reference-1)   
      * [Reference](#reference-2)
   * [Prometheus](#prometheus)
      * [Reference](#reference-3)
   * [OpenTSDB](#opentsdb)
      * [Reference](#reference-4)
   * [Troubleshooting](#troubleshooting)
   * [Reference](#reference-5)
   * [h1 size](#h1-size)
      * [h2 size](#h2-size)
         * [h3 size](#h3-size)
            * [h4 size](#h4-size)
               * [h5 size](#h5-size)
   * [Table of Contents](#table-of-contents-1)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)



# InfluxDB  

## Installation  
```
version: '3'

services:
  influxdb:
    container_name: influxdb
    image: influxdb:latest
    volumes:
      - ./influxDB/influxdb2:/var/lib/influxdb2:rw
    ports:
      - "8086:8086"
    
  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    #hostname: grafana
    ports:
      - 3000:3000
    volumes:
      - ./grafana/grafana:/var/lib/grafana

volumes:
  influxdb2:
```
```
localhost:3000でアクセスし、
user nameとpasswordを両方admin
```

### Reference  
[ファイナンス分野で時系列データベースinfluxDBを使う Python 時系列 Finance influxdb 2022-08-27](https://qiita.com/ixtlan001/items/c87e4b2c4a97d7dba800)
[ファイナンス分野でInfluxDB+Grafanaを使う（株価をローソク足表示） Python 時系列解析 Finance influxdb grafana 2022-08-27](https://qiita.com/ixtlan001/items/268dfab0d1ee21887602)  
```
データソースの追加(influxDBとの連携設定)

GrafanaのConfigurationメニュー→"Data sources"→"Add data source"をクリック。
下記項目を入力して"Save & test"をクリック。

    "Query Language" : "Flux"を選択
    "URL" : http://influxdb:8086
    "Basic Auth Details"のUserとPassword : influxDBのユーザー名とパスワード
    "Organization" : influxDBで登録しているorganization名
    "Token" : influxDBのAPI Tokenをコピ
```

```
Dashboard作成

画面左側のメニューからDashboards→New dashboard→Add a new panelを順に辿る。

query入力部分にFlux（influxDBのクエリ言語）で例えば下記を入力（Fordの株価の場合）:

from(bucket: "influxdb_stock_prices")
|> range(start: v.timeRangeStart, stop: v.timeRangeStop)
|> filter(fn: (r) => r["_measurement"] == "stock prices")
|> filter(fn: (r) => r["NAME"] == "ford")
|> filter(fn: (r) => r["SYMBOL"] == "F")

画面上部の時計マークの所をクリックしてFromをnow-2M、ToをnowにしてApply Time Rangeをクリック。

右上のパネルのタイプとして"Time series"が選ばれている所のドロップダウンメニューから"Candlestick"を選択。
```

```
Bollinger Band等の表示

以下はinfluxdbの_fieldにOHLCV以外の"Upper Bollinger Band"、"Lower Bollinger Band"が入っていることを前提としています。

    "Additional fields"で"Include"を選択
    "Point size"を1に変更（これはお好みで）

ここまででとりあえずOHLCV以外の線が表示されます。

    線の下を不透明にする
        "+ Add field override"をクリック
        "Fields with name"を選択
        "Upper Bollinger Band(base field name)"を選択
        "+ Add override property"で"Graph styles > Fill Opacity"を選択して20程度に設定
        "+ Add override property"で"Standard options > Color scheme"を選択して"Single color"を選択、右端のカラーパレット（default黒になってて見にくいです）で好みの色を選択

同様のことをLower Bollinger Bandに対しても繰り返します。
```

```
Legendテキストの変更

デフォールトではLegendに使われるテキストラベルが長たらしいので下記で変更できます。

    パネルのEdit画面で"Overrides"タブを開く。
    Add field overrideをクリック
    Fields with nameを選択
    変更したい変数を選択
    Add override propertyで"Standard options > Display name"を選択
    新しいテキストラベルを入力
```

[influxdb-flux-change-or-alias-legend-label-from-temp-host-xx-topic-yy-just-to-yy](https://community.grafana.com/t/influxdb-flux-change-or-alias-legend-label-from-temp-host-xx-topic-yy-just-to-yy/49596)  


[influxdb+grafanaで変数を利用して個別の株価パネルを複製  Python 時系列解析 Finance influxdb grafana 2022-08-28](https://qiita.com/ixtlan001/items/7ba21c1f94fc4547fcca)  
[Influxdb 2.0 how to get a tag all values? Apr 25, 2020](https://stackoverflow.com/questions/61424275/influxdb-2-0-how-to-get-a-tag-all-values)  


[Docker玩轉InfluxDB 2022-01-15](https://wenwender.wordpress.com/2022/01/15/docker%e7%8e%a9%e8%bd%89influxdb/)  
[Docker玩轉Grafana(feat. InfluxDB) 2022-01-18](https://wenwender.wordpress.com/2022/01/18/docker%e7%8e%a9%e8%bd%89grafanafeat-influxdb/)  
[Docker建立 BTC 即時價格Dashboard 2022-01-19](https://wenwender.wordpress.com/2022/01/19/docker%e5%bb%ba%e7%ab%8b-btc-%e5%8d%b3%e6%99%82%e5%83%b9%e6%a0%bcdashboard/)  

```
補充: (因為幣安的API請求到的資料是timestamp，這裡我們一律將其轉成datetime的格式)
	
datetime.datetime.fromtimestamp(ds[0]/ 1e3)
```

```
Grafana Dashboard

這裡一樣的步驟是，先到InfluxDB取得SQL語法，再把它貼到Grafana去，這裡我就不再示範，如果有忘記的可以去看這篇文 Docker玩轉Grafana，有個小提醒是，記得要先去influxDB建立bucket，不然資料會insert不進去喔。

最後呈現的結果大概會像這樣，而且資料是會不斷的更新的。
```

[透過Grafana繪製即時BTC K線圖 2022-02-13](https://wenwender.wordpress.com/2022/02/13/%e9%80%8f%e9%81%8egrafana%e7%b9%aa%e8%a3%bd%e5%8d%b3%e6%99%82btc-k%e7%b7%9a%e5%9c%96-2/)
```
實作
傳送門
首先，需要先確認Grafana的版本>8.3，因為K線的Panel是Grafana在8.3版本後新增的功能。
第一步，仍然是要將BTC的資料寫進Influxdb裡，詳細的細節可以參考此篇文章 。
第二步，在Grafana中建立Panel(Candlestick)，並且建立搜索。
```
```
from(bucket: "cryptocurrency") |> range(start: v.timeRangeStart, stop: v.timeRangeStop) |> filter(fn: (r) => r["_measurement"] == "bitcoin") |> filter(fn: (r) => r["type"] == "5m")
```
```
大家在蒐集資料的時候，可能會有自己的measurement或type，記得要調整。
```

```
另外，我們也想要同時看到移動平均線。

Influxdb本身的Query就有支援Moving Average，因此我們只要再新增這段Query，就可以獲得以收盤價繪製的移動平均線。如果要畫m10或m20，只要修改movingAverage(n: n)的數字即可。
```
```
from(bucket: "cryptocurrency")  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)  |> filter(fn: (r) => r["_measurement"] == "bitcoin")  |> filter(fn: (r) => r["_field"] == "close")  |> filter(fn: (r) => r["type"] == "$5m")  |> rename(columns: {_field: "m5"})  |> movingAverage(n: 5)
```


[InfluxDB記憶體耗用居高不下(踩雷筆記) 2022-01-27](https://wenwender.wordpress.com/2022/01/27/influxdb%e8%a8%98%e6%86%b6%e9%ab%94%e8%80%97%e7%94%a8%e5%b1%85%e9%ab%98%e4%b8%8d%e4%b8%8b%e8%b8%a9%e9%9b%b7%e7%ad%86%e8%a8%98/)  

```
整理一下InfluxDB和PostgresDB的差別和比較以及實際使用InfluxDB上遇到的問題。

   1. InfluxDB 針對時間序列進行了大量優化。所以當寫入量很大時可能不會遇到很多問題，它使用壓縮來使用更少的空間。
   2. InfluxDB 是為時間序列製作的 NOSQL 數據庫
   3. 刪除數據需要較高的耗能(No-SQL的特性)
   4. “InfluxDB 不支持 UPDATE 語句。但是，在相同時間戳重新插入完全相同的key值，此時將用新的值去代替舊的值。
   5. 儲存同樣數量的時間序列數據，與 PostgreSQL 相比，InfluxDB 僅使用約 1/4 的空間。
   6. 查詢大量數據時，InfluxDB被打爆(因為沒有Index)

問題一:記憶體耗用高
問題二:插入時間跨度長的數據會造成性能下降和內存耗盡
```
[Grafana實時呈現攝影機畫面 2022-01-28](https://wenwender.wordpress.com/2022/01/28/grafana%e5%af%a6%e6%99%82%e5%91%88%e7%8f%be%e6%94%9d%e5%bd%b1%e6%a9%9f%e7%95%ab%e9%9d%a2/)  

[python-binance](https://python-binance.readthedocs.io/en/latest/)  

[Paper Reading:利用CNN神經網路來交易ETF 2019-09-15](https://wenwender.wordpress.com/2019/09/15/%e8%ab%96%e6%96%87%e9%96%b1%e8%ae%80%e5%88%a9%e7%94%a8cnn%e7%a5%9e%e7%b6%93%e7%b6%b2%e8%b7%af%e4%be%86%e4%ba%a4%e6%98%93etf/)  
[實作:透過LSTM預測股票 2019-10-18](https://wenwender.wordpress.com/2019/10/18/%e5%af%a6%e4%bd%9c%e9%80%8f%e9%81%8elstm%e9%a0%90%e6%b8%ac%e8%82%a1%e7%a5%a8/)   

## DataSet Insertation  
[grap_taiwan_stock_list.py](grap_taiwan_stock_list.py)  
[init_influxdb.py](init_influxdb.py)  
[update_influxdb.py](update_influxdb.py)  

### Reference  
[x01963815/grab-stocks-data-to-influxdb May 1, 2018](https://github.com/x01963815/grab-stocks-data-to-influxdb)
```
從 Google Finance 上抓取台灣上市公司股價資料，並且存入 InfluxDB 資料庫中

init_influxdb.ipynb：初始化InfluxDB股價資料庫
update_influxdb.ipynb：更新InfluxDB股價資料庫
```

## Reference  

[Distributed-System-Spark](https://github.com/aaron1aaron2/NCCU_110-2_Distributed-System-Spark_final?tab=readme-ov-file)  
```
本專案以Spark-MLlib API實現爬蟲資料缺失自動補救機制，先透過FinMind API爬取每日股票，將資料存入Influx Database，當爬蟲部分出現錯誤而無法依序取得資料時，系統將自動呼叫MLlib API存取Database資料並進行預測，再將預測結果寫回Database，最後以Plotly API 和 Dash API進行資料視覺化比較有補救與未補救的差異，以下為我們整體專案的介紹和相關API的安裝流程。
```

[MarkhamLee/internet-and-iot-data-platform Commits on Sep 16, 2024](https://github.com/MarkhamLee/internet-and-iot-data-platform)  
```
Using Airflow, Grafana, InfluxDB, Node-RED & Postgres to bring together useful information from a variety of sources, 
e.g., finance, weather, task management and IoT devices 
```
[sruon/telegraf-stocks Jan 27, 2022](https://github.com/sruon/telegraf-stocks)  
```
Retrieve Stock infos from Yahoo Finance in a format ready to consume for Telegraf - InfluxDB.
```
[hilli/finance-influxdb Aug 27, 2020](https://github.com/search?q=InfluxDB++finance&type=repositories)
```
Daemon that will import Equity (Stocks) data from Yahoo Finance and insert it into InfluxDB
```
[11harini04/StockTick Jun 23, 2021](https://github.com/11harini04/StockTick)  
```
Scraping stock data of Neyveli India Limited (NLCINDIA) from Yahoo Finance for storing it in InfluxDB, querying and forecasting the prices of the stock for the upcoming days. 
STEPS:
   1. Web Scraping data from Yahoo Finance.
   2. Since stock data is time series data, it is inserted into InfluxDB, which is a time series database.
   3. Data is queried and forecasted using the following models:
      Autoregressive integrated moving average (ARIMA)
      Long Short Term Memory (LSTM)
   4. Smoothing using Moving Average to identify trends in the stock.
   5. Risk analysis was done on the stock by finding the Sharpe ratio and Sortino ratio of the stock.
```

[InfluxDB 3.0 Python Client](https://github.com/InfluxCommunity/influxdb3-python)  
[influxdb-client-python](https://github.com/influxdata/influxdb-client-python)  
```
This repository contains the Python client library for use with InfluxDB 2.x and Flux
```
[gusutabopb/aioinflux  Aug 5, 2023](https://github.com/gusutabopb/aioinflux)
```
Asynchronous Python client for InfluxDB

For InfluxDB v2+ support, please use the official Python client library.

Asynchronous Python client for InfluxDB. Built on top of aiohttp and asyncio. 
Aioinflux is an alternative to the official InfluxDB Python client.
```
[AdvancedClimateSystems/inflow Commits on Jan 24, 2024](https://github.com/AdvancedClimateSystems/inflow)  
```
Simple python InfluxDB client library

A simple InfluxDB Python client library. It is an alternative for the official InfluxDB Python client library.

Inflow officially supports Python 2.7 and up, but the latest Python 3 version is recommended.
InfluxDB is supported from version 1.0 and up.
```
[wuan/klimalogger Commits on Jan 28, 2024](https://github.com/wuan/klimalogger)
```
a climate sensor logger client for a InfluxDB backend written in python
```

[Raspberry Pi上のInfluxDBに格納したデータをGrafanaで可視化する（Chronografとの比較も）RaspberryPi influxdb grafana IoT Chronograf 2020-05-29](https://qiita.com/yoroyasu/items/5893849a896aec6da25c)  

[InfluxDB 2016-01-06](http://yume190.github.io/2016/01/06/InfluxDB/)  
```
時序性資料庫。拿來監看 Metric 還不錯！
```

# Prometheus  

## Reference    
[RaspberryPi4 influxDBとGrafana編 RaspberryPi influxdb grafana 2023-05-05](https://qiita.com/kanon700/items/e3a8a1cea4bcd635a002)  

[【Grafana】 基礎から徹底解説 〜 実際に導入までしてみる 〜 監視 grafana prometheus オープンソース 視覚化 2020-05-13](https://qiita.com/MetricFire/items/bbf10dbd60c6b85ccee0)  
[子供がPCで遊んでいないかPrometheusで監視する 育児 prometheus AlertManager 2024-04-01](https://qiita.com/ipppppei/items/6a0958de500ffc634c94)  

[Owner avatar 1102_Dist_Sys Prometheus 監控和 Grafana 視覺化及報警 ](https://github.com/kebwlmbhee/1102_Dist_Sys)  

[Grafana Agent によるメトリクス収集と Grafana による可視化に入門する grafana Prometheus 2024-04-11](https://qiita.com/Shigai/items/c80281c2b965b88582c7)  
[Grafana®とは？ MySQL PostgreSQL grafana ClickHouse OpenSearch 2023-10-30](https://qiita.com/tomozilla/items/cd8eee21fb7d032c49e4)  
[grafana dashboard で環境差分を扱う Tips grafana prometheus 2024-06-01](https://qiita.com/hiroakiyoshii/items/ff4e82ba5acea78cefc7)  
[Prometheus + Node_exporter + Grafanaでシステム管理 grafana prometheus node_exporter 2024-03-13](https://qiita.com/Charon9/items/09745a2ca1279045f10f)  
[家計支出をGrafanaで可視化 PostgreSQL Docker grafana 2024-03-24](https://qiita.com/nagomiita/items/792204beb9c10e542fa9)  
[[Grafana 7.x] データベースを Sqlite3 から MySQL へ移行 (マイグレーション) する MySQL SQLite3 grafana 2021-02-18](https://qiita.com/sho7650/items/b5022313fc473a938a37)  
[Linux: データ可視化ソフト「Grafana」を無料インストールしてみた＋「Prometheus」と連携させてみた Bash Linux grafana prometheus 2023-11-05](https://qiita.com/frozencatpisces/items/f6e331c1c1c14be7275d)  
[PrometheusのExporterをPythonで作る。Client Library無しで Python prometheus 2022-06-30](https://qiita.com/rk05231977/items/f37ce713c06c170715f7)  

[Prometheus Python Client](https://github.com/prometheus/client_python?tab=readme-ov-file)  
[如何用python实时监控股票，并且持续扫描大盘？ Prometheus 2023-05-20](https://blog.csdn.net/m0_59164520/article/details/130778612)  


# OpenTSDB    

## Reference    


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



