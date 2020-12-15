from day14_2 import masked_value


def test_masked_value():
    indexes = masked_value(42, '000000000000000000000000000000X1001X')
    assert len(indexes) == 4
    assert 26 in indexes and 27 in indexes and 58 in indexes and 59 in indexes

    indexes = masked_value(26, '00000000000000000000000000000000X0XX')
    assert len(indexes) == 8
    assert 16 in indexes and 17 in indexes and 18 in indexes and 19 in indexes
    assert 24 in indexes and 25 in indexes and 26 in indexes and 27 in indexes
