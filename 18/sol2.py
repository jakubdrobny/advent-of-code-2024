from collections import deque
import sys

n, m = -1, -1
grid = []


def can():
    q = deque([(0, 0)])
    vis = [[-1 for _ in range(m)] for _ in range(n)]
    vis[0][0] = 0

    while q:
        y, x = q.popleft()
        for dy, dx in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            ny, nx = y + dy, x + dx
            if (
                ny >= 0
                and nx >= 0
                and ny < n
                and nx < m
                and vis[ny][nx] == -1
                and grid[ny][nx] != "#"
            ):
                vis[ny][nx] = vis[y][x] + 1
                q.append((ny, nx))

    return vis[-1][-1] != -1


for line in sys.stdin:
    if (n, m) == (-1, -1):
        n, m = map(int, line.strip("\n").split())
        grid = [["." for _ in range(m)] for _ in range(n)]
    else:
        x, y = map(int, line.strip("\n").split(","))
        grid[y][x] = "#"
        if not can():
            print(x, y)
            break
