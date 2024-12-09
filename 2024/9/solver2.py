# Part 2

from itertools import groupby

with open('input') as f:
    ns = list(map(int, list(f.read().strip())))

disk = [(-1 if i % 2 == 1 else int(i/2)) for i, n in enumerate(ns) for _ in range(n)]

idx = 0
block_lengths = [] #[0] is the item, [1] is the length, and [2] is the starting index
for key, group in groupby(disk):
    l = len(list(group))
    block_lengths.append([key, l, idx])
    idx += l

files = [b for b in block_lengths if b[0] != -1]
empty_blocks = [b for b in block_lengths if b[0] == -1]

# for each file, backwards
for file in files[::-1]:
    # find the first empty block with enough space, to the right of the original block
    try:
        first_empty_block = [b for b in empty_blocks if b[1] >= file[1]][0]
        if first_empty_block[2] > file[2]:
            continue
    except IndexError:
        continue

    # edit the file's starting index
    file[2] = first_empty_block[2]

    # then, edit empty block length and increment its starting index by that length (length will go to 0 eventually)
    first_empty_block[1] -= file[1]
    first_empty_block[2] += file[1]

# finally, populate an array with the files at their starting index. fill everything else with -1s
new_disk = [-1] * len(disk)
for file in files:
    for i in range(file[1]):
        new_disk[file[2] + i] = file[0]

# print the checksum
print(sum([n * i for i, n in enumerate(new_disk) if n != -1]))
