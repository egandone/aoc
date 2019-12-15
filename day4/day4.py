from password import is_valid

good_count = 0
for password in range(125730, 579382):
    if is_valid(password):
        #        print(f'{password} is good')
        good_count += 1

print(f'There are {good_count} possibilites')
