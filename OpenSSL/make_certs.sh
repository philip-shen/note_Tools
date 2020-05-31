#!/bin/bash
# make_certs.sh
# ----------------------------
# generate private key file, certificate signing request, 
# and self-signed certificates with Subject Alternative Name.
#
# environment:
# ubuntu 18.04 , openssl 1.1.1
#
# if you want to use @-notation in subjectAltName , 
# then you can write the text file SAN-${COMMON_NAME].txt as following :
# ---
# $ cat SAN-foo.bar.local.txt 
# subjectAltName=@alt_names
# [alt_names]
# DNS.1 = foo.bar.local
# IP.1 = 10.20.30.40
# $
# ---

function usage() {
    echo "$0 [common name]"
}

if [ $# -lt 1 ]; then
    usage
    exit 0
fi

COMMON_NAME=$1
OUTDIR=certs

# private key file
KEY_FILE=${OUTDIR}/${COMMON_NAME}.key

# certificate signing request file
CSR_FILE=${OUTDIR}/${COMMON_NAME}.csr

# self-signed certificates
CRT_FILE=${OUTDIR}/${COMMON_NAME}.crt

# Subject Alternative Name
# e.g. DNS, IP-Address
EXT_FILE=SAN-${COMMON_NAME}.txt

SUBJECT="/C=JP/ST=Tokyo/O=example.org/CN=${COMMON_NAME}/"
DAYS=365

mkdir -p ${OUTDIR}

if [ ! -f ${EXT_FILE} ]; then
    echo "extfile [${EXT_FILE}] not found. create ..."
    echo "subjectAltName=DNS:${COMMON_NAME}" > ${EXT_FILE}
fi

echo ""
echo "create key file and csr file ..."

openssl req -nodes -new \
    -newkey rsa:4096 \
    -keyout ${KEY_FILE} \
    -out ${CSR_FILE} \
    -subj ${SUBJECT} \
    -days ${DAYS}

echo "key [${KEY_FILE}]"
ls -l ${KEY_FILE}

echo "csr [${CSR_FILE}]"
ls -l ${CSR_FILE}

echo ""
echo "create crt file"

openssl x509 \
    -in ${CSR_FILE} \
    -out ${CRT_FILE} \
    -req -signkey ${KEY_FILE} \
    -extfile ${EXT_FILE} \
    -days ${DAYS}

if [ ! -f ${CRT_FILE} ]; then
    echo ""
    echo "crt file [${CRT_FILE}] not found."
    exit 1
fi

echo "crt [${CRT_FILE}]"
ls -l ${CRT_FILE}

echo ""
echo "confirm certificates"
openssl x509 -text -noout -in ${CRT_FILE}

echo ""
echo "done."
exit 0
