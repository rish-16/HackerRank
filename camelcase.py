s = 'saveChangesInTheEditor'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
words = 1

if s != '':
	for i in alphabet:
		S = list(s)

		for j in S:
			if j == i.upper():
				words += 1
else:
	pass

print (words)
