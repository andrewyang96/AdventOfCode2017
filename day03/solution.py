import math

def spiral(num: int) -> int:
    level = round(math.sqrt(num - 1) / 2)
    if level == 0:
        return 0
    min_nums_at_level = [(2 * level - 1) ** 2 + level + 2 * i * level for i in range(4)]
    return min(map(lambda n: abs(n - num), min_nums_at_level)) + level
