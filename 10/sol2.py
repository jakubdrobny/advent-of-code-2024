from collections import deque
import sys

g = []
for line in sys.stdin:
    g.append(list(line.strip("\n")))

n, m = len(g), len(g[0])

res = 0

for i in range(n):
    for j in range(m):
        if g[i][j] == "0":
            q = deque()
            q.append((i, j))

            score = 0
            while q:
                ci, cj = q.popleft()
                if g[ci][cj] == "9":
                    score += 1

                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    ni, nj = ci + dx, cj + dy
                    if (
                        ni >= 0
                        and nj >= 0
                        and ni < n
                        and nj < m
                        and int(g[ci][cj]) + 1 == int(g[ni][nj])
                    ):
                        q.append((ni, nj))

            res += score

print(res)
