Table of Contents
=================

   * [Table of Contents](#table-of-contents)
   * [MongoDB Installation](#mongodb-installation)
      * [Register Windows Services](#register-windows-services)
   * [MongoDB Configuration](#mongodb-configuration)
      * [mongodb.conf](#mongodbconf)
   * [RethinkDB](#rethinkdb)
      * [Realtime 讀取資料](#realtime-讀取資料)
         * [1st original](#1st-original)
         * [2nd insert to rethinkdb](#2nd-insert-to-rethinkdb)
         * [3rd update status](#3rd-update-status)
      * [篩選資料](#篩選資料)
         * [1st insert data](#1st-insert-data)
         * [2nd cursor next](#2nd-cursor-next)
   * [Troubleshooting](#troubleshooting)
   * [Reference](#reference)
   * [h1 size](#h1-size)
      * [h2 size](#h2-size)
         * [h3 size](#h3-size)
            * [h4 size](#h4-size)
               * [h5 size](#h5-size)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)

# MongoDB Installation  
[MongoDB的安装配置（zip版）2019-11-13](https://blog.csdn.net/J_wb49/article/details/103050462?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param)

## Register Windows Services  
```
mongod --config E:\MongoDB\mongodb-win32-x86_64-2008plus-ssl-3.4.23\mongo.conf --install --serviceName “MongoDB”
```

![alt tag](https://img-blog.csdnimg.cn/20191113154953429.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0pfd2I0OQ==,size_16,color_FFFFFF,t_70)

![alt tag](https://img-blog.csdnimg.cn/20191113154959393.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0pfd2I0OQ==,size_16,color_FFFFFF,t_70)

```
net start mongodb
```

![alt tag](https://img-blog.csdnimg.cn/20191113155007190.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0pfd2I0OQ==,size_16,color_FFFFFF,t_70)


[MongoDB 學習筆記 (一) : 在 Win10 上安裝 MongoDB 2019年1月16日](http://yhhuang1966.blogspot.com/2019/01/mongodb-win10-mongodb.html)

# MongoDB Configuration    
[MongoDB之conf配置文件详解(五) 2018-08-15](https://www.cnblogs.com/cwp-bg/p/9479945.html)  

## mongodb.conf
```
# 普通配置文件
# mongodb.conf

dbpath=/var/lib/mongodb  
logpath=/var/log/mongodb/mongodb.log 
pidfilepath=/var/log/mongodb/master.pid  
directoryperdb=true  
logappend=true  
bind_ip=127.0.0.1 
port=27017  
fork=true  

# 集群配置文件
dbpath=/var/lib/mongodb  
logpath=/var/log/mongodb/mongodb.log 
pidfilepath=/var/log/mongodb/master.pid  
directoryperdb=true  
logappend=true  
replSet=name  
bind_ip=127.0.0.1 
port=27017  
fork=true  
noprealloc=true 
```

```
# mongodb.conf

# 数据库文件位置
dbpath=/var/lib/mongodb

#日志文件的路径
logpath=/var/log/mongodb/mongodb.log

# 是否追加方式写入日志，默认True
logappend=true

# 设置绑定ip
bind_ip = 127.0.0.1
# 设置端口
port = 27017

# 是否以守护进程方式运行，默认false
fork = true

# 启用日志文件，默认启用
journal=true

# 启用定期记录CPU利用率和 I/O 等待,默认false
#cpu = true

# 是否以安全认证方式运行，默认是不认证的非安全方式
#noauth = true
#auth = true

# 详细记录输出，默认false
#verbose = true

#用于开发驱动程序时验证客户端请求
#objcheck = true

# # 启用数据库配额管理,默认false
#quota = true

# 设置oplog日志记录等级，默认0
#   0=off (default)
#   1=W
#   2=R
#   3=both
#   7=W+some reads
#oplog = 0

# 是否打开动态调试项，默认false
#nocursors = true

# 忽略查询提示，默认false
#nohints = true

# 禁用http界面，默认为localhost：28017
#nohttpinterface = true

# 关闭服务器端脚本，这将极大的限制功能，默认false
#noscripting = true

# 关闭扫描表，任何查询将会是扫描失败
#notablescan = true

# 关闭数据文件预分配
#noprealloc = true

# 为新数据库指定.ns文件的大小，单位:MB
# nssize = <size>

# 用于Mongo监控服务器的Accout token。
#mms-token = <token>

# Mongo监控服务器的服务器名称。
#mms-name = <server-name>

# Mongo监控服务器的Ping间隔时间，即心跳
#mms-interval = <seconds>

# Replication Options

# 设置主从复制参数
#slave = true # 设置从节点
#source = master.example.com # 指定从节点的主节点
# Slave only: 指定要复制的单个数据库
#only = master.example.com
# or
#master = true # 设置主节点
#source = slave.example.com 

# 设置副本集的名字，所有的实例指定相同的名字属于一个副本集
replSet = name

#pairwith = <server:port>

# 仲裁服务器地址
#arbiter = <server:port>

# 默认为false，用于从实例设置。是否自动重新同步
#autoresync = true

# 指定的复制操作日志（OPLOG）的最大大小
#oplogSize = <MB>

# 限制复制操作的内存使用
#opIdMem = <bytes>

# 设置ssl认证
# Enable SSL on normal ports
#sslOnNormalPorts = true

# SSL Key file and password
#sslPEMKeyFile = /etc/ssl/mongodb.pem
#sslPEMKeyPassword = pass
```

# RethinkDB  

## Realtime 讀取資料  
[Rethink DB 初探 Jul 2, 2017](https://medium.com/bryanyang0528/rethink-db-%E5%88%9D%E6%8E%A2-42d4d477a72b)  

```
傳統資料庫（例如mysql）只有在當我們主動 select 的時候才會提取資料．
如果我們要持續監聽資料庫有沒有新增資料，就必須定期的去詢問資料．這樣一來會增加資料庫無謂的負擔．
而 RethinkDB 可以在資料庫近來資料庫，主動的將資料推送到使用者手中．

首先我們開啟一個新的 terminal 連線，進入 iPython，並且和 RethinkDB建立連線：
```

```
import rethinkdb as r
r.connect( "localhost", 28015).repl()
#重點我們這裡將監聽 test 這個table，只要有任何改變就通知我們
cursor = r.table("test").changes().run()
for document in cursor:
    print(document)
```  

### 1st original  
<img src="https://miro.medium.com/max/875/1*aocssTyNOKj89TYy4f8_sg.png" width="400" height="300">  

### 2nd insert to rethinkdb  
<img src="https://miro.medium.com/max/875/1*TYQcvkrXapJFSVov07pY7Q.png" width="400" height="300">

### 3rd update status   
<img src="https://miro.medium.com/max/875/1*EBQKCgVWJMMisPCiEiFMWg.png" width="800" height="200">

## 篩選資料  
[Rethink DB 初探 Jul 2, 2017](https://medium.com/bryanyang0528/rethink-db-%E5%88%9D%E6%8E%A2-42d4d477a72b)  

先建立兩個監控單位：  

```
cursor = r.table("test").filter({'user_id': "5566"}).changes().run()
cursor2 = r.table("test").filter({'user_id':"7788"}).changes().run()
```

### 1st insert data  
<img src="https://miro.medium.com/max/875/1*aszhLKLdG4le4-hamZZv6A.png" width="400" height="500">  

### 2nd cursor next  
<img src="https://miro.medium.com/max/875/1*7BeF3l4bg4DDItQ4D9Cbqg.png" width="400" height="200">  


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


