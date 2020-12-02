import re
from collections import Counter


def check_password(min, max, l, password):
    counter = Counter(password)
    return l in counter and counter[l] >= min and counter[l] <= max


with open("input.txt") as input:
    ok_count = 0
    while line := input.readline():
        m = re.match("(\d+)-(\d+) (.): (.*)$", line.strip())
        min = int(m[1])
        max = int(m[2])
        c = m[3]
        password = m[4]
        ok = check_password(min, max, c, password)
        if ok:
            ok_count += 1

print(f'{ok_count}')
