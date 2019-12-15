import pytest
from intcomputer import execute
from itertools import permutations
import mock 
import builtins


def test_execute():
    #    1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
    assert execute([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]

    #    2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
    assert execute([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]

    #    2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
    assert execute([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]

    #    1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.
    assert execute([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [
        30, 1, 1, 4, 2, 5, 6, 0, 99]

def test_day2_part1():
    day2_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,9,19,23,2,13,23,27,1,6,27,31,2,6,31,35,2,13,35,39,1,39,10,43,2,43,13,47,1,9,47,51,1,51,13,55,1,55,13,59,2,59,13,63,1,63,6,67,2,6,67,71,1,5,71,75,2,6,75,79,1,5,79,83,2,83,6,87,1,5,87,91,1,6,91,95,2,95,6,99,1,5,99,103,1,6,103,107,1,107,2,111,1,111,5,0,99,2,14,0,0]
    day2_input[1] = 12
    day2_input[2] = 2
    day2_output = execute(day2_input)
    assert day2_output[0] == 2890696

def test_day2_part2():
    day2_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,9,19,23,2,13,23,27,1,6,27,31,2,6,31,35,2,13,35,39,1,39,10,43,2,43,13,47,1,9,47,51,1,51,13,55,1,55,13,59,2,59,13,63,1,63,6,67,2,6,67,71,1,5,71,75,2,6,75,79,1,5,79,83,2,83,6,87,1,5,87,91,1,6,91,95,2,95,6,99,1,5,99,103,1,6,103,107,1,107,2,111,1,111,5,0,99,2,14,0,0]
    day2_input[1] = 82
    day2_input[2] = 26
    day2_output = execute(day2_input)
    assert day2_output[0] == 19690720

def test_in_out1():
    with mock.patch.object(builtins, 'input', lambda _: '1'):
        assert execute([3,0,4,0,99]) == [1,0,4,0,99]
        assert execute([3,5,4,5,99,0]) == [3,5,4,5,99,1]

def test_add_immediate():
    assert execute([1101,17,13,5,99,0]) == [1101,17,13,5,99,30]
    assert execute([1101,-1,6,5,99,0]) == [1101,-1,6,5,99,5]

def test_mult_immediate():
    assert execute([1102,12,12,5,99,0]) == [1102,12,12,5,99,144]
    assert execute([1102,-2,7,5,99,0]) == [1102,-2,7,5,99,-14]

def test_day5_step2():
    # Check if IN is 8
    with mock.patch.object(builtins, 'input', lambda _: '8'):
        assert execute([3,9,8,9,10,9,4,9,99,-1,8]) == [3,9,8,9,10,9,4,9,99,1,8]
    # Check if IN is 1
    with mock.patch.object(builtins, 'input', lambda _: '5'):
        assert execute([3,9,8,9,10,9,4,9,99,-1,8]) == [3,9,8,9,10,9,4,9,99,0,8]

    # 3,9,7,9,10,9,4,9,99,-1,8 - Using position mode, 
    # consider whether the input is less than 8; 
    #   output 1 (if it is) 
    #   or 0 (if it is not).
    with mock.patch.object(builtins, 'input', lambda _: '5'):
        assert execute([3,9,7,9,10,9,4,9,99,-1,8]) == [3,9,7,9,10,9,4,9,99,1,8]
    with mock.patch.object(builtins, 'input', lambda _: '8'):
        assert execute([3,9,7,9,10,9,4,9,99,-1,8]) == [3,9,7,9,10,9,4,9,99,0,8]

    # 3,3,1108,-1,8,3,4,3,99 - Using immediate mode, 
    # consider whether the input is equal to 8; 
    #   output 1 (if it is) 
    #   or 0 (if it is not).
    with mock.patch.object(builtins, 'input', lambda _: '5'):
        assert execute([3,3,1108,-1,8,3,4,3,99]) == [3,3,1108,0,8,3,4,3,99]
    with mock.patch.object(builtins, 'input', lambda _: '8'):
        assert execute([3,3,1108,-1,8,3,4,3,99]) == [3,3,1108,1,8,3,4,3,99]

    # 3,3,1107,-1,8,3,4,3,99 - Using immediate mode, 
    # consider whether the input is less than 8; 
    #   output 1 (if it is) 
    #   or 0 (if it is not).
    with mock.patch.object(builtins, 'input', lambda _: '5'):
        assert execute([3,3,1107,-1,8,3,4,3,99]) == [3,3,1107,1,8,3,4,3,99]
    with mock.patch.object(builtins, 'input', lambda _: '8'):
        assert execute([3,3,1107,-1,8,3,4,3,99]) == [3,3,1107,0,8,3,4,3,99]

    with mock.patch.object(builtins, 'input', lambda _: '5'):
        assert execute([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
