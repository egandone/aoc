bus_ids = []
with open("input.txt") as input:
    target = int(input.readline().strip())
    for i, id in enumerate(input.readline().strip().split(',')):
        if id != 'x':
            bus_ids.append((i, int(id)))

# print(f'target is {target}')
print(f'bus ids {bus_ids}')

# return the offset from t of
# the next departure time for the
# given bus


def get_next_departure_time_offset(t, id):
    return 0 if t % id == 0 else (((t // id) + 1) * id - t)


bus_with_max_offset = max(bus_ids, key=lambda bus: bus[1])
print(f'max_bus {bus_with_max_offset}')
check_range = range(0, len(bus_ids))
t_check_max = bus_with_max_offset[1]
t_check_max = 100000000000000
t_check_max += get_next_departure_time_offset(
    t_check_max, bus_with_max_offset[1])

check_offsets = tuple([bus_ids[i][0] for i in check_range])
while True:
    t = t_check_max - bus_with_max_offset[0]
    if t % bus_ids[0][1] == 0:
        offsets = tuple([get_next_departure_time_offset(
            t, bus_ids[i][1]) for i in check_range])
        print(f'@ {t} - {offsets}')
        if offsets == check_offsets:
            break

    t_check_max += bus_with_max_offset[1]


print(f'{t}')
