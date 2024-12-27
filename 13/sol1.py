import sys

MAX_INT = 1 << 30


def parse_line(l, last_split):
    l = l.split(": ")
    dx, dy = l[1].split(", ")
    return int(dx.split(last_split)[1]), int(dy.split(last_split)[1])


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

    cur_tokens = MAX_INT
    for use_a in range(0, 101):
        for use_b in range(0, 101):
            if (
                ba_dx * use_a + bb_dx * use_b == tg_x
                and ba_dy * use_a + bb_dy * use_b == tg_y
            ):
                cur_tokens = min(cur_tokens, use_a * 3 + use_b)

    if cur_tokens != MAX_INT:
        total_tokens += cur_tokens

print(total_tokens)
