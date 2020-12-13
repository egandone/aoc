with open("input.txt") as input:
    target = int(input.readline().strip())
    bus_ids = [int(id)
               for id in input.readline().strip().split(',') if id != 'x']

print(f'target is {target}')
print(f'bus ids {bus_ids}')

bus_times = dict()
for id in bus_ids:
    bus_time = target
    if target % id > 0:
        bus_time = ((target // id) + 1) * id
    bus_times[id] = bus_time
    print(f'{id} --> {bus_time}')

earliest_bus = min(bus_ids, key=lambda id: bus_times[id] - target)
print(f'earliest bus id {earliest_bus} @ {bus_times[earliest_bus]}')
answer = (bus_times[earliest_bus] - target) * earliest_bus
print(f'puzzle answer = {answer}')
