from itertools import combinations
with open("input.txt") as input:
    lines = input.readlines()
print(f'found {len(lines)} lines')
numbers = [int(line.strip()) for line in lines if line.strip()]
matches = [c for c in combinations(numbers, 2) if c[0] + c[1] == 2020]
for match in matches:
    product = match[0] * match[1] 
    print(f'{match[0]} + {match[1]} is 2020, product is {product}')