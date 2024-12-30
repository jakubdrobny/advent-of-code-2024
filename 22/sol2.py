import sys
from collections import defaultdict

res = 0


def prune(x):
    return x % 16777216


def mix(x, y):
    return x ^ y


def process(x):
    x = mix(x, x * 64)
    x = prune(x)
    x = prune(mix(x, x // 32))
    x = prune(mix(x, x * 2048))
    return x


seqs = []

for line in sys.stdin:
    line = line.strip("\n")
    cur = int(line)
    cd = defaultdict(int)
    digs = [int(str(cur)[-1])]
    deltas = []
    for it in range(1, 2001):
        n_cur = process(cur)
        digs.append(int(str(n_cur)[-1]))
        deltas.append(digs[-1] - digs[-2])
        if len(deltas) >= 4:
            k = tuple(deltas[-4:])
            if k not in cd:
                cd[k] = digs[-1]
        cur = n_cur
    seqs.append(cd)

income = defaultdict(int)
for i, s in enumerate(seqs):
    for k in s:
        income[k] += s[k]
print(max(income.values()))
