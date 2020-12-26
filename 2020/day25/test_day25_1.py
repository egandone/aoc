from day25_1 import find_iteration_count, calc_key


def test_find_iteration_count():
    assert find_iteration_count(7, 5764801) == 8
    assert find_iteration_count(7, 17807724) == 11


def test_calc_key():
    assert calc_key(17807724, 8) == 14897079
