import sys

inp = ""

for line in sys.stdin:
    inp += line.strip("\n")

# we don't care about the last free space
if len(inp) % 2 == 0:
    inp = inp[:-1]

cnt_free = []
cur_free = 0
cur_disk_pos = 0

block_starts = []

disk = []
id = 0
for idx, space in enumerate(inp):
    free_block = idx % 2 == 1
    if free_block:
        id += 1

    chr = "." if free_block else str(id)
    size = int(space)
    for it in range(size):
        disk.append(chr)

    block_starts.append(cur_disk_pos)
    cur_disk_pos += size

    if free_block:
        cur_free += size

free_idx = block_starts[1]
last_file_disk_idx = cur_disk_pos - 1

while free_idx < last_file_disk_idx:
    while disk[free_idx] != ".":
        free_idx += 1
    while disk[last_file_disk_idx] == ".":
        last_file_disk_idx -= 1

    if free_idx >= last_file_disk_idx:
        break

    disk[free_idx], disk[last_file_disk_idx] = disk[last_file_disk_idx], disk[free_idx]
    free_idx += 1
    last_file_disk_idx -= 1

checksum = 0
for pos, chr in enumerate(disk):
    if chr == ".":
        break

    checksum += pos * int(chr)

print(checksum)
