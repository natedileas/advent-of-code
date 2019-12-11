import queue
import time
import logging

from intcode import IntCodeComp


def make_amplifier_series(prog, phases, feedback=False):
	
	amps = []
	lastout = None
	for i in range(5):

		out_ = queue.Queue()
		amp = IntCodeComp(prog,
			input_=lastout if lastout is not None else queue.Queue(),
			output_=out_
			)
		lastout	= out_
		amp._input.put(phases[i])

		amps.append(amp)


	if feedback:
		phase0 = amps[0]._input.get()
		amps[0]._input = amps[-1]._output
		amps[0]._input.put(phase0)

	amps[0]._input.put(0)

	while any([not amp.done for amp in amps]):
		# logging.info([not amp.done for amp in amps])
		for i, amp in enumerate(amps):
			logging.info('WAIT {}'.format(i))
			amp.process()
	
	return amps[-1]._output.get()


if __name__ == '__main__':
	import logging
	logging.basicConfig(level=logging.ERROR, format='%(relativeCreated)6d %(threadName)s %(message)s')

	from itertools import permutations

	# part 1
	amplifier_prog = [int(item) for item in open('input7.txt', 'r').read().split(',')]
	# max_amp = 0
	# for phases in permutations([0,1,2,3,4]):
	# 	max_amp = max(max_amp, make_amplifier_series(amplifier_prog, phases))

	# print('Part 1: ', max_amp)

	# amplifier_prog = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
	# amplifier_prog = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54, -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4, 53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
	max_amp = 0
	for phases in permutations(list(range(5,10))):
		max_amp = max(max_amp, make_amplifier_series(amplifier_prog, phases, feedback=True))

	print('Part 2: ', max_amp)

	# amplifier_prog = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
	# make_amplifier_series(amplifier_prog, [4,3,2,1,0])

	
