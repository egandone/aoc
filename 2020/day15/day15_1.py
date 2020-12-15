
def run(start_sequence):

    numbers = [n for n in start_sequence]
    turn = len(numbers) + 1
    number = start_sequence[-1]
    while turn <= 2020:
        found = [i for i, n in enumerate(numbers) if n == number]
        if len(found) > 1:
            number = found[-1] - found[-2]
        else:
            number = 0
        numbers.append(number)
        turn += 1

    return number


if __name__ == "__main__":
    print(run([7, 14, 0, 17, 11, 1, 2]))
