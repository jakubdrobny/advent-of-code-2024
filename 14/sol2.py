import sys

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
    return ((x + dx) % dim + dim) % dim


for it in range(10000):
    n_rbts = []

    g = [["." for _ in range(m)] for _ in range(n)]

    for rbt in rbts:
        pcol, prow, dcol, drow = rbt
        col = update(pcol, dcol, m)
        row = update(prow, drow, n)

        n_rbts.append([col, row, dcol, drow])
        g[row][col] = "X"

    rbts = list(n_rbts)

    for i in range(n):
        for j in range(m - 9):
            s = "".join(g[i][j + c] for c in range(9))
            if s == "XXXXXXXXX":
                print(it + 1)
                sys.exit(0)
