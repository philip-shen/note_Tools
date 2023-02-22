
Table of Contents
=================

   * [Notes of Google Drive](#notes-of-google-drive)
   * [Google Drive Client](#google-drive-client)
      * [8. Google-drive-ocamlfuse](#8-google-drive-ocamlfuse)
   * [Google-drive-ocamlfuse](#google-drive-ocamlfuse)
      * [OCaml Installation](#ocaml-installation)
      * [google-drive-ocamlfuse Installtion](#google-drive-ocamlfuse-installtion)
      * [Authorize it with Google](#authorize-it-with-google)
      * [Automated mount/unmount](#automated-mountunmount)
   * [h1 size](#h1-size)
      * [h2 size](#h2-size)
         * [h3 size](#h3-size)
            * [h4 size](#h4-size)
               * [h5 size](#h5-size)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)

# Notes of Google Drive
Take a note of Google Drive

# Google Drive Client  
[13 Best Google Drive Clients for Linux in 2022](https://linuxhint.com/best_google_drive_clients_linux/)
## 8. Google-drive-ocamlfuse
[8. Google-drive-ocamlfuse]() 

# Google-drive-ocamlfuse  
[Use Google Drive as a local directory on Linux Posted on Feb 18, 2021](https://dev.to/yawaramin/use-google-drive-as-a-local-directory-on-linux-1b9)

## OCaml Installation 
[How to install opam](https://opam.ocaml.org/doc/Install.html)

```
bash -c "sh <(curl -fsSL https://raw.githubusercontent.com/ocaml/opam/master/shell/install.sh)"
```

##  google-drive-ocamlfuse Installtion 
[astrada/google-drive-ocamlfuse](https://github.com/astrada/google-drive-ocamlfuse)

```
sudo add-apt-repository ppa:alessandro-strada/ppa
sudo apt-get update
sudo apt-get install google-drive-ocamlfuse
```

## Authorize it with Google

```
google-drive-ocamlfuse
```

```
$ google-drive-ocamlfuse
Access token retrieved correctly.
```

## Automated mount/unmount  
```
mkdir ~/GoogleDrive
```

```
# ~/.config/systemd/user/gdfuse.service
[Unit]
Description=google-drive-ocamlfuse - mount Google Drive as a filesystem
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=/home/YOURNAME/.opam/default/bin/google-drive-ocamlfuse -f /home/YOURNAME/GoogleDrive
ExecStop=/usr/bin/fusermount -u /home/YOURNAME/GoogleDrive

[Install]
WantedBy=multi-user.target
```
(Be sure to replace YOURNAME with your username.)


* []()  
![alt tag]()
<img src="" width="500" height="500">

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