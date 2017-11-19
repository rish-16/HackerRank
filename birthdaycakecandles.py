import sys

arr = [3, 1, 2, 3]
n = len(arr)

def birthdayCakeCandles(n, ar):
	max_height = max(ar)

	max_count = 0

	for i in ar:
		if i == max_height:
			max_count += 1

	return max_count


print (birthdayCakeCandles(n ,arr))
