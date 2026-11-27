"""
LeetCode 494: Target Sum
Difficulty: Medium
Pattern: 2-D Dynamic Programming
Video Reference: https://www.youtube.com/watch?v=g0npyaQtAQM
Complexity:
    - Time: O(n * total)
    - Space: O(total)
"""

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        combined = total + target
        if abs(target) > total or combined % 2:
            # The signed-sum equation requires an in-range target and matching parity.
            return 0
        subset_target = combined // 2
        # dp[s] counts subsets of processed numbers whose sum is s.
        ways = [0] * (subset_target + 1)
        # The empty subset is the single way to make zero before reading numbers.
        ways[0] = 1
        # A positive-sign subset of this sum determines all remaining negative signs.
        for value in nums:
            # Descending sums preserve 0/1 use of each input position.
            for subtotal in range(subset_target, value - 1, -1):
                # Each old subset can omit value or include it exactly once.
                ways[subtotal] += ways[subtotal - value]
            # A zero value doubles all states because its two sign choices differ.
        # The reduction counts assignments even when multiple positions share a value.
        return ways[subset_target]


if __name__ == "__main__":
    solution = Solution()
    assert solution.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
    assert solution.findTargetSumWays([1], 1) == 1
    assert solution.findTargetSumWays([1], 2) == 0
    assert solution.findTargetSumWays([0, 0, 1], 1) == 4
    print("All tests passed")
