import sys

ans = 0

for line in sys.stdin:
    b = list(map(int, line.split()))

    n = len(b)
    ok_total = False

    for idx in range(n):
        ok = True
        a = b[:idx] + b[idx + 1 :]
        for i in range(len(a) - 1):
            d = abs(a[i] - a[i + 1])
            if (a[0] < a[1]) != (a[i] < a[i + 1]) or d < 1 or d > 3:
                ok = False
                break

        if ok:
            ok_total = True
            break

    ans += int(ok_total)

print(ans)
