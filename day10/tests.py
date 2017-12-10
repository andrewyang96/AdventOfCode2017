from solution import knot_hash
from solution import knot_hash2

with open('input.txt', 'r') as f:
    input_str = f.readline().strip()
    lens = [int(n) for n in input_str.split(',')]

assert knot_hash(5, [3, 4, 1, 5]) == 12
print(knot_hash(256, lens))

assert knot_hash2('') == 'a2582a3a0e66e6e86e3812dcb672a272'
assert knot_hash2('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
assert knot_hash2('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
assert knot_hash2('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'

print(knot_hash2(input_str))
