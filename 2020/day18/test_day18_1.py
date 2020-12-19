from day18_1 import run_expr


def test_expressions():
    assert run_expr('1 + 2 * 3 + 4 * 5 + 6') == 71
    assert run_expr('2 * 3 + (4 * 5)') == 26
    assert run_expr('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 437.
    assert run_expr('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 12240.
    assert run_expr('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 13632
