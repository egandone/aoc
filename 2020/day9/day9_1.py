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


#lines = sample_lines
preamble_count = 25
with open("input.txt") as input:
    lines = [l.strip() for l in input.readlines()]

numbers = [int(l) for l in lines]

for index in range(preamble_count, len(numbers)):
    check_set = numbers[index - preamble_count:index]
    if not check_xmas_sum(numbers[index], check_set):
        print(f'{numbers[index]} cannot be computed from {check_set}')
