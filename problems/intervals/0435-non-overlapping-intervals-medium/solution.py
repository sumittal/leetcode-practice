"""
LeetCode 435: Non-overlapping Intervals
Difficulty: Medium
Pattern: Intervals
Video Reference: https://www.youtube.com/watch?v=nONCGxWoUfM
Complexity:
    - Time: O(n log n)
    - Space: O(n)
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sorting by end time makes the greedy choice earliest to release its resource.
        # Earliest finishing intervals leave the most room for future choices.
        intervals.sort(key=lambda item: item[1])
        kept = 0
        # Counting retained intervals makes the required removals the complement.
        end = float("-inf")
        # Starting below every valid endpoint lets the first interval always qualify.
        # end is the finish time of the last interval kept by the greedy schedule.
        for start, finish in intervals:
            if start >= end:
                # Touching endpoints are compatible, so the interval can be retained.
                kept += 1
                end = finish  # Retain this interval and advance the boundary.
            # Overlapping candidates are discarded; the retained finish stays unchanged.
        return len(intervals) - kept


if __name__ == "__main__":
    solution = Solution()
    assert solution.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert solution.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert solution.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
    assert solution.eraseOverlapIntervals([]) == 0
    print("All tests passed")
