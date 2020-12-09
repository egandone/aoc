import re


def get_children(lines, colour):
    print(f'looking for {colour}')
    p = re.compile(f'{colour} bags contain.*')
    matching_line = [l for l in lines if p.match(l)]
    print(f'  found {matching_line[0]}')
    total = 1
    if not matching_line[0].endswith('contain no other bags.'):
        for m in re.findall("(\d+) ([^,]*) bag", matching_line[0]):
            count = int(m[0])
            sub_count = get_children(lines, m[1])
            total += count*sub_count
    print(f'total for {colour} is {total}')
    return total


with open("input.txt") as input:
    lines = [line.strip() for line in input.readlines()]

# lines = """shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.""".split('\n')

# don't count the top level bag in the total
c = get_children(lines, 'shiny gold') - 1
print(f'Total count = {c}')
