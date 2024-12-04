import re
from typing import List

DUMMY_CHAR = "P"

with open('input') as f:
    it: str = f.read().strip()

def count_lines(lines: List[str]):
    return sum([len(re.findall("XMAS", line)) + len(re.findall("SAMX", line)) for line in lines])

def part1(t: str = it) -> int:
    horizontal: int = count_lines(t.split("\n"))
    vertical: int = count_lines(["".join(x) for x in zip(*t.split("\n"))])
    diagonal_right: int = count_lines(["".join(x) for x in zip(*[s[len(s)-i:] + "P" + s[:len(s) - i] for i, s in enumerate(t.split("\n"))])])
    diagonal_left: int = count_lines(["".join(x) for x in zip(*[s[i:] + "P" + s[:i] for i, s in enumerate(t.split("\n"))])])

    return horizontal + vertical + diagonal_left + diagonal_right

def part2(t: str = it) -> int:
    ls = t.split("\n")
    return sum([len([c for ci, c in enumerate(l) if 0 < ci < len(l) - 1 and all([w in {"SAM", "MAS"} for w in [f"{ls[li - 1][ci - 1]}{c}{ls[li + 1][ci + 1]}", f"{ls[li + 1][ci - 1]}{c}{ls[li - 1][ci + 1]}"]])]) for li, l in enumerate(ls) if 0 < li < len(ls) - 1])

if __name__ == "__main__":
    print(part2())
