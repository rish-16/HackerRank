import sys

arr = [1, 4, 4, 4, 5, 3]
n = len(arr)

def migratoryBirds(n, ar):
	categories = [1,2,3,4,5]
	counts = [0,0,0,0,0]

	for i in range(len(ar)):
		for j in range(len(categories)):
			if ar[i] == categories[j]:
				counts[j] += 1

	max_count = max(counts)

	index = counts.index(max_count)

	return categories[index]

print (migratoryBirds(n, arr))
