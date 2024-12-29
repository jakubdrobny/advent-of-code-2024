import sys

items = []

ans = 0

reading_queries = False
for line in sys.stdin:
    if line == "\n":
        reading_queries = True
    else:
        if not reading_queries:
            items = line.strip("\n").split(", ")
        else:
            s = line.strip("\n")
            n = len(s)

            can = [False for _ in range(n + 1)]
            can[0] = True

            for i in range(1, n + 1):
                for item in items:
                    can[i] = (
                        can[i] or can[i - len(item)]
                        if len(item) <= i and s[i - len(item) : i] == item
                        else can[i]
                    )

            if can[-1]:
                ans += 1

print(ans)
