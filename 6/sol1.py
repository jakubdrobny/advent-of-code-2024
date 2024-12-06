import sys

g = []

for line in sys.stdin:
    g.append(line.strip("\n"))

vis = set()
h, w = len(g), len(g[0])

x, y = -1, -1

for i in range(h):
    for j in range(w):
        if g[i][j] == "^":
            y, x = i, j
            break
    if x != -1:
        break

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
dr = 0

while x >= 0 and y >= 0 and x < w and y < h:
    vis.add((x, y))

    ny, nx = y + dy[dr], x + dx[dr]
    if ny < 0 or nx < 0 or ny >= h or nx >= w:
        break

    if g[ny][nx] == "#":
        dr = (dr + 1) % 4
    else:
        y, x = ny, nx

print(len(vis))
