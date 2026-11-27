"""
LeetCode 416: Partition Equal Subset Sum
Difficulty: Medium
Pattern: 1-D Dynamic Programming
Video Reference: https://www.youtube.com/watch?v=IsvocB5BJhw
Complexity:
    - Time: O(n * target)
    - Space: O(target)
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            # An odd total cannot be split into two equal integer sums.
            return False
        target = total // 2
        # reachable[s] means a subset of processed values can sum to s.
        reachable = [False] * (target + 1)
        reachable[0] = True
        # Each input value is a distinct 0/1 choice, even when values repeat.
        for value in nums:
            # Descending totals prevent this item from being used a second time.
            for subtotal in range(target, value - 1, -1):
                # A sum is reachable already or by adding value to a prior sum.
                reachable[subtotal] = (
                    reachable[subtotal] or reachable[subtotal - value]
                )
            # The one-dimensional table is the space-optimized form of 2-D subset DP.
            if reachable[target]:
                # No later number can invalidate an already found subset.
                return True
        # If the target was never reached, no equal partition exists.
        return reachable[target]


if __name__ == "__main__":
    solution = Solution()
    assert solution.canPartition([1, 5, 11, 5]) is True
    assert solution.canPartition([1, 2, 3, 5]) is False
    assert solution.canPartition([1, 2, 5]) is False
    assert solution.canPartition([2, 2]) is True
    print("All tests passed")
