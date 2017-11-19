string = 'hello world'
container = []

for word in string.split():
	current = list(word)
	new_letter = current[0].upper()

	current[0] = new_letter

	this_word = ''.join(current)

	container.append(this_word)

sentence = ' '.join(container)

print (string)
print (sentence)
