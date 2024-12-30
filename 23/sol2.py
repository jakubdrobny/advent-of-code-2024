from collections import defaultdict
import sys

g = defaultdict(set)

for line in sys.stdin:
    line = line.strip("\n").split("-")
    g[line[0]].add(line[1])
    g[line[1]].add(line[0])

ans = set()

for u in g:
    for v in g[u]:
        for z in g[v]:
            if u != z and z in g[u]:
                ans.add(tuple(sorted([u, v, z])))
while True:
    nans = set()
    for t in ans:
        tl = list(t)
        for v in g[tl[0]]:
            if v not in tl:
                ok = True
                for sus in tl:
                    if v not in g[sus]:
                        ok = False
                        break
                if ok:
                    nans.add(tuple(sorted(tl + [v])))
    if len(nans) == 0:
        l = list(ans)
        l.sort()
        print(",".join(list(l[0])))
        break
    ans = set(nans)
