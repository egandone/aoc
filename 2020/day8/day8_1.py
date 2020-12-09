class CPU:
    def __init__(self):
        self.acc = 0


class NOP:
    def __init__(self, i):
        pass

    def execute(self, cpu):
        return 1


class ACC:
    def __init__(self, i):
        self._acc = i

    def execute(self, cpu):
        cpu.acc += self._acc
        return 1


class JMP:
    def __init__(self, i):
        self._jmp = i

    def execute(self, cpu):
        return self._jmp


instructions = []
with open("input.txt") as input:
    for line in input.readlines():
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

executed_lines = set()
i = 0
cpu = CPU()
while i not in executed_lines:
    executed_lines.add(i)
    i += instructions[i].execute(cpu)

print(f'{cpu.acc}')
