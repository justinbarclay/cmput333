#mfirst.txt contains first names of dead musicians
f = open("mfirst.txt", "r")
firstName = []

for line in f:
	line = line.strip("\n")
	firstName.append(line)

f.close()

#mlast.txt contains first names of dead musicians
f = open("mlast.txt", "r")
lastName = []

for line in f:
	line = line.strip("\n")
	lastName.append(line)

f.close()

#output of all combinations between first/last names
f = open("donem.txt", "w")
for i in range(len(firstName)):
	f.write(firstName[i] + lastName[i] + "\n")
	#print(firstName[i] + lastName[i] + "\n")
	last = lastName[i].lower()
	f.write(firstName[i] + last + "\n")
	#print(firstName[i] + last + "\n")
	last = lastName[i].upper()
	f.write(firstName[i] + last + "\n")
	#print(firstName[i] + last + "\n")

	first = firstName[i].lower()
	f.write(first + lastName[i] + "\n")
	#print(first + lastName[i] + "\n")
	last = lastName[i].lower()
	f.write(first + last + "\n")
	#print(first + last + "\n")
	last = lastName[i].upper()
	f.write(first + last + "\n")
	#print(first + last + "\n")

	first = first.upper()
	f.write(first + lastName[i] + "\n")
	#print(first + lastName[i] + "\n")
	last = lastName[i].lower()
	f.write(first + last + "\n")
	#print(first + last + "\n")
	last = lastName[i].upper()
	f.write(first + last + "\n")
	#print(first + last + "\n")

f.close()

