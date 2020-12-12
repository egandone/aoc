import collections
import itertools

with open("input2.txt") as input:
    lines = input.readlines()

ok_count = 0


def check_adapters(adapters):
    global ok_count
    c = list(adapters)
    is_ok = not any([c[i+1] - c[i] > 3 for i in range(0, len(c) - 1)])
    if is_ok:
        ok_count += 1
        print(f'{ok_count}')
    # else:
    #     print(f'{c} is not ok')
    return is_ok


total_count = 0


def check(adapters, start_n):
    #    print(f'{start_n}')
    global total_count
    print(f'{adapters}')
    removal_candidates = [adapters[n] for n in range(0, len(
        adapters) - 2) if (adapters[n] > start_n) and (adapters[n+1] - adapters[n-1] <= 3)]
#    print(f'removals {removal_candidates}')

#    adapter_set = tuple(adapters)
#    check_range = len(adapters) - 2
    count = 0
    for s in removal_candidates:
        total_count += 1
        if (total_count % 1000000) == 0:
            print(f'{total_count}')
        count += 1
        sub_list = list(adapters)
        sub_list.remove(s)
#        if not any([sub_list[i+1] - sub_list[i] > 3 for i in range(0, check_range)]):
        count += check(sub_list, s)
    return count


print(f'len(lines) = {len(lines)}')

adapters = [int(l.strip()) for l in lines]
adapters.append(0)
adapters.append(max(adapters)+3)
adapters = sorted(adapters)
print(f'{adapters}')

count = 1 + check(adapters, 0)

print(f'{count}')
