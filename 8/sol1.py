from collections import defaultdict
import sys

g = []

for line in sys.stdin:
    g.append(line.strip("\n"))

n, m = len(g), len(g[0])

pos = defaultdict(list)

for i in range(n):
    for j in range(m):
        if g[i][j] != ".":
            pos[g[i][j]].append((i, j))

pos_set = set()

for p in pos:
    poss = pos[p]
    ln = len(poss)
    for i in range(ln):
        for j in range(i):
            dx, dy = poss[i][0] - poss[j][0], poss[i][1] - poss[j][1]
            p1, p2 = (poss[j][0] - dx, poss[j][1] - dy), (
                poss[i][0] + dx,
                poss[i][1] + dy,
            )
            if p1[0] >= 0 and p1[0] < n and p1[1] >= 0 and p1[1] < m:
                pos_set.add(p1)
            if p2[0] >= 0 and p2[0] < n and p2[1] >= 0 and p2[1] < m:
                pos_set.add(p2)

print(len(pos_set))
