from collections import deque
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
                and g[ny][nx] != "#"
            ):
                dist[ny][nx] = dist[cy][cx] + 1
                q.append((ny, nx))
    return dist


dist_from_start = bfs(si, sj)
dist_from_end = bfs(ei, ej)

normal_way = dist_from_start[ei][ej]
ans = 0
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if g[i][j] == "#":
            for dy1, dx1 in delta:
                for dy2, dx2 in delta:
                    ni1, nj1, ni2, nj2 = i + dy1, j + dx1, i + dy2, j + dx2
                    if (
                        (dy1, dx1) != (dy2, dx2)
                        and g[ni1][nj1] != "#"
                        and g[ni2][nj2] != "#"
                    ):
                        cheated_way = (
                            min(
                                dist_from_start[ni1][nj1] + dist_from_end[ni2][nj2],
                                dist_from_end[ni1][nj1] + dist_from_start[ni2][nj2],
                            )
                            + 2
                        )
                        if cheated_way < normal_way:
                            saved = normal_way - cheated_way
                            if saved >= 100:
                                ans += 1
print(ans >> 1)
