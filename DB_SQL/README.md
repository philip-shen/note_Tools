Table of Contents
=================

   * [Table of Contents](#table-of-contents)
   * [Purpose](#purpose)
   * [01 SQL Syntax](#01-sql-syntax)
      * [AVG、SUM &amp; COUNT](#avgsum--count)
   * [02 Select same column from multiple tables](#02-select-same-column-from-multiple-tables)
      * [1 How to select rows from two tables where both have the same value in the same field?](#1-how-to-select-rows-from-two-tables-where-both-have-the-same-value-in-the-same-field)
      * [2 Select same column from multiple tables only WHERE something = something](#2-select-same-column-from-multiple-tables-only-where-something--something)
      * [3 從兩個資料表取出重複資料](#3-從兩個資料表取出重複資料)
   * [03 Merge two tables on multiple columns without duplicate rows](#03-merge-two-tables-on-multiple-columns-without-duplicate-rows)
      * [1 join two different tables and remove duplicated entries](#1-join-two-different-tables-and-remove-duplicated-entries)
      * [2 Join two tables on multiple columns without duplicate rows](#2-join-two-tables-on-multiple-columns-without-duplicate-rows)
   * [04 Sqlite merge tables](#04-sqlite-merge-tables)
      * [1 Combining two tables in sqlite3](#1-combining-two-tables-in-sqlite3)
      * [2 Combine two tables in SQLite](#2-combine-two-tables-in-sqlite)
      * [3 Merging two tables in sqlite from different database](#3-merging-two-tables-in-sqlite-from-different-database)
   * [05 Prevent duplicate values in LEFT JOIN](#05-prevent-duplicate-values-in-left-join)
      * [1 Prevent duplicate values in LEFT JOIN](#1-prevent-duplicate-values-in-left-join)
      * [2 Left Join without duplicate rows from left table](#2-left-join-without-duplicate-rows-from-left-table)
   * [Troubleshooting](#troubleshooting)
   * [Reference](#reference)
   * [h1 size](#h1-size)
      * [h2 size](#h2-size)
         * [h3 size](#h3-size)
            * [h4 size](#h4-size)
               * [h5 size](#h5-size)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)

# Purpose  
Take note of SQL DB stuffs  

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

# 02 Select same column from multiple tables   
## 1 How to select rows from two tables where both have the same value in the same field?   
[How to select rows from two tables where both have the same value in the same field? Mar 24, 2015](https://stackoverflow.com/questions/29231737/how-to-select-rows-from-two-tables-where-both-have-the-same-value-in-the-same-fi) 

```
I have two tables that have the same column names.

There is a field called Call_Status in both tables.

I want to retrieve the records having Call_Status="Open" from both tables. 
i.e. I want a query that can retrieve all the records of table1 having call_Status="Open" 
& then from table2 having call_Status="Open"
```

```
If you want to get all the matching rows from the first table and all the matching rows from the second table 
(as opposed to joining rows together), then you could use a union.

SELECT column names FROM table1 WHERE call_status='Open'
UNION ALL
SELECT column names FROM table2 WHERE call_status='Open'
```

```
You can use UNION instead of UNION ALL to get unique rows, as pointed out by Fionnuala.
```

## 2 Select same column from multiple tables only WHERE something = something   
[Select same column from multiple tables only WHERE something = something ](https://stackoverflow.com/questions/17092697/select-same-column-from-multiple-tables-only-where-something-something)  

```
I have two tables with very similar structures.

Universidades
nombre | contenido | becas | fotos etc etc etc
Internados
nombre | todo | becas | fotos etc etc etc

I want to write an SQL statement that will select the nombre from both of them and return it as an array only when it matches. 
From what I have seen UNION SELECT seems to be the way to do this. 
I added WHERE on the end and I think this is where its going wrong. 
So far I am receiving the first row of the first table. 
```

```
One issue to point out before we solve the problem is that each query in a UNION is distinct and requires its own WHERE clause. 
The only clause that applies to the UNION as a whole is ORDER BY. So your query as is needs some tweaking:
```

```
You can think about JOIN and UNION this way:

    JOIN: connects rows horizontally
        Matches them on conditions
        
        Creates new columns
        
        Doesn't exactly create rows because all data comes from existing rows, 
        but it will duplicate a row from one input when the conditions match multiple rows in the other input. 
        If both inputs have duplicates then it multiplies the count of rows from one input by the count of matching rows from the other.
        
        If there is no match condition at all (think CROSS JOIN) then 
        you can get a cartesian product which is each row in one input matched to each row in the other.
        
        When using an OUTER join--LEFT, RIGHT, FULL--if rows from the inner input (or either input with FULL) do not match the other, 
        NULLs will be placed into the columns for the other input.

    UNION: stacks rows vertically
        Generally, creates new rows
        
        No conditions are used, there is no real matching
        
        UNION by itself (not UNION ALL) will remove duplicate rows, even if one input has no rows
```

```
Note that the UNION could be modified to do the job, though this is not ideal:

SELECT nombre
FROM (
   SELECT nombre
   FROM dbo.internados
   WHERE nombre = ?
   UNION ALL
   SELECT nombre
   FROM dbo.universidades
   WHERE nombre = ?
) N
GROUP BY nombre
HAVING Count(*) = 2
;
```

## 3 從兩個資料表取出重複資料   
[從兩個資料表取出重複資料 2006-08-16 17:20](http://www.blueshop.com.tw/board/FUM20041006152735ZFS/BRD20060816171927YBU.html)  

```
想請問各位
我目前有兩個資料表
其中一個資料表會多出一個不同的欄位
其他的欄位兩個資料表都是一樣的,資料也可能會有重複的
所以我現在想抓出兩個資料表重複的資料
不知道該怎麼下SQL語法? 
```

```
設
tabel 1的資料為
號碼1 繳費金額 繳費日期
12345 50 20060815
23456 30 20060612

tabel2的資料為
號碼1 號碼2 繳費金額 繳費日期
12345 abcde 50 20060816
73929 keoie 30 20060810

我想要的結果是
號碼1 號碼2 繳費金額 繳費日期
12345 abcde 50 20060816
12345 50 20060815

抓兩個table號碼1相同的資料
謝謝~ 
```

```
#9 

Select 號碼1 , '' as 號碼2 , 繳費金額 , 繳費日期 From Table1
Where 號碼1 in (Select distinct 號碼1 From Table2)
Union
Select 號碼1 , 號碼2 , 繳費金額 , 繳費日期 From Table2
Where 號碼1 in (Select distinct 號碼1 From Table1)
Order by 號碼1,號碼2
```

```
# 10
有沒有下Distinct，IN出來的結果應該都是一樣的
可以直接UNION下WHERE就行了~_~

SELECT * FROM
(
	SELECT 號碼1, '' as 號碼2, 繳費金額, 繳費日期 FROM Table1
	UNION ALL
	SELECT 號碼1, 號碼2, 繳費金額, 繳費日期 FROM Table2
) as vw
	WHERE 號碼1=12345
```

```
呵~忘了是要找重覆的資料了
#9才是正確的~_~ 
```

```
建立一個VIEW 或 將資料在寫入第三的TABLE
只要INSERT 的時候先INSERT tabel 1的資料再INSERT tabel2的資料
然後TABLE3再將oder by 寫好 就可以將資料取出 
```

# 03 Merge two tables on multiple columns without duplicate rows  

## 1 join two different tables and remove duplicated entries  
[join two different tables and remove duplicated entries Jan 13, 2013](https://stackoverflow.com/questions/14303573/join-two-different-tables-and-remove-duplicated-entries)  

```
table1:

id_s  name   post_code     city     subject
------------------------------------------
1     name1  postal1    city1    subject1
2     name2  postal2    city2    subject2
3     name3  postal3    city3    subject3
4     name4  postal4    city4    subject4
...
~350

table2:

id_p  name   post_code     city     subject
------------------------------------------
1     name1  postal1    city1    subject1
2     name2  postal2    city2    subject2
3     name3  postal3    city3    subject3
4     name4  postal4    city4    subject4 
...
~1200
```

```
I want to join both tables, and remove entries with same name and postal code. 
I found some answers on how to do it but they were too complicated.
```

```
Edit: To store data from both table without duplicates, do this

INSERT INTO TABLE1
SELECT * FROM TABLE2 A
WHERE NOT EXISTS (SELECT 1 FROM TABLE1 X 
                  WHERE A.NAME = X.NAME AND 
                  A.post_code = x.post_code)
```

```
SELECT * INTO newtable FROM table1
UNION
SELECT * FROM table2;

This will create a newtable from both table1 and table2 without any duplicates
```

## 2 Join two tables on multiple columns without duplicate rows  
[Join two tables on multiple columns without duplicate rows](https://stackoverflow.com/questions/38492883/join-two-tables-on-multiple-columns-without-duplicate-rows)  

```
I have two tables:

Table A:

    id

Table B:

    id1
    id2
    ... (lots of other columns)
```

```
I want to get all the rows in B where either B.id1 or B.id2 is A.id 
(all A.id are distinct. This isn't the case for B).
```

```
select b.*
from b
where exists (select 1 from a where a.id = b.id1) or
      exists (select 1 from a where a.id = b.id2);

In most databases, this would be the most efficient method for this type of logic. 
I'm not 100% sure that this is true in Hive, but it is definitely worth a try.
```

```
An alternative approach would be left joins:

select b.*
from b left join
     a a1
     on b.id1 = a1.id left join
     a a2
     on b.id2 = a2.id
where a1.id is not null or a2.id is not null;

This might have better performance in Hive, if the exists does not have good optimization.
```

# 04 Sqlite merge tables  
## 1 Combining two tables in sqlite3  
[Combining two tables in sqlite3 ](https://stackoverflow.com/questions/8696155/combining-two-tables-in-sqlite3)  
```
Table 1

CREATE TABLE temp_entries (
    id INTEGER PRIMARY KEY, 
    sensor NUMERIC, 
    temp NUMERIC, 
    date NUMERIC);

Table 2

CREATE TABLE "restInterface_temp_entry" (
    "id" integer NOT NULL PRIMARY KEY,
    "dateTime" integer NOT NULL,
    "sensor" integer NOT NULL,
    "temp" integer NOT NULL
);
```

```
id is not unique between the two tables. I would like to create another table with the same schema as Table 2. 
I would like the id for the entries in Table 1 to start from 0 and then 
the entries from table 2 to start after the last entry from table 1.

Ideally I would like to just add the entries from Table 1 to Table 2 and "reindex" the primary key 
so that it was in the same ascending order that "dateTime" is.
```

```
Figured it out.

    Open current database.

    Attach to original database

    ATTACH '/orig/db/location' as orig

    Move records from current database to old database, leaving out the PK

    insert into orig.restInterface_temp_entry(dateTime,sensor,temp)
    ...> select dateTime,sensor,temp from main.restInterface_temp_entry;

    Clear current databases table

    delete from main.restInterface_temp_entry where id > 0

    Copy everything updated records from original databases table back to current.

    insert into main.restInterface_temp_entry(id,dateTime,sensor,temp)
    ...> select id,dateTime,sensor,temp
    ...> from orig.restInterface_temp_entry;
```


## 2 Combine two tables in SQLite 
[Combine two tables in SQLite Jan 4, 2010](https://stackoverflow.com/questions/1998770/combine-two-tables-in-sqlite)  
```
I have two tables, ta and tb:

ta:

key col1  
--------
k1 a 
k2 c 

tb:

key col2  
-------
k2 cc 
k3 ee 

They connected by "key". I want to know how can I get a table, tc, like:

key col1 col2  
-------------
k1 a  
k2 c cc 
k3  ee
```

```


Make a VIEW of the two tables. 
Write a SELECT ... JOIN statement that gives you the result you want, and then use that as the base for a VIEW.

Example:

CREATE VIEW
  database.viewname
AS
  SELECT
    ta.key, 
    ta.col1,
    tb.col2
  FROM
    ta
   LEFT JOIN
    tb
   USING(key)
```

```
Using a VIEW is the right way to go if you're looking for the data to reflect changes in the original tables.

If you do actually want the data to be copied into a new table, you'll need to do something like:

CREATE TABLE tc(key,col1,col2)

INSERT INTO tc (key,col1,col2)
SELECT ta.key, ta.col1, tb.col2
FROM ta FULL OUTER JOIN tb USING(key)
```

## 3 Merging two tables in sqlite from different database  
[Merging two tables in sqlite from different database ](https://stackoverflow.com/questions/18712761/merging-two-tables-in-sqlite-from-different-database)  
```
A sample table would be like this with the desired result. But the problem is these two tables are in different databases.

Table 1: Employee_Pro_Profile
Columns: Emp_Id, Emp_Name, Emp_Sal

Table 2: Employee_Personal_Profile
Columns: Emp_Id, Emp_Home_Address, Emp_Phone

Resulting Table: Employee_Complete
Columns: Emp_Id, Emp_Name, Emp_Sal, Emp_Home_Address, Emp_Phone
```

```
The ATTACH DATABASE statement adds another database file to the current database connection. ATTACH LINK

Run this:

attach database DatabaseA.db as DbA;
attach database DatabaseB.db as DbB;
```

```
Now you can reference the databases as you do with tables...

select
  *
from
  DbA.Table1 A
  inner join 
  DbB.Table2 B on B.Emp_Id = A.Emp_Id;
```

# 05 Prevent duplicate values in LEFT JOIN  
## 1 Prevent duplicate values in LEFT JOIN 
[Prevent duplicate values in LEFT JOIN May 23, 2015](https://stackoverflow.com/questions/30410622/prevent-duplicate-values-in-left-join) 
```
Sql Query :

SELECT p.id, p.person_name, d.department_name, c.phone_number 
FROM person p
  LEFT JOIN department d 
    ON p.id = d.person_id
  LEFT JOIN contact c 
    ON p.id = c.person_id;
```

```
Result :

id|person_name|department_name|phone_number
--+-----------+---------------+------------
1 |"John"     |"Finance"      |"023451"
1 |"John"     |"Finance"      |"99478"
1 |"John"     |"Finance"      |"67890"
1 |"John"     |"Marketing"    |"023451"
1 |"John"     |"Marketing"    |"99478"
1 |"John"     |"Marketing"    |"67890"
2 |"Barbara"  |"Finance"      |""
3 |"Michelle" |""             |"005634"
```

```
So, here is what I want:

id|person_name|department_name|phone_number
--+-----------+---------------+------------
1 |"John"     |"Finance"      |"023451"
1 |"John"     |"Marketing"    |"99478"
1 |"John"     |""             |"67890"
2 |"Barbara"  |"Finance"      |""
3 |"Michelle" |""             |"005634"
```

```
SELECT p.id, p.person_name, d.department_name, c.phone_number
FROM   person p
LEFT   JOIN (
   SELECT person_id, min(department_name) AS department_name
   FROM   department
   GROUP  BY person_id
   ) d ON d.person_id = p.id
LEFT   JOIN (
   SELECT person_id, min(phone_number) AS phone_number
   FROM   contact
   GROUP  BY person_id
   ) c ON c.person_id = p.id;
```

## 2 Left Join without duplicate rows from left table  
[Left Join without duplicate rows from left table Mar 31, 2014](https://stackoverflow.com/questions/22769641/left-join-without-duplicate-rows-from-left-table)
```
SELECT 
C.Content_ID,
C.Content_Title,
M.Media_Id

FROM tbl_Contents C
LEFT JOIN tbl_Media M ON M.Content_Id = C.Content_Id 
ORDER BY C.Content_DatePublished ASC
```

```
Try an OUTER APPLY

SELECT 
    C.Content_ID,
    C.Content_Title,
    C.Content_DatePublished,
    M.Media_Id
FROM 
    tbl_Contents C
    OUTER APPLY
    (
        SELECT TOP 1 *
        FROM tbl_Media M 
        WHERE M.Content_Id = C.Content_Id 
    ) m
ORDER BY 
    C.Content_DatePublished ASC
```

```
Alternatively, you could GROUP BY the results

SELECT 
    C.Content_ID,
    C.Content_Title,
    C.Content_DatePublished,
    M.Media_Id
FROM 
    tbl_Contents C
    LEFT OUTER JOIN tbl_Media M ON M.Content_Id = C.Content_Id 
GROUP BY
    C.Content_ID,
    C.Content_Title,
    C.Content_DatePublished,
    M.Media_Id
ORDER BY
    C.Content_DatePublished ASC
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



