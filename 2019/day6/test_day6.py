import pytest
from day6 import get_pairs, build_graph, get_length_to_COM, get_path_to_COM


def test_get_pairs():
    pairs = get_pairs()
    assert len(pairs) == 2242
    for pair in pairs:
        assert len(pair) == 2


def test_get_length_to_COM():
    pairs = get_pairs()
    graph = build_graph(pairs)
    assert 'COM' not in graph
    assert graph['FJH'] == 'COM'
    assert get_length_to_COM(graph, 'FJH') == 1
    assert get_length_to_COM(graph, 'XLG') == 2
    assert get_length_to_COM(graph, 'NF6') == 25


def test_get_path_to_COM():
    pairs = get_pairs()
    graph = build_graph(pairs)
    assert 'COM' not in graph
    assert graph['FJH'] == 'COM'
    assert get_path_to_COM(graph, 'FJH') == ['FJH', 'COM']
    assert get_path_to_COM(graph, 'XLG') == ['XLG', 'FJH', 'COM']
    assert len(get_path_to_COM(graph, 'NF6')) == 26
