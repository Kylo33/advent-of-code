# This is my original solution for Part 1. It takes roughly 11 minutes to run LOL

from collections import defaultdict
from queue import Queue

DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def main():
    with open("input") as f:
        grid = [list(l) for l in f.read().strip().split("\n")]
        start_pos = [(x, y) for y, line in enumerate(grid) for x, ch in enumerate(line) if ch == 'S'][0]
        end_pos = [(x, y) for y, line in enumerate(grid) for x, ch in enumerate(line) if ch == 'E'][0]

    print(f"Part 1: {part1(grid, start_pos, end_pos)}")


def part1(grid, start_pos, end_pos):
    no_cheat_cost = get_cost(grid, start_pos, end_pos)
    saves = defaultdict(int)
    for y, line in enumerate(grid):
        for x, ch in enumerate(line):
            if ch == "#":
                cost_without = get_cost([l if y != ay else [*l[:x], '.', *l[x + 1:]] for ay, l in enumerate(grid)], start_pos, end_pos)
                saves[no_cheat_cost - cost_without] += 1
            print(x, y)

    return sum(val for key, val in saves.items() if key >= 100)


def get_cost(grid, start_pos, end_pos):
    seen = set()
    q = Queue()
    q.put((start_pos, 0))
    while not q.empty():
        pos, cost = q.get()
        x, y = pos
        if (x, y) in seen:
            continue
        seen.add((x, y))
        if (x, y) == end_pos:
            return cost
        neighbors = [(x + dx, y + dy) for dx, dy in DELTAS if 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid)]
        for neighbor_x, neighbor_y in neighbors:
            if grid[neighbor_y][neighbor_x] != '#':
                q.put(((neighbor_x, neighbor_y), cost + 1))


if __name__ == '__main__':
    main()