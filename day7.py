import queue
import time
import logging

from intcode import IntCodeComp

logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')

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

	amps[0]._input.put(0)
	time.sleep(1)
	[amp.start() for amp in amps]

	if feedback:
		amps[0]._input = amps[-1]._output

	
	while True:
		logging.debug('WAIT')
		amps[-1].join(1)

		if not amps[-1].is_alive():
			break
	
	return amps[-1]._output.pop()


if __name__ == '__main__':
	import logging
	logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')

	from itertools import permutations

	# part 1
	amplifier_prog = [int(item) for item in open('input7.txt', 'r').read().split(',')]
	max_amp = 0
	for phases in permutations([0,1,2,3,4]):
		max_amp = max(max_amp, make_amplifier_series(amplifier_prog, phases))

	print('Part 1: ', max_amp)

	max_amp = 0
	for phases in permutations(list(range(5,10))):
		max_amp = max(max_amp, make_amplifier_series(amplifier_prog, phases, feedback=True))

	print('Part 2: ', max_amp)

	# amplifier_prog = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
	# make_amplifier_series(amplifier_prog, [4,3,2,1,0])

	
