import sys
from collections import defaultdict

ITERATIONS = 75

stones = defaultdict(int)

for line in sys.stdin:
    for stone in list(map(int, line.strip("\n").split(" "))):
        stones[stone] += 1

for it in range(ITERATIONS):
    new_stones = defaultdict(int)

    for stone in stones:
        cnt = stones[stone]
        if stone == 0:
            new_stones[1] += cnt
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            new_stones[int(str_stone[: len(str_stone) // 2])] += cnt
            new_stones[int(str_stone[len(str_stone) // 2 :])] += cnt
        else:
            new_stones[stone * 2024] += cnt

    stones = new_stones

res = 0
for stone in stones:
    res += stones[stone]
print(res)
