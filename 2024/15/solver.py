def main():
    with open("input") as f:
        ls = f.read().strip().split("\n\n")
        instructions, board = ls[1].replace("\n", ""), ls[0].split("\n")
        boxes = get_all_coordinates(board, "O")
        walls = get_all_coordinates(board, "#")
        robot = list(get_all_coordinates(board, "@"))[0]

    print(f"Part 1: {part1(boxes, walls, robot, instructions)}")


def get_all_coordinates(board, symbol):
    return {(x, y) for y, line in enumerate(board) for x, char in enumerate(line) if char == symbol}


def move(instruction):
    dx, dy = 0, 0
    if instruction == "^":
        dy = -1
    elif instruction == "v":
        dy = 1
    elif instruction == ">":
        dx = 1
    elif instruction == "<":
        dx = -1
    else:
        raise Exception("Invalid instruction")

    return dx, dy


def move_boxes(boxes, walls, cursor, delta):
    if cursor in walls: # Can't move
        return False
    elif cursor not in boxes: # We hit an empty space, it can move
        return True

    new_cursor = (cursor[0] + delta[0], cursor[1] + delta[1])
    if move_boxes(boxes, walls, new_cursor, delta):
        boxes.remove(cursor)
        boxes.add(new_cursor)
        return True
    else:
        return False


def part1(boxes, walls, robot, instructions):
    for instruction in instructions:
        delta = move(instruction)
        new_robot_pos = (robot[0] + delta[0], robot[1] + delta[1])
        boxes_moved = move_boxes(boxes, walls, new_robot_pos, delta)
        if boxes_moved:
            robot = new_robot_pos

    return sum(map(lambda b: b[1] * 100 + b[0], boxes))


def part2():
    ...


if __name__ == "__main__":
    main()