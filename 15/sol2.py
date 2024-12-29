from collections import defaultdict
import sys

g = []
instructions = ""

reading_grid = True
for line in sys.stdin:
    if line == "\n":
        reading_grid = False
    else:
        line = line.strip("\n")
        if reading_grid:
            nline = []
            for c in line:
                nline.extend(list(c + c if c in "#." else "[]" if c == "O" else "@."))
            g.append(nline)
        else:
            instructions += line

n, m = len(g), len(g[0])

ci, cj = -1, -1
for i in range(n):
    for j in range(m):
        if g[i][j] == "@":
            ci, cj = i, j

di = {"^": -1, "v": 1, "<": 0, ">": 0}
dj = {"^": 0, "v": 0, "<": -1, ">": 1}
inv_op = {"^": "v", "v": "^", "<": ">", ">": "<"}

for instruction in instructions:
    ni, nj = ci + di[instruction], cj + dj[instruction]
    if g[ni][nj] in "[]":
        if instruction in "^v":
            pos_to_move = set([(ni, nj), (ni, nj + (-1 if g[ni][nj] == "]" else 1))])
            delta_pos = set(pos_to_move)
            can_move = True
            while can_move and len(delta_pos) > 0:
                new_delta_pos = set()
                for pos in delta_pos:
                    n2i, n2j = (
                        pos[0] + di[instruction],
                        pos[1] + dj[instruction],
                    )

                    if g[n2i][n2j] == "#":
                        can_move = False
                        break

                    if g[n2i][n2j] in "[]":
                        new_delta_pos.add((n2i, n2j))
                        new_delta_pos.add(
                            (n2i, n2j + (-1 if g[n2i][n2j] == "]" else 1))
                        )
                pos_to_move.update(new_delta_pos)
                delta_pos = set(new_delta_pos)
            if can_move:
                pos_by_rows = defaultdict(list)
                for pos in pos_to_move:
                    pos_by_rows[pos[0]].append(pos)
                pos_by_rows[ci].append((ci, cj))
                for row in pos_by_rows:
                    pos_by_rows[row] = list(sorted(pos_by_rows[row]))
                cur_row = (
                    min(pos_by_rows.keys()) - 1
                    if instruction == "^"
                    else max(pos_by_rows.keys()) + 1
                )
                while cur_row != ci:
                    next_row = cur_row + (-1 if instruction == "v" else 1)
                    for pos in pos_by_rows[next_row]:
                        g[cur_row][pos[1]], g[next_row][pos[1]] = (
                            g[next_row][pos[1]],
                            g[cur_row][pos[1]],
                        )
                    cur_row = next_row
                g[ci][cj] = "."
                g[ni][nj] = "@"
                ci, cj = ni, nj
        else:
            n2i, n2j = ni + di[instruction], nj + dj[instruction]
            while g[n2i][n2j] in "[]":
                n2i, n2j = n2i + di[instruction], n2j + dj[instruction]
            if g[n2i][n2j] == ".":
                while (n2i, n2j) != (ci, cj):
                    n3i, n3j = (
                        n2i + di[inv_op[instruction]],
                        n2j + dj[inv_op[instruction]],
                    )
                    g[n2i][n2j], g[n3i][n3j] = g[n3i][n3j], g[n2i][n2j]
                    n2i, n2j = n3i, n3j
                ci, cj = ni, nj
    elif g[ni][nj] == ".":
        g[ni][nj] = "@"
        g[ci][cj] = "."
        ci, cj = ni, nj


answer = 0
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if g[i][j] == "[":
            answer += 100 * i + j
print(answer)
