
def get_tree_count(lines, dx, dy):
    x = dx
    y = dy
    tree_count = 0
    while y < len(lines):
        mx = x % len(lines[y])  # wraps each line
        c = lines[y][mx]
        if c == '#':
            tree_count += 1
        x += dx
        y += dy
    return tree_count


with open('input.txt') as input:
    lines = [line.strip() for line in input.readlines()]

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
tree_counts = [get_tree_count(lines, slope[0], slope[1]) for slope in slopes]

product = 1
for tree_count in tree_counts:
    product *= tree_count
print(f'{tree_counts} --> {product}')
