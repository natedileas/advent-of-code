import numpy as np
INPUT = open('input11.txt').read()

charmap = {
		'.': 0,
		'L': 1,
		'#': 2,
	}
revcharmap = {v:k for k,v in charmap.items()}

def data2arr(data):
	
	arr = []

	for line in data.splitlines():
		if not line: continue
		arrline = []
		for char in line:
			arrline.append(charmap[char])
		arr.append(arrline)

	return np.asarray(arr)

def print_arr(arr):
	lines = []
	for y in range(arr.shape[0]):
		line = ''
		for x in range(arr.shape[1]):
			line += revcharmap[arr[y,x]]
		lines.append(line)
	return '\n'.join(lines)

def num_occupied_8(arr, y, x):
	return (arr[max(y-1,0):min(y+2,arr.shape[0]),max(x-1,0):min(x+2,arr.shape[1])] == 2).sum() - int(arr[y,x] == 2)

def apply_rules1(arr):
	"""
	0 floor
	1 empty
	2 occupied
	"""
	newarr = np.zeros(arr.shape)
	for y in range(arr.shape[0]):
		for x in range(arr.shape[1]):
			state = arr[y,x]
			n = num_occupied_8(arr, y, x)
			if state == 1 and n == 0:
				newarr[y,x] = 2
			elif state == 2 and n >= 4:
				newarr[y,x] = 1
			else:
				newarr[y,x] = state

	return newarr

def num_seen_occupied(arr, y, x):
	count = 0

	up = arr[0:y,x][::-1]   # closer to the start is closer in vision
	down = arr[y+1:arr.shape[0],x]   # closer to the start is closer in vision
	try:
		count += int(up[up != 0][0] == 2)
	except:
		pass

	try:
		count += int(down[down != 0][0] == 2)
	except:
		pass

	# count += int(down[down != 0][0] == 2)
	left = arr[y,0:x][::-1]   # closer to the start is closer in vision
	right = arr[y,x+1:arr.shape[1]]   # closer to the start is closer in vision
	# count += int(left[left != 0][0] == 2)
	# count += int(right[right != 0][0] == 2)

	try:
		count += int(left[left != 0][0] == 2)
	except:
		pass
	try:
		count += int(right[right != 0][0] == 2)
	except:
		pass

	yidx = np.arange(0, y)[::-1]
	xidx = np.arange(0, x)[::-1]
	yidx = yidx[:min(len(yidx), len(xidx))]
	xidx = xidx[:min(len(yidx), len(xidx))]

	leftupdiag = arr[yidx, xidx]
	try:
		count += int(leftupdiag[leftupdiag != 0][0] == 2)
	except:
		pass
	# count += int(leftupdiag[leftupdiag != 0][0] == 2)

	yidx = np.arange(y+1, arr.shape[0])
	xidx = np.arange(0, x)[::-1]
	yidx = yidx[:min(len(yidx), len(xidx))]
	xidx = xidx[:min(len(yidx), len(xidx))]

	leftdowndiag = arr[yidx, xidx]
	try:
		count += int(leftdowndiag[leftdowndiag != 0][0] == 2)
	except:
		pass
	# count += int(leftdowndiag[leftdowndiag != 0][0] == 2)
#

	yidx = np.arange(0, y)[::-1]
	xidx = np.arange(x+1, arr.shape[1])
	yidx = yidx[:min(len(yidx), len(xidx))]
	xidx = xidx[:min(len(yidx), len(xidx))]

	rightupdiag = arr[yidx, xidx]
	# count += int(leftupdiag[leftupdiag != 0][0] == 2)
	try:
		count += int(rightupdiag[rightupdiag != 0][0] == 2)
	except:
		pass

	yidx = np.arange(y+1, arr.shape[0])
	xidx = np.arange(x+1, arr.shape[1])
	yidx = yidx[:min(len(yidx), len(xidx))]
	xidx = xidx[:min(len(yidx), len(xidx))]

	rightdowndiag = arr[yidx, xidx]
	try:
		count += int(rightdowndiag[rightdowndiag != 0][0] == 2)
	except:
		pass

	# count += int(rightdowndiag[rightdowndiag != 0][0] == 2)

	return count



def apply_rules2(arr):
	"""
	0 floor
	1 empty
	2 occupied
	"""
	newarr = np.zeros(arr.shape)
	for y in range(arr.shape[0]):
		for x in range(arr.shape[1]):
			state = arr[y,x]
			n = num_seen_occupied(arr, y, x)
			if state == 1 and n == 0:
				newarr[y,x] = 2
			elif state == 2 and n >= 5:
				newarr[y,x] = 1
			else:
				newarr[y,x] = state

	return newarr

def run_till_stable1(arr):
	i = 0
	while True:
		print(i, '=============')
		print(print_arr(arr))
		oldarr = arr.copy()
		arr = apply_rules1(oldarr)

		if (oldarr == arr).all():
			break

		i += 1

	return arr

def run_till_stable2(arr):
	i = 0
	while True:
		print(i, '=============')
		# print(print_arr(arr))
		oldarr = arr.copy()
		arr = apply_rules2(oldarr)

		if (oldarr == arr).all():
			break

		i += 1

	return arr

TEST1 = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

if __name__ == '__main__':
	arr = data2arr(INPUT)
	# print(arr)
	# for i in range(5):
	# 	arr = apply_rules1(arr)
	# 	print(arr)
	arr = run_till_stable2(arr)
	print((arr == 2).sum(), 37)
