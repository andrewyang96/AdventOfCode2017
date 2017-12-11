from solution import hex_grid
from solution import hex_grid2

with open('input.txt', 'r') as f:
    steps = [s for s in f.readline().strip().split(',')]

assert hex_grid(['ne', 'ne', 'ne']) == 3
assert hex_grid(['ne', 'ne', 'sw', 'sw']) == 0
assert hex_grid(['ne', 'ne', 's', 's']) == 2
assert hex_grid(['se', 'sw', 'se', 'sw', 'sw']) == 3

print(hex_grid(steps))
print(hex_grid2(steps))
