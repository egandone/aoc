import math


class Ferry:
    # west is +ive x
    # north is +ive y
    _position = (0, 0)
    _heading = (-1, 0)  # start heading east (i.e. negative west)

    def north(self, n):
        self._position = (self._position[0], self._position[1] + n)

    def south(self, n):
        self._position = (self._position[0], self._position[1] - n)

    def west(self, n):
        self._position = (self._position[0] + n, self._position[1])

    def east(self, n):
        self._position = (self._position[0] - n, self._position[1])

    def forward(self, n):
        self._position = (
            self._position[0] + n * self._heading[0], self._position[1] + n * self._heading[1])

    # counter clockwise rotation (aka. left rotation)
    def rotate(self, r):
        r = math.radians(r)
        self._heading = (round(self._heading[0] * math.cos(r) - self._heading[1] * math.sin(r), 2),
                         round(self._heading[0] * math.sin(r) + self._heading[1] * math.cos(r), 2))

    def manhattan_distance(self):
        return abs(self._position[0]) + abs(self._position[1])

    def __repr__(self):
        return f'@{self._position} heading {self._heading}'


ferry = Ferry()
with open("input.txt") as input:
    for line in [line.strip() for line in input.readlines()]:
        op = line[0]
        n = int(line[1:])
        if op == 'N':
            ferry.north(n)
        elif op == 'S':
            ferry.south(n)
        elif op == 'E':
            ferry.east(n)
        elif op == 'W':
            ferry.west(n)
        elif op == 'L':
            ferry.rotate(-n)
        elif op == 'R':
            ferry.rotate(n)
        elif op == 'F':
            ferry.forward(n)
        else:
            print(f'unknown operation {op} {n}')
        print(f'{line} --> {ferry}')

print(f'{ferry}')
print(f'Manhattan distance = {ferry.manhattan_distance()}')
