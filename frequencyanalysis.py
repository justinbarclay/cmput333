def prompt(phrase):
    filename = input(phrase)
    if len(filename) < 1:
        return ""
    return open(filename)

def printFreq(freq, total):
    for key, value in freq.items():
        print(str(key) + ": " + str(value/float(total)))

def genArray(fileHandle):
    #flatMaps the byte file into a single array
    byteArray = []
    for line in encrypted:
        byteArray += line

    return byteArray

def findXMostNGrams(nGrams, x):
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
    start = 0
    end = size
    length =len(byteArray)
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

def getCount(array):
    count = {}
    for num in array:
        if hex(num) in count.keys():
            count[hex(num)] += 1.0
        else:
            count[hex(num)] = float(1)
    return count


if __name__ == "__main__":
    encrypted = open("./cipher_text/ciphertext1", "rb")
    count = {}
    totalBytes = 0

    byteArray = genArray(encrypted)
    count = getCount(byteArray)
#    printFreq(count, len(byteArray))
    threeGrams = countNGrams(byteArray,3)

    print(findXMostNGrams(threeGrams, 20))
