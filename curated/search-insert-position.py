from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        # Searching a half-open range also supports insertion at the end.
        right = len(nums)
        # The half-open interval narrows toward the lower-bound insertion point.
        while left < right:
            middle = (left + right) // 2
            # Sorted order makes each midpoint comparison decisive.
            # Values below target cannot be the first valid position.
            if nums[middle] < target:
                left = middle + 1
            else:
                # Keep middle so an equal value can be returned as its first index.
                right = middle
            # The discarded half cannot contain the lower bound.
        # left may equal len(nums) when target exceeds every element.
        # The lower bound is also the insertion position for a missing target.
        return left


if __name__ == "__main__":
    solution = Solution()
    assert solution.searchInsert([1, 3, 5, 6], 5) == 2
    assert solution.searchInsert([1, 3, 5, 6], 2) == 1
    assert solution.searchInsert([1, 3, 5, 6], 7) == 4
    assert solution.searchInsert([1, 3, 5, 6], 0) == 0
    assert solution.searchInsert([], 1) == 0
    print("All tests passed")
