#firstrussian.txt contains first names of all generals
f = open("firstrussian.txt", "r")
firstName = []
for line in f:
	line = line.strip("\n")
	firstName.append(line)
	line = line.lower()
	firstName.append(line)
	line = line.upper()
	firstName.append(line)

f.close()

#lastrussian.txt contains last names of all generals
f = open("lastrussian.txt", "r")
lastName = []
for line in f:
	line = line.rstrip()
	lastName.append(line)
	line = line.lower()
	lastName.append(line)
	line = line.upper()
	lastName.append(line)

f.close()

#donerussian.txt contains all combinations
f = open("donerussian.txt", "w")
conn = ["_", "$", "%"]
for c in range(len(conn)):
	for i in range(len(firstName)):
		f.write(firstName[i] + conn[c] + lastName[i] + "\n")
	
f.close()