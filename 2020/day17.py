import numpy as np
INPUT = open('input17.txt').read()
TEST = """
.#.
..#
###
"""


def convert2state(data):
	state = [[[i for i in l] for l in data.splitlines() if l]]
	state = np.asarray(state) == '#'
	return state


def apply_rules(state1):
	state1 = np.pad(state1, [(2,2), (2,2), (2,2)])
	state2 = np.zeros(state1.shape, dtype=bool)
	zlen, ylen, xlen = state2.shape

	for z in range(1,zlen - 1):
		for y in range(1,ylen - 1):
			for x in range(1,xlen - 1):
				neighborindices = [(zz,yy,xx) for zz in range(z-1,z+2) for yy in range(y-1,y+2) for xx in range(x-1,x+2)]
				neighborindices.remove((z,y,x))
				neighborindices = tuple(np.array(neighborindices).T)

				# print(neighborindices)

				sumneighbors = state1[neighborindices].sum()
				curstate = state1[z,y,x]
				if curstate == True:
					if 2 <= sumneighbors <= 3:
						state2[z,y,x] = True
					else:
						state2[z,y,x] = False
				else:
					if sumneighbors == 3:
						state2[z,y,x] = True
					else:
						state2[z,y,x] = False
	return state2


def convert2state_hyper(data):
	state = [[[[i for i in l] for l in data.splitlines() if l]]]
	state = np.asarray(state) == '#'
	return state



def apply_rules_hyper(state1):
	state1 = np.pad(state1, [(2,2), (2,2), (2,2), (2,2)])
	state2 = np.zeros(state1.shape, dtype=bool)
	wlen, zlen, ylen, xlen = state2.shape

	for w in range(1, wlen - 1):
		for z in range(1,zlen - 1):
			for y in range(1,ylen - 1):
				for x in range(1,xlen - 1):
					neighborindices = [(ww,zz,yy,xx) for ww in range(w-1,w+2) for zz in range(z-1,z+2) for yy in range(y-1,y+2) for xx in range(x-1,x+2)]
					neighborindices.remove((w,z,y,x))
					neighborindices = tuple(np.array(neighborindices).T)

					# print(neighborindices)

					sumneighbors = state1[neighborindices].sum()
					curstate = state1[w,z,y,x]
					if curstate == True:
						if 2 <= sumneighbors <= 3:
							state2[w,z,y,x] = True
						else:
							state2[w,z,y,x] = False
					else:
						if sumneighbors == 3:
							state2[w,z,y,x] = True
						else:
							state2[w,z,y,x] = False
	return state2


# INPUT = TEST
# state = convert2state(INPUT)
# # print(state)

# for i in range(6):
# 	print(i)
# 	# print(state)
# 	state = apply_rules(state)

# # import pprint
# # pprint.pprint(state)

# print(state.sum())

state = convert2state_hyper(INPUT)
for  i in range(6):
	print(i)
	state = apply_rules_hyper(state)

print(state.sum())
