import re


def masked_value(value, mask):
    masked_value = value
    if mask:
        masked_value = ''.join(
            map(lambda p: p[1] if p[1] != 'X' else p[0], zip(f'{value:036b}', mask)))
        masked_value = int(masked_value, 2)
    return masked_value


with open('input.txt') as input:
    lines = [line.strip() for line in input.readlines()]

mem = dict()
for line in lines:
    if line.startswith('mask'):
        mask = line.split('=')[1].strip()
        print(f'mask = {mask}')
    else:
        match = re.match(r'mem\[(\d*)\] = (\d*)$', line)
        if match:
            index = int(match[1])
            value = int(match[2])
            mem[index] = masked_value(value, mask)

all_values_sum = sum(mem.values())
print(f'{all_values_sum}')
