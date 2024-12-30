import sys

# i dont really know why this works though, just from reddit, i cant anymore this year bruh
# wrong ops are when:
#  - non highest zXY does not have XOR op
#  - XOR has operands and result non xAB, yCD, zEF
#  - output of AND without x00 in either operand is input for non OR operation
#  - output of XOR is input for OR operation
# bruh why these should hold i have no clue at all, but finally 50 stars, can rest :DD

ops = []
reading_ops = False
highest_z = "z00"
for line in sys.stdin:
    if line == "\n":
        reading_ops = True
    elif reading_ops:
        x, op, y, _, z = line.strip("\n").split()
        ops.append((x, op, y, z))
        if z[0] == "z" and int(z[1:]) > int(highest_z[1:]):
            highest_z = z
wrong = set()
for op1, op, op2, res in ops:
    if res[0] == "z" and op != "XOR" and res != highest_z:
        wrong.add(res)
    if (
        op == "XOR"
        and res[0] not in "xyz"
        and op1[0] not in "xyz"
        and op2[0] not in "xyz"
    ):
        wrong.add(res)
    if op == "AND" and "x00" not in [op1, op2]:
        for subop1, subop, subop2, subres in ops:
            if (res == subop1 or res == subop2) and subop != "OR":
                wrong.add(res)
    if op == "XOR":
        for subop1, subop, subop2, subres in ops:
            if (res == subop1 or res == subop2) and subop == "OR":
                wrong.add(res)

print(",".join(sorted(wrong)))
