"""
LeetCode 918: Maximum Sum Circular Subarray
Difficulty: Medium
Pattern: Greedy
Video Reference: https://www.youtube.com/watch?v=fxT9KjakYPM
Complexity:
    - Time: O(n)
    - Space: O(1)
"""

from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Nonempty input guarantees valid initial Kadane states.
        # Maximum Kadane state covers a non-wrapping segment.
        max_ending = max_total = nums[0]
        # Minimum Kadane state identifies the segment omitted by a wrap.
        min_ending = min_total = nums[0]
        total = nums[0]
        for value in nums[1:]:
            # Extend the current segment or begin a new one at this value.
            max_ending = max(value, max_ending + value)
            max_total = max(max_total, max_ending)
            min_ending = min(value, min_ending + value)
            min_total = min(min_total, min_ending)
            total += value
            # Both extrema end at the current position after this update.
            # The prefix total supports the complementary circular segment.
        # If every value is negative, total - min_total would be an empty choice.
        if max_total < 0:
            return max_total
        # The optimum is either ordinary or the complement of the minimum segment.
        return max(max_total, total - min_total)


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxSubarraySumCircular([1, -2, 3, -2]) == 3
    assert solution.maxSubarraySumCircular([5, -3, 5]) == 10
    assert solution.maxSubarraySumCircular([-3, -2, -3]) == -2
    assert solution.maxSubarraySumCircular([7]) == 7
    print("All tests passed")
