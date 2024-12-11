from math import log10
from functools import cache


def main():
    with open("input") as f:
        stones = list(map(int, f.read().strip().split(" ")))
    
    print("25:", sum(count_stones(stone, 25) for stone in stones))
    print("75:", sum(count_stones(stone, 75) for stone in stones))


@cache
def count_stones(stone: int, blinks: int) -> int:
    if blinks == 0:
        return 1
    
    if stone == 0:
        return count_stones(1, blinks - 1)
    
    digit_count = int(log10(stone)) + 1

    if digit_count % 2 == 0:
        e_digit_count = 10 ** (digit_count // 2)
        fh, sh = stone // e_digit_count, stone % e_digit_count
        return count_stones(fh, blinks - 1) + count_stones(sh, blinks - 1)
    
    return count_stones(stone * 2024, blinks - 1)

if __name__ == "__main__":
    main()