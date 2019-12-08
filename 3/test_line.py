import pytest
from line import SegmentDirection, Wire, build_wire, find_intersections


def test_segment_direction():
    up = SegmentDirection('U')
    assert up.next_point((0, 0)) == (1, 0)

    down = SegmentDirection('D')
    assert down.next_point((0, 0)) == (-1, 0)

    right = SegmentDirection('R')
    assert right.next_point((0, 0)) == (0, 1)

    left = SegmentDirection('L')
    assert left.next_point((0, 0)) == (0, -1)


def test_distance_algorithm():
    wire1 = build_wire('R75,D30,R83,U83,L12,D49,R71,U7,L72')
    wire2 = build_wire('U62,R66,U55,R34,D71,R55,D58,R83')
    crosses = find_intersections(wire1, wire2)
    assert abs(crosses[0][0]) + abs(crosses[0][1]) == 159

    wire1 = build_wire('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51')
    wire2 = build_wire('U98,R91,D20,R16,D67,R40,U7,R15,U6,R7')
    crosses = find_intersections(wire1, wire2)
    assert abs(crosses[0][0]) + abs(crosses[0][1]) == 135


def test_wire():
    # R8,U5,L5,D3
    wire1 = Wire()
    wire1.add_segment(SegmentDirection('R'), 8)
    wire1.add_segment(SegmentDirection('U'), 5)
    wire1.add_segment(SegmentDirection('L'), 5)
    wire1.add_segment(SegmentDirection('D'), 3)

    assert wire1.get_points_set() == {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8),
                                      (1, 8), (2, 8), (3, 8), (4, 8), (5, 8),
                                      (5, 7), (5, 6), (5, 5), (5, 4), (5, 3),
                                      (4, 3), (3, 3), (2, 3)}
    wire1b = build_wire('R8,U5,L5,D3')
    assert wire1b.get_points_set() == wire1.get_points_set()

    # U7,R6,D4,L4
    wire2 = Wire()
    wire2.add_segment(SegmentDirection('U'), 7)
    wire2.add_segment(SegmentDirection('R'), 6)
    wire2.add_segment(SegmentDirection('D'), 4)
    wire2.add_segment(SegmentDirection('L'), 4)

    assert wire2.get_points_set() == {(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                      (7, 1), (7, 2), (7, 3), (7,
                                                               4), (7, 5), (7, 6),
                                      (6, 6), (5, 6), (4, 6), (3, 6),
                                      (3, 5), (3, 4), (3, 3), (3, 2)}

    wire2b = build_wire('U7,R6,D4,L4')
    assert wire2b.get_points_set() == wire2.get_points_set()
