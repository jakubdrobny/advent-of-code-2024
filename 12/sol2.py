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

comp = [[0 for _ in range(m)] for _ in range(n)]
area = [0 for _ in range(n * m + 1)]
sides = [0 for _ in range(n * m + 1)]

comp_idx = 1

for i in range(n):
    for j in range(m):
        if comp[i][j]:
            continue

        comp[i][j] = comp_idx
        comp_idx += 1
        q = deque()
        q.append((i, j))

        while q:
            ci, cj = q.popleft()
            area[comp[i][j]] += 1

            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                ni, nj = ci + dx, cj + dy

                if same_plant(ci, cj, ni, nj) and not comp[ni][nj]:
                    comp[ni][nj] = comp[i][j]
                    q.append((ni, nj))

# get sides from top + bottom
for i in range(n):
    for di in [-1, 1]:
        l = 0
        while l < m:
            while l < m and same_plant(i, l, i + di, l):
                l += 1

            if l == m:
                continue

            r = l
            while r < m and not same_plant(i, r, i + di, r) and same_plant(i, l, i, r):
                r += 1

            sides[comp[i][l]] += 1
            l = r

# get sides from left + right
for j in range(m):
    for dj in [-1, 1]:
        l = 0
        while l < n:
            while l < n and same_plant(l, j, l, j + dj):
                l += 1

            if l == n:
                continue

            r = l
            while r < n and not same_plant(r, j, r, j + dj) and same_plant(l, j, r, j):
                r += 1

            sides[comp[l][j]] += 1
            l = r

total_price = 0

for i in range(1, n * m + 1):
    total_price += sides[i] * area[i]

print(total_price)
