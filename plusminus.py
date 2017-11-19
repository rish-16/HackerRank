import sys

array = [-4, 3, -9, 0, 4, 1]
arr_len = len(array)

neg_count = 0
pos_count = 0
zero_count = 0

for i in array:
	if i > 0:
		pos_count += 1
	elif i < 0:
		neg_count += 1
	elif i == 0:
		zero_count += 1

print ('{0:.6f}'.format(float(pos_count/arr_len)))
print ('{0:.6f}'.format(float(neg_count/arr_len)))
print ('{0:.6f}'.format(float(zero_count/arr_len)))
