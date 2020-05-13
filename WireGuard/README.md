# Purpose  
Take note of WireGuard  

# Table of Contents  
[Instllation](#instllation)  

[WireGuard setup](#wireguard-setup)  
[Client-side](#client-side)  


# Instllation  
Ubuntu ≤ 19.04 [module – v0.0.20200215 & tools – v1.0.20200206]
```
$ sudo add-apt-repository ppa:wireguard/wireguard
$ sudo apt-get update
$ sudo apt-get install wireguard
```

# WireGuard setup  

## Client-side  
```
wg0.conf

    [Interfac
    [Interface]
    PrivateKey = <Client private key>
    # Switch DNS server while connected. 
    # Could be your internal DNS server, used on Omnia, or external
    DNS = <your_DNS_IP> 
     
    # The addresses the client will bind to. Either IPv4 or IPv6. /31 and /32 are not supported.
    Address = 10.0.10.2/24
     
    [Peer]
    PublicKey = <Server public key>
    # Optional key known to both client and server; improves security
    PresharedKey = <Pre-shared key from server for this client>
     
    # The IP range that we may send packets to for this peer. 
    # 0.0.0.0/0 will route all traffic through VPN
    AllowedIPs = 0.0.0.0/0
     
    # Address of the server
    Endpoint = <server IP>:<server port>
     
    # Send periodic keepalives to ensure connection stays up behind NAT.
    PersistentKeepalive = 25
```

# Installing WireGuard in WSL 2  
[Installing WireGuard in WSL 2 Feb 10,2020](https://medium.com/@centerorbit/installing-wireguard-in-wsl-2-dd676520cb21)  
## The Fix  
```
cd ~
mkdir workspace
cd workspace
git clone --depth 1 https://github.com/microsoft/WSL2-Linux-Kernel.git
git clone --depth 1 https://git.zx2c4.com/wireguard-linux-compat
git clone --depth 1 https://git.zx2c4.com/wireguard-tools
```


# Troubleshooting


# Reference
[ラズパイに構築したWireGuardにmacOS、iOSからVPN接続してみた Mar 04, 2019](https://qiita.com/dkuji/items/3a44930e5c37f7587668)  

[WireGuard をつかってみる Aug 04, 2018](https://qiita.com/kjm/items/4344e5ccaaf9f02e5d69)  
## Client-side  
[Client-side](https://qiita.com/kjm/items/4344e5ccaaf9f02e5d69#client-side)  


[最新のモダンVPN WireGuardを検証 実践的な設定や運用について Feb 16, 2020](https://qiita.com/falconws/items/4a16f8700855bdd0570c)  
[iPadを開発機にするまでの道のり~コンテナを用いた開発環境の構築~ Dec 16, 2019](https://qiita.com/uesyn/items/de999f43cd15c0064b93)  
[]()  


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
