openssl enc -e -des-ecb -nosalt -in plaintext -out cipherecberror.enc -k "01234567"

openssl enc -e -des-cbc -nosalt -in plaintext -out ciphercbcerror.enc -k "01234567"

openssl enc -e -des-cfb -nosalt -in plaintext -out ciphercfberror.enc -k "01234567"

openssl enc -e -des-ofb -nosalt -in plaintext -out cipherofberror.enc -k "01234567"



du -b cipherecb.enc
             
du -b ciphercbc.enc
             
du -b ciphercfb.enc
             
du -b cipherofb.enc
