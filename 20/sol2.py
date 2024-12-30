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
            ):
                dist[ny][nx] = dist[cy][cx] + 1
                if g[ny][nx] != "#":
                    q.append((ny, nx))
    return dist


ds, de = bfs(si, sj), bfs(ei, ej)
cheats = set()
THRESHOLD = 100
L = 22
normal_way = ds[ei][ej]
for a in range(n):
    for b in range(m):
        for c in range(max(0, a - L), min(n, a + L)):
            for d in range(max(0, b - L), min(m, b + L)):
                if g[a][b] != "#" or g[c][d] == "#":
                    continue
                for da, db in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    na, nb = a + da, b + db
                    cost = abs(na - c) + abs(nb - d)
                    if (
                        na >= 0
                        and nb >= 0
                        and na < n
                        and nb < m
                        and g[na][nb] != "#"
                        and cost <= 20
                    ):
                        cheated_way = ds[na][nb] + cost + de[c][d]
                        saved = normal_way - cheated_way
                        if saved >= THRESHOLD:
                            key = tuple(sorted([(na, nb), (c, d)]))
                            cheats.add(key)
print(len(cheats))
