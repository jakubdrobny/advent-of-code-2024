import sys

inp = ""

for line in sys.stdin:
    inp += line.strip("\n")

# we don't care about the last free space
if len(inp) % 2 == 0:
    inp = inp[:-1]

cur_disk_pos = 0


def block_start(block):
    return block[0]


def block_length(block):
    return block[1]


file_blocks = []
free_blocks = []

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

    cur_block = [cur_disk_pos, size]
    if free_block:
        free_blocks.append(cur_block)
    else:
        file_blocks.append(cur_block)

    cur_disk_pos += size

file_blocks_idx = len(file_blocks) - 1

while file_blocks_idx > 0:
    cur_file_block = file_blocks[file_blocks_idx]
    free_block_idx = 0
    while free_block_idx < len(free_blocks) and block_start(
        free_blocks[free_block_idx]
    ) < block_start(cur_file_block):
        if block_length(free_blocks[free_block_idx]) >= block_length(cur_file_block):
            free_block_pos = block_start(free_blocks[free_block_idx])
            cur_block_pos = block_start(cur_file_block)
            for b in range(block_length(cur_file_block)):
                disk[free_block_pos], disk[cur_block_pos] = (
                    disk[cur_block_pos],
                    disk[free_block_pos],
                )
                free_block_pos += 1
                cur_block_pos += 1

            # delete free block from free blocks, if no space left
            if disk[free_block_pos] != ".":
                free_blocks = (
                    free_blocks[:free_block_idx] + free_blocks[free_block_idx + 1 :]
                )
            else:
                free_blocks[free_block_idx] = [
                    free_block_pos,
                    block_length(free_blocks[free_block_idx])
                    - block_length(cur_file_block),
                ]

            break

        free_block_idx += 1

    file_blocks_idx -= 1

checksum = 0
for pos, chr in enumerate(disk):
    if chr == ".":
        continue

    checksum += pos * int(chr)

print(checksum)
