if __name__ == "__main__":
    # This script generates the long coordinates around the CSC building
    allCombinations = []
    base = "53.526563N,-113.52"
    end = "894W"
    for i in range(0, 10):
        current = base + str(i) + end
        allCombinations.append(current)
    keyFile = open("part2Keys.txt", "w")
    for line in allCombinations:
        keyFile.write(line + "\n")
