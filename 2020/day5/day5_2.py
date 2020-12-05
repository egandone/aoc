with open("input.txt") as input:
    lines = input.readlines()

ids = [int(line.strip().replace('F', '0').replace('B', '1').replace(
    'L', '0').replace('R', '1'), 2) for line in lines]
highest_seat = max(ids)
lowest_seat = min(ids)
print(f'seat range = {lowest_seat} -> {highest_seat}')

empty_seats = [id for id in range(lowest_seat, highest_seat) if id not in ids]
print(f'missing seats: {empty_seats}')
