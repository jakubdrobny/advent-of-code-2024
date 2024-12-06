import sys

ans = 0

digits = "0123456789"

for line in sys.stdin:
    i = 0
    n = len(line)
    while i + 8 < n:
        if line[i : i + 4] == "mul(":
            j = i + 4
            while j < n and line[j] in digits:
                j += 1
            if j == i + 4 or j == n or line[j] != ",":
                i = j
                continue
            x = int(line[i + 4 : j])
            j += 1
            s = j
            while j < n and line[j] in digits:
                j += 1
            if s == j or j == n or line[j] != ")":
                i = j
                continue
            y = int(line[s:j])
            ans += x * y
            i = j + 1
        else:
            i += 1

print(ans)
