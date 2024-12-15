MOVES = {
    "^": (0, -1),
    "v": (0, 1),
    ">": (1, 0),
    "<": (-1, 0),
}

def main():
    with open("input") as f:
        lines = f.read().strip().split("\n\n")
        instructions, board = [MOVES[char] for char in lines[1].replace("\n", "")], lines[0].split("\n")
        boxes = get_all_coordinates(board, "O")
        walls = get_all_coordinates(board, "#")
        robot = list(get_all_coordinates(board, "@"))[0]

    print(f"Part 1: {part1(boxes.copy(), walls, robot, instructions)}")
    print(f"Part 2: {part2(boxes, walls, robot, instructions)}")


def get_all_coordinates(board, symbol):
    return {(x, y) for y, line in enumerate(board) for x, char in enumerate(line) if char == symbol}

def gps(boxes):
    return sum(map(lambda b: b[1] * 100 + b[0], boxes))

def part1(boxes, walls, robot, instructions):
    for dx, dy in instructions:
        new_robot_pos = (robot[0] + dx, robot[1] + dy)
        boxes_moved = move_boxes_part1(boxes, walls, new_robot_pos, (dx, dy))
        if boxes_moved:
            robot = new_robot_pos

    return gps(boxes)


def move_boxes_part1(boxes, walls, cursor, delta):
    if cursor in walls:  # Can't move
        return False
    if cursor not in boxes:  # We hit an empty space, it can move
        return True

    new_cursor = (cursor[0] + delta[0], cursor[1] + delta[1])
    if move_boxes_part1(boxes, walls, new_cursor, delta):
        boxes.remove(cursor)
        boxes.add(new_cursor)
        return True
    return False

def print_grid(boxes, walls, robot):
    for y in range(7):
        for x in range(14):
            print("#" if (x, y) in walls else "[" if (x, y) in boxes else "]" if (x - 1, y) in boxes else "@" if (x, y) == robot else ".", end="")
        print()

def part2(boxes, walls, robot, instructions):
    boxes = {(box_x * 2, box_y) for box_x, box_y in boxes}
    walls = {new_wall for wall_x, wall_y in walls for new_wall in [(wall_x * 2, wall_y), (wall_x * 2 + 1, wall_y)]}
    robot = (robot[0] * 2, robot[1])
    for dx, dy in instructions:
        new_robot_pos = (robot[0] + dx, robot[1] + dy)
        if wide_boxes_can_move(boxes, walls, new_robot_pos, (dx, dy)):
            move_wide_boxes(boxes, walls, new_robot_pos, (dx, dy))
            robot = new_robot_pos

    return gps(boxes)


def wide_boxes_can_move(boxes, walls, cursor, delta):
    # If the cursor is in a wall, nothing can move there.
    if cursor in walls:
        return False

    x, y = cursor
    dx, dy = delta

    # If the cursor is not in any box, something definitely can move there.
    box_x, box_y = cursor if cursor in boxes else (x - 1, y)
    if not (box_x, box_y) in boxes:
        return True

    # If we are trying to move horizontally, check if the next box over can move (or the other part of this box)
    if dy == 0:
        return wide_boxes_can_move(boxes, walls, (x + dx, y + dy), delta)

    # If we are trying to move vertically, check that both spots above/below the box can move
    return (wide_boxes_can_move(boxes, walls, (box_x, box_y + dy), delta)
            and wide_boxes_can_move(boxes, walls, (box_x + 1, box_y + dy), delta))


def move_wide_boxes(boxes, walls, cursor, delta):
    cursor_x, cursor_y = cursor
    dx, dy = delta

    # Base case: we are at an empty space and nothing has to happen
    box_x, box_y = cursor if cursor in boxes else (cursor_x - 1, cursor_y)
    if not (box_x, box_y) in boxes:
        return

    # If we are moving horizontally, move everything else, then this box
    if dy == 0:
        move_wide_boxes(boxes, walls, (cursor_x + dx, cursor_y + dy), delta)

        # We could be on the right of a box, so only move the box if we are on the left
        if cursor in boxes:
            boxes.remove(cursor)
            boxes.add((cursor_x + dx, cursor_y + dy))
        return

    # If we are moving vertically, move everything in both tiles in front of the box that's moving
    move_wide_boxes(boxes, walls, (box_x, box_y + dy), delta)
    move_wide_boxes(boxes, walls, (box_x + 1, box_y + dy), delta)

    # Finally, move this box over. If the same box is tried to move twice, it's OK because it will
    # be removed from the set twice (doesn't make a difference) and added to the new set twice in the same
    # position (doesn't make a difference)
    boxes.remove((box_x, box_y))
    boxes.add((box_x, box_y + dy))


if __name__ == "__main__":
    main()