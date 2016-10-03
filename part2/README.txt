All python scripts are assumed to be run under Python 3.5
1) To findKeys against a large selection of fileSignatures, it is assumed that
   ciphertext2 is running in the same location that you're calling the scrypt.
   second you must set fileSignatures to the name of the file containing the 
   the guessed plaintext. Then make sure part1 is uncommented and part2 is commented.
   Once the setup is done run "python findKey.py" it will then print to stdout
   a list of keys that are printable in plaintext. Copy this key into a new file.
2) Ensure that any key in your keyfile is seperated by a new line character. Then
   run "python decryptViginere.py keyfile.txt ciphertext2" again where keyfile.txt
   contains 1 or more keys and ciphertext2 is the ciphertext.
3) If the key is only a partial decryption, then look for patters in the partially
   deciphered plaintext and uncomment part 2 and start guessing at the possible 
   plain text for that section
