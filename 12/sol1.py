from collections import deque
import sys


def inside(i, j):
    return i >= 0 and j >= 0 and i < n and j < m


def same_plant(i1, j1, i2, j2):
    if inside(i1, j1) and inside(i2, j2):
        return g[i1][j1] == g[i2][j2]

    return False


g = []

for line in sys.stdin:
    g.append(list(line.strip("\n")))

n, m = len(g), len(g[0])

vis = [[0 for _ in range(m)] for _ in range(n)]

total_price = 0

for i in range(n):
    for j in range(m):
        if vis[i][j]:
            continue

        vis[i][j] = 1
        q = deque()
        q.append((i, j))

        perimeter, area = 0, 0

        while q:
            ci, cj = q.popleft()
            area += 1

            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                ni, nj = ci + dx, cj + dy

                if not same_plant(ci, cj, ni, nj):
                    perimeter += 1

                if inside(ni, nj) and same_plant(ci, cj, ni, nj) and not vis[ni][nj]:
                    vis[ni][nj] = 1
                    q.append((ni, nj))

        total_price += area * perimeter

print(total_price)
