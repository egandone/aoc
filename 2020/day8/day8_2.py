class CPU:
    def __init__(self):
        self.acc = 0


class Opcode:
    def __init__(self, operand):
        self._operand = operand

    def repr(self, prefix):
        return f'{prefix} {self._operand: 4}'


class NOP(Opcode):
    def execute(self, cpu):
        return 1

    def __repr__(self):
        return super().repr('nop')


class ACC(Opcode):
    def execute(self, cpu):
        cpu.acc += self._operand
        return 1

    def __repr__(self):
        return super().repr('add')


class JMP(Opcode):
    def execute(self, cpu):
        return self._operand

    def __repr__(self):
        return super().repr('jmp')


def create_opcode(line):
    opcode, operand = line.strip().split(' ')
    operand = int(operand)
    if opcode == 'nop':
        return NOP(operand)
    elif opcode == 'acc':
        return ACC(operand)
    elif opcode == 'jmp':
        return JMP(operand)
    else:
        raise ValueError(f'unknown opcode {opcode}')


def parse_program(lines):
    instructions = [create_opcode(l) for l in lines]
    return instructions


def run_program(instructions):
    executed_lines = set()
    i = 0
    cpu = CPU()
    while i < len(instructions):
        if i in executed_lines:
            raise ValueError('infinite loop')
        executed_lines.add(i)
        i += instructions[i].execute(cpu)

    return cpu.acc


with open("input.txt") as input:
    instructions = parse_program(input.readlines())

for i in range(0, len(instructions)):
    if type(instructions[i]) is not ACC:
        new_instructions = instructions[:i]
        if type(instructions[i]) is NOP:
            new_instructions.append(JMP(instructions[i]._operand))
        else:
            new_instructions.append(NOP(instructions[i]._operand))
        new_instructions.extend(instructions[i+1:])

        try:
            acc = run_program(new_instructions)
            print(f'successfull result: {acc}')
            break
        except:
            print(
                f'replacing "{instructions[i]}" --> "{new_instructions[i]}" failed')
    else:
        print(f' skipping "{instructions[i]}"')
