f = open("9LetterWords.txt", "r")
words = list(f.read().split())
f.close()
#print(words)

f = open("9Word.txt", "w")
for word in words:
	f.write(word.lower() + "\n")