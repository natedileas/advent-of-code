
if __name__ == '__main__':
	from intcode import *
	comp = IntCodeComp([3,9,8,9,10,9,4,9,99,-1,8])
	comp.put_input(8)
	comp.process()

	print(comp.get_output())