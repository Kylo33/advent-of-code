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
    if cursor not in boxes and (cursor[0] - 1, cursor[1]) not in boxes: # We hit an empty space, it can move
        return
    if delta[1] == 0:
        move_boxes(boxes, walls, (cursor[0] + delta[0], cursor[1]), delta)
        if cursor in boxes:
            boxes.remove(cursor)
            boxes.add((cursor[0] + delta[0], cursor[1]))
        return
    moving_box = cursor if cursor in boxes else (cursor[0] - 1, cursor[1])
    move_boxes(boxes, walls, (moving_box[0], moving_box[1] + delta[1]), delta)
    move_boxes(boxes, walls, (moving_box[0] + 1, moving_box[1] + delta[1]), delta)
    boxes.remove(moving_box)
    boxes.add((moving_box[0], moving_box[1] + delta[1]))


def can_move(boxes, walls, cursor, delta):
    if cursor in walls:
        return False
    left_cursor = (cursor[0] - 1, cursor[1])
    if cursor not in boxes and left_cursor not in boxes:
        return True
    box_inside = cursor if cursor in boxes else left_cursor

    if delta[1] == 0:
        return can_move(boxes, walls, (cursor[0] + delta[0], cursor[1]), delta)

    box_inside_right = (box_inside[0] + 1, box_inside[1])
    return can_move(boxes, walls, (box_inside[0], box_inside[1] + delta[1]), delta) and can_move(boxes, walls, (box_inside_right[0], box_inside_right[1] + delta[1]), delta)


def print_grid(boxes, walls, robot):
    for y in range(7):
        for x in range(14):
            print("#" if (x, y) in walls else "[" if (x, y) in boxes else "]" if (x - 1, y) in boxes else "@" if (x, y) == robot else ".", end="")
        print()


def part1(boxes, walls, robot, instructions):
    boxes = {(box[0] * 2, box[1]) for box in boxes}
    walls = {(wall[0] * 2, wall[1]) for wall in walls} | {(wall[0] * 2 + 1, wall[1]) for wall in walls}
    robot = (robot[0] * 2, robot[1])
    for instruction in instructions:
        delta = move(instruction)
        new_robot_pos = (robot[0] + delta[0], robot[1] + delta[1])
        if can_move(boxes, walls, new_robot_pos, delta):
            # print("Can move")
            move_boxes(boxes, walls, new_robot_pos, delta)
            robot = new_robot_pos
            # print_grid(boxes, walls, robot)

    return sum(map(lambda b: b[1] * 100 + b[0], boxes))


if __name__ == "__main__":
    main()