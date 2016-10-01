#!/bin/bash

openssl enc -des-ecb -nosalt -in cipherecberror.enc -out ecbErrorDecrypt.txt -d -k "01234567"
                                                                       
openssl enc -des-cbc -nosalt -in ciphercbcerror.enc -out cbcErrorDecrypt.txt -d -k "01234567"
                                                                   
openssl enc -des-cfb -nosalt -in ciphercfberror.enc -out cfbErrorDecrypt.txt -d -k "01234567"
                                                                   
openssl enc -des-ofb -nosalt -in cipherofberror.enc -out ofbErrorDecrypt.txt -d -k "01234567"


