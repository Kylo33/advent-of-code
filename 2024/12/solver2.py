from itertools import chain
from enum import Enum

class Side(Enum):
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    LEFT = 4


DELTAS = {
    Side.TOP: (0, -1),
    Side.BOTTOM: (0, 1),
    Side.RIGHT: (1, 0),
    Side.LEFT: (-1, 0),
}

def main():
    with open("input") as f:
        farm = [list(line) for line in f.read().strip().split("\n")]
        regions = get_regions(farm)

    part1 = 0
    part2 = 0
    for region in regions:
        area = len(region)
        fences = set() # set of (x, y, side)
        for x, y in region:
            fences |= {(x, y, side) for side, deltas in DELTAS.items() if (x + deltas[0], y + deltas[1]) not in region}

        sides = 0
        for x, y, side in fences:
            if (side == Side.TOP or side == Side.BOTTOM) and (x + 1, y, side) in fences:
                if (x + 1, y, side) in fences:
                    continue
            else:
                if (x, y + 1, side) in fences:
                    continue
            sides += 1

        part1 += area * len(fences)
        part2 += area * sides

    print("Part 1:", part1)
    print("Part 2:", part2)


def get_regions(farm):
    regions = []
    visited = set()
    for y, line in enumerate(farm):
        for x, plant in enumerate(line):
            if (x, y,) not in visited:
                regions.append(traverse(x, y, farm, visited))
    return regions


def traverse(x, y, farm, visited):
    if (x, y) in visited:
        return set()
    visited.add((x, y))
    neighbors = [(x + deltas[0], y + deltas[1]) for _, deltas in DELTAS.items() if in_farm(farm, x, y, *deltas)]
    return {(x, y)} | set(chain.from_iterable([traverse(nx, ny, farm, visited) for nx, ny in neighbors if farm[y][x] == farm[ny][nx]]))


def in_farm(farm, x, y, dx, dy):
    return 0 <= y + dy < len(farm) and 0 <= x + dx < len(farm[0])


if __name__ == "__main__":
    main()