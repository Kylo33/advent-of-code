from heapq import heappop, heappush

WIDTH, HEIGHT = 71, 71
DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def main():
    with open("input") as f:
        pos_bytes = [(int(line.split(",")[0]), int(line.split(",")[1])) for line in f.read().strip().split("\n")]

    print(f"Part 1: {a_star_search(pos_bytes)[1]}")
    print(f"Part 2: {part2(pos_bytes)}")


def a_star_search(pos_bytes, count=1024):
    pos_bytes = set(pos_bytes[:count])
    start = (0, 0)
    end = (WIDTH - 1, HEIGHT - 1)

    h = lambda ax, ay: abs(end[0] - ax) + abs(end[1] - ay)

    q = [(0 + h(start[0], start[1]), (start, 0, set()))]
    seen = set()

    while len(q) > 0:
        cost, node = heappop(q)
        pos, dist, path = node

        if pos in seen:
            continue
        seen.add(pos)

        if pos == end:
            return node

        x, y = pos
        neighbors = [(x + dx, y + dy) for dx, dy in DELTAS]
        for nx, ny in neighbors:
            if (not (nx, ny) in pos_bytes) and 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
                heappush(q, (h(nx, ny) + dist + 1, ((nx, ny), dist + 1, path | {pos})))

    return None

def part2(pos_bytes):
    path = a_star_search(pos_bytes, count=1)[2]
    for i, pos in enumerate(pos_bytes, start=1):
        if pos in path:
            node = a_star_search(pos_bytes, count=(i + 1))
            if node is None:
                return ",".join(map(str, pos))
            path = node[2]

if __name__ == "__main__":
    main()