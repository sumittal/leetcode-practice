from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # This patience-sorting summary gives O(n log n) time without storing a full DP.
        # Tails are increasing and store the smallest ending value for each length.
        tails = []
        # There is one smallest ending value for every achievable subsequence length.
        for value in nums:
            # Replace the first tail >= value; equal values do not extend a strict sequence.
            index = bisect_left(tails, value)
            # bisect_left preserves strict increase by replacing equal-valued tails.
            # Appending is possible only when value extends every current tail.
            if index == len(tails):
                tails.append(value)
            # A smaller tail improves that length's chance to extend later.
            else:
                # Replacing preserves sorted tails while improving this length's endpoint.
                tails[index] = value
        # tails stores minimum endings by length, not necessarily one actual subsequence.
        return len(tails)


if __name__ == "__main__":
    solution = Solution()
    assert solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert solution.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
    assert solution.lengthOfLIS([]) == 0
    print("All tests passed")
