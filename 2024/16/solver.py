import heapq
from enum import Enum

DELTAS = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0)
}


def main():
    with open("input") as f:
        maze = f.read().strip().split("\n")
        start = find_char("S", maze), "E"
        end = find_char("E", maze)

    p1 = part1(maze, start)
    print(f"Part 1: {p1}")
    print(f"Part 2: {part2(maze, start, p1)}")


def find_char(char, maze):
    return [(x, y) for y, line in enumerate(maze) for x, ch in enumerate(line) if ch == char][0]


def get_new_directions(direction):
    ds = ["N", "E", "S", "W"]
    idx = ds.index(direction)
    return ds[(idx - 1) % 4], ds[(idx + 1) % 4]


def part1(maze, start):
    priority_queue = []
    reindeer, dxn = start

    direction = DELTAS[dxn]
    straight_ahead = (reindeer[0] + direction[0], reindeer[1] + direction[1])
    if not maze[straight_ahead[1]][straight_ahead[0]] == '#':
        heapq.heappush(priority_queue, (1, (straight_ahead, dxn)))

    for new_dxn in get_new_directions(dxn):
        new_direction = DELTAS[new_dxn]
        ahead = (reindeer[0] + new_direction[0], reindeer[1] + new_direction[1])
        if not maze[ahead[1]][ahead[0]] == '#':
            heapq.heappush(priority_queue, (1001, (ahead, new_dxn)))

    seen = {reindeer}
    while len(priority_queue) > 0:
        cost, pos_info = heapq.heappop(priority_queue)
        node, dxn = pos_info
        if node in seen:
            continue
        seen.add(node)
        x, y = node
        if maze[y][x] == "E":
            return cost

        possible_next_nodes = []
        straight_ahead = (x + DELTAS[dxn][0], y + DELTAS[dxn][1])
        possible_next_nodes.append((cost + 1, (straight_ahead, dxn)))
        for new_dxn in get_new_directions(dxn):
            new_direction = DELTAS[new_dxn]
            ahead = (x + new_direction[0], y + new_direction[1])
            possible_next_nodes.append((cost + 1001, (ahead, new_dxn)))

        for next_node in filter(lambda n: maze[n[1][0][1]][n[1][0][0]] != '#', possible_next_nodes):
            heapq.heappush(priority_queue, next_node)

    return -1



def part2(maze, start, p1):
    tiles = set()
    reindeer, dxn = start

    return len(tiles)


if __name__ == "__main__":
    main()