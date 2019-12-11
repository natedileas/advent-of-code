import numpy as np
import logging
import sys
import queue
import threading
logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')

class Memory(list):
	def _allocateTo(self, index):
		self.extend([0]*(index - len(self) + 1))

	def __getitem__(self, index_or_slice):
		if isinstance(index_or_slice, (int, np.int32, np.int)):
			if index_or_slice < 0:
				raise IndexError('index less than 0')
			elif index_or_slice > len(self) - 1:
				return 0
			else:
				return super(Memory, self).__getitem__(index_or_slice)

		elif isinstance(index_or_slice, slice):
			retvals = []
			for index in range(*index_or_slice.indices(index_or_slice.stop+1)):
				if index < 0:
					raise IndexError('index less than 0')
				elif index > len(self) - 1:
					retvals.append(0)
				else:
					retvals.append(super(Memory, self).__getitem__(index))

			return retvals

		else:
			raise IndexError('Index is not a single index or a slice.')

	def __setitem__(self, index_or_slice, value):
		if isinstance(index_or_slice, int):
			if index_or_slice < 0:
				raise IndexError('index less than 0')
			elif index_or_slice > len(self) - 1:
				self._allocateTo(index_or_slice)
				self[index_or_slice] = value
			else:
				super(Memory, self).__setitem__(index_or_slice, value)

		elif isinstance(index_or_slice, slice):
			for i, index in enumerate(range(*index_or_slice.indices(index_or_slice.stop+1))):
				if index < 0:
					raise IndexError('index less than 0')
				elif index > len(self) - 1:
					self._allocateTo(index)
					self[index] = value[i]
				else:
					super(Memory, self).__setitem__(index, value)
		else:
			raise IndexError('Index is not a single index or a slice.')

class OP:
	def __init__(self, n_params, operator, assigns=True, jumps=False):
		self.n_params = n_params
		self.operator = operator
		self.assigns = assigns
		self.jumps = jumps

class IntCodeComp(threading.Thread):

	OPS = \
	{
		1: OP(4, np.sum),   # sum of 2 inputs
		2: OP(4, np.prod),   # product of 2 inputs
		3: OP(2, None),   # input
		4: OP(2, None, assigns=False),   # output
		5: OP(3, lambda val: val[0] != 0, jumps=True, assigns=False),   # jump if true
		6: OP(3, lambda val: val[0] == 0, jumps=True, assigns=False),   # jump if false
		7: OP(4, lambda arr: int(arr[0] < arr[1])),   # less than
		8: OP(4, lambda arr: int(arr[0] == arr[1])),   # equals
	}

	def __init__(self, program, input_=queue.Queue(), output_=queue.Queue()):
		super(IntCodeComp, self).__init__()
		self.program = Memory(program)
		self._input = input_
		self._output = output_
		self.position = 0
		self.relative_base = 0

		# patch input + output ops
		self.OPS[3].operator = self.input
		self.OPS[4].operator = self.output

	def input(self, *args, **kwargs):
		logging.debug('Input: ')
		# all items move from left to right
		return int(self._input.get())

	def output(self, arr):
		# all items move from left to right
		logging.debug('Output: ')
		self._output.put(arr[0])

	def run(self):
		self.process()

	def process(self):
		# logging.debug(self.program)

		# patch input + output ops
		self.OPS[3].operator = self.input
		self.OPS[4].operator = self.output
	
		logging.info('START')
		while self.position < len(self.program) - 1:	
			logging.debug('self.position: {}'.format(self.position))
			# logging.debug('self.position: {}, self.program: {}'.format(self.position, self.program))
			nextCode = self.program[self.position]
			opcode = abs(nextCode) % 100   # last 2 digits of code

			parametermodes = []
			if str(abs(nextCode) // 100):   # there are explicit parameter modes
				parametermodes = [int(mode) for mode in str(abs(nextCode) // 100)]   # remaining digits

			if opcode == 99:
				logging.warning('HALT')
				break

			elif opcode in self.OPS:
				self.procOP(self.OPS[opcode], parametermodes)

			else:
				raise ValueError('Invalid opcode {}'.format(opcode))

		logging.info('EXIT')

		return self.program

	def procOP(self, op, modes=[]):
		""" process an operation on n operands. 

		modes of parameters are default 0, which indicates 
		position mode. mode 1 is immediate or value mode

		"""
		if op.assigns:
			raw_operands = self.program[self.position+1:self.position+op.n_params-1]
			destination = self.program[self.position+op.n_params-1]
		else:
			raw_operands = self.program[self.position+1:self.position+op.n_params]
			destination = None

		# if there is no mode specified or leading 0s, make them explicit
		while len(modes) < len(raw_operands):
					modes.insert(0, 0)
		modes = modes[::-1]

		# process operands according to the mode of each
		processed_operands = []
		for i, operand in enumerate(raw_operands):
			if modes[i] == 1:
				processed_operands.append(operand)
			elif modes[i] == 0:
				processed_operands.append(self.program[operand])
			else:
				raise ValueError('Operand mode {} not supported'.format(modes[i]))

		if op.jumps:
			if op.operator(processed_operands):
				self.position = processed_operands[1]
			else:
				self.position += op.n_params
		else:
			if op.assigns:
				self.program[destination] = op.operator(processed_operands)
			else:
				op.operator(processed_operands)
			
			self.position += op.n_params


if __name__ == '__main__':
	# day 2
	# realprog = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,9,19,23,2,23,13,27,1,27,9,31,2,31,6,35,1,5,35,39,1,10,39,43,2,43,6,47,1,10,47,51,2,6,51,55,1,5,55,59,1,59,9,63,1,13,63,67,2,6,67,71,1,5,71,75,2,6,75,79,2,79,6,83,1,13,83,87,1,9,87,91,1,9,91,95,1,5,95,99,1,5,99,103,2,13,103,107,1,6,107,111,1,9,111,115,2,6,115,119,1,13,119,123,1,123,6,127,1,127,5,131,2,10,131,135,2,135,10,139,1,13,139,143,1,10,143,147,1,2,147,151,1,6,151,0,99,2,14,0,0]
	# fixed_prog = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,9,19,23,2,23,13,27,1,27,9,31,2,31,6,35,1,5,35,39,1,10,39,43,2,43,6,47,1,10,47,51,2,6,51,55,1,5,55,59,1,59,9,63,1,13,63,67,2,6,67,71,1,5,71,75,2,6,75,79,2,79,6,83,1,13,83,87,1,9,87,91,1,9,91,95,1,5,95,99,1,5,99,103,2,13,103,107,1,6,107,111,1,9,111,115,2,6,115,119,1,13,119,123,1,123,6,127,1,127,5,131,2,10,131,135,2,135,10,139,1,13,139,143,1,10,143,147,1,2,147,151,1,6,151,0,99,2,14,0,0]
	# print(intCodeProc(fixed_prog)[0])

	logging.basicConfig(level=logging.DEBUG)


	# day 5 part 1; input 1
	TESTprog = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,68,5,225,1101,71,12,225,1,117,166,224,1001,224,-100,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1001,66,36,224,101,-87,224,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1101,26,51,225,1102,11,61,224,1001,224,-671,224,4,224,1002,223,8,223,1001,224,5,224,1,223,224,223,1101,59,77,224,101,-136,224,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,1101,11,36,225,1102,31,16,225,102,24,217,224,1001,224,-1656,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,101,60,169,224,1001,224,-147,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1102,38,69,225,1101,87,42,225,2,17,14,224,101,-355,224,224,4,224,102,8,223,223,1001,224,2,224,1,224,223,223,1002,113,89,224,101,-979,224,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1102,69,59,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,677,677,224,1002,223,2,223,1006,224,329,1001,223,1,223,1007,226,226,224,1002,223,2,223,1006,224,344,1001,223,1,223,1108,226,677,224,102,2,223,223,1005,224,359,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,374,101,1,223,223,1107,677,226,224,1002,223,2,223,1006,224,389,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,404,101,1,223,223,1008,677,226,224,102,2,223,223,1005,224,419,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,434,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,449,1001,223,1,223,108,226,677,224,102,2,223,223,1005,224,464,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,479,101,1,223,223,1007,226,677,224,102,2,223,223,1006,224,494,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,509,101,1,223,223,108,677,677,224,102,2,223,223,1006,224,524,1001,223,1,223,8,226,677,224,102,2,223,223,1005,224,539,101,1,223,223,107,677,226,224,102,2,223,223,1005,224,554,1001,223,1,223,8,226,226,224,102,2,223,223,1006,224,569,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,584,1001,223,1,223,1108,226,226,224,102,2,223,223,1005,224,599,1001,223,1,223,1107,677,677,224,1002,223,2,223,1006,224,614,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,629,1001,223,1,223,108,226,226,224,102,2,223,223,1005,224,644,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,659,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226]
	intCodeProc(TESTprog)
