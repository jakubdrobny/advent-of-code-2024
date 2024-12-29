from collections import deque
import sys

idx = {"A": 0, "B": 1, "C": 2}
rev_idx = ["A", "B", "C"]

regs = [0, 0, 0]
program = []

reading_registers = True
for line in sys.stdin:
    if line == "\n":
        reading_registers = False
    else:
        line = line.strip("\n")
        if reading_registers:
            line = line.split(": ")
            regs[idx[line[0].split()[1]]] = int(line[1])
        else:
            program = list(map(int, line.split(": ")[1].split(",")))


# lmao
def get_literal_operand(val):
    return val


def get_combo_operand(regs, val):
    if val < 4:
        return val
    return regs[idx[rev_idx[val - 4]]]


def _dv(regs, reg_idx, operand):
    numerator = regs[idx["A"]]
    denominator = 1 << get_combo_operand(regs, operand)
    regs[reg_idx] = numerator // denominator
    return regs


def bxl(regs, operand):
    regs[idx["B"]] = regs[idx["B"]] ^ get_literal_operand(operand)
    return regs


def bst(regs, operand):
    regs[idx["B"]] = get_combo_operand(regs, operand) % 8
    return regs


def jnz(regs, operand, old_ip):
    val_a = regs[idx["A"]]
    if val_a == 0:
        return old_ip + 2
    lit_op = get_literal_operand(operand)
    return old_ip + 2 if lit_op == old_ip else lit_op


def bxc(regs):
    regs[idx["B"]] = regs[idx["B"]] ^ regs[idx["C"]]
    return regs


def out(regs, operand):
    return get_combo_operand(regs, operand) % 8


def run_prog(a_val):
    regs = [a_val, 0, 0]
    output = []
    ip = 0
    while ip + 1 < len(program):
        new_ip = ip + 2
        op = program[ip + 1]
        match program[ip]:
            case 0:
                regs = _dv(regs, idx["A"], op)
            case 1:
                regs = bxl(regs, op)
            case 2:
                regs = bst(regs, op)
            case 3:
                new_ip = jnz(regs, op, ip)
            case 4:
                regs = bxc(regs)
            case 5:
                output.append(out(regs, op))
            case 6:
                regs = _dv(regs, idx["B"], program[ip + 1])
            case 7:
                regs = _dv(regs, idx["C"], program[ip + 1])
        ip = new_ip
    return output


q = deque([""])
while q:
    oct_val = q.popleft()
    for d in range(8):
        n_oct_val = oct_val + str(d)
        dec_val = int(n_oct_val, 8)

        res = run_prog(dec_val)

        if res == program:
            print(dec_val)
            sys.exit(0)

        if res == program[-len(res) :]:
            q.append(n_oct_val)
