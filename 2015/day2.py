
def estimate_present_size(p):
	l, w, h = p
	sa = 2*l*w + 2*w*h + 2*h*l

	mins1 = min(p)
	p.remove(mins1)
	mins2 = min(p)

	return sa + mins2 * mins1

def min_perimeter(p):
	l, w, h = p
	all_ps = [2*l+2*w, 2*l+2*h, 2*w+2*h]
	return min(all_ps) + l * w * h

lines = open('input2.txt').read().splitlines()
presents = [[int(i) for i in l.split('x')] for l in lines]

print(estimate_present_size([2,3,4]))
print(min_perimeter([2,3,4]))
print(estimate_present_size([1,1,10]))
print(min_perimeter([1,1,10]))
print(sum(map(min_perimeter, presents)))
print(sum(map(estimate_present_size, presents)))