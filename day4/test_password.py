import pytest

from password import is_valid


def test_is_valid():
    assert not is_valid(555555)
    assert not is_valid(223450)
    assert not is_valid(123789)
    assert not is_valid(123444)
    assert is_valid(333344)
