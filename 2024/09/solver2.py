# Part 2

import heapq

with open('input') as f:
    ns = list(map(int, list(f.read().strip())))

idx = 0
block_lengths = [] #[0] is the item, [1] is the length, and [2] is the starting index
for i, n in enumerate(ns):
    block_lengths.append([i // 2 if i % 2 == 0 else -1, n, idx])
    idx += n

files = [b for b in block_lengths if b[0] != -1]
empty_blocks = [b for b in block_lengths if b[0] == -1]

empty_block_heapqs = ([], [], [], [], [], [], [], [], [], []) # 0-9 heapqs that hold empty blocks of that size

for block in empty_blocks:
    length, start_index = block[1], block[2]
    heapq.heappush(empty_block_heapqs[length], (start_index, block))

# for each file, backwards
for file in files[::-1]:
#     # find the first empty block with enough space, to the right of the original block
    try:
        possible_heapqs = [i for i in range(file[1], len(empty_block_heapqs)) if len(empty_block_heapqs[i]) > 0 and empty_block_heapqs[i][0][1][2] < file[2]]
        if len(possible_heapqs) == 0:
            continue
        best_heapq = min(possible_heapqs, key=lambda i: empty_block_heapqs[i][0])
        first_empty_block = heapq.heappop(empty_block_heapqs[best_heapq])[1]
    except IndexError:
        continue

    # edit the file's starting index
    file[2] = first_empty_block[2]

    # then, edit empty block length and increment its starting index by that length
    first_empty_block[1] -= file[1]
    first_empty_block[2] += file[1]

    heapq.heappush(empty_block_heapqs[first_empty_block[1]], (first_empty_block[2], first_empty_block))

print(sum(file[0] * (file[2] + i) for file in files for i in range(file[1])))
