from collections import defaultdict
from typing import Dict, Tuple, List, Set
from itertools import combinations

def part1():
    antinodes: Set[Tuple[int, int]] = set()

    for freq in frequencies:
        for node_a, node_b in combinations(frequencies[freq], 2):
            dx, dy = node_b[0] - node_a[0], node_b[1] - node_a[1]
            antinodes.add((node_b[0] + dx, node_b[1] + dy,))
            antinodes.add((node_a[0] - dx, node_a[1] - dy,))

    on_grid = lambda an: 0 <= an[1] < len(grid) and 0 <= an[0] < len(grid[0])
    return len(list(filter(on_grid, antinodes)))

def part2():
    antinodes: Set[Tuple[int, int]] = set()
    on_grid = lambda xi, yi: 0 <= yi < len(grid) and 0 <= xi < len(grid[0])

    for freq in frequencies:
        for node_a, node_b in combinations(frequencies[freq], 2):
            dx, dy = node_b[0] - node_a[0], node_b[1] - node_a[1]
            x, y = node_b[0], node_b[1]
            while on_grid(x, y):
                antinodes.add((x, y))
                x += dx
                y += dy

            x, y = node_a[0], node_a[1]
            while on_grid(x, y):
                antinodes.add((x, y))
                x -= dx
                y -= dy

    return len(antinodes)

if __name__ == '__main__':
    with open("input") as f:
        grid = f.read().strip().split("\n")

    frequencies: Dict[str, List[Tuple[int, int]]] = defaultdict(list)
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char != ".":
                frequencies[char].append((x, y,))
    print("☃️ Advent of Code - Dec 8, 2024 ☃️")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")