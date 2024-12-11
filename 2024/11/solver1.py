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
        elif len(str(stone)) % 2 == 0:
            halves = str(stone)[:len(str(stone)) // 2], str(stone)[len(str(stone)) // 2:]
            new_stones.extend(map(int, halves))
        else:
            new_stones.append(stone * 2024)

    return new_stones


if __name__ == "__main__":
    main()