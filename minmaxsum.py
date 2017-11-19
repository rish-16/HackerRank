import sys
from pprint import pprint

arr = [1, 2, 3, 4, 5]
possible_sums = []

for i in range(len(arr)-1):
	for j in range(len(arr)-i):
		possible_sums.append(arr[i] + arr[j])


print (possible_sums)
