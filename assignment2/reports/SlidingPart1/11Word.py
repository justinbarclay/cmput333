#11letterwords.txt contains all words from website 
#https://www.bestwordlist.com/11letterwords.txt
f = open("11LetterWords.txt", "r")
words = list(f.read().split())
f.close()
#print(words)

#11word.txt contains all words one line at a time and lowercased
f = open("11Word.txt", "w")
for word in words:
	f.write(word.lower() + "\n")
	f.write(word + "\n")