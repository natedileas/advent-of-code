INPUT = '871369452'
TEST1 = '389125467'

def str2cups(s):
    return list(map(int, s))

def move(cups, currcup):
    # cups = [cups[i] for i in range(cups.index(currcup)-len(cups)-1, cups.index(currcup)-1)]
    # cups to move
    threecups = []
    for i in range(3):
        # TODO wrap
        threecups.append(cups.pop((cups.index(currcup)+1) % len(cups)))

    # print('pick up: ', threecups, cups)
    # find destination cup
    i = 1
    while True:
        try:
            cup = (currcup - i) % 10
            dest = cups.index(cup)
            break
        except ValueError:
            i += 1

    # print('destination:', cups[dest])

    for i in range(3):
        cups.insert(dest+1, threecups.pop())

    return cups, cups[(cups.index(currcup) + 1) % len(cups)]


def do_moves(s,n=10):
    cups = str2cups(s)
    currcup = cups[0]
    for i in range(n):
        # print(f'move {i+1}')
        # print('cups:', cups)
        # print('currcup:', currcup)

        cups, currcup = move(cups, currcup)
        # print()

    # order from 1
    index1 = cups.index(1)
    return ''.join(map(str, (cups[i] for i in range(index1-len(cups)+1,index1))))


def move_big(cups, currcup, lencups=10**6):
    # cups to move
    

    return cups, cups[(cups.index(currcup) + 1) % len(cups)]


class LLNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# @profile
def do_moves_big(s, n=10**7):
    cups = str2cups(s)
    
    cup2node = {}
    first = LLNode(cups[0])
    cup2node[cups[0]] = first
    prev = first
    for i in cups[1:]:
        nextnode = LLNode(i)
        cup2node[i] = nextnode
        prev.next = nextnode
        prev = nextnode

    for i in range(max(cups)+1, 10**6+1):
        nextnode = LLNode(i)
        cup2node[i] = nextnode
        prev.next = nextnode
        prev = nextnode

    prev.next = first 
    curr = first

    for ii in range(n):
        if ii % 10000 == 0: print('\r', ii, end='')

        # get three cups to the right of currcupindex
        next1 = curr.next
        next2 = next1.next
        next3 = next2.next
        newcurrnext = next3.next

        # find destination cups
        nextcup = curr.value
        while True:
            nextcup -= 1
            if nextcup < 1:
                nextcup = 10**6
            if (cup2node[nextcup].value == next1.value or
                cup2node[nextcup].value ==  next2.value or
                cup2node[nextcup].value ==  next3.value):
                continue
            else:
                break
            
        dest1 = cup2node[nextcup]
        dest2 = dest1.next
        # insert
        dest1.next = next1
        next3.next = dest2
        # next
        curr.next = newcurrnext
        curr = curr.next

    print()
    node1 = cup2node[1]
    node2 = node1.next
    node3 = node2.next
    print(node2.value, node3.value, node2.value * node3.value)
    return node2.value * node3.value


if __name__ == '__main__':
    # print(do_moves(TEST1, 10))
    # print(do_moves(TEST1, 100))
    # print(do_moves(INPUT, 100))
    print(do_moves_big('389125467'))
    print(do_moves_big(INPUT))
