import sys
from heapq import heappop, heappush

g = []

for line in sys.stdin:
    g.append(list(line.strip("\n")))

n, m = len(g), len(g[0])

si, sj, ei, ej = -1, -1, -1, -1
for i in range(n):
    for j in range(m):
        if g[i][j] == "S":
            si, sj = i, j
        if g[i][j] == "E":
            ei, ej = i, j

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

dist = [[[-1 for _ in range(4)] for _ in range(m)] for _ in range(n)]
dist[si][sj][3] = 0
dist[si][sj][2] = dist[si][sj][1] = dist[si][sj][0] = 1000
q = []
for i in range(4):
    heappush(q, (dist[si][sj][i], si, sj, i))
while q:
    cd, ci, cj, cs = heappop(q)
    if cd > dist[ci][cj][cs]:
        continue
    ni, nj = ci + dx[cs], cj + dy[cs]
    if g[ni][nj] != "#":
        for i in range(4):
            nd = cd + 1 + (1000 if i != cs else 0)
            if dist[ni][nj][i] == -1 or nd < dist[ni][nj][i]:
                dist[ni][nj][i] = nd
                heappush(q, (nd, ni, nj, i))
print(min(dist[ei][ej]))
