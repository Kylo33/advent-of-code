from solver import part1, part2

def test_part1_horizontal():
    assert part1("XMAS") == 1
    assert part1("SAMX") == 1
    assert part1("MMMAMXMASMM") == 1
    assert part1("MMSAMXMM") == 1

def test_part1_vertical():
    assert part1("X\nM\nA\nS") == 1
    assert part1("S\nA\nM\nX") == 1

def test_part1_diagonal():
    assert part1("XMMM\nMMMM\nMMAM\nMMMS") == 1
    assert part1("SMMM\n"
                 "AAAA\n"
                 "SSMS\n"
                 "SSSX\n") == 1

def test_part1_combined():
    assert part1("""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""") == 18

def test_part2_combined():
    assert part2("""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""") == 9