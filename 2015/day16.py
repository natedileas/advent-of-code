sue = """
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
"""

sue_n = dict((line.split(':') for line in filter(None, sue.splitlines())))

for attr in sue_n:
	sue_n[attr] = int(sue_n[attr])
# print(sue_n)

import re

all_sues_text = open('input16.txt').read()
all_sues = {}
for line in all_sues_text.splitlines():
	if line:
		n = int(re.match(r'^Sue (\d+):', line).group(1))
		rhs = line[line.find(':')+1:]

		attributes = {item.split(':')[0].strip():int(item.split(':')[1].strip()) for item in rhs.split(',')}
		all_sues[n] = attributes

# print(all_sues)

for sue in all_sues:
	if all((sue_n[attr] == all_sues[sue].get(attr) for attr in sue_n if all_sues[sue].get(attr))):
		print(sue)
		# break

# for sue, attrs in all_sues.items():
# 	for attr, value in sue_n.items():
# 		if attrs.get(attr) == value:
# 			print(sue, attr)


for sue in all_sues:
	match = True

	match &= sue_n['cats'] < all_sues[sue].get('cats', 1000)
	match &= sue_n['trees'] < all_sues[sue].get('trees', 1000)
	match &= sue_n['pomeranians'] > all_sues[sue].get('pomeranians', -1)
	match &= sue_n['goldfish'] > all_sues[sue].get('goldfish', -1)

	match &= sue_n['children'] == all_sues[sue].get('children', sue_n['children'])
	match &= sue_n['samoyeds'] == all_sues[sue].get('samoyeds', sue_n['samoyeds'])
	match &= sue_n['akitas'] == all_sues[sue].get('akitas', sue_n['akitas'])
	match &= sue_n['vizslas'] == all_sues[sue].get('vizslas', sue_n['vizslas'])
	match &= sue_n['cars'] == all_sues[sue].get('cars', sue_n['cars'])
	match &= sue_n['perfumes'] == all_sues[sue].get('perfumes', sue_n['perfumes'])

	if match:
		print(sue)
		# break