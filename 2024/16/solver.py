import heapq
import json

DELTAS = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0)
}

BIG_NUMBER = 1000000000000


def main():
    with open("input") as f:
        maze = f.read().strip().split("\n")
        start = find_char("S", maze)
        end = find_char("E", maze)

    p1_ans = part1(maze, start, end, "E")
    p2_ans = part2(maze, start, end, "E", p1_ans)
    print(f"Part 1: {p1_ans}")
    print(f"Part 2: {p2_ans}")


def find_char(char, maze):
    return [(x, y) for y, line in enumerate(maze) for x, ch in enumerate(line) if ch == char][0]


def get_new_directions(direction):
    ds = ["N", "E", "S", "W"]
    idx = ds.index(direction)
    return ds[(idx - 1) % 4], ds[(idx + 1) % 4]


def shortest_paths(maze, start, dxn, to=None):
    costs = [[(-1, "") for _ in range(len(maze[0]))] for _ in range(len(maze))]
    priority_queue = []
    x, y = start
    costs[y][x] = (0, dxn)
    dx, dy = DELTAS[dxn]

    straight_ahead = (x + dx, y + dy)
    if not maze[straight_ahead[1]][straight_ahead[0]] == '#':
        heapq.heappush(priority_queue, (1, (straight_ahead, dxn)))

    for new_dxn in get_new_directions(dxn):
        new_dx, new_dy = DELTAS[new_dxn]
        new_x, new_y = x + new_dx, y + new_dy
        if not maze[new_y][new_x] == '#':
            heapq.heappush(priority_queue, (1001, ((new_x, new_y), new_dxn)))

    seen = {(x, y)}
    while len(priority_queue) > 0:
        cost, pos_info = heapq.heappop(priority_queue)
        node, dxn = pos_info
        if node in seen:
            continue
        seen.add(node)
        x, y = node
        costs[y][x] = cost, dxn

        if (x, y) == to:
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

    if to is not None:
        return BIG_NUMBER
    
    return costs


def part1(maze, start, end, starting_dxn):
    return shortest_paths(maze, start, starting_dxn, to=end)

def part2(maze, start, end, starting_dxn, p1_ans):
    costs = shortest_paths(maze, start, starting_dxn)

    through_best_path = {start, end}
    for y, line in enumerate(costs):
        for x, cost_info in enumerate(line):
            cost, starting_dxn = cost_info
            if cost == -1 or (x, y) == end:
                continue
            if cost + shortest_paths(maze, (x, y), starting_dxn, to=end) == p1_ans:
                through_best_path.add((x, y))
    
    return len(through_best_path)
            

if __name__ == "__main__":
    main()