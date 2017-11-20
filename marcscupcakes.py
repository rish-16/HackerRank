import more_itertools as mit
from pprint import pprint

c = [1, 3, 2]
n = len(c)

possible_miles = []

def random_permute_generator(iterable, n):
    for _ in range(n):
        yield mit.random_permutation(iterable)

possible_combos = (list(set(list(random_permute_generator(c, 20)))))

for combo in possible_combos:
    miles = 0
    no_of_cupcakes_eaten = 0
    for calorie_value in combo:
        miles_needed = (2^no_of_cupcakes_eaten) * calorie_value
        miles += miles_needed
        no_of_cupcakes_eaten += 1

    possible_miles.append(miles)

pprint (min(possible_miles))