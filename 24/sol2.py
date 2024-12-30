from collections import defaultdict
import sys

reading_vals = True
values = defaultdict(int)
ops = []
for line in sys.stdin:
    if line == "\n":
        reading_vals = False
    else:
        line = line.strip("\n")
        if reading_vals:
            line = line.split(": ")
            values[line[0]] = int(line[1])
        else:
            line = line.split(" -> ")
            x = line[0].split(" ")
            ops.append(x + [line[1]])
solved = [False for _ in range(len(ops))]
while not all(solved):
    for i in range(len(ops)):
        if solved[i]:
            continue
        op = ops[i]
        if op[0] in values and op[2] in values:
            v1, v2 = values[op[0]], values[op[2]]
            values[op[3]] = (
                v1 & v2 if op[1] == "AND" else v1 | v2 if op[1] == "OR" else v1 ^ v2
            )
            solved[i] = True
bn = ""
for k in sorted(values.keys(), reverse=True):
    if k[0] == "z":
        bn += str(values[k])
    else:
        break
print(int(bn, 2))
