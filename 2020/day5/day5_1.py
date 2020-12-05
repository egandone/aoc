with open("input.txt") as input:
    lines = input.readlines()

ids = [int(line.strip().replace('F', '0').replace('B', '1').replace(
    'L', '0').replace('R', '1'), 2) for line in lines]
highest_seat = max(ids)
print(f'{highest_seat}')
