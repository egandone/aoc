import re
import string


def get_str(nodes, i, protect=False):
    if type(nodes[i]) is not list:
        return [nodes[i]]
    else:
        all_strs = []
        for l in nodes[i]:
            if len(l) == 1:
                all_strs.extend(get_str(nodes, l[0]))
                if i == 8 and not protect:
                    g1 = get_str(nodes, l[0])
                    g2 = get_str(nodes, 8, True)
                    for _g1 in g1:
                        for _g2 in g2:
                            all_strs.append(_g1 + _g2)
            elif len(l) == 2:
                g1 = get_str(nodes, l[0])
                g2 = get_str(nodes, l[1])
                for _g1 in g1:
                    for _g2 in g2:
                        all_strs.append(_g1 + _g2)
                if i == 11 and not protect:
                    g1 = get_str(nodes, l[0])
                    g2 = get_str(nodes, 11, True)
                    g3 = get_str(nodes, l[1])
                    for _g1 in g1:
                        for _g2 in g2:
                            for _g3 in g3:
                                all_strs.append(_g1 + _g2 + _g3)
            elif len(l) == 3:
                g1 = get_str(nodes, l[0])
                g2 = get_str(nodes, l[1])
                g3 = get_str(nodes, l[2])
                for _g1 in g1:
                    for _g2 in g2:
                        for _g3 in g3:
                            all_strs.append(_g1 + _g2 + _g3)
            else:
                raise ValueError(f'node too long {len(l)}')
        return all_strs


mode = 0
nodes = dict()
good_messages = []
line_0 = []
with open("input3.txt") as input:
    for line in input.readlines():
        line = line.strip()
        if not line:
            mode += 1
            line_0 = get_str(nodes, 0)
        elif mode == 0:
            id, data = line.split(':')
            data = data.strip()
            if data.startswith('"'):
                nodes[int(id)] = data.strip('"')
            else:
                nodes[int(id)] = []
                for l in data.split('|'):
                    nodes[int(id)].append([int(_) for _ in l.strip().split()])
        else:
            if line in line_0:
                good_messages.append(line)

print(f'{len(good_messages)}')
