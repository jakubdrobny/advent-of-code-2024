import sys

ans = 0

for line in sys.stdin:
    a = list(map(int, line.split()))

    n = len(a)
    ok = True
    for i in range(n - 1):
        d = abs(a[i] - a[i + 1])
        if (a[0] < a[1]) != (a[i] < a[i + 1]) or d < 1 or d > 3:
            ok = False
            break

    ans += int(ok)

print(ans)
