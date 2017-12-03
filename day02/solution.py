import itertools
from typing import List

def checksum(spreadsheet: List[List[int]]) -> int:
    return sum(map(lambda row: max(row) - min(row), spreadsheet))

def checksum2(spreadsheet: List[List[int]]) -> int:
    def process_row(row: List[int]) -> int:
        for x, y in itertools.combinations(row, 2):
            if x > y and x % y == 0:
                return x // y
            elif x < y and y % x == 0:
                return y // x
        raise RuntimeError()
    return sum(map(process_row, spreadsheet))
