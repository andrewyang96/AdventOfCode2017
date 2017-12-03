from solution import checksum
from solution import checksum2

assert checksum([
    [5, 1, 9, 5],
    [7, 5, 3],
    [2, 4, 6, 8]
]) == 18

with open('input.txt', 'r') as f:
    spreadsheet = [[int(num) for num in row.split()] for row in f]
print(checksum(spreadsheet))

assert checksum2([
    [5, 9, 2, 8],
    [9, 4, 7, 3],
    [3, 8, 6, 5]
]) == 9

print(checksum2(spreadsheet))
