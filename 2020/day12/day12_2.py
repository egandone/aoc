import math


class Waypoint:
    # west is +ive x
    # north is +ive y
    _position = (-10, 1)

    def north(self, n):
        self._position = (self._position[0], self._position[1] + n)

    def south(self, n):
        self._position = (self._position[0], self._position[1] - n)

    def west(self, n):
        self._position = (self._position[0] + n, self._position[1])

    def east(self, n):
        self._position = (self._position[0] - n, self._position[1])

    # counter clockwise rotation (aka. left rotation)
    def rotate(self, r):
        r = math.radians(r)
        self._position = (round(self._position[0] * math.cos(r) - self._position[1] * math.sin(r), 2),
                          round(self._position[0] * math.sin(r) + self._position[1] * math.cos(r), 2))

    def get_movement(self, d):
        return (d*self._position[0], d*self._position[1])


class Ferry:
    # west is +ive x
    # north is +ive y
    _position = (0, 0)

    def forward(self, waypoint, n):
        (dx, dy) = waypoint.get_movement(n)
        self._position = (
            self._position[0] + dx, self._position[1] + dy)

    def manhattan_distance(self):
        return abs(self._position[0]) + abs(self._position[1])

    def __repr__(self):
        return f'@{self._position}'


ferry = Ferry()
waypoint = Waypoint()
with open("input.txt") as input:
    for line in [line.strip() for line in input.readlines()]:
        op = line[0]
        n = int(line[1:])
        if op == 'N':
            waypoint.north(n)
        elif op == 'S':
            waypoint.south(n)
        elif op == 'E':
            waypoint.east(n)
        elif op == 'W':
            waypoint.west(n)
        elif op == 'L':
            waypoint.rotate(-n)
        elif op == 'R':
            waypoint.rotate(n)
        elif op == 'F':
            ferry.forward(waypoint, n)
        else:
            print(f'unknown operation {op} {n}')
        print(f'{line} --> {ferry}')

print(f'{ferry}')
print(f'Manhattan distance = {ferry.manhattan_distance()}')
