import re

with open("input") as f:
    t = f.read().strip()

def part1(inp = t):
    ns = re.findall(r"mul\((\d+),(\d+)\)", inp)
    total = sum([int(x) * int(y) for x, y in ns])
    return total

def part2(inp = t):
    cs = re.findall(r"(don't\(\)|do\(\)|mul\(\d+,\d+\))", inp)
    ns = []
    do = True
    for c in cs:
        if c == "don't()":
            do = False
        elif c == "do()":
            do = True
        elif do:
            ns.append(map(int, re.match(r"mul\((\d+),(\d+)\)", c).groups()))
    total = sum([int(x) * int(y) for x, y in ns])
    return total

if __name__ == "__main__":
    print(part2())
