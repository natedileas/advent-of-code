
class InfiniteLoopException(Exception): pass

class Boot:
	def __init__(self, data):
		self.lines = list(filter(lambda l:l, data.splitlines()))
		self.index = 0
		self.acc = 0

	def run(self):
		indices = []
		self.index = 0
		self.acc = 0	

		while self.index < len(self.lines):
			if self.index in indices:
				raise InfiniteLoopException(f'infinite loop at index: {self.index}')

			indices.append(self.index)
			op = self.lines[self.index]
			
			# print(op, self.index, self.acc)
			optype, num = op.split()

			if optype == 'nop':
				self.index += 1
				continue
			elif optype == 'jmp':
				self.index += int(num)
			elif optype == 'acc':
				self.index += 1
				self.acc += int(num)

	def fix_program(self):
		for i, line in enumerate(self.lines):
			optype, num = line.split()
			oldline = line
			if optype == 'nop':
				newline = 'jmp ' + num
			elif optype == 'jmp':
				newline = 'nop ' + num
			else:
				newline = oldline

			self.lines[i] = newline
			try:
				self.run()
				return
			except InfiniteLoopException:
				pass

			self.lines[i] = oldline


TEST1 = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

INPUT = open('input8.txt').read()

if __name__ == '__main__':
	b = Boot(INPUT)

	try:
		b.run()
	except InfiniteLoopException:
		pass
	print('part 1:', b.acc)

	b.fix_program()
	print('part 2:', b.acc)
