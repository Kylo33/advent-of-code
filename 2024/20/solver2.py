from collections import defaultdict
from queue import Queue

DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def solve(max_dist):
    portals = get_portals(max_dist)
    from_end = costs_from(end_pos)
    from_start = costs_from(start_pos)

    count = 0
    for first_portal, second_portal, cost in portals:
        path_cost = from_start[first_portal] + cost + from_end[second_portal]
        if from_start[end_pos] - path_cost >= 100:
            count += 1
    return count


def get_portals(max_cost): # Can exit a wall and then re-enter 🤦
    portals = []
    found_portals = defaultdict(set)
    for sx, sy in paths:
        q = Queue()
        q.put(((sx, sy), 0))
        seen = set()

        while not q.empty():
            pos, cost = q.get()
            if pos in seen:
                continue
            seen.add(pos)
            x, y = pos

            for dx, dy in DELTAS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < len(ls[0]) and 0 <= ny < len(ls)):
                    continue

                if cost + 1 <= max_cost:
                    q.put(((nx, ny), cost + 1))
                    if (nx, ny) not in walls and (nx, ny) not in found_portals[(sx, sy)]:
                        found_portals[(sx, sy)].add((nx, ny))
                        portals.append(((sx, sy), (nx, ny), cost + 1))
                
    return portals


def costs_from(start):
    dist = 0
    costs = {start: dist}
    cursor = start
    while True:
        x, y = cursor
        try:
            cursor_opts = [(x + dx, y + dy) for dx, dy in DELTAS if (x + dx, y + dy) not in walls and (x + dx, y + dy) not in costs]
            cursor = cursor_opts[0]
        except IndexError:
            return costs
        dist += 1
        costs[cursor] = dist
    

if __name__ == '__main__':
    with open("input") as f:
        ls = f.read().strip().split("\n")
        walls = {(x, y) for y, line in enumerate(ls) for x, ch in enumerate(line) if ch == '#'}
        paths = {(x, y) for y, line in enumerate(ls) for x, ch in enumerate(line) if ch != '#'}
        start_pos = [(x, y) for y, line in enumerate(ls) for x, ch in enumerate(line) if ch == 'S'][0]
        end_pos = [(x, y) for y, line in enumerate(ls) for x, ch in enumerate(line) if ch == 'E'][0]
    print(f"Part 1: {solve(2)}")
    print(f"Part 2: {solve(20)}")