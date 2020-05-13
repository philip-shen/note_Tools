# Purpose  
Take note of SQL DB stuffs  

# Table of Contents  
[01 SQL Syntax](#01-sql-syntax)  
[AVG、SUM & COUNT](#avgsum--count)  


# 01 SQL Syntax  
## AVG、SUM & COUNT  
[【SQL】數學運算AVG、SUM & COUNT Nov 17, 2017](http://xxanalystxx.blogspot.com/2017/11/sqlavgsum-count.html)  

* AVG() / SUM()  
```
SELECT AVG([POINT]) AS 'AVG',SUM([POINT]) AS 'SUM'
FROM [DETAIL]
---AVG、SUM的計算都只會出現總計的，
---除非還有另外設定條件去做計算
```

* COUNT()  
```
SELECT COUNT([NAME]) AS 'COUNT'
FROM [DETAIL]
---COUNT就是計算筆數，一樣只會出現一個COUNT的數字，
---這邊要注意，因為沒有設其他條件，
---所以並不會將名字重複的歸納為群組計算
```

```
SELECT [NAME], AVG([POINT]) AS 'AVG2',SUM([POINT]) AS 'SUM'
    , COUNT([NUMBER]) AS'COUNT'
---進行運算的欄位都只會出現一個數字，但又需要列出姓名
---故需要增加更嚴謹的條件
FROM [DETAIL]
GROUP BY [NAME]
---GROUP BY就是告知SQL要以什麼為分類依據
---設定[NAME]的話她會將相同名字的做群組計算
ORDER BY AVG([POINT]) DESC
---利用前面提及過的ORDER BY作排序
---因為AVG([POINT])的新欄位名稱「AVG2」是在下這個指令時同時成立，
---所以無法分辨這個欄位，需要再度利用算是作為代表，
---除非撰寫為子查詢或者TEMP表之類的方法讓指令執行前就成立此新欄位
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
