from solution import get_letters
from solution import get_num_steps

def process_file(f):
    return [list(char for char in line.strip('\n')[:-1]) for line in f]

with open('test_input.txt', 'r') as f:
    test_grid = process_file(f)

with open('input.txt', 'r') as f:
    grid = process_file(f)

assert get_letters(test_grid) == 'ABCDEF'
print(get_letters(grid))

assert get_num_steps(test_grid) == 38
print(get_num_steps(grid))
