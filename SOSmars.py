import sys

S = 'SOSSOT'
n = 3
actual = list('SOS')
split = [S[i:i+n] for i in range(0, len(S), n)]
mistakes = []
count = 0

for i in split:
	if i != actual:
		mistakes.append(i)

for i in mistakes:
	for letter in range(len(i)):
		if i[letter] != actual[letter]:
			count += 1

print (count)
