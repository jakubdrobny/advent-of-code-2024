import sys

locks = []
keys = []

cur = []
for line in sys.stdin:
    line = line.strip("\n")
    if not line:
        if cur[0] == "#" * len(cur[0]):
            lock = []
            for j in range(len(cur[0])):
                i = 1
                while cur[i][j] == "#":
                    i += 1
                lock.append(i - 1)
            locks.append(lock)
        else:
            key = []
            for j in range(len(cur[0])):
                i = len(cur) - 1
                while cur[i][j] == "#":
                    i -= 1
                key.append(len(cur) - i - 2)
            keys.append(key)
        cur = []
    else:
        cur.append(line)

pairs = 0

for lock in locks:
    for key in keys:
        ok = all(lock[i] + key[i] <= 5 for i in range(len(lock)))
        if ok:
            pairs += 1

print(pairs)
