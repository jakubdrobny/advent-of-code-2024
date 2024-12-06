import sys
from collections import defaultdict

a, b = [], []

for line in sys.stdin:
    x, y = map(int, line.split())
    a.append(x)
    b.append(y)

cnt = defaultdict(int)

for x in b:
    cnt[x] += 1

ans = 0

for x in a:
    ans += x * cnt[x]

print(ans)
