"""
LeetCode 57: Insert Interval
Difficulty: Medium
Pattern: Intervals
Video Reference: https://www.youtube.com/watch?v=A8NUOmlwOlM
Complexity:
    - Time: O(n)
    - Space: O(n)
"""

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # Preserve intervals that lie strictly before the new range.
        result = []
        # i divides the input into emitted, overlapping, and not-yet-visited ranges.
        i = 0
        start, end = newInterval
        # Equality at the boundary still counts as overlap and must be merged.
        while i < len(intervals) and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1  # These end before the insertion.
        while i < len(intervals) and intervals[i][0] <= end:
            # Merge by expanding both bounds; the expanded end may absorb more ranges.
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        # Once a start exceeds the expanded end, all remaining intervals stay separate.
        result.append([start, end])
        # Since the input is sorted, the untouched suffix is already ordered.
        result.extend(
            intervals[i:]
        )  # The remaining sorted intervals start after the merge.
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [
        [1, 2],
        [3, 10],
        [12, 16],
    ]
    assert solution.insert([], [2, 5]) == [[2, 5]]
    assert solution.insert([[1, 2]], [4, 5]) == [[1, 2], [4, 5]]
    print("All tests passed")
