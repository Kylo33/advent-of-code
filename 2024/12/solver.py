from enum import Enum
from typing import Tuple, List, Set


class Side(Enum):
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    LEFT = 4

    @classmethod
    def is_vertical(cls, side):
        return side == Side.TOP or side == Side.BOTTOM


DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))
SIDES = (Side.RIGHT, Side.LEFT, Side.BOTTOM, Side.TOP)


def main():
    with open("input") as f:
        farm = [list(line) for line in f.read().strip().split("\n")]
        regions: List[Set[Tuple[int, int]]] = get_regions(farm)

    print(f"Part 1: {part1(regions)}")
    print(f"Part 2: {part2(regions)}")


def part1(regions: List[Set[Tuple[int, int]]]) -> int:
    total = 0
    for region in regions:
        area = len(region)
        perimeter = 0
        for x, y in region:
            neighbors = {
                (
                    x + dx,
                    y + dy,
                )
                for dx, dy in DELTAS
            }
            perimeter += len(neighbors - region)

        total += area * perimeter
    return total


def part2(regions: List[Set[Tuple[int, int]]]) -> int:
    total = 0
    for region in regions:
        area = len(region)
        fences: Set[Tuple[int, int, Side]] = set()  # (x, y, side)
        for x, y in region:
            fences |= {
                (x, y, side)
                for side, dx, dy in zip(SIDES, *zip(*DELTAS))
                if (x + dx, y + dy) not in region
            }

        sides = 0
        for x, y, side in fences:
            if Side.is_vertical(side):
                if (x + 1, y, side) in fences:
                    continue
            elif (x, y + 1, side) in fences:
                continue
            sides += 1

        total += area * sides
    return total


def get_regions(farm: List[List[str]]) -> List[Set[Tuple[int, int]]]:
    regions: List[Set[Tuple[int, int]]] = []
    visited: Set[Tuple[int, int]] = set()

    for y, line in enumerate(farm):
        for x, plant in enumerate(line):
            if (
                x,
                y,
            ) not in visited:
                region: Set[Tuple[int, int]] = set()
                traverse(x, y, farm, visited, region)
                regions.append(region)

    return regions


def traverse(
    x: int,
    y: int,
    farm: List[List[str]],
    visited: Set[Tuple[int, int]],
    region: Set[Tuple[int, int]],
):
    if (x, y) in visited:
        return
    visited.add((x, y))
    region.add((x, y))

    neighbors = (
        (x + dx, y + dy)
        for dx, dy in DELTAS
        if 0 <= y + dy < len(farm) and 0 <= x + dx < len(farm[0])
    )

    for nx, ny in neighbors:
        if farm[y][x] == farm[ny][nx]:
            traverse(nx, ny, farm, visited, region)


if __name__ == "__main__":
    main()
