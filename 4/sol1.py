import sys

g = []
for line in sys.stdin:
    g.append(line.strip("\n"))

n, m = len(g), len(g[0])

cnt = 0

for i in range(n):
    for j in range(m):
        word = g[i][j : j + 4]
        if word == "XMAS" or word == "SAMX":
            cnt += 1
        if i >= 3:
            word = g[i][j] + g[i - 1][j] + g[i - 2][j] + g[i - 3][j]
            if word == "XMAS" or word == "SAMX":
                cnt += 1
        if i >= 3 and j >= 3:
            word = g[i][j] + g[i - 1][j - 1] + g[i - 2][j - 2] + g[i - 3][j - 3]
            if word == "XMAS" or word == "SAMX":
                cnt += 1
        if i >= 3 and j + 3 < m:
            word = g[i][j] + g[i - 1][j + 1] + g[i - 2][j + 2] + g[i - 3][j + 3]
            if word == "XMAS" or word == "SAMX":
                cnt += 1

print(cnt)
