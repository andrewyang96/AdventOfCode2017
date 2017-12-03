from mypy.types import List

def checksum(spreadsheet: List[List[int]]) -> int:
    return sum(map(lambda row: max(row) - min(row), spreadsheet))
