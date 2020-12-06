declarations = []
current_declarations = None
with open("input.txt") as input:
    for line in input.readlines():
        if line.strip():
            if current_declarations == None:
                current_declarations = []
                declarations.append(current_declarations)
            current_declarations.append(set(line.strip()))
        else:
            current_declarations = None
counts = []
for d in declarations:
    union_set = d[0]
    for i in range(1, len(d)):
        union_set = union_set.intersection(d[i])
    count = len(union_set)
    counts.append(count)

s = sum([c for c in counts])
print(f'Sum of all {len(declarations)} counts = {s}')
