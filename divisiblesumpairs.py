import sys

n = 6
k = 3
arr = [1, 3, 2, 6, 1, 2]

def solve(n, k ,ar):
	possible_combos = []
	for i in range(len(ar)):
		for j in range(len(ar)):
			ij_sum = ar[i] + ar[j]
			if (i < j) and (ij_sum % k == 0):
				possible_combos.append([i,j])

	return len(possible_combos)

print (solve(n,k,arr))
