import re
from collections import Counter


def check_password(i1, i2, l, password):
    ok1 = (len(password) >= i1) and (password[i1-1] == l)
    ok2 = (len(password) >= i2) and (password[i2-1] == l)
    return (ok1 and not ok2) or (not ok1 and ok2)


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
