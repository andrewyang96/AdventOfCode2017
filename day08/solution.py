from collections import defaultdict
from typing import DefaultDict
from typing import List
from typing import Tuple

compare_funcs = {
    '==': lambda registers, lhs_register, rhs: registers[lhs_register] == rhs,
    '!=': lambda registers, lhs_register, rhs: registers[lhs_register] != rhs,
    '>': lambda registers, lhs_register, rhs: registers[lhs_register] > rhs,
    '<': lambda registers, lhs_register, rhs: registers[lhs_register] < rhs,
    '>=': lambda registers, lhs_register, rhs: registers[lhs_register] >= rhs,
    '<=': lambda registers, lhs_register, rhs: registers[lhs_register] <= rhs
}

modify_funcs = {
    'inc': lambda x, y: x + y,
    'dec': lambda x, y: x - y
}


def largest_value(instructions: List[Tuple]) -> int:
    registers = defaultdict(int)
    for register, instruction, number, lhs_register, comp, rhs in instructions:
        if compare_funcs[comp](registers, lhs_register, rhs):
            registers[register] = modify_funcs[instruction](registers[register], number)
    return max(registers.values())

def largest_value2(instructions: List[Tuple]) -> int:
    registers = defaultdict(int)
    highest_ever = 0
    for register, instruction, number, lhs_register, comp, rhs in instructions:
        if compare_funcs[comp](registers, lhs_register, rhs):
            registers[register] = modify_funcs[instruction](registers[register], number)
        highest_ever = max(highest_ever, max(registers.values()))
    return highest_ever
