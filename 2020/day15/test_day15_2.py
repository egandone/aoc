from day15_2 import run


def test_run_small():
    assert run([0, 3, 6], 2020) == 436
    assert run([1, 3, 2], 2020) == 1
    assert run([2, 1, 3], 2020) == 10
    assert run([1, 2, 3], 2020) == 27
    assert run([2, 3, 1], 2020) == 78
    assert run([3, 2, 1], 2020) == 438
    assert run([3, 1, 2], 2020) == 1836


def test_run_large():
    assert run([0, 3, 6], 30000000) == 175594
    assert run([1, 3, 2], 30000000) == 2578
    assert run([2, 1, 3], 30000000) == 3544142
    assert run([1, 2, 3], 30000000) == 261214
    assert run([2, 3, 1], 30000000) == 6895259
    assert run([3, 2, 1], 30000000) == 18
    assert run([3, 1, 2], 30000000) == 362
