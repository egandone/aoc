from day18_2 import run_expr


def test_expressions():
    assert run_expr('1 + 2 * 3 + 4 * 5 + 6') == 231
    assert run_expr('1 + (2 * 3) + (4 * (5 + 6))') == 51
    assert run_expr('2 * 3 + (4 * 5)') == 46
    assert run_expr('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 1445
    assert run_expr('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 669060
    assert run_expr('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 23340
