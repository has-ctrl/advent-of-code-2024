import re
from get_day_input import get_input

registers, program = get_input(day=17).split("\n\n")
registers = [int(d) for d in re.findall(r"\d+", registers)]
program = [int(d) for d in re.findall(r"\d+", program)]


def one() -> str:
    """
    Using the information provided by the debugger, initialize the registers to the given values, then run the program.
    Once it halts, what do you get if you use commas to join the values it output into a single string?
    """
    pointer = 0
    out = []
    while pointer < len(program) - 1:
        opcode, literal_operand = program[pointer], program[pointer + 1]
        combo_operand = registers[literal_operand - 4] if literal_operand in (4, 5, 6) else literal_operand
        match opcode:
            case 0:
                registers[0] = int(registers[0] / 2 ** combo_operand)
            case 1:
                registers[1] = registers[1] ^ literal_operand
            case 2:
                registers[1] = combo_operand % 8
            case 3:
                if registers[0] != 0:
                    pointer = literal_operand
                    continue
            case 4:
                registers[1] = registers[1] ^ registers[2]
            case 5:
                out.append(combo_operand % 8)
            case 6:
                registers[1] = int(registers[0] / 2 ** combo_operand)
            case 7:
                registers[2] = int(registers[0] / 2 ** combo_operand)
        pointer += 2
    return ",".join([str(i) for i in out])


def two() -> int:
    """
    """
    return 0


print(f"1. {one()}")
print(f"2. {two()}")
