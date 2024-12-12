from itertools import chain

DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def main():
    with open("test_input") as f:
        farm = [list(line) for line in f.read().strip().split("\n")]
        regions = get_regions(farm)

    total = 0
    for region in regions:
        area = len(region)
        perimeter = 0
        for x, y in region:
            neighbors = {(x + dx, y + dy,) for dx, dy in DELTAS}
            perimeter += len(neighbors - region)

        total += area * perimeter

    print("Part 1:", total)


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
    neighbors = [(x + dx, y + dy) for dx, dy in DELTAS if in_farm(farm, x, y, dx, dy)]
    return {(x, y)} | set(chain.from_iterable([traverse(nx, ny, farm, visited) for nx, ny in neighbors if farm[y][x] == farm[ny][nx]]))


def in_farm(farm, x, y, dx, dy):
    return 0 <= y + dy < len(farm) and 0 <= x + dx < len(farm[0])


if __name__ == "__main__":
    main()