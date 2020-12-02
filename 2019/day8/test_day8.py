from day8 import read_input, split_into_layers, get_pixel_count, layers_to_pixels


def test_read_input():
    input_data = read_input()
    total_len = len(input_data)
    # Ensure that the input file contains a
    # integer number of layers.  Since each layer is
    # 25x6 there the total should be an integer
    # multiple of this
    assert total_len % (25 * 6) == 0


def test_split_into_layers():
    input_data = read_input()
    layers = split_into_layers(input_data)
    assert len(layers) == (len(input_data) / (25*6))
    for layer in layers:
        assert len(layer) == 25 * 6


def test_get_pixel_count():
    layers = split_into_layers(read_input())
    for layer in layers:
        total_pixel_count = sum([get_pixel_count(layer, p) for p in range(10)])
        assert total_pixel_count == len(layer)


def test_layers_to_pixels():
    input_data = [int(p) for p in '0222112222120000']
    layers = split_into_layers(input_data, width=2, height=2)
    pixels = layers_to_pixels(layers, width=2, height=2)
    assert pixels == [0, 1, 1, 0]
