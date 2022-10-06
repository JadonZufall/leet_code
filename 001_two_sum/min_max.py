"""

The solution is slower then the sort_nums solution but saves more memory
Runtime: 136ms,
Memory: 14.8mb, Beats 99.55 %
"""
from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    min_val = min(nums)
    max_val = max(nums)
    for index, value in enumerate(nums):
        other = target - value
        if min_val < other > max_val:
            continue
        for j, v in enumerate(nums):
            if j == index or v != other:
                continue
            return [index, j]
