from day14_1 import masked_value


def test_masked_value():
    assert masked_value(4324, None) == 4324
    assert masked_value(11, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X') == 73
    assert masked_value(101, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X') == 101
    assert masked_value(0, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X') == 64
