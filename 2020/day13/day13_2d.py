bus_ids = []
with open("input1.txt") as input:
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
    bus_time = t
    if t % id > 0:
        bus_time = ((t // id) + 1) * id
    return bus_time - t


t = 0
check_range = range(0, len(bus_ids))
while True:
    #    print(f'@ {t} - {offsets}')
    if all([(t + bus_ids[i][0]) % bus_ids[i][1] == 0 for i in check_range]):
        break
    t += bus_ids[0][1]

print(f'{t}')
