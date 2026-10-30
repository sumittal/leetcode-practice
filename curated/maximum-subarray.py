from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # The nonempty-array constraint allows a real element as the initial candidate.
        # Starting from nums[0] preserves the best answer when all values are negative.
        ending = best = nums[0]
        # Each scan step either extends the prior ending range or restarts at value.
        # ending is constrained to ranges that include the current index.
        for value in nums[1:]:
            # Only contiguous ranges ending at this value need to be compared.
            # Restart if extending the old range is worse than starting at this value.
            ending = max(value, ending + value)
            # The global best may end earlier than this position.
            best = max(best, ending)
        # best may represent an earlier endpoint than the final scan position.
        return best


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert solution.maxSubArray([1]) == 1
    assert solution.maxSubArray([5, 4, -1, 7, 8]) == 23
    assert solution.maxSubArray([-3, -1, -2]) == -1
    print("All tests passed")
