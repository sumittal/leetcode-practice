"""
LeetCode 238: Product of Array Except Self
Difficulty: Medium
Pattern: Arrays & Hashing
Video Reference: https://www.youtube.com/watch?v=bNvIQI2wAjk
Complexity:
    - Time: O(n)
    - Space: O(1) extra
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # The output doubles as storage for prefix products and later final answers.
        result = [1] * len(nums)
        # prefix is the product of all values strictly before the current index.
        prefix = 1
        for index, value in enumerate(nums):
            # At this point result[index] contains only the product to its left.
            result[index] = prefix
            # Advance the prefix only after writing it, so nums[index] is excluded.
            prefix *= value

        # suffix will similarly hold the product strictly to the right.
        suffix = 1
        # Reverse traversal combines each stored prefix with its matching suffix.
        for index in range(len(nums) - 1, -1, -1):
            # Multiply in the right-side product without allocating another array.
            result[index] *= suffix
            # Update after combining so the current value is not included in its answer.
            suffix *= nums[index]
        # Zeros need no special case: either running product naturally makes answers zero.
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert solution.productExceptSelf([1]) == [1]
    assert solution.productExceptSelf([2, 0, 0]) == [0, 0, 0]
    assert solution.productExceptSelf([2, 3]) == [3, 2]
    print("All tests passed")
