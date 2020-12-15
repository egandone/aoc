
def run(start_sequence, n):

    numbers = {n: i for i, n in enumerate(start_sequence[:-1], start=1)}
    number = start_sequence[-1]
    for turn in range(len(numbers) + 1,  n):
        if number in numbers:
            next_number = turn - numbers[number]
            numbers[number] = turn
            number = next_number
        else:
            numbers[number] = turn
            number = 0
    return number


if __name__ == "__main__":
    print(run([0, 3, 6], 30000000))
    print(run([7, 14, 0, 17, 11, 1, 2], 30000000))
