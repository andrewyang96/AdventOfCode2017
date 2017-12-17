from solution import parse_dance_moves
from solution import dance
from solution import dance2

with open('input.txt', 'r') as f:
    dance_moves = parse_dance_moves(f.readline().strip())

test_moves = parse_dance_moves('s1,x3/4,pe/b')

assert ''.join(dance(list('abcde'), test_moves)) == 'baedc'
print(''.join(dance(list('abcdefghijklmnop'), dance_moves)))

assert ''.join(dance2(list('abcde'), test_moves, 2)) == 'ceadb'
print(''.join(dance2(list('abcdefghijklmnop'), dance_moves, 1000000000)))
