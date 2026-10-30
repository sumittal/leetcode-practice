from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # The inclusive search interval always contains the minimum element.
        left = 0
        right = len(nums) - 1
        # Stop at one candidate; using left < right keeps middle+1 in bounds.
        while left < right:
            middle = (left + right) // 2
            # A midpoint above the right edge lies in the pre-pivot range.
            if nums[middle] > nums[right]:
                # The pivot and minimum must be strictly after this midpoint.
                left = middle + 1
            else:
                # Keep middle: it may itself be the minimum.
                right = middle
        # The converged index is the minimum, including the unrotated case.
        return nums[left]


if __name__ == "__main__":
    solution = Solution()
    assert solution.findMin([3, 4, 5, 1, 2]) == 1
    assert solution.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert solution.findMin([11, 13, 15, 17]) == 11
    assert solution.findMin([1]) == 1
    assert solution.findMin([3, 1, 2]) == 1
    print("All tests passed")
