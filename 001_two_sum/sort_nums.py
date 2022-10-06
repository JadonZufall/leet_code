"""
This method requires more space but only has to iterate over the list once after sorting.  We start out by
creating a copy of the list and then sorting it.  We then declare pointers one starting at the beginning of
the list and one starting at the end this is basically getting the min and max values.  Then we see if the
values add up to the target number and if they don't we check if the result is greater then or less then
the target value and we increment the relevant pointer.  Then we have to search back through the original
list and find the original indexes of the values, there is probably a better way to implement this without
having to use extra memory.

This solution is in O(n log n) in the worst case situation I believe.
Runtime 61ms, Beats 96.66% of submissions.
Memory 15.1mb, Beats 65.90% of submissions.
"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    sorted_nums = nums.copy()
    sorted_nums.sort()
    p1 = 0
    p2 = len(nums) - 1
    while True:
        val = sorted_nums[p1] + sorted_nums[p2]
        if val == target:
            num1, num2 = sorted_nums[p1], sorted_nums[p2]
            r1, r2 = None, None
            for index, i in enumerate(nums):
                if i == num1 and r1 is None:
                    r1 = index
                elif i == num2 and r2 is None:
                    r2 = index
            return [r1, r2]
        elif val < target:
            p1 += 1
        elif val > target:
            p2 -= 1

