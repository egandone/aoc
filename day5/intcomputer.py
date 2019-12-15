from aoc_opcode import Add, Mult, In, Out, End, IfTrue, IfFalse, Less, Equals


def create_opcode(opcode):
    full_opcode = f'{opcode:05d}'
    param_modes = (int(full_opcode[2]), int(
        full_opcode[1]), int(full_opcode[0]))
    f = full_opcode[3:]
    if f == '01':
        return Add(param_modes)
    elif f == '02':
        return Mult(param_modes)
    elif f == '03':
        return In()
    elif f == '04':
        return Out(param_modes)
    elif f == '05':
        return IfTrue(param_modes)
    elif f == '06':
        return IfFalse(param_modes)
    elif f == '07':
        return Less(param_modes)
    elif f == '08':
        return Equals(param_modes)
    else:
        return End()


def execute(instructions):
    position = 0
    while position >= 0:
        #        print(f'[{position}] {instructions}')
        opcode = instructions[position]
        position += 1
        opcode = create_opcode(opcode)
        position = opcode.execute(instructions, position)

    return instructions
