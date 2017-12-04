from solution import valid
from solution import valid2

with open('input.txt', 'r') as f:
    passphrases = [p.split() for p in f]

assert valid(['aa bb cc dd ee'.split()]) == 1
assert valid(['aa bb cc dd aa'.split()]) == 0
assert valid(['aa bb cc dd aaa'.split()]) == 1

print(valid(passphrases))

assert valid2(['abcde fghij'.split()]) == 1
assert valid2(['abcde xyz ecdab'.split()]) == 0
assert valid2(['a ab abc abd abf abj'.split()]) == 1
assert valid2(['iiii oiii ooii oooi oooo'.split()]) == 1
assert valid2(['oiii ioii iioi iiio'.split()]) == 0

print(valid2(passphrases))
