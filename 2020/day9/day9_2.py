import itertools
sample_lines = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".split('\n')
preamble_count = 5


def check_xmas_sum(num, check_list):
    return num in [p[0]+p[1] for p in itertools.combinations(check_list, 2)]

# find all sub-lists of length n


def sub_lists(l, n):
    sub_lists = []
    for start_index in range(0, len(l) - n + 1):
        sub_list = l[start_index:start_index + n]
        sub_lists.append(sub_list)
    return sub_lists


#lines = sample_lines
preamble_count = 25
with open("input.txt") as input:
    lines = [l.strip() for l in input.readlines()]

numbers = [int(l) for l in lines]

# Just keep increasing the sub_list lengths
for n in range(2, len(numbers)+1):
    for l in sub_lists(numbers, n):
        if sum(l) == 85848519:
            print(f'found {l}')
            print(f'{min(l)} -> {max(l)}, added together is {min(l) + max(l)}')
