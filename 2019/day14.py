import math

# def Node:
#   def __init__(self, label, value):
#       self.label = label
#       self.value = value
#       self.children = []

def parseitem(item):
    amount, unit = item.strip().split()
    return [int(amount), unit]

def count_ore(reactions, root='FUEL', bottom='ORE'):
    mapp = {}
    mapp[bottom] = (1, None)
    suminputs = {}
    for line in reactions.splitlines():
        if line:
            ins, out = line.split('=>')
            inputs = [parseitem(i) for i in ins.split(',')]
            outamount, outunit = parseitem(out)
            mapp[outunit] = outamount, inputs

            for inamount, inunit in inputs:
                suminputs.setdefault(inunit, 0)
                suminputs[inunit] += inamount

    def _cnt_ore_recur(outunit, level=0):
        # this works if every reaction is separate. but I need to count up all the instances and then divide into them.
        outamount, inputs = mapp[outunit]

        if outunit == bottom:
            return outamount

        ore = 0
        for inamount, inunit in inputs:
            logging.debug(f'{level}: {outunit}, {outamount}, {inunit}, {inamount}')
            ore += _cnt_ore_recur(inunit, level=level+1) * outamount * suminputs[inunit]
            logging.debug(f'{level}: {outunit}, {ore}')

        return ore

    def _cnt_ore_cum(outunit):
        # starting from root
        # for a given input, find all the inputs of the same type
        pass

    return _cnt_ore_recur(root)
        

def map2graph(reactions):
    graph = {}
    graph['ORE'] = [1, []]

    for line in reactions.splitlines():
        if line:
            ins, out = line.split('=>')
            inputs = [parseitem(i) for i in ins.split(',')]
            outamount, outunit = parseitem(out)
            graph[outunit] = [outamount, inputs]

    def find_all_paths(start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to 
            end_vertex in graph """
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for amount, vertex in graph[start_vertex][1]:
            if vertex not in path:
                extended_paths = find_all_paths(vertex, 
                                                 end_vertex, 
                                                 path)
                for p in extended_paths: 
                    paths.append(p)
        return paths

    # zero all the amounts
    def zero_amounts(g):
        for unit, (amount, inputs) in g.items():
            g[unit][0] = 0
            g[unit][1] = []
            for (inamount, inunit) in inputs:
                g[unit][1].append([0, inunit])


    def accum_paths(paths, end='ORE'):
        while any((any(p) for p in paths)):
            for path in paths:
                if path:
                    # take the first item off the path
                    unit = path.pop(0)
                    if unit == end:
                        path = []
                        break

                    nextunit = path[0]
                    # move it's requirements to the next item


                    amount, inputs = graph[unit]
                    nextamount, nextinputs = graph[nextunit]
                    convamount = [i[0] for i in inputs if i[1]==nextunit][0]
                    if nextunit == end:
                        path = []
                    graph_accum[nextunit][0] += convamount
                

    import pprint
    pprint.pprint(graph)
    paths = find_all_paths('FUEL', 'ORE')
    print(paths)

    import copy
    graph_accum = copy.deepcopy(graph)
    zero_amounts(graph_accum)
    pprint.pprint(graph_accum)
    accum_paths(paths)
    pprint.pprint(graph_accum)




TESTMAP1 = """
10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL
"""

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)

    # print(count_ore(TESTMAP1))
    print(map2graph(TESTMAP1))
