class OpCode:
    def __init__(self, inmodes=(0, 0, 0)):
        self._inmodes = inmodes

    def get_in(self, index, instructions, position):
        v = instructions[position]
        if self._inmodes[index] == 0:
            v = instructions[v]
        return v

    def execute(self, instructions, position):
        return position


class Add(OpCode):
    def __init__(self, inmodes):
        super().__init__(inmodes)

    def execute(self, instructions, position):
        in1 = self.get_in(0, instructions, position)
        in2 = self.get_in(1, instructions, position + 1)
        instructions[instructions[position+2]] = in1 + in2
        return position + 3


class Mult(OpCode):
    def __init__(self, inmodes):
        super().__init__(inmodes)

    def execute(self, instructions, position):
        in1 = self.get_in(0, instructions, position)
        in2 = self.get_in(1, instructions, position + 1)
        instructions[instructions[position+2]] = in1 * in2
        return position + 3


class IfTrue(OpCode):
    def __init__(self, inmodes):
        super().__init__(inmodes)

    def execute(self, instructions, position):
        in1 = self.get_in(0, instructions, position)
        in2 = self.get_in(1, instructions, position + 1)
        if in1 != 0:
            return in2
        else:
            return position + 2


class IfFalse(OpCode):
    def __init__(self, inmodes):
        super().__init__(inmodes)

    def execute(self, instructions, position):
        in1 = self.get_in(0, instructions, position)
        in2 = self.get_in(1, instructions, position + 1)
        if in1 == 0:
            return in2
        else:
            return position + 2


class Less(OpCode):
    def __init__(self, inmodes):
        super().__init__(inmodes)

    def execute(self, instructions, position):
        in1 = self.get_in(0, instructions, position)
        in2 = self.get_in(1, instructions, position + 1)
        if in1 < in2:
            instructions[instructions[position+2]] = 1
        else:
            instructions[instructions[position+2]] = 0
        return position + 3


class Equals(OpCode):
    def __init__(self, inmodes):
        super().__init__(inmodes)

    def execute(self, instructions, position):
        in1 = self.get_in(0, instructions, position)
        in2 = self.get_in(1, instructions, position + 1)
        if in1 == in2:
            instructions[instructions[position+2]] = 1
        else:
            instructions[instructions[position+2]] = 0
        return position + 3


class In(OpCode):
    def execute(self, instructions, position):
        _in = int(input('IN: '))
        instructions[instructions[position]] = _in
        return position + 1


class Out(OpCode):
    def __init__(self, inmodes):
        super().__init__(inmodes)

    def execute(self, instructions, position):
        out = self.get_in(0, instructions, position)
        print(out)
        return position + 1


class End(OpCode):
    def execute(self, instructions, position):
        return -1
