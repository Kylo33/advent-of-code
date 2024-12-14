import re
from collections import defaultdict
from functools import reduce
from queue import Queue

WIDTH, HEIGHT = 101, 103
DELTAS = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if not (dx == 0 and dy == 0)]


def main():
    with open("input") as f:
        robots = defaultdict(list)
        for l in f.read().strip().split("\n"):
            m = re.fullmatch(r"p=(?P<px>\d+),(?P<py>\d+) v=(?P<vx>-?\d+),(?P<vy>-?\d+)", l)
            px, py, vx, vy = list(map(int, (m["px"], m["py"], m["vx"], m["vy"])))
            robots[(px, py,)].append((vx, vy,))

    print(f"Part 1: {part1(robots)}")
    print(f"Part 2: {part2(robots)}")


def step(robots):
    r = defaultdict(list)
    for px, py in robots:
        for vx, vy in robots[(px, py)]:
            r[((px + vx) % WIDTH, (py + vy) % HEIGHT)].append((vx, vy,))
    return r


def part1(robots):
    quadrants = [0 for _ in range(4)]
    for _ in range(100):
        robots = step(robots)
    for px, py in robots:
        robot_count = len(robots[(px, py)])

        pos_y = py < HEIGHT // 2
        neg_y = py > HEIGHT // 2
        neg_x = px < WIDTH // 2
        pos_x = px > WIDTH // 2

        if pos_y:
            if neg_x:
                quadrants[0] += robot_count
            elif pos_x:
                quadrants[1] += robot_count
        elif neg_y:
            if neg_x:
                quadrants[2] += robot_count
            elif pos_x:
                quadrants[3] += robot_count

    return reduce(lambda x, y: x * y, quadrants)


def part2(robots): # px, py, vx, vy
    largest_blob = 0
    steps = 0
    while True:
        # BFS robots to find largest blob
        seen = set()
        for robot in robots:
            x, y = robot
            q = Queue()
            q.put(robot)
            blob_size = 0
            while not q.empty():
                r = q.get()
                if r in seen:
                    continue
                blob_size += 1
                seen.add(r)
                neighbors = {(r[0] + dx, r[1] + dy) for dx, dy in DELTAS if 0 <= r[0] + dx < WIDTH and 0 <= r[1] + dy < HEIGHT}
                for neighbor in neighbors & robots.keys():
                    q.put(neighbor)

            largest_blob = max(largest_blob, blob_size)

        if largest_blob > 40:
            break

        # Move the robots
        robots = step(robots)
        steps += 1

    # Write robots to a file
    lines = ["".join(['#' if (x, y) in robots else '.' for x in range(WIDTH)]) + "\n" for y in range(HEIGHT)]
    with open("output", "w") as of:
        of.writelines(lines)

    return steps


if __name__ == "__main__":
    main()