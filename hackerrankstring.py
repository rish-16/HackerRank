words = ['hereiamstackerrank', 'hackerworld']

for word in words:
	current = list(set(word.lower()))
	target = list(set('hackerrank'))

	print (current, target)
