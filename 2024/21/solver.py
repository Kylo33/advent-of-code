from queue import Queue


DOOR_KEYPAD = (
    "789",
    "456",
    "123",
    " 0A",
)

ROBOT_KEYPAD = (
    " ^A",
    "<v>",
)

DELTAS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

DELTA_TO_DIR = {
    (1, 0): ">",
    (-1, 0): "<",
    (0, 1): "v",
    (0, -1): "^"
}


def main():
    with open("input") as f:
        door_codes = f.read().strip().split("\n")
    
    print(f"Part 1: {part1(door_codes)}")


def part1(door_codes):
    s = 0
    for door_code in door_codes[:1]:
        first_robot_directions = first_robot(door_code)
        # second_robot_directions = second_robot(first_robot_directions)
        # third_robot_directions = third_robot(second_robot_directions)
        # s += len(third_robot_directions) * int(door_code[:3])
    
    return s


def first_robot(door_code):
    pos = get_initial_pos(DOOR_KEYPAD)
    directions = []
    for ch in door_code:
        new_directions, pos = bfs_keypad(DOOR_KEYPAD, pos, ch)
        directions.extend(new_directions)
    
    return directions

  
def bfs_keypad(keypad, initial_pos, goal):
    directions = ["A"]
    parents = {}
    q = Queue()
    q.put(initial_pos)
    seen = set()

    while not q.empty():
        pos = q.get()
        if pos in seen:
            continue
        seen.add(pos)

        x, y = pos
        if keypad[y][x] == goal:
            break

        for n_pos in [(x + dx, y + dy) for dx, dy in DELTAS if 0 <= x + dx < len(keypad[0]) and 0 <= y + dy < len(keypad) and keypad[y + dy][x + dx] != ' ']:
            q.put(n_pos)
            if n_pos not in parents and n_pos not in seen:
                parents[n_pos] = pos

    cursor = pos
    while cursor in parents:
        d = cursor[0] - parents[cursor][0], cursor[1] - parents[cursor][1]
        directions.append(DELTA_TO_DIR[d])
        cursor = parents[cursor]
    directions.reverse()
    return directions, pos


def third_robot(second_robot_directions):
    pos = get_initial_pos(ROBOT_KEYPAD)
    directions = []
    for direction in second_robot_directions:
        new_directions, pos = bfs_keypad(ROBOT_KEYPAD, pos, direction)
        directions.extend(new_directions)
    
    return directions


def get_initial_pos(keypad):
    poss = [(x, y) for y, line in enumerate(keypad) for x, ch in enumerate(line) if ch == 'A']
    return poss[0]


if __name__ == "__main__":
    main()