import sys

g = []
instructions = ""

reading_grid = True
for line in sys.stdin:
    if line == "\n":
        reading_grid = False
    else:
        line = line.strip("\n")
        if reading_grid:
            g.append(list(line))
        else:
            instructions += line

n, m = len(g), len(g[0])

ci, cj = -1, -1
for i in range(n):
    for j in range(m):
        if g[i][j] == "@":
            ci, cj = i, j

di = {"^": -1, "v": 1, "<": 0, ">": 0}
dj = {"^": 0, "v": 0, "<": -1, ">": 1}

for instruction in instructions:
    ni, nj = ci + di[instruction], cj + dj[instruction]
    if g[ni][nj] == "O":
        n2i, n2j = ni, nj
        while g[n2i][n2j] == "O":
            n2i, n2j = n2i + di[instruction], n2j + dj[instruction]
        if g[n2i][n2j] == ".":
            g[ci][cj] = "."
            g[ni][nj] = "@"
            g[n2i][n2j] = "O"
            ci, cj = ni, nj
    elif g[ni][nj] == ".":
        g[ni][nj] = "@"
        g[ci][cj] = "."
        ci, cj = ni, nj

answer = 0
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if g[i][j] == "O":
            answer += 100 * i + j
print(answer)
