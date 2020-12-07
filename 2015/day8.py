import re

TEST1 = r"""
""
"abc"
"aaa\"aaa"
"\x27"
"""

if __name__ == '__main__':
	data = open('input8.txt').read()
	lines = data.splitlines()

	codelen = lambda s: len(s)
	def memlen(s):

		news = re.sub(r'\\x[a-f0-9]{2}|\\\"|\\\\', 'a', s)
		news = re.sub(r'^"|"$', '', news)
		# print(s, news)

		return len(news) 

	def enclen(s):

		news = re.sub(r'\\',r'\\\\', s)
		news = re.sub(r'"',r'\\"', news)
		news = '"{}"'.format(news)

		# print(s, news, len(news))
		# news = re.sub(r'\\',r'\\\\', s)
		return len(news)


	def difflen(lines):
		return sum((codelen(l) - memlen(l) for l in lines))
	
	def diffenclen(lines):
		return sum((enclen(l) - codelen(l) for l in lines))

	print(difflen(TEST1.splitlines()))
	print(difflen(lines))

	print(diffenclen(TEST1.splitlines()))
	print(diffenclen(lines))