from solution import group_score
from solution import count_canceled_chars

with open('input.txt') as f:
    stream = f.readline().strip()

assert group_score('{}') == 1
assert group_score('{{{}}}') == 6
assert group_score('{{},{}}') == 5
assert group_score('{{{},{},{{}}}}') == 16
assert group_score('{<a>,<a>,<a>,<a>}') == 1
assert group_score('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
assert group_score('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9
assert group_score('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3

print(group_score(stream))

assert count_canceled_chars('<>') == 0
assert count_canceled_chars('<random characters>') == 17
assert count_canceled_chars('<<<<>') == 3
assert count_canceled_chars('<{!>}>') == 2
assert count_canceled_chars('<!!>') == 0
assert count_canceled_chars('<!!!>>') == 0
assert count_canceled_chars('<{o"i!a,<{i<a>') == 10

print(count_canceled_chars(stream))
