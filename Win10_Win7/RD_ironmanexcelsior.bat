@echo off
Set SERVER=ironmanexcelsior.ddns.net
rem Set /P USERNAME="Username:"
rem Set /P PASSWORD="Password:"
Set USERNAME=test
Set PASSWORD=test

Cmdkey /generic:TERMSRV/%SERVER% /user:%USERNAME% /pass:%PASSWORD%
Start mstsc /v:%SERVER%
Timeout 5
Cmdkey /delete:TERMSRV/%SERVER%