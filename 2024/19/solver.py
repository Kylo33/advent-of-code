from functools import cache

def main():
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

    
def part1():
    return len([design for design in designs if count_possible(design) > 0])


def part2():
    return sum(count_possible(design) for design in designs)


@cache
def get_possible_patterns(design):
    return [design[:i] for i in range(1, len(design) + 1) if design[:i] in patterns]


@cache
def count_possible(design: str):
    if not design:
        return 1

    return sum([count_possible(design[len(pattern):]) for pattern in get_possible_patterns(design)])


if __name__ == "__main__":
    with open("input") as f:
        raw = f.read().strip().split("\n\n")
        patterns = set(raw[0].split(", "))
        designs = raw[1].split("\n")
    main()