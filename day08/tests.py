from solution import largest_value
from solution import largest_value2

def process_line(line):
    register, instruction, number, _, lhs_register, comp, rhs = line.strip().split()
    number = int(number)
    rhs = int(rhs)
    return (register, instruction, number, lhs_register, comp, rhs)

with open('test_input.txt', 'r') as f:
    test_instructions = []
    for line in f:
        test_instructions.append(process_line(line))

with open('input.txt', 'r') as f:
    instructions = []
    for line in f:
        instructions.append(process_line(line))

assert largest_value(test_instructions) == 1
print(largest_value(instructions))

assert largest_value2(test_instructions) == 10
print(largest_value2(instructions))
