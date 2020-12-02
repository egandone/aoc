
def read_input():
    with open('input.txt') as day8_file:
        line = day8_file.read()
        return [int(c) for c in line.strip()]


def split_into_layers(image_data, width=25, height=6):
    layers = []
    image_pixels = width * height
    total_layers = int(len(image_data) / image_pixels)
    for layer in range(total_layers):
        offset = layer * image_pixels
        layer = image_data[offset: offset+image_pixels]
        layers.append(layer)
    return layers


def get_pixel_count(layer, pixel_value):
    return len([p for p in layer if p == pixel_value])


def layers_to_pixels(layers, width=25, height=6):
    pixels = []
    for p in range(width * height):
        pixel = None
        for layer in layers:
            if (pixel == None) and (layer[p] in (0, 1)):
                pixel = layer[p]
        pixels.append(pixel)
    return pixels


if __name__ == '__main__':
    layers = split_into_layers(read_input())
    print(f'{len(layers)} total layers')

    layers.sort(key=lambda l: get_pixel_count(l, 0))
    zeros_count = get_pixel_count(layers[0], 0)
    ones_count = get_pixel_count(layers[0], 1)
    twos_count = get_pixel_count(layers[0], 2)
    print(
        f'lowest zero count = {zeros_count} -> 1''s * 2''s = {ones_count * twos_count}')

    layers = split_into_layers(read_input())
    pixels = layers_to_pixels(layers)
    print("decoded image:")
    for r in range(0, 6*25, 25):
        rendered = ''.join(
            [f'{"*" if p == 1 else " "}' for p in pixels[r:r+25]])
        print(rendered)
