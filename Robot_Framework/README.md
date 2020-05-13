# Purpose
Take note of Robot Framework  

# Table of Contents  
[robotframework + seleniumlibrary](#robotframework-+-seleniumlibrary)  
[Windows Application Driver on Windows](#windows-application-driver-on-windows)  


# robotframework + seleniumlibrary  
[robotframework + seleniumlibrary 参考情報まとめ  Jan 18, 2019](https://qiita.com/atmaru/items/84c4bb10430572cdf67d)  
[robotframework + seleniumlibrary 導入 Jan 21, 2019](https://qiita.com/atmaru/items/e40ce6fd4a5928dd2521)    
* 環境や前提条件  
```
windows10 pro
PowerShell
python3.7
```

* 手順  
## python install  
## robotframework + seleniumlibrary install  

Powershellからコマンドラインでinstall
```
> pip install robotframework-seleniumlibrary==3.3.1
```

robotコマンドでrobot frameworkを起動してみると、少なくとも引数一つ必要だけど一つもないよと怒られる。
```
> robot
[ ERROR ] Expected at least 1 argument, got 0.

Try --help for usage information.
```

## web driver(chrome) install  
## Testing  
* test.robotというgoogleにアクセスするだけのテストを作成。  
```
*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      https://www.google.co.jp/
${BROWSER}        Chrome

*** Test Cases ***
Valid Login
    Open Browser To Login Page
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Google
```

* テスト実行  
```
PS C:\robot> robot .\test.robot
==============================================================================
Test :: Simple example using SeleniumLibrary.
==============================================================================
Valid Login
DevTools listening on ws://127.0.0.1:52052/devtools/browser/e1098142-dc9c-4b12-a75e-63a0ba65d175
Valid Login                                                           | PASS |
------------------------------------------------------------------------------
Test :: Simple example using SeleniumLibrary.                         | PASS |
1 critical test, 1 passed, 0 failed
1 test total, 1 passed, 0 failed
==============================================================================
Output:  C:\robot\output.xml
Log:     C:\robot\log.html
Report:  C:\robot\report.html
```

* log.htmlを開き赤色になっている項目を確認すれば、エラーの要因がわかります。
![alt tag](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F29032%2Ff6e0db85-0057-5bf1-1b18-c4ab23f3bdba.png?ixlib=rb-1.2.2&auto=compress%2Cformat&gif-q=60&w=1400&fit=max&s=5b6a1f7bbc024db770c44ee41d671775) 


[robotframework + seleniumlibrary で空白文字を扱う ](https://qiita.com/atmaru/items/afc90e2d27deda623cef)  
## 手段  
* google1.robot  
```
*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary
Library           String
Suite Teardown     Close Browser

*** Variables ***
${URL}            https://google.com/
${BROWSER}        Chrome

*** Test Cases ***
Googleでいろいろ検索する
    Googleを開く
    検索する  robotframework
    検索する  'robotframework'
    検索する  ' robotframework'
    検索する  ' robotframework '
    検索する  ' robotframework 
    検索する  ' !"#$%&'()=~|`*+<>? '
    検索する  'あかさたな'

*** Keywords ***
Googleを開く
    Open Browser    ${URL}    ${BROWSER}

検索する  [Arguments]  ${val}
    ${quote}=  クォーテーション確認  ${val}
    ${string}=  Run Keyword If  ${quote}==True   先頭後尾削除  ${val}
    ...         ELSE                             Set Variable  ${val}
    Log To Console  ${string} 
    InputText      xpath=//input[@title="検索"]  ${string}
    Press Keys  None  RETURN
    Capture Page Screenshot


クォーテーション確認  [Arguments]  ${val}
    ${head}=  Get Substring  ${val}  0  1
    ${tail}=  Get Substring  ${val}  -1
    ${quote}=  Set Variable If  "${head}"=="\'" and "${tail}"=="\'"  True  False
    [Return]  ${quote}


先頭後尾削除   [Arguments]  ${val}
    # 先頭削除
    ${string}=  Get Substring  ${val}     1
    # 後尾削除
    ${string}=  Get Substring  ${string}  0  -1
    [Return]  ${string}
```

# Windows Application Driver on Windows  
[Windows Application DriverでWindowsアプリケーションのテストを自動化する～Python編 Apr 19, 2017](https://qiita.com/totutiteta/items/ff29fcabff921057f959)  

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
