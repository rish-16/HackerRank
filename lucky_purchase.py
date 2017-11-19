import sys

def func(brands, values):
	no_of_brands = len(brands)
	no_of_costs = len(values)

	possible_brands = []
	possible_costs = []
	rejects = []

	for index in range(no_of_brands):
		cost_for_brand = values[index]
		count4 = 0
		count7 = 0
		count_unwanted = 0

		# Consider brand if 4 and 7 in the number or else rejct
		for number in str(cost_for_brand):
			if number == '4':
				count4 += 1
			elif number == '7':
				count7 += 1
			elif number != '4' or number != '7':
				count_unwanted += 1

		if count_unwanted > 0:
			rejects.append(brands[index])

		elif count4 == count7:
			possible_brands.append(brands[index])
			possible_costs.append(values[index])

		else:
			rejects.append(brands[index])

	if len(possible_brands) == 0:
		best_brand = -1

	elif len(possible_brands) > 0:
		min_cost = min(possible_costs)
		index_for_min_cost = values.index(min_cost)
		best_brand = brands[index_for_min_cost]

	print (best_brand)

if __name__ == "__main__":
	n = int(input().strip())
	brands = []
	costs = []
	for a0 in range(n):
		name, value = input().strip().split(' ')
		name, value = [str(name), int(value)]
		brands.append(name)
		costs.append(value)

	func(brands, costs)
