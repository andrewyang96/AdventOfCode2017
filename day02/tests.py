from solution import checksum

assert checksum([
    [5, 1, 9, 5],
    [7, 5, 3],
    [2, 4, 6, 8]
]) == 18

with open('input.txt', 'r') as f:
    spreadsheet = [[int(num) for num in row.split()] for row in f]
print(checksum(spreadsheet))
