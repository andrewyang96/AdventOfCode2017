
from typing import List

def jumps(nums: List[int]) -> int:
    idx = 0
    steps = 0
    while idx < len(nums):
        nums[idx] += 1
        idx += nums[idx] - 1
        steps += 1
    return steps

def jumps2(nums: List[int]) -> int:
    idx = 0
    steps = 0
    while idx < len(nums):
        if nums[idx] >= 3:
            nums[idx] -= 1
            idx += nums[idx] + 1
        else:
            nums[idx] += 1
            idx += nums[idx] - 1
        steps += 1
    return steps
