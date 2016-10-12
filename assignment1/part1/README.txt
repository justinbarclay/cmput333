All python scripts were written with the intent of being un on Python 3.5
How to use:
1) Frequency Analysis:
   - It should be noted that frequencyanalysis.py is intended to be run in two
   parts
   a) To first run the script, fileName needs to be set to the encrypted ciphertext
   and that ciphertext should be in the same directory as where you're running
   the script from. Second, you should set maxKeyLength to a reasonable maximum
   length for the keyLenght. The default is 20.
   b) After running the program, you can comment out Part 1 and uncomment Part 2.
   After reading the output from the file, it should highlight some of the keys
   lengths that have an IoC over 0.06, it is up to the user discretion which length
   to try based on this, but I recommend the IoC closest to 0.67. If no IoC is
   close to 0.067, it is a good chance that the key length is not within the range
   or that the text is not english. After, you choose your length, set
   guessedKeylength to the key length you want to test and run the file.
   It will output the guess key in a file called keys.txt

2) Once we have the keyfile generated, we run decryptViginere.py. Running
   this file is much simpler. First you must set the keylength in decryptViginere
   and then enter the following command into the console 
   "python decryptviginere.py keys.txt ciphertext1" where keys.txt is the file
   containing the keys and ciphertext1 is the ciphertext. If the keyfile contains
   one key, it will then output a decrypted text, which you then verify by hand
   that it's decrypted.
