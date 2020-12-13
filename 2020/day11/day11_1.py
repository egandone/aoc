import collections
import copy


def print_grid(grid):
    for y in range(0, len(grid)):
        print(''.join(grid[y]))


def get_seat_count(grid):
    seat_counter = collections.Counter()
    for row in grid:
        for seat in row:
            seat_counter.update(seat)
    return seat_counter


def get_adacent_seats(grid, y, x):
    seat_counter = collections.Counter()
    min_y = max(0, y-1)
    max_y = min(len(grid)-1, y+1)
    min_x = max(0, x - 1)
    max_x = min(len(grid[0])-1, x+1)
    for _y in range(min_y, max_y+1):
        for _x in range(min_x, max_x+1):
            if (_y != y) or (_x != x):
                seat_counter.update(grid[_y][_x])
    return seat_counter


def run_iteration(grid):
    _grid = copy.deepcopy(grid)
    updates = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            seats = get_adacent_seats(grid, y, x)
            if grid[y][x] == 'L':
                if '#' not in seats:
                    _grid[y][x] = '#'
                    updates += 1
            elif grid[y][x] == '#':
                if '#' in seats and seats['#'] >= 4:
                    _grid[y][x] = 'L'
                    updates += 1
    return _grid, updates


grid = []
with open("input.txt") as input:
    for line in [line.strip() for line in input.readlines()]:
        grid.append([c for c in line])

print_grid(grid)

i = 1
while True:
    grid, updates = run_iteration(grid)
    if updates == 0:
        break
    print(f'===== iteration {i}, {updates} updates =====')
#    print_grid(grid)

print("==== final grid =====")
print_grid(grid)
seats = get_seat_count(grid)
print(f'Total occupied count = {seats["#"]}')
