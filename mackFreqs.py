# This is mack's attempt at doing frequency analysis as Justin is smarter than
# me. Primarily implimenting
# http://www.simonsingh.net/The_Black_Chamber/vigenere_cracking_tool.html to
# figure out why it won't work
//TEESS

def buildDict():
    # Builds and returns an dict to do frequency analysis
    # Format = Repeating Sequence: spacing
    # Working from a formatted hexdump
    userFile= open('./cipher_text/c1tmb')
    hex_bytes = []
    for line in userFile:
        position = 1
        pair = "" 
        for item in line:
            if item != " " and item != '\n': 
                pair += item
                position +=1
            if position % 2 == 0:
                hex_bytes.append(pair)
                pair = ""
    print("hex bytes", hex_bytes)
    return 



if __name__ == "__main__":
    buildDict()

