from intcode import *
import logging


if __name__ == '__main__':
	# logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')

	# # p = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
	# p = [1102,34915192,34915192,7,4,7,99,0]
	# # p = [104,1125899906842624,99]
	# c = IntCodeComp(p)
	# c.process()
	
	# while True:
	# 	print(c._output.get(False))


	input9 = [int(i) for i in open('input9.txt', 'r').read().split(',') if i.strip()]

	c = IntCodeComp(input9)
	c._input.put(2)
	c.process()

	while True:
		print(c._output.get(False))
