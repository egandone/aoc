from collections import Counter


def print_grid(grid, origin, dims):
    for z in range(origin[0], origin[0]+dims[0]):
        print(f'z is {z-origin[0]}')
        for y in range(origin[1], origin[1]+dims[1]):
            print(' '.join([grid[z][y][x]
                            for x in range(origin[2], origin[2]+dims[2])]))


def get_neighbours(grid, z, y, x):
    counter = Counter()
    for dz in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx != 0 or dy != 0 or dz != 0:
                    counter.update(grid[z+dz][y+dy][x+dx])

    if grid[z][y][x] == '#':
        if counter['#'] in (2, 3):
            return '#'
        else:
            return '.'
    else:
        if counter['#'] == 3:
            return '#'
        else:
            return '.'


with open("input.txt") as input:
    lines = [line.strip() for line in input.readlines() if line.strip()]

iterations = 6
dim_z = 1
dim_y = len(lines)
dim_x = len(lines[0])

final_dim_z = dim_z + 2*iterations + 2
final_dim_y = dim_y + 2*iterations + 2
final_dim_x = dim_x + 2*iterations + 2
total_grid = [[['.' for x in range(0, final_dim_x)] for y in range(
    0, final_dim_y)] for z in range(0, final_dim_z)]

origin = (iterations+1, iterations+1, iterations+1)

initial_grid = [[[lines[y][x]
                  for x in range(0, dim_x)] for y in range(0, dim_y)]]

for y in range(0, dim_y):
    for x in range(0, dim_x):
        total_grid[origin[0]][origin[1]+y][origin[2]+x] = initial_grid[0][y][x]


for iteration in range(1, iterations+1):
    print_grid(total_grid, origin, (dim_z, dim_y, dim_x))

    origin = (origin[0]-1, origin[1]-1, origin[2]-1)
    dim_z += 2
    dim_y += 2
    dim_x += 2
    print(f'iteration {iteration} - {origin} {dim_z}x{dim_y}x{dim_x}')
    new_grid = [[['.' for x in range(0, final_dim_x)] for y in range(
        0, final_dim_y)] for z in range(0, final_dim_z)]

    for z in range(0, dim_z):
        for y in range(0, dim_y):
            for x in range(0, dim_x):
                new_grid[origin[0]+z][origin[1]+y][origin[2]+x] = get_neighbours(
                    total_grid, origin[0]+z, origin[1]+y, origin[2]+x)

    total_grid = new_grid

c = Counter()
for z in total_grid:
    for y in z:
        for x in y:
            c.update(x)
print(f'total active = {c["#"]}')
