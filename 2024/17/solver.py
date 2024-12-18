import re

def main():
    with open("input") as f:
        matches = re.fullmatch(r"Register A: (?P<a>\d+)\nRegister B: (?P<b>\d+)\nRegister C: (?P<c>\d+)\n\nProgram: (?P<prog>[\d,]+)", f.read().strip())
        register_a, register_b, register_c = tuple(map(int, (matches["a"], matches["b"], matches["c"])))
        program = list(map(int, matches["prog"].split(",")))

    print(",".join(map(str, part1(register_a, register_b, register_c, program))))
    print(part2(program))


def combo(operand, register_a, register_b, register_c):
    match operand:
        case operand if 0 <= operand <= 3:
            return operand
        case 4:
            return register_a
        case 5:
            return register_b
        case 6:
            return register_c


def part1(register_a, register_b, register_c, program):
    output = []

    instruction_pointer = 0
    while 0 <= instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]

        if opcode == 0:
            # adv
            register_a = register_a >> combo(operand, register_a, register_b, register_c)
        elif opcode == 1:
            # bxl
            register_b = register_b ^ operand
        elif opcode == 2:
            # bst
            register_b = combo(operand, register_a, register_b, register_c) % 8
        elif opcode == 3:
            # jnz
            if register_a != 0:
                instruction_pointer = operand
                continue
        elif opcode == 4:
            # bxc
            register_b = register_b ^ register_c
        elif opcode == 5:
            # out
            output.append(combo(operand, register_a, register_b, register_c) % 8)
        elif opcode == 6:
            # adv
            register_b = register_a >> combo(operand, register_a, register_b, register_c)
        elif opcode == 7:
            # cdv
            register_c = register_a >> combo(operand, register_a, register_b, register_c)

        instruction_pointer += 2

    return output

def part2(program):
    solutions = []
    solve(program, solutions)
    return min(solutions)


def solve(program, solutions, a = 0):
    if len(program) == 0:
        solutions.append(a)
        return

    for bits in range(8):
        b = bits ^ 2
        c = ((a << 3) + bits) >> b
        b = b ^ c
        b = b ^ 7
        if b % 8 == program[-1]:
            solve(program[:-1], solutions, (a << 3) + bits)


if __name__ == "__main__":
    main()