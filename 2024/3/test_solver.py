from solver import part1, part2

def test_part1():
    assert part1("mul(4,3)") == 12
    assert part1("mul(44,3)") == 132
    assert part1("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))") == 161

def test_part2():
    assert part2("mul(4,3)") == 12
    assert part2("don't()asmul(4,3)") == 0
    assert part2("don't()do()mul(5,10)") == 50
    assert part2("do()mul(3,6)") == 18