import sys

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


for line in sys.stdin:
    line = line.strip("\n")
    cur = int(line)
    for it in range(2000):
        cur = process(cur)
    res += cur

print(res)
