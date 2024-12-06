import sys
from collections import defaultdict

RULES = "RELUS"
UPDATES = "UPDATES"

rules = defaultdict(list)

mode = RULES

ans = 0

for line in sys.stdin:
    if line == "\n":
        mode = UPDATES
        continue

    line = line.strip("\n")
    if mode == RULES:
        x, y = list(map(int, line.split("|")))
        rules[y].append(x)
    else:
        a = list(map(int, line.split(",")))
        ok = True
        for i in range(1, len(a)):
            for j in range(i):
                if a[i] in rules[a[j]]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            ans += a[len(a) // 2]

print(ans)
