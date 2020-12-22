import numpy as np

INPUT = """
Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1
"""

TEST1 = """
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""	

def text2ingredients(text):
	ingredients = {}
	for line in filter(None, text.splitlines()):
		name, attributes = line.split(':')
		ingredients[name] = {attr.split()[0]:int(attr.split()[1]) for attr in attributes.split(',')}

	return ingredients


def prod(iter):
	product = 1
	for i in iter:
		product *= i
	return product


def get_all_proportions(n, l):
	amounts = []
	def find_props(p, level=0):
		print(level, p)
		if len(p) == n - 1:
			p.append(l - sum(p))
			# p = sorted(p)
			# if not p in amounts:
			amounts.append(p)
			return

		for amount in range(l - sum(p) + 1):
			np = p + [amount]
			find_props(np, level=level+1)

	find_props([])
	return amounts


def find_best_recipe(ingredients, total=100):
	maxscore = 0
	for prop in get_all_proportions(len(ingredients), total):
		# props = dict(zip(ingredients.keys(), prop))
		arr = np.asarray([[v for k, v in values.items() if k != 'calories'] for values in ingredients.values()])
		proparr = np.asarray(prop)[:,np.newaxis]
		score = np.prod(np.clip((arr * proparr).sum(axis=0), 0, np.inf))
		maxscore = max(score, maxscore)
		print(prop, score)

	return maxscore



def find_best_recipe_calorie_limit(ingredients, calorie_limit=500, total=100):
	maxscore = 0
	for prop in get_all_proportions(len(ingredients), total):
		# props = dict(zip(ingredients.keys(), prop))
		arr = np.asarray([[v for k, v in values.items() if k != 'calories'] for values in ingredients.values()])
		proparr = np.asarray(prop)[:,np.newaxis]

		calories = np.array([[values['calories']] for values in ingredients.values()])

		if (calories * proparr).sum() != 500: 
			continue

		score = np.prod(np.clip((arr * proparr).sum(axis=0), 0, np.inf))
		maxscore = max(score, maxscore)
		print(prop, score)

	return maxscore


if __name__ == '__main__':
	# INPUT = TEST1
	ingredients = text2ingredients(INPUT)
	print(ingredients)
	# print(get_all_proportions(2, 10))
	print(find_best_recipe(ingredients))
	# part 1: 18965440
	print(find_best_recipe_calorie_limit(ingredients))
	# part 2: 15862900