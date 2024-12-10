from typing import Tuple, Set

with open("input") as f:
    grid = [list(map(int, l)) for l in f.read().strip().split("\n")]
    grid_height = len(grid)
    grid_width = len(grid[0])

trailheads = [(x, y) for y, row in enumerate(grid) for x, n in enumerate(row) if n == 0]

def count_trails(head: Tuple[int, int]):
    x, y = head
    if grid[y][x] == 9:
        return 1
    ds = ((1, 0), (-1, 0), (0, 1), (0, -1))
    neighbors = [(x + dx, y + dy) for dx, dy in ds if 0 <= x + dx < grid_width and 0 <= y + dy < grid_height]
    steadily_increasing_neighbors = [neighbor for neighbor in neighbors if grid[neighbor[1]][neighbor[0]] == grid[y][x] + 1]
    return sum(count_trails(neighbor) for neighbor in steadily_increasing_neighbors)

score_sum = 0
for trailhead in trailheads:
    score_sum += count_trails(trailhead)

print(score_sum)