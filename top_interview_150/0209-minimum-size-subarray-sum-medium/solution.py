"""
LeetCode 209: Minimum Size Subarray Sum
Difficulty: Medium
Pattern: Sliding Window
Video Reference: https://www.youtube.com/watch?v=aYqYMIqZx5s
Complexity:
    - Time: O(n)
    - Space: O(1)
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Positive values make the window sum monotonic as either edge moves.
        # The sentinel is longer than any possible valid array window.
        left = 0
        current_sum = 0
        shortest = len(nums) + 1
        for right, value in enumerate(nums):
            current_sum += value
            # While valid, remove left values to seek a shorter qualifying window.
            while current_sum >= target:
                shortest = min(shortest, right - left + 1)
                current_sum -= nums[left]
                left += 1
            # After shrinking, the window is again below target.
            # Repeating the loop records every valid suffix ending at right.
        # An untouched sentinel means no contiguous subarray reached target.
        # Each index enters and leaves the window at most once.
        # This movement bound gives linear total work despite the nested loop.
        return 0 if shortest == len(nums) + 1 else shortest


if __name__ == "__main__":
    solution = Solution()
    assert solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert solution.minSubArrayLen(4, [1, 4, 4]) == 1
    assert solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert solution.minSubArrayLen(5, [5]) == 1
    print("All tests passed")
