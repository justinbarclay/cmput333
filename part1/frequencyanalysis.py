def prompt(phrase):
    # grab a file handle based on user input
    filename = input(phrase)
    if len(filename) < 1:
        return ""
    return open(filename)

def printFreq(freq, total):
    # given a dictionary and the length of the source of the dictionary, print out the freuncy of all items in the dictionary
    for key, value in freq.items():
        print(str(key) + ": " + str(value / float(total)))

def genArray(fileHandle):
    # flatMaps the byte file into a single array
    byteArray = []
    for line in encrypted:
        byteArray += line

    return byteArray

def findXMostNGrams(nGrams, x):
    # iterates over a dictionary and returns the x most frequent items in the dictionary as a list of tuples
    if x > len(nGrams):
        return "X is too big"

    xHighest = []
    for i in range(x):
        highest = (0, 0)
        for key, value in nGrams.items():
            if value > highest[1]:
                highest = (key, value)
        nGrams.pop(highest[0])
        xHighest.append(highest)
    return xHighest

def countNGrams(byteArray, size):
    # Given a byte array, it returns a dict of a count of all unique nGrams of a specific size in the array
    start = 0
    end = size
    length = len(byteArray)
    nGrams = {}

    if size < 1:
        return "size needs to be greater then one"
    if size > length:
        return "size should be smaller than the length of the file"

    while(end < length):
        nGram = ""
        for num in byteArray[start:end]:
            nGram += "/" + hex(num)
        if nGram in nGrams.keys():
            nGrams[nGram] += 1.0
        else:
            nGrams[nGram] = float(1)
        start += 1
        end += 1
    return nGrams

def getCount(array, split=None):
    # given an array, returns a dict of a count of all unique items in the array
    # take in an optional split parameter, that will evenly distribute the array into
    # n sub arrays
    if split is None or (type(split) == int and split < 1):
        count = {}
        for num in array:
            if hex(num) in count.keys():
                count[hex(num)] += 1.0
            else:
                count[hex(num)] = float(1)
        return count
    else:
        count = []
        for i in range(split):
            # Initialize array full of n dicts
            count.append({})
        for index, num in enumerate(array):
            if hex(num) in count[index % split].keys():
                count[index % split][hex(num)] += 1.0
            else:
                count[index % split][hex(num)] = float(1)
        return count


def findGCD(nGrams):
    #This is the wrong thought process for finding length of key using nGrams.
    #takes a list of tuples of nGrams and their counts and returns the smallest GCD that is not prime
    #if one exists
    #this is an O(n^2) operation as each nGram is being compared against all other nGrams

    #There is a gotcha when usinf the GCD is that some combinations of nGrams are going to be red herrings and therefore this method is hard to automate
    #as it takes eyeballing and guessing
    commonDivisors =[1]
    for i in range(len(nGrams)):
        for j in range(i + 1, len(nGrams)):
            divisor = gcd(nGrams[i][1], nGrams[j][1])
            if divisor > 1:
                commonDivisors.append(divisor)

    return commonDivisors

def gcd(a, b):
    # Algorithm taken from https://en.wikipedia.org/wiki/Greatest_common_divisor
    # the gcd is 2^d * a
    d = 0
    while a % 2 == 0 and b % 2 == 0:
        a /= 2
        b /= 2
        d += 1
    while a != b:
        if a % 2 == 0:
            a /= 2
        elif b % 2 == 0:
            b /= 2
        elif a > b:
            a = (a - b) / 2
        else:
            b = (b - a) / 2
    return (2**d) * a

def ioc(count, phi):
    # http://www.thonky.com/kryptos/index-of-coincidence
    # Generates the index of coincidence for a given text using the monographic phi test
    # coincidence in a random text (0.0385)
    # probabilities of coincidence in English plaintext (0.0667)
    # count should be a dictionary of hex bytes and counts of occurence of hex bytes in text
    # As mentioned above, the index of coincidence of an English plaintext message is usually
    # between 1.50 and 2.00 if the message consists of 50 or more letters. The larger the message, the closer it should be to 1.73.

    # The monographic phi test is not very reliable for texts that are 50 letters or shorter in length, such as the example on this page.
    total = 0
    total_char = 0
    for key, value in count.items():
        total += (value * (value - 1))
        total_char += value
    n = total_char * (total_char - 1)
    return (total) / n

def splitHex(num):
    if type(num) is str:
        toHex = ord(num)
    else:
        toHex = num
    upperHalf = toHex >> 4
    lowerHalf = toHex & 15
    return upperHalf, lowerHalf

def findHexBits(plainChar, keyChar):
    # A function that given to 4 bit numbers finds a hex value
    ph, pl = splitHex(plainChar)
    kh, kl = splitHex(keyChar)
    print(hex(ord(keyChar)))
    print(kh, kl)
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
    # print hex(hexMap[ph][kl] << 4)
    # print hex(hexMap[pl][kh])
    # print type(hex((hexMap[ph][kl] << 4) + hexMap[pl][kh]))
    return (hexMap[ph][kl] << 4) + hexMap[pl][kh]

def findMatch(byteArray, byte):
    return byteArray.index(byte)

def generateAllKeys(keys):
    collection = []
    for key in keys[0].get():
        permutationofKey = []
        
        

def findKey(cipher, plain):
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
    ph, pl = splitHex(plain)
    ch, cl = splitHex(cipher)
    return ((findMatch(hexMap[pl], cl) << 4) + findMatch(hexMap[ph], ch))

def findKeys(common, letters):
    # The idea behind this function is to assume that to test the most
    # common letters in the english alphabet against the most popular
    # hex values(letter) in the cipher text
    # It then counts up how many times a key common letter resovles to
    # a common key
    # Later we assume that the most common key is the likely key for that position
    # We could also just generate all keys given possible given what we
    # found here
    main = {}
    for letter in common:
        for cipher in letters:
            key = findKey(chr(int(cipher[0], 16)), letter)
            
            if key < 128:
                if key in main:
                    main[key] += 1
                else:
                    main[key] = 1
    return main

def findMostLikelyKeys(keys):
    # Given a list of dictionary objects, it returns a list of ints that respresent
    # the most frequent keys in each dictionary
    bestMatch = []
    print(keys)
    for possibleKey in keys:
        try:
            bestMatch.append(max(possibleKey, key=possibleKey.get))
        except:
            bestMatch.append(0);

    return bestMatch


def cartesian(lists):
    # Provides the cartesian product of a list of lists
    if lists == []:
        return [()]
    return [x + (y,) for x in cartesian(lists[:-1]) for y in lists[-1]]

def findSequence(array, sequence):
    # Finds all index of a subsequence in an array
    foundIndexes = []
    for i in range(len(array)):
        if array[i] == sequence[0] and equal(array[i: i + len(sequence)], sequence):
            foundIndexes.append(i)
    return foundIndexes

def equal(first, second):
    # simple equality checker
    print(first)
    print(second)
    if len(first) != len(second):
        return False
    for i in range(len(first)):
        if first[i] != second[i]:
            return False
    print(True)
    return True

def getListOfKeys(keys):
    # Takes in a list of dictionaries and returns a list of list of the keys
    # of the dictionaries
    listsOfKeys = []
    for dictionary in keys:
        listsOfKeys.append(list(dictionary.keys()))
    return listsOfKeys

def convertHexStringToInt(hexString):
    #Convert a hex string to int
    intList = []
    splitString = hexString.split("/")[1:]
    for item in splitString:
        intList.append(int(item, 16))

    return intList

if __name__ == "__main__":
    #Examples of how to use some of the functions
    encrypted = open("cipher_text/ciphertext1", "rb")
    headers = open("headers.txt")
    byteArray = genArray(encrypted)

    for line in headers:
        for index, byte in enumerate(line):
            char = chr(findKey(byteArray[index], byte))
            print(hex(ord(char)))
            print(char)
    
    for i in range(1, 400):
        # Spluts the byte array into i sub arrays
        count = getCount(byteArray, i)
        
        # a list to hold IOC for each subarray
        iocs = []
        for j in count:
            iocs.append(ioc(j, 0.0667))
        if (sum(iocs)/len(count)) > 0.06:
            print("*****")
        print(str(i) + ": " + str(sum(iocs) / len(count)))

    count = getCount(byteArray, 7)
    common = ["e", "t", "a", "o", "i", "n", "s", "r"]

    probableKeys = []
    for index, array in enumerate(count):
        print(index)

        most = findXMostNGrams(array, 7)
        print(most)
        keys = findKeys(common, most)
        bestKeys = {}
        for key, value in keys.items():
            if value > 1:
                bestKeys[key] = value
                print(str(key) + ": " + str(value))
        probableKeys.append(bestKeys)

    mostProbableKeys = findMostLikelyKeys(probableKeys)
    print("most probably keys: ", mostProbableKeys)
    keyFile = open("keys.txt", "wb")
    keyFile.write(bytes(mostProbableKeys))
# letter	count	 	letter	frequency
# E	21912	 	E	12.02
# T	16587	 	T	9.10
# A	14810	 	A	8.12
# O	14003	 	O	7.68
# I	13318	 	I	7.31
# N	12666	 	N	6.95
# S	11450	 	S	6.28
# R	10977	 	R	6.02
