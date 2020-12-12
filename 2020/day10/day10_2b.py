import collections
import itertools

lines = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".split('\n')

# lines = """16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4""".split('\n')

with open("input.txt") as input:
    lines = input.readlines()


def check_adapters(adapters):
    c = list(adapters)
    is_ok = not any([c[i+1] - c[i] > 3 for i in range(0, len(c) - 1)])
    # if is_ok:
    #      print(f'{c} is ok')
    # else:
    #     print(f'{c} is not ok')
    return is_ok

print(f'len(lines) = {len(lines)}')

adapters = [int(l.strip()) for l in lines]
adapters.append(0)
adapters.append(max(adapters)+3)
adapters = sorted(adapters)
print(f'{adapters}')

removal_candidates = [adapters[n] for n in range(1,len(adapters) - 1) if (adapters[n+1] - adapters[n-1] < 3)]
print(f'{removal_candidates}')

adapter_set = set(adapters)
counts = [1]
for s in range(1, len(removal_candidates) + 1):
    print(f'testing combinations of len {s}')
    count = 0
    if counts[s - 1] > 0:
        for removal_set in itertools.combinations(removal_candidates, s):
            test_set = adapter_set - set(removal_set)
            if check_adapters(test_set):
                count += 1
    counts.append(count)

print(f'{count}')