"""
Brute force method of solving this problem, this fails one of the test cases as it takes to long,
so I am going to have to find a better method of solving this problem.

With this solution we would have to iterate over each element for each element meaning the time is
O(N^2) so there is a better solution.
"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i, a in enumerate(nums):
        for j, b in enumerate(nums):
            if i == j:
                continue
            elif a + b == target:
                return [i, j]
