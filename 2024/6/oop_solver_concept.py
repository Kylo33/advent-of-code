from typing import List, Tuple, Dict
from enum import Enum


class Action(Enum):
    MOVED = 2
    TURNED = 1
    ESCAPED = 0


class Area:
    _data: List[str]
    initial_guard_position: Tuple[int, int] | None

    def __init__(self, data: List[str]):
        self._data = data
        initial_guard_position = None
        for c_y, row in enumerate(area):
            found = False
            for c_x, char in enumerate(row):
                if char == "^":
                    initial_guard_position = c_x, c_y
                    found = True
                    break
            if found:
                break
        if initial_guard_position is None:
            raise ValueError("No guard found in area")

    def __iter__(self):
        self._row = 0
        return self

    def __next__(self):
        try:
            result = self._data[self._row]
        except IndexError:
            raise StopIteration
        self._row += 1
        return result

    def get(self, x: int, y: int):
        if y < 0 or x < 0:
            raise IndexError
        return self._data[y][x]

    def set(self, x: int, y: int, char: str):
        if len(char) != 1:
            raise ValueError("char must have length 1")
        self._data[y] = self._data[y][:x] + char + self._data[y][x + 1 :]

    def __str__(self):
        return "\n".join(self._data)

    def with_obstacle_at(self, x, y):
        row_copy = self._data[y][:x] + "#" + self._data[y][x + 1 :]
        return [*self._data[:y], row_copy, *self._data[y + 1 :]]


class Guard:
    dx, dy = 0, -1

    def __init__(self, area: Area, initial_guard_position: Tuple[int, int] = None):
        self._area = area
        self.x, self.y = (
            initial_guard_position
            if initial_guard_position
            else area.initial_guard_position
        )

    """
    Advances this guard or turns if there is an obstacle.
    :return this guard remains in the Area
    """

    def move(self) -> Action:
        nx, ny = self.x + self.dx, self.y + self.dy
        try:
            if self._area.get(nx, ny) == "#":
                self._turn_right()
                return Action.TURNED
            else:
                self.x, self.y = nx, ny
                return Action.MOVED
        except IndexError:
            return Action.ESCAPED

    def _turn_right(self):
        self.dx, self.dy = -self.dy, self.dx

    @property
    def pos(self) -> Tuple[int, int]:
        return self.x, self.y


def part1(area: Area):
    guard = Guard(area)
    area.set(*guard.pos, "X")
    while guard.move():
        area.set(*guard.pos, "X")

    return sum([line.count("X") for line in area])


def part2(area):
    initial_guard_position = area.initial_guard_position
    areas: List[Area] = [
        area.with_obstacle_at(x, y)
        for y, line in enumerate(area)
        for x, char in enumerate(line)
        if char == "X" and (x, y) != area.initial_guard_position
    ]
    for area in areas:
        collision_record: Dict[] = {}
        guard = Guard(area, initial_guard_position=initial_guard_position)



if __name__ == "__main__":
    with open("input") as input_file:
        area = Area(input_file.read().strip().split("\n"))

    print("❄️ Advent of Code - Dec 6, 2024 ❄️")
    print(f"Part 1: {part1(area)}")
    print(f"Part 2: {part2(area)}")
