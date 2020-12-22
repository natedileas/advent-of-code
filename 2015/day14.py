INPUT = """
Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
Blitzen can fly 13 km/s for 4 seconds, but then must rest for 49 seconds.
Rudolph can fly 20 km/s for 7 seconds, but then must rest for 132 seconds.
Cupid can fly 12 km/s for 4 seconds, but then must rest for 43 seconds.
Donner can fly 9 km/s for 5 seconds, but then must rest for 38 seconds.
Dasher can fly 10 km/s for 4 seconds, but then must rest for 37 seconds.
Comet can fly 3 km/s for 37 seconds, but then must rest for 76 seconds.
Prancer can fly 9 km/s for 12 seconds, but then must rest for 97 seconds.
Dancer can fly 37 km/s for 1 seconds, but then must rest for 36 seconds.
"""

TEST1 = """
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
"""

REGEX = r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\."

import re
import itertools
import pprint

if __name__ == '__main__':
	# INPUT = TEST1
	deers = {}
	for line in filter(None, INPUT.splitlines()):
		name, speed, duration, rest = re.fullmatch(REGEX, line).groups()
		deers[name] = dict(speed=int(speed), duration=int(duration), rest=int(rest))

	print(deers)

	def distance(deer, time):
		# calculate the how far the deer is at time t
		cycle = deer['duration'] + deer['rest']

		# number of full cycles + 		any partial cycles           *	 km/s 		 *  s per cycle actually moving
		dist = ((time // cycle) + min(time % cycle, deer['duration']) / deer['duration']) * deer['speed'] * deer['duration']

		return dist

	# print([distance(deer, 1) for deer in deers.values()])
	# print([distance(deer, 10) for deer in deers.values()])
	# print([distance(deer, 11) for deer in deers.values()])
	# print([distance(deer, 12) for deer in deers.values()])
	# print([distance(deer, 138) for deer in deers.values()])
	# print([distance(deer, 139) for deer in deers.values()])
	# print([distance(deer, 1000) for deer in deers.values()])
	print(max((distance(deer, 2503) for deer in deers.values())))

	for i in range(2503):
		leaddeer = max(deers, key=lambda d: distance(deers[d], i))
		deers[leaddeer].setdefault('score', 0)
		deers[leaddeer]['score'] += 1

	print(deers[max(deers, key=lambda d:deers[d].get('score',0))]['score'])
