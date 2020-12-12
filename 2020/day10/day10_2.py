import collections

# lines = """28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3""".split('\n')

lines = """16
10
15
5
1
11
7
19
6
12
4""".split('\n')

# with open("input.txt") as input:
#     lines = input.readlines()


def check_adapters(adapters):
    c = sorted(adapters)
    is_ok = not any([c[i+1] - c[i] > 3 for i in range(0, len(c) - 1)])
    if is_ok:
         print(f'{c} is ok')
    # else:
    #     print(f'{c} is not ok')
    return is_ok


checked_map = {}


def get_count(start, end, adapters):
    global checked_map
    if len(adapters) > 0 and tuple(adapters) not in checked_map:
        check_list = [start, end]
        check_list.extend(adapters)
        checked_map[tuple(adapters)] = check_adapters(check_list)
        if checked_map[tuple(adapters)]:
            for a in adapters:
                subset = [x for x in adapters if x != a]
                get_count(start, end, subset)


print(f'len(lines) = {len(lines)}')

adapters = [int(l.strip()) for l in lines]
adapters = sorted(adapters)
print(f'{adapters}')
device_jolt = max(adapters) + 3
print(f'device is {device_jolt}')
get_count(0, device_jolt, adapters)

count = 0
for k, v in checked_map.items():
    if v:
        count += 1
        # print(k)
print(f"Total count = {count}")
