#!/bin/bash
# add subject alternative name to openssl.cnf
# ubunt 18.04

CNF_FILE=/etc/ssl/openssl.cnf
sudo cp ${CNF_FILE} ${CNF_FILE}.org

linenum=$( grep -n "^# Include email address in subject alt name: another PKIX recommendation" ${CNF_FILE} | cut -f 1 -d ':' )

FQDN=hoge.local
IP_ADDR=192.168.0.10

sudo sed -i -e "${linenum}a subjectAltName=@alt_names\
\n[alt_names]\
\nDNS.1 = ${FQDN}\
\nIP.1 = ${IP_ADDR}\
\n" ${CNF_FILE}

echo "result:"
sudo diff ${CNF_FILE} ${CNF_FILE}.org
exit 0
