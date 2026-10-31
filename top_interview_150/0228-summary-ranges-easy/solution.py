"""
LeetCode 228: Summary Ranges
Difficulty: Easy
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+228+Summary+Ranges+neetcode
Complexity:
    - Time: O(n)
    - Space: O(n)
"""

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Each scan begins at the first value not used by a previous range.
        # The input's sorted uniqueness guarantees runs never overlap.
        ranges = []
        index = 0
        while index < len(nums):
            start = nums[index]
            end = start
            # Consecutive values extend the current inclusive range.
            while index + 1 < len(nums) and nums[index + 1] == nums[index] + 1:
                index += 1
                end = nums[index]
            # Singletons omit the arrow; longer runs show both endpoints.
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append("%d->%d" % (start, end))
            # Move past the endpoint before searching for another range.
            index += 1
            # Every inner-loop advance consumes one consecutive value.
        # Every input value belongs to exactly one formatted range.
        # The algorithm writes only output strings and leaves nums unchanged.
        return ranges


if __name__ == "__main__":
    solution = Solution()
    assert solution.summaryRanges([0, 1, 2, 4, 5, 7]) == [
        "0->2", "4->5", "7"
    ]
    assert solution.summaryRanges([0, 2, 3, 4, 6, 8, 9]) == [
        "0", "2->4", "6", "8->9"
    ]
    assert solution.summaryRanges([]) == []
    assert solution.summaryRanges([-1]) == ["-1"]
    print("All tests passed")
