import sys

ITERATIONS = 100

n, m = -1, -1

rbts = []

for line in sys.stdin:
    if (n, m) == (-1, -1):
        n, m = map(int, line.split())
    else:
        line = line.split(" ")
        col, row = map(int, line[0].split("=")[1].split(","))
        dcol, drow = map(int, line[1].split("=")[1].split(","))
        rbts.append([col, row, dcol, drow])


def update(x, dx, dim):
    return ((x + ITERATIONS * dx) % dim + dim) % dim


quads = [[0, 0], [0, 0]]

for rbt in rbts:
    pcol, prow, dcol, drow = rbt
    col = update(pcol, dcol, m)
    row = update(prow, drow, n)

    if col == m // 2 or row == n // 2:
        continue

    qrow, qcol = col // ((m + 1) // 2), row // ((n + 1) // 2)
    quads[qrow][qcol] += 1

print(quads[0][0] * quads[0][1] * quads[1][0] * quads[1][1])
