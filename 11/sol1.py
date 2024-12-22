import sys

ITERATIONS = 25

stones = []

for line in sys.stdin:
    stones = list(map(int, line.strip("\n").split(" ")))

for it in range(ITERATIONS):
    new_stones = []

    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            new_stones.append(int(str_stone[: len(str_stone) // 2]))
            new_stones.append(int(str_stone[len(str_stone) // 2 :]))
        else:
            new_stones.append(stone * 2024)

    stones = list(new_stones)

print(len(stones))
