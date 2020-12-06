declarations = []
current_declaration = None
with open("input.txt") as input:
    for line in input.readlines():
        if line.strip():
            if current_declaration == None:
                current_declaration = set()
                declarations.append(current_declaration)
            current_declaration.update([c for c in line.strip()])
        else:
            current_declaration = None

s = sum([len(d) for d in declarations])
print(f'Sum of all {len(declarations)} counts = {s}')
