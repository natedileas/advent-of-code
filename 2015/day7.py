import re


class Circuit:
	def __init__(self, desc):
		self.desc = desc
		self.wires = {}
		self.ops = {
			'AND': lambda a, b: a & b,
			'OR': lambda a, b: a | b,
			'LSHIFT': lambda a, b: a << b,
			'RSHIFT': lambda a, b: a >> b,
			'NOT': lambda a: 2**16 + (~a),
		}

	def run(self):
		lines = self.desc.copy()

		while lines:
			# for line in lines:
			line = lines.pop(0)
			if line:
				ret = self.parse_line(line)
				if ret == -1:
					print('ERROR:', line)
				elif ret == -2:
					# not ready yet. put to the back of the line
					lines.append(line)


	def parse_line(self, line):
		inputs, output = line.split('->')
		output = output.strip()
		inputs = inputs.strip()

		match = re.fullmatch(r'([a-z]+|\d+)', inputs)
		if match:
			ina = match.group()

			try:
				a = int(ina) if ina.isnumeric() else self.wires[ina]
			except KeyError:
				return -2

			self.wires[output] = a
			return 0

		match = re.fullmatch(r'([a-z]+|\d+) (AND|OR|LSHIFT|RSHIFT) ([a-z]+|\d+)', inputs)
		if match:
			ina, op, inb = match.groups()

			try:
				a = int(ina) if ina.isnumeric() else self.wires[ina]
				b = int(inb) if inb.isnumeric() else self.wires[inb]
			except KeyError:
				return -2

			self.wires[output] = self.ops[op](a, b)
			return 0

		match = re.fullmatch(r'NOT ([a-z]+)', inputs)
		if match:
			ina, = match.groups()

			try:
				a = int(ina) if ina.isnumeric() else self.wires[ina]
			except KeyError:
				return -2

			self.wires[output] = self.ops['NOT'](a)
			return 0

		return -1

class CircuitGraph:
	ops = {
			'AND': lambda a, b: a & b,
			'OR': lambda a, b: a | b,
			'LSHIFT': lambda a, b: a << b,
			'RSHIFT': lambda a, b: a >> b,
			'NOT': lambda a: 2**16 + (~a),
		}

	def __init__(self, desc):
		self.desc = desc
		self.graph = {}
		self.wires = {}
		self.parse_lines()

	def run(self):
		# find the top node, and start there. Walk the graph and perform the ops.
		while not all((v is not None for (v,i,o) in self.graph.values())):
			for node, (value, inputs, outputs) in self.graph.items():
				if value is None:
					outputs = outputs[0]
					op = outputs[-1]
					if op == 'NOT':
						ina, op = outputs
						ready = True

						if isinstance(ina, str):
							if ina in self.wires:
								a = self.wires[ina]
							else:
								ready &= False
						else:
							a = ina
						if ready:
							self.wires[node] = self.ops[op](a)
							self.graph[node][0] = self.wires[node]

					else:
						ina, inb, op = outputs

						ready = True

						if isinstance(ina, str):
							if ina in self.wires:
								a = self.wires[ina]
							else:
								ready &= False
						else:
							a = ina

						if isinstance(inb, str):
							if inb in self.wires:
								b = self.wires[inb]
							else:
								ready &= False
						else:
							b = inb

						
						if ready:
							self.wires[node] = self.ops[op](a, b)
							self.graph[node][0] = self.wires[node]

	def make_node(self, label, value=None):
		if not label in self.graph:
			self.graph[label] = [value, [], []]

	def add_edge(self, input1, output, op):
		self.make_node(input1)
		self.make_node(output)
		self.graph[input1][1].append((output, op))
		self.graph[output][2].append((input1, op))

	def add_dual_edge(self, in1, in2, output, op):
		self.make_node(in1)
		self.make_node(in2)
		self.make_node(output)

		self.graph[in1][1].append((output, op))
		self.graph[in2][1].append((output, op))
		self.graph[output][2].append((in1, in2, op))

	def parse_lines(self):
		for line in self.desc:
			if not line: continue

			inputs, output = line.split('->')
			output = output.strip()
			inputs = inputs.strip()


			match = re.fullmatch(r'\d+', inputs)
			if match:
				value = int(match.group())
				# self.graph[output]

				self.make_node(output, value)
				self.wires[output] = value

			match = re.fullmatch(r'([a-z]+|\d+) (AND|OR|LSHIFT|RSHIFT) ([a-z]+|\d+)', inputs)
			if match:
				ina, op, inb = match.groups()

				a = int(ina) if ina.isnumeric() else ina
				b = int(inb) if inb.isnumeric() else inb

				self.make_node(output, None)
				self.add_dual_edge(a, b, output, op)

			match = re.fullmatch(r'NOT ([a-z]+)', inputs)
			if match:
				ina, = match.groups()

				self.make_node(output, None)
				self.add_edge(ina, output, 'NOT')

TEST1 = """
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
"""

if __name__ == '__main__':
	
	c = Circuit(TEST1.splitlines())
	c.run()
	print(c.wires)

	c = Circuit(open('input7.txt').read().splitlines())
	c.run()
	print(c.wires)
	print(c.wires['a'])

	c = Circuit(open('input7-2.txt').read().splitlines())
	# c.wires['b'] = 46065
	c.run()
	print(c.wires['a'])
