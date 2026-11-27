"""
LeetCode 128: Longest Consecutive Sequence
Difficulty: Medium
Pattern: Arrays & Hashing
Video Reference: https://www.youtube.com/watch?v=P6RZZMu_maU
Complexity:
    - Time: O(n)
    - Space: O(n)
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # A set removes duplicates and gives constant-average-time membership checks.
        values = set(nums)
        # Zero is also the correct answer for an empty input.
        longest = 0
        for value in values:
            # A value with a predecessor belongs to a run already counted elsewhere.
            if value - 1 in values:
                continue
            # Only sequence starts enter this expansion, so each run is walked once.
            length = 1
            # Extend while the next consecutive value exists, regardless of input order.
            while value + length in values:
                length += 1
            # Keep the longest complete run seen so far.
            longest = max(longest, length)
        # Return the maximum run length, or zero when the set was empty.
        return longest


if __name__ == "__main__":
    solution = Solution()
    assert solution.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert solution.longestConsecutive([1, 0, 1, 2]) == 3
    assert solution.longestConsecutive([]) == 0
    assert solution.longestConsecutive([-2, -1, 0, 2, 2]) == 3
    print("All tests passed")
