
# with open('test2.txt', 'r') as f:
with open('input2.txt', 'r') as f:
  lines = f.readlines()

data = [l.split() for l in lines]
rngs = [[int(i) for i in d[0].split('-')] for d in data]
ltrs = [d[1].replace(':', '') for d in data]

n_valid_pass = 0
for i in range(len(data)):
 nltrs = len(data[i][2]) - len(data[i][2].replace(ltrs[i], ''))
 n_valid_pass += rngs[i][0] <= nltrs <= rngs[i][1]


print('Part 1: ', n_valid_pass) # 655

n_valid_pass2 = 0
for i in range(len(data)):
 p = data[i][2]

 valid = True
 # try:
 loc1 = p[rngs[i][0]-1] == ltrs[i]
 # except:
  # loc1 = False

 # try:
 loc2 = p[rngs[i][1]-1] == ltrs[i]
 # except:
  # loc2 = False

 n_valid_pass2 += loc1 ^ loc2

print('Part 2: ', n_valid_pass2) # not 456