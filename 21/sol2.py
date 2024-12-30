from collections import defaultdict
import functools
from itertools import permutations
import sys


def get_shortest_paths(keypad):
    paths = defaultdict(set)
    rows, cols = len(keypad), len(keypad[0])

    def bad_path(p, r1, c1):
        cr, cc = r1, c1
        for m in p:
            if m == "<":
                cc -= 1
            if m == ">":
                cc += 1
            if m == "^":
                cr -= 1
            if m == "v":
                cr += 1
            if keypad[cr][cc] == "":
                return True
        return False

    for r1 in range(rows):
        for c1 in range(cols):
            if keypad[r1][c1] == "":
                continue
            for r2 in range(rows):
                for c2 in range(cols):
                    if keypad[r2][c2] == "":
                        continue
                    if (r1, c1) == (r2, c2):
                        paths[(keypad[r1][c1], keypad[r2][c2])].add("")
                    else:
                        dr, dc = r1 - r2, c1 - c2
                        path = ("^" if dr > 0 else "v") * abs(dr)
                        path += ("<" if dc > 0 else ">") * abs(dc)
                        for path_perm in permutations(path):
                            if not bad_path(path_perm, r1, c1):
                                paths[(keypad[r1][c1], keypad[r2][c2])].add(
                                    "".join(path_perm)
                                )
    return paths


head_pos = list()


@functools.cache
def solve(target, target_idx, depth):
    global head_pos
    if depth == len(head_pos):
        return len(target)

    if len(target) == target_idx:
        return 0

    path = (head_pos[depth], target[target_idx])
    s = 10**20
    what = num_paths[path] if depth == 0 else dir_paths[path]
    for pos_seq in what:
        s = min(s, solve(pos_seq + "A", 0, depth + 1))
    head_pos[depth] = target[target_idx]
    return s + solve(target, target_idx + 1, depth)


num_keypad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["", "0", "A"]]
dir_keypad = [["", "^", "A"], ["<", "v", ">"]]

num_paths = get_shortest_paths(num_keypad)
dir_paths = get_shortest_paths(dir_keypad)

total = 0
for line in sys.stdin:
    tg = line.strip("\n")
    head_pos = list("A" for _ in range(26))
    res = solve(tg, 0, 0)
    contrib = int(tg[:-1]) * res
    total += contrib
    print(res, "*", int(tg[:-1]), "=", contrib)
print("final ans:", total)
