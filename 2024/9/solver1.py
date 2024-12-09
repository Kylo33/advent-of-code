# Part 1

with open('input') as f:
    ns = list(map(int, list(f.read().strip())))

disk = [(-1 if i % 2 == 1 else int(i/2)) for i, n in enumerate(ns) for _ in range(n)]

front_cur, back_cur = 0, len(disk) - 1

while front_cur < back_cur:
    if disk[back_cur] != -1:
        while disk[front_cur] != -1:
            front_cur += 1
        if not front_cur < back_cur:
            break
        disk[front_cur] = disk[back_cur]
        disk[back_cur] = -1
    back_cur -= 1

print(sum([nstr * i for i, nstr in enumerate(disk) if nstr != -1]))