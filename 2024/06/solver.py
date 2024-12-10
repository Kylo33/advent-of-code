with open("input") as f:
    b = [list(l) for l in f.read().strip().split("\n")]

def print_b(b=b):
    print("\n".join(["".join(l) for l in b]), end="\n\n")

def part1():
    facing = [0, -1] # x offset, y offset. +x is right, +y is down 
    for i, l in enumerate(b):
        for j, c in enumerate(l):
            if c == '^':
                y, x = i, j

    while True:
        b[y][x] = "X"
        nx, ny = x + facing[0], y + facing[1]
        try:
            if b[ny][nx] == "#":
                facing[0], facing[1] = facing[1] * -1, facing[0]
            else:
                x = nx
                y = ny
        except IndexError:
            break
    
    return sum([l.count("X") for l in b])

def part2():
    # Make a copy of the board with one new obstacle in each possible location
    bstr = "\n".join(["".join(l) for l in b])
    abss = [bstr[:i] + "#" + bstr[i + 1:] for i, c in enumerate(bstr) if c not in "^\n"]
    ab = [b for b in [bs.split("\n") for bs in abss]]

    return len(list(filter(guard_loops, ab)))

def guard_loops(b):
    facing = [0, -1] # x offset, y offset. +x is right, +y is down 

    # Find the guard
    for i, l in enumerate(b):
        for j, c in enumerate(l):
            if c == '^':
                y, x = i, j

    t = set()

    while True:
        ps = ",".join(map(str, [x, y, *facing]))
        if ps in t:
            return True
        t.add(ps)

        nx, ny = x + facing[0], y + facing[1]
        if nx < 0 or ny < 0: # Curse you, Python!
            return False

        try:
            if b[ny][nx] == "#":
                facing[0], facing[1] = facing[1] * -1, facing[0]
            else:
                x, y = nx, ny
        except IndexError:
            return False

if __name__ == "__main__":
    print(part1())