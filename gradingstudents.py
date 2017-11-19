arr = [73, 67, 38, 33]
new_arr = []

def solve(grades):
	for i in grades:
		if i >= 38:
			for j in range(3):
				value = (j+1)
				if (i + value) % 5 == 0:
					if value < 3:
						new_arr.append(i + value)
					else:
						new_arr.append(i)
		else:
			new_arr.append(i)

solve(arr)
print (new_arr)
