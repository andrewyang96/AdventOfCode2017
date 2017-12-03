import itertools
import math
from typing import Iterator

def spiral(num: int) -> int:
    level = round(math.sqrt(num - 1) / 2)
    if level == 0:
        return 0
    min_nums_at_level = [(2 * level - 1) ** 2 + level + 2 * i * level for i in range(4)]
    return min(map(lambda n: abs(n - num), min_nums_at_level)) + level

# Taken from https://www.reddit.com/r/adventofcode/comments/7h7ufl/2017_day_3_solutions/dqox0fv/
# No code was necessary... https://oeis.org/A141481

def spiral2(num: int) -> int:
    def compute_square(grid: dict, i: int, j: int) -> int:
        return sum(grid.get((k, l), 0) for k in range(i-1, i+2) for l in range(j-1, j+2))

    def sum_spiral() -> Iterator[int]:
        grid = {(0, 0): 1}
        i, j = 0, 0
        for s in itertools.count(1, 2):
            for _ in range(s):
                i += 1
                grid[i, j] = compute_square(grid, i, j)
                yield grid[i, j]
            for _ in range(s):
                j -= 1
                grid[i, j] = compute_square(grid, i, j)
                yield grid[i, j]
            for _ in range(s+1):
                i -= 1
                grid[i, j] = compute_square(grid, i, j)
                yield grid[i, j]
            for _ in range(s+1):
                j += 1
                grid[i, j] = compute_square(grid, i, j)
                yield grid[i, j]

    for x in sum_spiral():
        if x > num:
            return x
    raise RuntimeError()
