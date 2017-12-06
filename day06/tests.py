from solution import reallocate
from solution import reallocate2

with open('input.txt', 'r') as f:
    l = [int(n) for n in f.readline().split()]

assert reallocate([0, 2, 7, 0]) == 5
print(reallocate(l))

assert reallocate2([0, 2, 7, 0]) == 4
print(reallocate2(l))
