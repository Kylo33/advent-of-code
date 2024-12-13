import re

def main():
    with open("input") as f:
        bs = f.read().strip().split("\n\n")
        machines = []
        for b in bs:
            m = re.match(r"Button A: X\+(?P<ax>\d+), Y\+(?P<ay>\d+)\n"
                             r"Button B: X\+(?P<bx>\d+), Y\+(?P<by>\d+)\n"
                             r"Prize: X=(?P<px>\d+), Y=(?P<py>\d+)", b)
            machines.append({
                "a": (int(m.group("ax")), int(m.group("ay"))),
                "b": (int(m.group("bx")), int(m.group("by"))),
                "prize": (int(m.group("px")), int(m.group("py"))),
            })

    print("Part 1:", solve(machines))
    print("Part 2:", solve(machines, add_to_prize=10000000000000))

def solve(machines, add_to_prize=0):
    tokens = 0
    for machine in machines:
        ax, ay = machine["a"]
        bx, by = machine["b"]
        px, py = machine["prize"][0] + add_to_prize, machine["prize"][1] + add_to_prize

        b_pushes = round((py - ay*px/ax)/(by-ay*bx/ax))
        a_pushes = round((px - bx*b_pushes)/ax)

        if a_pushes * ax + b_pushes * bx == px and a_pushes * ay + b_pushes * by == py:
            tokens += 3 * round(a_pushes) + round(b_pushes)

    return tokens


if __name__ == "__main__":
    main()