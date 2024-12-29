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
par = [[[list() for _ in range(4)] for _ in range(m)] for _ in range(n)]
dist[si][sj][3] = 0
dist[si][sj][2] = dist[si][sj][1] = dist[si][sj][0] = 1000
par[si][sj][2] = par[si][sj][1] = par[si][sj][0] = list([(si, sj, 3)])
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
                par[ni][nj][i] = list()
                par[ni][nj][i].append((ci, cj, i) if i == cs else (ni, nj, cs))
                heappush(q, (nd, ni, nj, i))
            elif nd == dist[ni][nj][i]:
                par[ni][nj][i].append((ci, cj, i) if i == cs else (ni, nj, cs))

mn = 10**20
vis = set()
for i in range(4):
    if (dist[ei][ej][i] < mn and dist[ei][ej][i] != -1) or dist[ei][ej][i] == mn:
        if dist[ei][ej][i] < mn:
            vis = set()
        vis.add((ei, ej, i))
        mn = dist[ei][ej][i]
delta = set(vis)
while len(delta) > 0:
    new_delta = set()
    for pi, pj, ps in delta:
        for npi, npj, nps in par[pi][pj][ps]:
            if (npi, npj, nps) not in vis:
                vis.add((npi, npj, nps))
                new_delta.add((npi, npj, nps))
    delta = set(new_delta)
ans = set()
for x, y, _ in vis:
    ans.add((x, y))
print(len(ans))
