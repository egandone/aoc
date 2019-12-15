from intcomputer import execute
import mock
import builtins
from itertools import permutations
from threading import Thread
from queue import Queue

def get_mock_input(q):
    def mock_input(s):
        return q.get()
    return mock_input

def get_mock_output(q):
    def mock_output(s):
        q.put(int(s))
    return mock_output

def run_program(instructions, inq, outq):
    with mock.patch.object(builtins, 'input', get_mock_input(inq)):
        with mock.patch.object(builtins, 'print', get_mock_output(outq)):
            program = instructions.copy()
            execute(program)


def run_amplifiers(code, i1, i2, i3, i4, i5):
    inq1 = Queue()
    inq1.put(i1)
    inq2 = Queue()
    inq2.put(i2)
    inq3 = Queue()
    inq3.put(i3)
    inq4 = Queue()
    inq2.put(i2)
    inq5 = Queue()
    inq2.put(i2)
    amp1 = Thread(target=run_program(code, inq1, inq2)
    amp2 = Thread(target=run_program(code, inq2, inq3)
    amp3 = Thread(target=run_program(code, inq3, inq4)
    amp4 = Thread(target=run_program(code, inq4, inq5)
    amp5 = Thread(target=run_program(code, inq5, inq1)

    inq.put(i2)
    inq.put(outq.get())
    o2 = run_program(code, inq, outq)
    inq.put(i3)
    inq.put(outq.get())
    o3 = run_program(code, inq, outq)
    inq.put(i4)
    inq.put(outq.get())
    o4 = run_program(code, inq, outq)
    inq.put(i5)
    inq.put(outq.get())
    o5 = run_program(code, inq, outq)
    return outq.get()


if __name__ == "__main__":
    amp = [3,8,1001,8,10,8,105,1,0,0,21,38,47,64,85,106,187,268,349,430,99999,3,9,1002,9,4,9,1001,9,4,9,1002,9,4,9,4,9,99,3,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,102,5,9,9,1001,9,5,9,4,9,99,3,9,101,3,9,9,102,5,9,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,1002,9,3,9,101,2,9,9,102,4,9,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99]
    results = dict()
    for p in permutations([0,1,2,3,4]):
        out = run_amplifiers(amp, *p)
        print(f'{p} -> {out}')
        results[out] = p
    best = max(results)
    print(f'best output is {best} using {results[best]}')
