# Purpose
Take note of Cmder from VSCode.
# Table of Content  
[VS Code Python 中文亂碼](#vs-code-python-%E4%B8%AD%E6%96%87%E4%BA%82%E7%A2%BC)  
[01. 接著按下Ctrl + Shift + P，在框框輸入task，點設定工作執行器]()  
[02. 接著點tsconfig.json]()  
[03. 把出現的東西改成以下後Ctrl + S儲存]()  
[04. 按下Ctrl + Shift + B它就會建置並執行 結果不是亂碼了]()  

[Visual Studio Code & GitHub](#visual-studio-code--github)  
[Git: 四種將分支與主線同步的方法 19 Jun 2018](#git-%E5%9B%9B%E7%A8%AE%E5%B0%87%E5%88%86%E6%94%AF%E8%88%87%E4%B8%BB%E7%B7%9A%E5%90%8C%E6%AD%A5%E7%9A%84%E6%96%B9%E6%B3%95-19-jun-2018)  
[下載Github上特定Repository內的資料夾](#%E4%B8%8B%E8%BC%89github%E4%B8%8A%E7%89%B9%E5%AE%9Arepository%E5%85%A7%E7%9A%84%E8%B3%87%E6%96%99%E5%A4%BE)  

[Python IDE](#python-ide)  
[Extensions](#extensions)  
[Settings Sync](#settings-sync)  

[Python Journey (2) - VS Code 基本使用技巧](#python-journey-2---vs-code-%E5%9F%BA%E6%9C%AC%E4%BD%BF%E7%94%A8%E6%8A%80%E5%B7%A7)  
[How to enable intellisense for python in Visual Studio Code with anaconda3?](#how-to-enable-intellisense-for-python-in-visual-studio-code-with-anaconda3)  

[Troubleshooting](#troubleshooting)  


# VS Code Python 中文亂碼   
* [106.05.12 vs code python中文亂碼(含事前準備)](https://aben20807.blogspot.com/2017/05/1060512-vs-code-python.html?fbclid=IwAR0jp4rGrivOxgX7FFPGWk9hrbIU_lR7hnP8nB3MQMMvQfPsm54xqSqq0wg)  

## 01. 接著按下Ctrl + Shift + P，在框框輸入task，點設定工作執行器  
![alt tag](https://4.bp.blogspot.com/-O087Gt4Khaw/WRXSlj959II/AAAAAAAAKtw/VGgYncJdIuw47KvsbGCnSkkrS0YkYntYwCEw/s640/2017-05-12_224339.png)  

## 02. 接著點tsconfig.json  
![alt tag](https://1.bp.blogspot.com/-OQgQemphzmw/WRXSljjBzDI/AAAAAAAAKt0/_LZoRnqz65wn3JpXtM7jyq0bh-OOE-HbwCEw/s1600/2017-05-12_224406.png)  

## 03. 把出現的東西改成以下後Ctrl + S儲存  
```
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "0.1.0",
    "command": "python",
    "isShellCommand": true,
    "args": [
        "${file}"
    ],
    "showOutput": "always",
    "options": {
        "env": {
            "PYTHONIOENCODING": "UTF-8"
        }
    }
}   
```
![alt tag](https://3.bp.blogspot.com/-oncTzG6iERM/WRXSs5jMoYI/AAAAAAAAKt8/jnHm8B04HwAU1g_4cZEck-nvLBUcejTxgCEw/s640/2017-05-12_224632.png)  

## 04. 按下Ctrl + Shift + B它就會建置並執行 結果不是亂碼了  
```
s = "大家好，中文不亂碼OuO"
print(s)
```

![alt tag](https://1.bp.blogspot.com/-lwKpHn5VWUw/WRXSzcVdz1I/AAAAAAAAKuI/qti7k1fz4F8-K18vo7OMGUslLdqwetJfQCEw/s640/2017-05-12_224757.png)  

```
我為了不亂碼找了超久@@
主要是依靠tsconfig.json裡的

"options": {
        "env": {
            "PYTHONIOENCODING": "UTF-8"
        }
    }

如果不信邪可以先把這段砍掉執行看看
絕對吐亂碼

問題並非python、vs code而是M$的cmd
因為cmd的編碼是cp950的
所以vs code要用cmd進行輸出時需要轉換成cp950
就會轉換成全亂碼
```


* [VS Code 配置 2016-11-28](https://segmentfault.com/a/1190000005986197)  
Run Build Task 中文乱码 BUG

解决 Tasks: Run Build Task 即：Ctrl+Shift+B 时乱码 bug：  

方法一：
Python 文件添加：  
```
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
```

方法二：
tasks.json 文件添加 options 参数：  
```
{
    "version": "0.1.0",
    "command": "python",
    "isShellCommand": true,
    "args": ["${file}"],
    "showOutput": "always",
    "options": {
        "env": {
            "PYTHONIOENCODING": "UTF-8"
        }
    }
}
```

方法三：

直接在系统环境变量中添加：PYTHONIOENCODING 项，值为 UTF-8。

研究下 bug 成因：
```
import sys
print(sys.stdout.encoding)
```
Ctrl+Shift+B 运行代码上述代码，输出：cp936

Ctrl+F5 运行代码上述代码，输出：utf8

参数说明：

    ${workspaceRoot} -- the path of the folder opened in VS Code

    ${file} -- 当前打开的文件

    ${relativeFile} -- the current opened file relative to workspaceRoot

    ${fileBasename} -- 当前打开文件的文件名

    ${fileDirname} -- 当前打开文件所在的路径

    ${fileExtname} -- the current opened file's extension

    ${cwd} -- the task runner's current working directory on startup

相当于在终端中运行：<command> args，如：python script.py


# Visual Studio Code & GitHub
## Git: 四種將分支與主線同步的方法 19 Jun 2018
* [Git: 四種將分支與主線同步的方法](https://cythilya.github.io/2018/06/19/git-merge-branch-into-master/)
```
方法一：git pull

   * Step 1：切換到新分支。
   * Step 2：從遠端更新程式碼，並將 master 合併至新的分支。HEAD 指向新分支的程式碼。

方法二：git fetch + git merge

   * Step 1：取得遠端資料並更新本地 master 程式碼。
   * Step 2：將 master 的程式碼合併至新分支中。HEAD 指向新分支的程式碼。

方法三：git fetch + git rebase

   * Step 1：取得遠端資料並更新本地程式碼。
   * Step 2：切換到新分支，新分支以 master 為新的基準點，將分支所修改的程式碼紀錄接在後面。HEAD 指向 master 的程式碼。


   * Step 1：取得遠端資料並更新本地 master 程式碼。
   * Step 2：以 master 為新的參考基準點，將分支 <new_branch> 的修改接在新的基準點後。

註一

方法三的意義等同於 git pull origin master --rebase。

方法四：git cherry-pick

    Step 1：從遠端取得更新，接著切換到新分支。
    Step 2：使用 cherry-pick 將目前 origin/master 所在位置與新分支差異的提交紀錄揀選（合併）至新分支，並需要建立一個提交紀錄來儲存這些變更。

註 2

之後要合併回主線仍需使用前三種方法，例如：使用 git pull origin master，這樣就會形成一個小耳朵，表示回到主線了。
```

## 下載Github上特定Repository內的資料夾
* [下載Github上特定Repository內的資料夾 五月18, 2018](https://notes.andywu.tw/2018/%E4%B8%8B%E8%BC%89github%E4%B8%8A%E7%89%B9%E5%AE%9Arepository%E5%85%A7%E7%9A%84%E8%B3%87%E6%96%99%E5%A4%BE/)
* [Download a single folder or directory from a GitHub repo Aug 18 '11](https://stackoverflow.com/questions/7106012/download-a-single-folder-or-directory-from-a-github-repo)

# Python IDE
## Extensions  
### Settings Sync  
[Settings Sync](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync)  
* [VSCode設定同步及程式碼片段 2018-04-21](https://dotblogs.com.tw/artblog/2018/04/21/vscode_settings_sync)  
```
開發一陣子之後應該每個人或多或少都會習慣使用一些外掛套件，或者是程式碼片段，如果在多台電腦中逐一設定，那應該是很累人的事情。
來~介紹你好藥東西，燈燈燈燈~~
VSCode有個套件叫做Settings Sync，就是能夠幫忙處理掉這些煩人瑣碎的事情，讓你的時間專注於開發。
```

* [小克的 Visual Studio Code 必裝擴充套件（Extensions）私藏推薦 3/05/2019](https://blog.goodjack.tw/2018/03/visual-studio-code-extensions.html)  

```
如果你有多台電腦，可以幫你同步設定檔和安裝的套件（透過 GitHub Gist），支援背景自動同步
```

## Python Journey (2) - VS Code 基本使用技巧
* [Python Journey (2) - VS Code 基本使用技巧](http://www.weithenn.org/2018/05/python-journey-part02-how-to-use-vscode.html)
```
IntelliSense / Auto-Completion 機制
當 Python extension for Visual Studio Code 安裝完成後，在 VS Code 工具撰寫 Python 時便具備 IntelliSense / Auto-Completion 機制。
```

## How to enable intellisense for python in Visual Studio Code with anaconda3?
* [How to enable intellisense for python in Visual Studio Code with anaconda3?](https://stackoverflow.com/questions/36390815/how-to-enable-intellisense-for-python-in-visual-studio-code-with-anaconda3)
```
In vs code open command palette (Ctrl+Shift+p).

There select Python:Select Interpreter

Close you vs code and then try. If it still does not work. Try again by changing to:-

Python:Build Workspace symbols and re-open the vs code. That's all i did and got intelligence enabled.
```

* []()
# Troubleshooting  
## Linter pylint is not installed
[Linter pylint is not installed Apr 7 2017](https://stackoverflow.com/questions/43272664/linter-pylint-is-not-installed)  
```
1. Open a terminal (ctrl+~)
2. Run the command pip install pylint

If that doesn't work: On the off chance you've configured a non-default python path for your editor, you'll need to match that python's install location with the pip executable you're calling from the terminal.

This is an issue because the Python extension's settings enable pylint by default. If you'd rather turn off linting, you can instead change this setting from true to false in your user or workspace settings:

"python.linting.pylintEnabled": false
```

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
