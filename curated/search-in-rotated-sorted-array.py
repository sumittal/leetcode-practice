from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Keep an inclusive interval containing every index that may hold target.
        left = 0
        right = len(nums) - 1
        # The <= bound still examines a final single candidate when left == right.
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                # Return the original array index as soon as the target is found.
                return middle

            if nums[left] <= nums[middle]:
                # The left half is sorted; keep it only when target is within its bounds.
                if nums[left] <= target < nums[middle]:
                    # The midpoint was checked, so the remaining left range ends before it.
                    right = middle - 1
                else:
                    # Target is outside the sorted left range; discard that half.
                    left = middle + 1
            else:
                # Otherwise the right half is sorted and can be bounded the same way.
                if nums[middle] < target <= nums[right]:
                    # Keep the sorted right range, excluding the already-checked midpoint.
                    left = middle + 1
                else:
                    # Target is outside the sorted right range; discard that half.
                    right = middle - 1
        # An empty interval means no index in the array contains target.
        return -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert solution.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert solution.search([1], 0) == -1
    assert solution.search([1], 1) == 0
    assert solution.search([3, 1], 1) == 1
    assert solution.search([], 5) == -1
    print("All tests passed")
