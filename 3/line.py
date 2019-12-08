class SegmentDirection:
    def __init__(self, d):
        if d == 'R':
            self._d = (0, 1)
        elif d == 'L':
            self._d = (0, -1)
        elif d == 'U':
            self._d = (1, 0)
        elif d == 'D':
            self._d = (-1, 0)
        else:
            raise ValueError('Direction must be one of U,D,R,L')

    def next_point(self, p):
        return (p[0] + self._d[0], p[1] + self._d[1])


class Wire:
    def __init__(self):
        self._points = [(0, 0)]

    def add_segment(self, direction, length):
        p = self._points[-1]
        for _ in range(length):
            p = direction.next_point(p)
            self._points.append(p)

    def get_points_set(self):
        return set(self._points)

    def get_steps_to_point(self, p):
        step = 0
        if p in self._points:
            while self._points[step] != p:
                step += 1
        return step


def build_wire(path):
    segments = path.split(',')
    wire = Wire()
    for segment in segments:
        d = SegmentDirection(segment[0])
        l = int(segment[1:])
        wire.add_segment(d, l)
    return wire


def find_intersections(wire1, wire2):
    intersections = [p for p in wire1.get_points_set().intersection(
        wire2.get_points_set()) if p[0] != 0 or p[1] != 0]
    intersections.sort(key=lambda p: abs(p[0]) + abs(p[1]))
    return intersections
