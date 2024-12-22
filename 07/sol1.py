import sys

ans = 0

for line in sys.stdin:
    line = line.strip("\n").split(": ")
    tg, nums = int(line[0]), list(map(int, line[1].split()))

    op_cnt = len(nums) - 1
    for mask in range(1 << op_cnt):
        cur = nums[0]
        for bit in range(op_cnt):
            if mask >> bit & 1:
                cur += nums[bit + 1]
            else:
                cur *= nums[bit + 1]
        if cur == tg:
            ans += cur
            break

print(ans)
