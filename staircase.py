import sys

n = 6
arr = []

for height in range(n+1):
	for width in range(height):
		print (str((('\t')*height) + ('#')))
