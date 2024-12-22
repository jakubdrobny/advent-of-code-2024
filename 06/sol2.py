from collections import defaultdict
import sys

g = []

for line in sys.stdin:
    g.append(list(line.strip("\n")))


def will_cycle(cy, cx, cd):
    cvis = defaultdict(list)

    while cx >= 0 and cy >= 0 and cx < w and cy < h:
        ncy, ncx = cy + dy[cd], cx + dx[cd]
        if ncy < 0 or ncx < 0 or ncy >= h or ncx >= w:
            return False

        if g[ncy][ncx] != "#":
            cy, cx = ncy, ncx
        else:
            cd = (cd + 1) % 4

        if (cy, cx) in cvis and cd in cvis[(cy, cx)]:
            return True

        cvis[(cy, cx)].append(cd)

    return False


vis = defaultdict(int)
cycle_pos = set()
h, w = len(g), len(g[0])

x, y = -1, -1

for i in range(h):
    for j in range(w):
        if g[i][j] == "^":
            y, x = i, j
            g[y][x] = "."
            break
    if x != -1:
        break

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
dr = 0

for i in range(h):
    for j in range(w):
        if g[i][j] != "#" and (i, j) != (y, x):
            prv = g[i][j]
            g[i][j] = "#"
            if will_cycle(y, x, dr):
                cycle_pos.add((i, j))
            g[i][j] = prv

print(len(cycle_pos))
