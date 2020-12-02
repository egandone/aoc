import re

three_or_more_digits = re.compile(
    r'0{3,}|1{3,}|2{3,}|3{3,}|4{3,}|5{3,}|6{3,}|7{3,}|8{3,}|9{3,}')

two_digits = re.compile(
    r'0{2}|1{2}|2{2}|3{2}|4{2}|5{2}|6{2}|7{2}|8{2}|9{2}')


def is_valid(password):

    if password < 125730 or password > 579381:
        return False

    pstr = str(password)

    for i in range(1, 6):
        if int(pstr[i]) < int(pstr[i-1]):
            return False

    # Remove all 3 or more digit sequences
    pstr = three_or_more_digits.sub('', pstr)
    # Make sure there is still at least one 2 digit sequence.
    if not two_digits.search(pstr):
        return False

    return True
