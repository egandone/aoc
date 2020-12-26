def find_iteration_count(subject_number, target):
    value = 1
    iteration_count = 0
    while value != target:
        value = value * subject_number
        value = value % 20201227
        iteration_count += 1

    return iteration_count


def calc_key(subject_number, iteration_count):
    value = 1
    for _ in range(0, iteration_count):
        value = value * subject_number
        value = value % 20201227

    return value


def main():
    card_public_key = 13135480
    card_iteration_count = find_iteration_count(7, card_public_key)
    print(f'card count = {card_iteration_count}')
    door_public_key = 8821721
    door_iteration_count = find_iteration_count(7, door_public_key)
    print(f'door count = {door_iteration_count}')

    key1 = calc_key(card_public_key, door_iteration_count)
    key2 = calc_key(door_public_key, card_iteration_count)
    print(f'{key1} {key2}')


if __name__ == "__main__":
    main()
