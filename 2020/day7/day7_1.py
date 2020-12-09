import re


def get_parents(lines, colour):
    print(f'looking for {colour}')
    p = re.compile(f'.*contain.*\d+ {colour} bag.*')
    matching_lines = [l for l in lines if p.match(l)]
    full_set = set([re.match("^(.*) bags contain.*", l)[1]
                    for l in matching_lines])
    for c in list(full_set):
        full_set.update(get_parents(lines, c))
    return full_set


with open("input.txt") as input:
    lines = [line.strip() for line in input.readlines()]

# lines = """light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.""".split('\n')

parents = get_parents(lines, 'shiny gold')
print(f'Total count = {len(parents)}')
