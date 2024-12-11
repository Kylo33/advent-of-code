from math import log10


def main():
    with open("input") as f:
        stones = list(map(int, f.read().strip().split(" ")))
    
    for _ in range(25):
        stones = blink(stones)
    
    print(len(stones))


def blink(stones):
    new_stones = []

    for stone in stones:
        if stone == 0:
            new_stones.append(1)
            continue

        lst = int(log10(stone)) + 1
        elst = 10 ** lst

        if lst % 2 == 0:
            halves = stone // elst, stone % elst
            new_stones.extend(halves)
        else:
            new_stones.append(stone * 2024)

    return new_stones


if __name__ == "__main__":
    main()