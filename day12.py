import numpy as np
import logging
import itertools


class Moon:
	def __init__(self, x, y, z):
		self.position = np.array([x,y,z],dtype=int)
		self.velocity = np.array([0,0,0],dtype=int)
	
	def energy(self):
		return np.abs(self.position).sum() * np.abs(self.position).sum()

	@property
	def x(self):
		return self.position[0], self.velocity[0]

	@property
	def y(self):
		return self.position[1], self.velocity[1]

	@property
	def z(self):
		return self.position[2], self.velocity[2]

	def __repr__(self): return str(self)
	def __str__(self): return f'pos:{self.position} vel:{self.velocity}\n'		

def processMoons(moons, n):
	"""
	o apply gravity, consider every pair of moons. On each axis (x, y, and z), the velocity of each moon changes by exactly +1 or -1 to pull the moons together. For example, if Ganymede has an x position of 3, and Callisto has a x position of 5, then Ganymede's x velocity changes by +1 (because 5 > 3) and Callisto's x velocity changes by -1 (because 3 < 5). However, if the positions on a given axis are the same, the velocity on that axis does not change for that pair of moons.

Once all gravity has been applied, apply velocity: simply add the velocity of each moon to its own position. For example, if Europa has a position of x=1, y=2, z=3 and a velocity of x=-2, y=0,z=3, then its new position would be x=-1, y=2, z=6. This process does not modify the velocity of any moon.

	"""

	for i in range(n):
		logging.debug(moons)

		# gravity
		for moon1, moon2 in itertools.combinations(moons, 2):
			add = 1 * (moon1.position < moon2.position) - 1 * (moon1.position > moon2.position)
			add[moon1.position == moon2.position] = 0
			moon1.velocity += add
			moon2.velocity += np.negative(add)

		# update positions
		for moon in moons:
			moon.position += moon.velocity

	return moons


def predictRecurrence(moons):
	prev = [[None]]*3
	cycles = [[None]]*3
	for i in range(1000):
		
		prev[0].append([m.x for m in moons])
		prev[1].append([m.y for m in moons])
		prev[2].append([m.z for m in moons])

		moons = processMoons(moons,1)

		xs = [m.x for m in moons]
		if xs in prev[0]:
			cycles[0].append(i - prev[0].index(xs))

		if [m.y for m in moons] in prev[1]:
			cycles[1].append(i - prev[1].index([m.y for m in moons]))

		if [m.z for m in moons] in prev[2]:
			cycles[2].append(i - prev[2].index([m.z for m in moons]))

	return cycles


if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)
	tm1 = [Moon(x,y,z) for x,y,z in ((-1,0, 2), (2, -10, -7), (4, -8, 8), (3, 5, -1))]
	processMoons(tm1, 10)
	c = predictRecurrence(tm1)