from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # The one-house circle has no competing endpoint to exclude.
        if len(nums) == 1:
            return nums[0]

        def linear(values: List[int]) -> int:
            # The slice excludes one circle endpoint; the usual adjacent-house DP applies.
            # Empty slices are safe because both rolling totals start at zero.
            # This helper applies the linear recurrence to a non-circular slice.
            prev2 = prev1 = 0
            for value in values:
                # Keep the best of skipping this house or taking it after prev2.
                prev2, prev1 = prev1, max(prev1, prev2 + value)
            return prev1

        # Excluding either endpoint breaks the circular adjacency into a line.
        # These two ranges cover every legal choice without allowing both endpoints.
        # Comparing both slices covers every legal set of robbed houses.
        return max(linear(nums[:-1]), linear(nums[1:]))


if __name__ == "__main__":
    solution = Solution()
    assert solution.rob([2, 3, 2]) == 3
    assert solution.rob([1, 2, 3, 1]) == 4
    assert solution.rob([1, 2, 3]) == 3
    assert solution.rob([7]) == 7
    print("All tests passed")
