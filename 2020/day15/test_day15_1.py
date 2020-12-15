from day15_1 import run


def test_run():
    assert run([0, 3, 6]) == 436
    assert run([1, 3, 2]) == 1
    assert run([2, 1, 3]) == 10
    assert run([1, 2, 3]) == 27
    assert run([2, 3, 1]) == 78
    assert run([3, 2, 1]) == 438
    assert run([3, 1, 2]) == 1836
