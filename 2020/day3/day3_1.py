with open('input.txt') as input:
    lines = [line.strip() for line in input.readlines()]

dx = 3
dy = 1
x = dx
y = dy
tree_count = 0
while y < len(lines):
    mx = x % len(lines[y])
    c = lines[y][mx]
    print(f'lines[{y}][{x}/{mx}] --> {c}')
    if c == '#':
        tree_count += 1
    x += dx
    y += dy
print(f'hit {tree_count} trees')
