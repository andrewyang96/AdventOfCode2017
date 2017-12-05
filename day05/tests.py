from solution import jumps
from solution import jumps2

with open('input.txt', 'r') as f:
    nums = [int(n) for n in f]

assert jumps([0, 3, 0, 1, -3]) == 5
print(jumps(nums[:]))

assert jumps2([0, 3, 0, 1, -3]) == 10
print(jumps2(nums[:]))
