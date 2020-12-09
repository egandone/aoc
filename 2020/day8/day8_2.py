class CPU:
    def __init__(self):
        self.acc = 0


class NOP:
    def __init__(self, i):
        self._operand = i
        pass

    def execute(self, cpu):
        return 1

    def __repr__(self):
        return f'NOP {self._operand: 4}'


class ACC:
    def __init__(self, i):
        self._operand = i

    def execute(self, cpu):
        cpu.acc += self._operand
        return 1

    def __repr__(self):
        return f'ACC {self._operand: 4}'


class JMP:
    def __init__(self, i):
        self._operand = i

    def execute(self, cpu):
        return self._operand

    def __repr__(self):
        return f'JMP {self._operand: 4}'


def parse_program(lines):
    instructions = []
    for line in lines:
        opcode, operand = line.split(' ')
        operand = int(operand)
        if opcode == 'nop':
            instructions.append(NOP(operand))
        elif opcode == 'acc':
            instructions.append(ACC(operand))
        elif opcode == 'jmp':
            instructions.append(JMP(operand))
        else:
            raise ValueError(f'unknown opcode {opcode}')
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
            print(f'{acc}')
            break
        except:
            print(
                f'replacing "{instructions[i]}" --> "{new_instructions[i]}" failed')
    else:
        print(f' skipping "{instructions[i]}"')
