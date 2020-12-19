import re


class Field:

    def __init__(self, str):
        matches = re.match('^([^:]*): (\d*)-(\d*) or (\d*)-(\d*)$', str)
        self._name = matches[1]
        self._range1 = (int(matches[2]), int(matches[3]))
        self._range2 = (int(matches[4]), int(matches[5]))

    def is_valid(self, t):
        return (self._range1[0] <= t <= self._range1[1]) or (self._range2[0] <= t <= self._range2[1])

    def __repr__(self):
        return f'{self._name}: {self._range1} and {self._range2}'


def parse_file(filename):
    fields = []
    nearby_tickets = []
    with open(filename) as input:
        mode = 0
        while (line := input.readline()):
            line = line.strip()
            if not line:
                mode += 1
            elif mode == 0:
                field = Field(line)
                fields.append(field)
            elif mode == 1:
                if not line.startswith("your ticket"):
                    my_tickets = [int(n) for n in line.split(',')]
            elif mode == 2:
                if not line.startswith("nearby tickets"):
                    tickets = [int(n) for n in line.split(',')]
                    nearby_tickets.extend(tickets)

    return fields, my_tickets, nearby_tickets


def is_valid(t, fields):
    return any([f.is_valid(t) for f in fields])


def main(filename):
    fields, my_tickets, nearby_tickets = parse_file(filename)
    bad_fields = [t for t in nearby_tickets if not is_valid(t, fields)]
    return bad_fields


if __name__ == "__main__":
    bad_fields = main("input.txt")
    s = sum(bad_fields)
    print(f'{bad_fields} --> {s}')
