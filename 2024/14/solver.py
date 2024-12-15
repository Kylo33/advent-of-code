import re
from collections import defaultdict
from functools import reduce
from queue import Queue

WIDTH, HEIGHT = 101, 103
DELTAS = [
    (dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if not (dx == 0 and dy == 0)
]


def main():
    with open("input") as f:
        robots = defaultdict(list)
        for l in f.read().strip().split("\n"):
            match = re.fullmatch(
                r"p=(?P<px>\d+),(?P<py>\d+) v=(?P<vx>-?\d+),(?P<vy>-?\d+)", l
            )
            pos_x, pos_y, vel_x, vel_y = map(int, match.groups())
            robots[(pos_x, pos_y)].append((vel_x, vel_y))

    print(f"Part 1: {part1(robots)}")
    print(f"Part 2: {part2(robots)}")


def step(robots):
    r = defaultdict(list)
    for px, py in robots:
        for vx, vy in robots[(px, py)]:
            r[((px + vx) % WIDTH, (py + vy) % HEIGHT)].append(
                (
                    vx,
                    vy,
                )
            )
    return r


def part1(robots):
    final_positions = [
        (
            (position[0] + velocity[0] * 100) % WIDTH,
            (position[1] + velocity[1] * 100) % HEIGHT,
        )
        for position, velocities in robots.items()
        for velocity in velocities
    ]

    quadrants = [0 for _ in range(4)]
    for pos_x, pos_y in final_positions:
        if pos_x == WIDTH // 2 or pos_y == HEIGHT // 2:
            continue
        positive_y = pos_y < HEIGHT // 2
        positive_x = pos_x > WIDTH // 2

        if positive_y:
            quadrants[0 if positive_x else 1] += 1
        else:
            quadrants[2 if positive_x else 3] += 1

    return reduce(lambda x, y: x * y, quadrants)


def part2(robots):
    steps = 0
    while True:
        # BFS robots to find largest blob
        seen = set()
        largest_blob = 0
        for starting_robot in robots:
            q = Queue()
            q.put(starting_robot)
            blob_size = 0
            while not q.empty():
                robot = q.get()
                if robot in seen:
                    continue
                blob_size += 1
                seen.add(robot)
                robot_x, robot_y = robot
                neighbors = {
                    (robot_x + dx, robot_y + dy)
                    for dx, dy in DELTAS
                    if 0 <= robot_x + dx < WIDTH and 0 <= robot_y + dy < HEIGHT
                }
                for neighbor in neighbors & robots.keys():
                    q.put(neighbor)
            largest_blob = max(largest_blob, blob_size)

        if largest_blob > 40:
            break

        # Move the robots
        robots = step(robots)
        steps += 1

    # Write robots to a file — manually checked for christmas trees and adjusted the threshold above.
    lines = [
        "".join(["#" if (x, y) in robots else "." for x in range(WIDTH)]) + "\n"
        for y in range(HEIGHT)
    ]
    with open("output", "w") as of:
        of.writelines(lines)

    return steps


if __name__ == "__main__":
    main()
