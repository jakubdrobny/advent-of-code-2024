import sys

a, b = [], []

for line in sys.stdin:
    x, y = map(int, line.split())
    a.append(x)
    b.append(y)

a.sort()
b.sort()

ans = 0

for i in range(len(a)):
    ans += abs(a[i] - b[i])

print(ans)
