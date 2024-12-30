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
            if (u[0] == "t" or v[0] == "t" or z[0] == "t") and u != z and z in g[u]:
                ans.add(tuple(sorted([u, v, z])))

print(len(ans))
