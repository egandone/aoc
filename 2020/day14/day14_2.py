import re


def generate_permutation(list, location):
    new_list = []
    for v in list:
        c = v.copy()
        c[location] = '0'
        new_list.append(c)
        c = v.copy()
        c[location] = '1'
        new_list.append(c)
    return new_list


def masked_value(value, mask):
    bits = list(f'{value:036b}')
    X_locations = []
    for i, mask in enumerate(mask):
        if mask == 'X':
            bits[i] = '0'
            X_locations.append(i)
        elif mask == '1':
            bits[i] = '1'
    generated_values = [bits]
    for location in X_locations:
        generated_values = generate_permutation(generated_values, location)
    generated_values = [int(''.join(v), 2) for v in generated_values]
    return generated_values


def main():
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
                loc = int(match[1])
                value = int(match[2])
                indexes = masked_value(loc, mask)
                for index in indexes:
                    mem[index] = value

    all_values_sum = sum(mem.values())
    print(f'{all_values_sum}')


if __name__ == "__main__":
    main()
