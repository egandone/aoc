def find_first_hit(t0, dt, new_offset, new_delta):
    # Just walk through time until the time at the
    # offset is a whole multiple of the delta
    t = t0
    while True:
        if (t + new_offset) % new_delta == 0:
            break
        t += dt
    return t


def find_second_hit(t0, dt, new_offset, new_delta):
    # This just find the next hit after the current
    # position (assumes the current is a hit)
    return find_first_hit(t0 + dt, dt, new_offset, new_delta)


bus_ids = []
with open("input.txt") as input:
    target = int(input.readline().strip())
    for i, id in enumerate(input.readline().strip().split(',')):
        if id != 'x':
            bus_ids.append((i, int(id)))


# print(f'target is {target}')
print(f'bus ids {bus_ids}')

# Find the first t0 based on the first two entries
t0 = 0
current_dt = bus_ids[0][1]
for i in range(0, len(bus_ids)-1):
    current_bus = bus_ids[i]
    next_bus = bus_ids[i+1]
    # Find the next time the two buses hit the pattern
    t0 = find_first_hit(t0, current_dt, next_bus[0], next_bus[1])
    # ... and to compute the delta for the next iteration we
    #     need to find the next time the buses hit
    t1 = find_second_hit(t0, current_dt, next_bus[0], next_bus[1])
    current_dt = t1 - t0

# And then we just find the first hit with the last bus
final_hit = find_first_hit(t0, current_dt, bus_ids[-1][0], bus_ids[-1][1])
print(f'{final_hit}')
