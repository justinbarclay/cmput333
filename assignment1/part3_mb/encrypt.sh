openssl enc -e -des-ecb -nosalt -in plaintext -out cipherecb.enc -k "01234567" 

openssl enc -e -des-cbc -nosalt -in plaintext -out ciphercbc.enc -k "01234567"

openssl enc -e -des-cfb -nosalt -in plaintext -out ciphercfb.enc -k "01234567"

openssl enc -e -des-ofb -nosalt -in plaintext -out cipherofb.enc -k "01234567"



du -b cipherecb.enc
             
du -b ciphercbc.enc
             
du -b ciphercfb.enc
             
du -b cipherofb.enc
