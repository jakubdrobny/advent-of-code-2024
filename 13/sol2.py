import sys

MAX_INT = 1 << 30
DELTA = 10**13
EPS = 1e-2


def parse_line(l, last_split):
    l = l.split(": ")
    dx, dy = l[1].split(", ")
    return int(dx.split(last_split)[1]), int(dy.split(last_split)[1])


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return 0, 0

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


inp = []

for line in sys.stdin:
    line = line.strip("\n")
    if line:
        inp.append(line)

n = len(inp) // 3

total_tokens = 0

for it in range(n):
    line_idx = it * 3
    ba_dx, ba_dy = parse_line(inp[line_idx], "+")
    bb_dx, bb_dy = parse_line(inp[line_idx + 1], "+")

    x, y = 0, 0
    tg_x, tg_y = parse_line(inp[line_idx + 2], "=")
    tg_x, tg_y = tg_x + DELTA, tg_y + DELTA

    a, b, c, d = (
        [0, tg_x / bb_dx],
        [tg_x / ba_dx, 0],
        [0, tg_y / bb_dy],
        [tg_y / ba_dy, 0],
    )
    ix, iy = line_intersection((a, b), (c, d))
    if ix and iy and abs(ix - round(ix)) < EPS and abs(iy - round(iy)) < EPS:
        total_tokens += ix * 3 + iy

print(total_tokens)
