import sys

g = []
for line in sys.stdin:
    g.append(line.strip("\n"))

n, m = len(g), len(g[0])

cnt = 0

SMAS = set(["SAM", "MAS"])

for i in range(1, n - 1):
    for j in range(1, m - 1):
        w1, w2 = (
            g[i - 1][j - 1] + g[i][j] + g[i + 1][j + 1],
            g[i - 1][j + 1] + g[i][j] + g[i + 1][j - 1],
        )
        if w1 in SMAS and w2 in SMAS:
            cnt += 1

print(cnt)
