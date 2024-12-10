import math
from typing import List, TypedDict
from itertools import product
from enum import Enum

class Operation(Enum):
    ADD = 1
    MULTIPLY = 2
    CONCAT = 3

class Equations(TypedDict):
    ans: int
    nums: List[int]

def eq_is_valid(eq: Equations, operations: List[Operation]):
    ops_options = product(operations, repeat=len(eq["nums"]) - 1)
    for ops in ops_options:
        total = eq["nums"][0]
        if ops[-1] == Operation.MULTIPLY and eq["ans"] % eq["nums"][-1] != 0:
            continue
        if ops[-1] == Operation.CONCAT and not str(eq["ans"]).endswith(str(eq["nums"][-1])):
            continue

        for number, operator in zip(eq["nums"][1:], ops):
            if operator == Operation.ADD:
                total += number
            elif operator == Operation.MULTIPLY:
                total *= number
            elif operator == Operation.CONCAT:
                total = total * 10 ** (int(math.log10(number)) + 1) + number

        if total == eq["ans"]:
            return True
    return False

def part1():
    return sum([eq["ans"] for eq in eqs if eq_is_valid(eq, operations=[Operation.ADD, Operation.MULTIPLY])])

def part2():
    return sum([eq["ans"] for eq in eqs if eq_is_valid(eq, operations=[Operation.ADD, Operation.MULTIPLY, Operation.CONCAT])])

if __name__ == '__main__':
    with open("input") as f:
        ls = [l.split(": ") for l in f.read().strip().split("\n")]
        eqs: List[Equations] = [{
            "ans": int(l[0]),
            "nums": list(map(int, l[1].split(" ")))
        } for l in ls]
    print("⛄️ Advent of Code - Dec 7, 2024 ⛄️")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
