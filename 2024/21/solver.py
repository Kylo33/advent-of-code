from itertools import product


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

DIRECTIONS = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}


def main():
    with open("input") as f:
        door_codes = f.read().strip().split("\n")

    print(f"Part 1: {part1(door_codes)}")


def part1(door_codes):
    s = 0
    for door_code in door_codes[2:3]:
        first_robot_directions = first_robot(door_code)
        print(first_robot_directions)
        second_robot_directions = second_robot(first_robot_directions)

    return s


def first_robot(door_code):
    x, y = (2, 3)
    directions = []
    for ch in door_code:
        dxn = []
        ch_x, ch_y = [
            (x, y)
            for y, line in enumerate(DOOR_KEYPAD)
            for x, c in enumerate(line)
            if c == ch
        ][0]
        dxn.append(("v" if ch_y - y > 0 else "^") * abs(ch_y - y))
        dxn.append((">" if ch_x - x > 0 else "<") * abs(ch_x - x))
        directions.append(dxn)
        x, y = ch_x, ch_y

    return directions


def second_robot(first_robot_directions):
    reversed_combos = product([True, False], repeat=len(first_robot_directions))
    combos = [
        [
            (
                list(reversed(first_robot_directions[i]))
                if is_reversed
                else first_robot_directions[i]
            )
            for i, is_reversed in enumerate(reversed_combo)
        ]
        for reversed_combo in reversed_combos
    ]


if __name__ == "__main__":
    main()
