import collections
import copy


def print_grid(grid):
    for y in range(0, len(grid)):
        print("".join(grid[y]))


def get_seat_count(grid):
    seat_counter = collections.Counter()
    for row in grid:
        for seat in row:
            seat_counter.update(seat)
    return seat_counter


def get_closet_seat(grid, y, x, dy, dx):
    _y = y + dy
    _x = x + dx
    while _y >= 0 and _y < len(grid) and _x >= 0 and _x < len(grid[_y]):
        if grid[_y][_x] in ["L", "#"]:
            return grid[_y][_x]
        _y += dy
        _x += dx
    return "."


def get_directional_closet_seats(grid, y, x):
    seat_counter = collections.Counter()
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx != 0 or dy != 0:
                s = get_closet_seat(grid, y, x, dy, dx)
                seat_counter.update(s)
    return seat_counter


def run_iteration(grid):
    _grid = copy.deepcopy(grid)
    updates = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            seats = get_directional_closet_seats(grid, y, x)
            if grid[y][x] == "L":
                if "#" not in seats:
                    _grid[y][x] = "#"
                    updates += 1
            elif grid[y][x] == "#":
                if "#" in seats and seats["#"] >= 5:
                    _grid[y][x] = "L"
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
    print(f"===== iteration {i}, {updates} updates =====")
    i += 1
#    print_grid(grid)

print("==== final grid =====")
print_grid(grid)
seats = get_seat_count(grid)
print(f'Total occupied count = {seats["#"]}')
