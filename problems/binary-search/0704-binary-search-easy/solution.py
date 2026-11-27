"""
LeetCode 704: Binary Search
Difficulty: Easy
Pattern: Binary Search
Video Reference: https://www.youtube.com/watch?v=s4DPM8ct1pI
Complexity:
    - Time: O(log n)
    - Space: O(1)
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # The inclusive interval contains every index that may still match target.
        left = 0
        right = len(nums) - 1
        # An empty array starts with right below left and skips the loop.
        # The midpoint is safe because left and right are valid array bounds.
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                # The midpoint is already the required zero-based array index.
                return middle
            if nums[middle] < target:
                # Sorted order rules out the midpoint and everything to its left.
                left = middle + 1
            else:
                # Values at the midpoint and to its right are too large.
                right = middle - 1
            # Each branch strictly shrinks the candidate interval.
        # An empty candidate interval proves that target is absent.
        return -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert solution.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert solution.search([-1, 0, 3, 5, 9, 12], -1) == 0
    assert solution.search([5], 5) == 0
    assert solution.search([], 0) == -1
    print("All tests passed")
