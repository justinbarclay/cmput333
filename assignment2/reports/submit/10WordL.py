#10letterwords.txt contains all 10 letter words found at https://www.bestwordlist.com/10letterwords.txt
f = open("10LetterWords.txt", "r")
words = list(f.read().split())
f.close()

#all 2 char substitutions found from http://www.gamehouse.com/blog/leet-speak-cheat-sheet/
aSub = ["/\\", "(L"]
bSub = ["I3", "13","|3", "!3", "(3", "/3", ")3", "j3"]
dSub = ["|)", "(|", "[)", "I>", "|>", "T)", "I7", "cl", "|}", "|]" ]
eSub = ["[-"]
fSub = ["|=", "|#", "ph", "/="]
gSub = ["C-", "[,", "{,", "<-", "(."]
hSub = ["}{"]
iSub = ["[]", "]["]
jSub = ["_|", "_]"]
kSub = [">|", "|<", "/<", "1<", "|c", "|(", "|{"]
lSub = ["|_"]
mSub = ["^^", "nn"]
nSub = ["^/", "|V", "/V"]
oSub = ["()", "oh", "[]", "<>"]
pSub = ["|*", "|o", "|º", "|^", "|>", '|"', "|°", "|7"]
qSub = ["0_", "<|"]
rSub = ["I2", "|`", "|~", "|?", "/2", "|^", "lz", "|9", "12", "[z", ".-", "|2", "|-"]
sSub = ["es"]
uSub = ["L|"]
vSub = ["\/", "|/", "\|"]
wSub = ["VV", "\\N", "uu", "2u", "v²"]
xSub = ["><", "}{", ")(", "]["]
ySub = ["`/"]
zSub = ["7_", ">_"]

#10WordL.txt will contain the leet substitutions one character changed at a time
#perform substitutions on corresponding characters
f = open("10WordL.txt", "w")
for word in words:
	word = word.lower()
	
	if "a" in word:
		for char in aSub:
			word1 = word.replace("a", char)
			f.write(word1 + "\n")

	if "b" in word:
		for char in bSub:
			word1 = word.replace("b", char)
			f.write(word1 + "\n")

	if "d" in word:
		for char in dSub:
			word1 = word.replace("d", char)
			f.write(word1 + "\n")

	if "e" in word:
		for char in eSub:
			word1 = word.replace("e", char)
			f.write(word1 + "\n")

	if "f" in word:
		for char in fSub:
			word1 = word.replace("f", char)
			f.write(word1 + "\n")

	if "g" in word:
		for char in gSub:
			word1 = word.replace("g", char)
			f.write(word1 + "\n")

	if "h" in word:
		for char in hSub:
			word1 = word.replace("h", char)
			f.write(word1 + "\n")

	if "i" in word:
		for char in iSub:
			word1 = word.replace("i", char)
			f.write(word1 + "\n")

	if "j" in word:
		for char in jSub:
			word1 = word.replace("j", char)
			f.write(word1 + "\n")

	if "k" in word:
		for char in kSub:
			word1 = word.replace("k", char)
			f.write(word1 + "\n")

	if "l" in word:
		for char in lSub:
			word1 = word.replace("l", char)
			f.write(word1 + "\n")

	if "m" in word:
		for char in mSub:
			word1 = word.replace("m", char)
			f.write(word1 + "\n")

	if "n" in word:
		for char in nSub:
			word1 = word.replace("n", char)
			f.write(word1 + "\n")

	if "o" in word:
		for char in oSub:
			word1 = word.replace("o", char)
			f.write(word1 + "\n")

	if "p" in word:
		for char in pSub:
			word1 = word.replace("p", char)
			f.write(word1 + "\n")

	if "q" in word:
		for char in qSub:
			word1 = word.replace("q", char)
			f.write(word1 + "\n")

	if "r" in word:
		for char in rSub:
			word1 = word.replace("r", char)
			f.write(word1 + "\n")

	if "s" in word:
		for char in sSub:
			word1 = word.replace("s", char)
			f.write(word1 + "\n")

	if "u" in word:
		for char in uSub:
			word1 = word.replace("u", char)
			f.write(word1 + "\n")

	if "v" in word:
		for char in vSub:
			word1 = word.replace("v", char)
			f.write(word1 + "\n")

	if "w" in word:
		for char in wSub:
			word1 = word.replace("w", char)
			f.write(word1 + "\n")

	if "x" in word:
		for char in xSub:
			word1 = word.replace("x", char)
			f.write(word1 + "\n")

	if "y" in word:
		for char in ySub:
			word1 = word.replace("y", char)
			f.write(word1 + "\n")

	if "z" in word:
		for char in zSub:
			word1 = word.replace("z", char)
			f.write(word1 + "\n")
f.close()