import json

INPUT = json.load(open('input12.json'))

def sumnums(doc, s=0):
	if isinstance(doc, list):
		for element in doc:
			s += sumnums(element, 0)
	elif isinstance(doc, dict):
		for element in doc.values():
			s += sumnums(element, 0)
	elif isinstance(doc, int):
		s += doc

	return s

def sumnums2(doc, s=0):
	if isinstance(doc, list):
		for element in doc:
			s += sumnums2(element, 0)
	elif isinstance(doc, dict):
		if "red" in doc.values():
			return 0

		for element in doc.values():
			s += sumnums2(element, 0)

	elif isinstance(doc, int):
		s += doc

	return s

if __name__ == '__main__':
	
	print(sumnums(INPUT, 0))
	print(sumnums2(INPUT, 0))