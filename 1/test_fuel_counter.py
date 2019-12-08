import pytest
from fuel_counter import get_fuel_required, get_total_fuel_required


def test_get_fuel_required():
    assert get_fuel_required(12) == 2
    assert get_fuel_required(14) == 2
    assert get_fuel_required(1969) == 654
    assert get_fuel_required(100756) == 33583
    assert get_fuel_required(1) == 0


def test_get_total_fuel_required():
    assert get_total_fuel_required([12, 14]) == 4
    assert get_total_fuel_required(['12', '14']) == 4
