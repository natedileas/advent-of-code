
def boarding_pass_row(seq):
	assert len(seq) == 7

	# FBFBBFF
	seqb = seq.replace('F', '0').replace('B', '1')
	return int(seqb, 2)


def boarding_pass_col(seq):
	assert len(seq) == 3
	
	seqb = seq.replace('R', '1').replace('L', '0')
	return int(seqb, 2)

def row_id(seq):
	row, col = boarding_pass_row(seq[:7]), boarding_pass_col(seq[7:])
	return 8 * row + col


if __name__ == '__main__':
	print(row_id('FBFBBFFRLR'))
	print(row_id('BFFFBBFRRR'))
	print(row_id('FFFBBBFRRR'))
	print(row_id('BBFFBBFRLL'))

	ids = open('input5.txt').read().splitlines()
	all_ids = [row_id(i) for i in ids]
	print('p1:', max(all_ids))

"""
>>> d = np.diff(np.sort(all_ids))
>>> np.where(d != 1)
(array([652], dtype=int64),)
>>> np.sort(all_ids)[652]
698
>>> np.sort(all_ids)[651:654]
array([697, 698, 700])

"""
print('p2:', 699)