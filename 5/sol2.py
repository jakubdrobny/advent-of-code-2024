import sys
from collections import defaultdict, deque

RULES = "RELUS"
UPDATES = "UPDATES"


def topsort(rules, vt):
    deg = defaultdict(int)
    for v in vt:
        for u in rules[v]:
            if u in vt:
                deg[u] += 1

    q = deque()

    for v in vt:
        if deg[v] == 0:
            q.append(v)

    res = []
    while q:
        v = q.popleft()
        res.append(v)
        for u in rules[v]:
            deg[u] -= 1
            if deg[u] == 0:
                q.append(u)

    return res


rules = defaultdict(list)

mode = RULES

ans = 0

tp = []

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
        if not ok:
            st = set(a)
            res = []
            for v in topsort(rules, a):
                if v in st:
                    res.append(v)
            ans += res[len(res) // 2]

print(ans)
