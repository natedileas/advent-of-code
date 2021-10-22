TEST1 = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""

INPUT = TEST1
INPUT = open('input21.txt').read()

if __name__ == '__main__':
	
	foods = []
	for line in filter(None, INPUT.splitlines()):

		ingred, allergens = line.split('(contains')
		ingredients = ingred.split()
		allergens = [item.replace(')', '').strip() for item in allergens.split(',')]
		foods.append([ingredients, allergens])

	print(foods)

	allergen_map = {}
	all_allergens = list(set((a  for _,allergens in foods for a in allergens)))
	all_ingredients = set((a  for ingredients,_ in foods for a in ingredients))
	print(all_allergens)
	for allergen in all_allergens:
		possible_ingredients = None
		for ingredients, allergens in foods:
			if allergen in allergens:
				if not possible_ingredients:
					possible_ingredients = set(ingredients)
				else:
					possible_ingredients = possible_ingredients.intersection(set(ingredients))


		allergen_map[allergen] = possible_ingredients
	
	print(allergen_map)

	possible_allergen_ingredients = set((i for a in allergen_map.values() for i in a))
	print(possible_allergen_ingredients)

	not_allergens = all_ingredients - possible_allergen_ingredients
	print(not_allergens)

	print('part1:',sum((i in ingredients for i in not_allergens for ingredients,_ in foods)))

	allergen_map_canon = {}
	allergen_map_keys = list(allergen_map.keys())
	while allergen_map_keys:
		for i in range(len(allergen_map_keys)):
			key = allergen_map_keys.pop()
			if len(allergen_map[key]) == 1:
				allergen_map_canon[key] = allergen_map[key].pop()
				for possiblilites in allergen_map.values():
					try:
						possiblilites.remove(allergen_map_canon[key])
					except KeyError:
						pass
			else:
				allergen_map_keys.insert(0,key)

	print(allergen_map_canon)
	print('part2:', ','.join((allergen_map_canon[k] for k in sorted(allergen_map_canon.keys()))))
	