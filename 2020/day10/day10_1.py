import collections
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

with open("input.txt") as input:
    lines = input.readlines()

print(f'len(lines) = {len(lines)}')

adapters = [int(l.strip()) for l in lines]
adapters.append(0)
adapters.append(max(adapters) + 3)
adapters = sorted(adapters)
print(f'{len(adapters)} adapters --> {adapters}')


diffs = [adapters[i+1] - adapters[i] for i in range(0, len(adapters) - 1)]
c = collections.Counter(diffs)
print(f'1 count is {c[1]}, 3 count {c[3]}')
print(f'product = {c[1] * c[3]}')
