@echo off
Set SERVER=ironmanexcelsior.ddns.net:3399
rem Set /P USERNAME="Username:"
rem Set /P PASSWORD="Password:"
Set USERNAME=test01
Set PASSWORD=test01

Cmdkey /generic:TERMSRV/%SERVER% /user:%USERNAME% /pass:%PASSWORD%
Start mstsc /v:%SERVER%
Timeout 8
Cmdkey /delete:TERMSRV/%SERVER%