"""
LeetCode 34: Find First and Last Position of Element in Sorted Array
Difficulty: Medium
Pattern: Binary Search
Video Reference: https://www.youtube.com/watch?v=4sQL7R5ySUU
Complexity:
    - Time: O(log n)
    - Space: O(1)
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(value: int) -> int:
            # The returned index may equal the array length.
            left = 0
            right = len(nums)
            # Find the first index whose value is at least the requested bound.
            while left < right:
                middle = (left + right) // 2
                if nums[middle] < value:
                    left = middle + 1
                else:
                    right = middle
                # The lower-bound invariant remains a half-open candidate range.
            return left

        first = lower_bound(target)
        # Every matching index is at or after this first candidate.
        # If the first bound is not target, no matching range exists.
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        # The next value's lower bound lies just beyond the target's last copy.
        after_last = lower_bound(target + 1)
        # Integer values make target plus one the next distinct boundary.
        # Both searches are logarithmic and use constant auxiliary storage.
        return [first, after_last - 1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert solution.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert solution.searchRange([], 0) == [-1, -1]
    assert solution.searchRange([2], 2) == [0, 0]
    print("All tests passed")
