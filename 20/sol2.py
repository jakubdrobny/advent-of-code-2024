from collections import defaultdict, deque
import sys

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

MAX_INT = 10**20
L = 21

delta = [[-1, 0], [1, 0], [0, 1], [0, -1]]


def bfs(sy, sx):
    q = deque()
    q.append((sy, sx))
    dist = [[MAX_INT for _ in range(m)] for _ in range(n)]
    par = [[(-1, -1) for _ in range(m)] for _ in range(n)]
    dist[sy][sx] = 0
    while q:
        cy, cx = q.popleft()
        for dy, dx in delta:
            ny, nx = cy + dy, cx + dx
            if (
                ny >= 0
                and nx >= 0
                and ny < n
                and nx < m
                and dist[ny][nx] > dist[cy][cx] + 1
                and g[ny][nx] != "#"
            ):
                dist[ny][nx] = dist[cy][cx] + 1
                par[ny][nx] = (cy, cx)
                q.append((ny, nx))
    return dist, par


dist, par = bfs(si, sj)
path = [(ei, ej)]
ci, cj = par[ei][ej]
while (ci, cj) != (-1, -1):
    path.append((ci, cj))
    ci, cj = par[ci][cj]

path.reverse()

THRESHOLD = 100

normal_way = dist[ei][ej]

ans = set()

for i in range(len(path)):
    for j in range(i + 1, len(path)):
        i1, j1 = path[i]
        i2, j2 = path[j]
        for di, dj in delta:
            ni, nj = i1 + di, j1 + dj
            if g[ni][nj] == "#":
                d = abs(ni - i2) + abs(nj - j2)
                if d > 1 and d <= 20:
                    cheated_way = i + d + (len(path) - j)
                    saved = normal_way - cheated_way
                    if saved >= THRESHOLD:
                        ans.add(tuple(sorted([(i1, j1), (i2, j2)])))

print(len(ans))
