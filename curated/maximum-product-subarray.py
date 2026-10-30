from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # A nonempty input is guaranteed, so the first item seeds each ending state.
        # Both extrema begin at the first nonempty subarray.
        maximum = minimum = best = nums[0]
        # Both local extrema describe products that end at the same array position.
        for value in nums[1:]:
            # A negative swaps which prior extreme can become the new maximum.
            if value < 0:
                maximum, minimum = minimum, maximum
            # Keeping both extremes handles sign changes in any future multiplication.
            # Starting anew at value competes with extending either prior product.
            maximum = max(value, maximum * value)
            minimum = min(value, minimum * value)
            # Every contiguous product ending here is represented by one of these bounds.
            # best is global, while both extrema are local to the current endpoint.
            best = max(best, maximum)
        return best


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxProduct([2, 3, -2, 4]) == 6
    assert solution.maxProduct([-2, 0, -1]) == 0
    assert solution.maxProduct([-2, 3, -4]) == 24
    assert solution.maxProduct([-2]) == -2
    print("All tests passed")
