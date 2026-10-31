from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        # Distinct adjacent values prevent a flat edge from hiding direction.
        right = len(nums) - 1
        # A rising edge guarantees a peak somewhere to its right.
        while left < right:
            middle = (left + right) // 2
            # Compare only adjacent values; no global peak scan is required.
            # The larger right neighbor lies on a side containing a peak.
            if nums[middle] < nums[middle + 1]:
                left = middle + 1
            else:
                # A descending edge keeps a peak at middle or to its left.
                right = middle
            # Each comparison discards at least half the remaining candidates.
        # At convergence the surviving index is greater than both outside sentinels.
        # The problem guarantees at least one peak in this candidate interval.
        return left


if __name__ == "__main__":
    solution = Solution()
    for values in ([1, 2, 3, 1], [1, 2, 1, 3, 5, 6, 4], [1], [2, 1]):
        peak = solution.findPeakElement(list(values))
        assert values[peak] > (values[peak - 1] if peak else float("-inf"))
        assert values[peak] > (
            values[peak + 1] if peak + 1 < len(values) else float("-inf")
        )
    print("All tests passed")
