def prompt(phrase):
    filename = input(phrase)
    if len(filename) < 1:
        return ""
    return open(filename, "rb")

def splitHex(char):
    toHex = int(char)
    upperHalf = toHex >> 4
    lowerHalf = toHex & 15
    return upperHalf, lowerHalf

def findMatch(hexMap, byte, column):
    for index, row in enumerate(hexMap):
        if row[column] == byte:
            return index

def findPlain(cipher, key):
    hexMap = [
        [0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe], 
        [0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0], 
        [0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7], 
        [0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa],  
        [0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4],      
        [0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3],     
        [0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1], 
        [0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf], 
        [0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2],                             
        [0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5],                             
        [0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb],                             
        [0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6],                              
        [0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8],                              
        [0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9],                              
        [0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd],                              
        [0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc] 
    ]
    kh, kl = splitHex(key)
    ch, cl = splitHex(cipher)
    
    return ((findMatch(hexMap, ch, kl) << 4) + findMatch(hexMap, cl, kh))

def vigEncryptText(plaintext, key):
    encrypted = []
    keyLen = len(key)
    for index,char in enumerate(plaintext):
        if ord(char) > 31 and ord(char) < 127:
            encrypted.append(findHexBits(char, key[index%keyLen]))

    return encrypted

def vigDecryptText(cipherText, key):
    decrypted = []
    keyLen = len(key)
    for index, char in enumerate(cipherText):
        decrypted.append(findPlain(char, key[index % keyLen]))
    return decrypted

if __name__ == "__main__":

    keyPhrase = "What is the name of the key file? (please note, only the first line will be read for the key) "
    keyFile = prompt(keyPhrase)

    plaintextPhrase = "What is the name of the file you would like to decrypt? "
    plaintextFile = prompt(plaintextPhrase)

    if type(keyFile) == str and type(plaintextFile) == str and (len(keyFile) < 1 or len(plaintextFile) < 1):
        print("\nKey file or plaintext file does not exist\n")
    else:
        mainList = []
        keys = keyFile.readlines()
        for line in plaintextFile:
            mainList += line
        i=1
        for key in keys:
            name = "decrypted" + str(i) + ".txt"
            encryptedText = vigDecryptText(mainList, key)
            encrypted = open(name, "wb")
            encrypted.write(bytes(encryptedText))
            encrypted.close()
            i += 1
