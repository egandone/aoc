def find_first_hit(t0, dt, new_offset, new_delta):
    t = t0
    while True:
        if (t + new_offset) % new_delta == 0:
            break
        t += dt
    return t


def find_second_hit(t0, dt, new_offset, new_delta):
    t = t0 + dt
    while True:
        if (t + new_offset) % new_delta == 0:
            break
        t += dt
    return t


bus_ids = []
with open("input.txt") as input:
    target = int(input.readline().strip())
    for i, id in enumerate(input.readline().strip().split(',')):
        if id != 'x':
            bus_ids.append((i, int(id)))


# print(f'target is {target}')
print(f'bus ids {bus_ids}')

# Find the first t0 based on the first two entries
t0 = find_first_hit(0, bus_ids[0][1], bus_ids[1][0], bus_ids[1][1])
t1 = find_second_hit(t0, bus_ids[0][1], bus_ids[1][0], bus_ids[1][1])
current_dt = t1 - t0
for i in range(2, len(bus_ids)):
    bus_id = bus_ids[i]
    t0 = find_first_hit(t0, current_dt, bus_id[0], bus_id[1])

    # Don't need to update current_dt if it's the last one
    if (i < len(bus_ids) - 1):
        t1 = find_second_hit(t0, current_dt, bus_id[0], bus_id[1])
        current_dt = t1 - t0

print(f'{t0}')
