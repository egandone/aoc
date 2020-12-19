import re
from collections import Counter


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
                    nearby_tickets.append(tickets)

    return fields, my_tickets, nearby_tickets


def is_valid(t, fields):
    return any([f.is_valid(t) for f in fields])


def get_bad_fields(nearby_tickets, fields):
    all_fields = []
    for t in nearby_tickets:
        all_fields.extend(t)
    bad_fields = [t for t in all_fields if not is_valid(t, fields)]
    return bad_fields


def is_ticket_valid(ticket, fields):
    return all([is_valid(t, fields) for t in ticket])


def find_field_for_values(fields, values):
    possible_fields = []
    for f in fields:
        if all([f.is_valid(v) for v in values]):
            possible_fields.append(f)
    return possible_fields


if __name__ == "__main__":
    fields, my_tickets, nearby_tickets = parse_file("input.txt")
#    bad_fields = get_bad_fields(nearby_tickets, fields)
    good_tickets = [
        ticket for ticket in nearby_tickets if is_ticket_valid(ticket, fields)]
    good_tickets.append(my_tickets)
    field_counter = Counter([len(_) for _ in good_tickets])
    print(f'{field_counter}')

    matched_fields = []
    for i in range(0, field_counter.most_common()[0][0]):
        all_field_values = [fields[i] for fields in good_tickets]
        matched_field = find_field_for_values(fields, all_field_values)
        matched_fields.append(matched_field)
    # print('before narrowing')
    # for i, n in enumerate(matched_fields):
    #     print(f'   {i: 3} --> {n}')

    while any([len(m) > 1 for m in matched_fields]):
        single_matches = [m[0] for m in matched_fields if len(m) == 1]
        print(f'narrowing - single match count = {len(single_matches)}')
        new_matched_fields = []
        for m in matched_fields:
            new_m = m
            if len(m) > 1:
                new_m = [_ for _ in m if _ not in single_matches]
            new_matched_fields.append(new_m)
        matched_fields = new_matched_fields
        # for i, n in enumerate(matched_fields):
        #     print(f'   {i: 3} --> {n}')

    product = 1
    for i, n in enumerate(matched_fields):
        print(f'   {i: 3} {n[0]._name: >20} --> {my_tickets[i]}')
        if n[0]._name.startswith("departure"):
            product *= my_tickets[i]
    print(f'product of all \'departure\' fields = {product}')
