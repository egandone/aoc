
def get_pairs():
    with open('day6_input.txt') as infile:
        pairs = [line.strip().split(')')
                 for line in infile if len(line.strip()) > 0]
    return pairs


def build_graph(pairs):
    graph = dict()
    for pair in pairs:
        graph[pair[1]] = pair[0]
    return graph


def get_path_to_COM(graph, node):
    path = []
    while node != 'COM':
        path.append(node)
        node = graph[node]
    path.append(node)
    return path


def get_length_to_COM(graph, node):
    path_length = 1
    while graph[node] != 'COM':
        path_length += 1
        node = graph[node]
    return path_length


if __name__ == '__main__':
    graph = build_graph(get_pairs())
    total_length = sum([get_length_to_COM(graph, node) for node in graph])
    print(f'total_length = {total_length} for {len(graph)} orbits')

    my_path = set(get_path_to_COM(graph, "YOU"))
    santa_path = set(get_path_to_COM(graph, "SAN"))

    exclusive_nodes = my_path ^ santa_path
    trip_len = len(exclusive_nodes) - 2

    print(f'YOU->COM: {len(my_path)}')
    print(f'SAN->COM: {len(santa_path)}')
    print(f'YOU->SAN = {trip_len} hops')
