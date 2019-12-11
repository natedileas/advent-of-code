# prog 
import numpy as np
import logging
logging.basicConfig(level=logging.DEBUG)

def runProg(prog, pos=0):
	prog = np.asarray(prog)

	nextCode = prog[pos]
	if nextCode == 99:
		return prog
	elif nextCode == 1:
		prog[pos+3] = np.sum(prog[prog[pos+1:pos+2]])
	elif nextCode == 2:
		prog[pos+3] = np.prod(prog[prog[pos+1:pos+2]])
	else:
		raise ValueError('Invalid opcode {}'.format(nextCode))

	logging.debug(prog)

	return runProg(prog, pos+4)

def test_day2():
	assert np.all(runProg([1,9,10,3,2,3,11,0,99,30,40,50]) == np.asarray([3500,9,10,70, 2,3,11,0, 99, 30,40,50]))
print(test_day2())