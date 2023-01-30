Table of Contents
=================

   * [Table of Contents](#table-of-contents)
   * [Purpose](#purpose)
   * [office E5 账号注册链接 和 注意事项](#office-e5-账号注册链接-和-注意事项)
   * [免費 Office 辦公軟體   5TB 雲端硬碟無限續期](#免費-office-辦公軟體--5tb-雲端硬碟無限續期)
   * [Oneindex](#oneindex)
   * [Serveless Oneindex](#serveless-oneindex)
   * [Refresh API](#refresh-api)
   * [h1 size](#h1-size)
      * [h2 size](#h2-size)
         * [h3 size](#h3-size)
            * [h4 size](#h4-size)
               * [h5 size](#h5-size)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)


# Purpose  
Take note of M$ 365 E5


# office E5 账号注册链接 和 注意事项  
[office E5 账号注册链接 和 注意事项](https://www.freedidi.com/8226.html)  
[免費申請 office E5 開發者賬號，送5T私人網盤，附無限續期的教程！ | 零度解說](https://www.youtube.com/watch?v=eamiBQpzbrQ)


# 免費 Office 辦公軟體 + 5TB 雲端硬碟無限續期
[微軟開發者福利：免費 Office 辦公軟體 + 5TB 雲端硬碟無限續期](https://www.jkg.tw/p3341/)


# Oneindex  
[OneIndex 簡約的私人雲端硬碟](https://www.jkg.tw/p3341/#oneindex-%E7%B0%A1%E7%B4%84%E7%9A%84%E7%A7%81%E4%BA%BA%E9%9B%B2%E7%AB%AF%E7%A1%AC%E7%A2%9F)

[TimeBye/oneindex](https://github.com/TimeBye/oneindex)


# Serveless Oneindex  
[heymind/OneDrive-Index-Cloudflare-Worker](https://github.com/heymind/OneDrive-Index-Cloudflare-Worker)

[spencerwooo/onedrive-vercel-index](https://github.com/spencerwooo/onedrive-vercel-index)

[spencerwooo/onedrive-cf-index Deprecated](https://github.com/spencerwooo/onedrive-cf-index)


# Refresh API  
[利用Github Action刷Microsoft 365 E5开发者订阅API实现续订 2020-06-29](https://eblog.ink/archives/228/)

[E5 续订之 AutoApiSecret 2021-03-06](https://ma.ge/archives/89.html)

```
大概流程总结一下。

   1. Fork AutoApiSecret到github；

   2. Azure注册应用，选择任何组织目录，重定向url选web，填入http://localhost:53682/，注册，保存id和机密；

   3. 设置应用权限，选择files.read.all files.readwrite.all sites.read.all sites.readwriter.all user.read.all user.readwrite.all directory.read.all directory.readwrite.all mail.read mail.readwrite mailboxsetting.read mailboxsetting.readwrite，全部勾选，应为原有1个+12个，共计13个，授予权限；

   4. rclone执行命令.\rclone authorize "onedrive" "id" "机密"，弹出确认框，确认后返回refresh_token；

   5. 回到github自己项目下，修改1.txt，将refresh_token粘贴进去；

   6. 对项目setting项，分别增加secretCONFIG_ID id=r'id' CONFIG_KEY secret=r'机密'；

   7. 点击用户头像，进入用户setting项，选择developer setting，选择personal access tokens，增加GITHUB_TOKEN,选择repo、admin：repo_hook、workflow，生成token；

   8. 回到github自己项目下，star项目后，进入actions，随后刷新页面出现workflow项目，施工完成后，点击进入，查看testapi，是否十次运行成功；

   9. 默认设置为周一到周五，每六小时运行三轮，可自行修改crontab 12 */6 * * 1-5。
```

<img src="" width="500" height="400">

<img src="" width="500" height="400">

<img src="" width="500" height="400">


* []()

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


