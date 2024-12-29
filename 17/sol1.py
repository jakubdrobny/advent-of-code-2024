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

output = []


# lmao
def get_literal_operand(val):
    return val


def get_combo_operand(val):
    if val < 4:
        return val
    return regs[idx[rev_idx[val - 4]]]


def _dv(reg_idx, operand):
    numerator = regs[idx["A"]]
    denominator = 1 << get_combo_operand(operand)
    regs[reg_idx] = numerator // denominator


def bxl(operand):
    regs[idx["B"]] = regs[idx["B"]] ^ get_literal_operand(operand)


def bst(operand):
    regs[idx["B"]] = get_combo_operand(operand) % 8


def jnz(operand, old_ip):
    val_a = regs[idx["A"]]
    if val_a == 0:
        return old_ip + 2
    lit_op = get_literal_operand(operand)
    return old_ip + 2 if lit_op == old_ip else lit_op


def bxc():
    regs[idx["B"]] = regs[idx["B"]] ^ regs[idx["C"]]


def out(operand):
    return get_combo_operand(operand) % 8


ip = 0
while ip + 1 < len(program):
    new_ip = ip + 2
    op = program[ip + 1]
    match program[ip]:
        case 0:
            _dv(idx["A"], op)
        case 1:
            bxl(op)
        case 2:
            bst(op)
        case 3:
            new_ip = jnz(op, ip)
        case 4:
            bxc()
        case 5:
            output.append(out(op))
        case 6:
            _dv(idx["B"], program[ip + 1])
        case 7:
            _dv(idx["C"], program[ip + 1])
    ip = new_ip

print(",".join(map(str, output)))
