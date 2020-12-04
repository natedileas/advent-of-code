
req_fields = [
'byr', #(Birth Year)
'iyr', #(Issue Year)
'eyr', #(Expiration Year)
'hgt', #(Height)
'hcl', #(Hair Color)
'ecl', #(Eye Color)
'pid', #(Passport ID)
# 'cid', #(Country ID)
]

def is_valid_1(passport):
	valid = True

	for req in req_fields:
		valid &= (req in passport)

	return valid


def is_valid_2(passport):
	import re
	valid = is_valid_1(passport)

	valid &= (1920 <= int(passport.get('byr',0)) <= 2002)
	valid &= (2010 <= int(passport.get('iyr',0)) <= 2020)
	valid &= (2020 <= int(passport.get('eyr',0)) <= 2030)

	height = passport.get('hgt', '')
	try:
		heightval, heightunit = re.fullmatch('(\d+)(cm|in)', height).groups()
		if heightunit == 'cm':
			valid &= (150 <= int(heightval) <= 193)
		elif heightunit == 'in':
			valid &= (59 <= int(heightval) <= 76)
		else:
			valid &= False
	except AttributeError:
		valid &= False

	valid &= re.fullmatch('#[0-9a-f]{6}', passport.get('hcl', '')) is not None
	valid &= passport.get('ecl', '') in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl','oth')
	valid &= re.fullmatch('\d{9}', passport.get('pid', '')) is not None

	return valid

def parse_passport(data):
	pp = {}
	for kvp in data.split():
		key, value = kvp.split(':')
		pp[key] = value

	return pp

# with open('test4.txt', 'r') as f:
with open('input4.txt', 'r') as f:
# with open('invalid4.txt', 'r') as f:
# with open('valid4.txt', 'r') as f:
	data = f.read()

passports = [parse_passport(d) for d in data.split('\n\n')]

count_valid = 0
for passport in passports:
	count_valid += int(is_valid_1(passport))
print('Part 1:', count_valid)  # 200

count_valid = 0
for passport in passports:
	count_valid += int(is_valid_2(passport))
print('Part 2:', count_valid) # 116

