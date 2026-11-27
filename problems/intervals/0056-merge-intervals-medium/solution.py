"""
LeetCode 56: Merge Intervals
Difficulty: Medium
Pattern: Intervals
Video Reference: https://www.youtube.com/watch?v=44H3cEC2fFM
Complexity:
    - Time: O(n log n)
    - Space: O(n)
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # No endpoint exists when there are no intervals to combine.
        if not intervals:
            return []
        # Sorting makes starts monotone, so overlaps can be merged in one pass.
        intervals.sort(key=lambda item: item[0])
        # Store a copy so extending the result does not alter an input interval.
        merged = [intervals[0][:]]
        # After each iteration, merged is sorted and contains no overlapping neighbors.
        for start, end in intervals[1:]:
            # The first range is already in merged; process each later range once.
            # A gap starts a new merged range; overlap extends the prior one.
            if start <= merged[-1][1]:
                # Sorted starts make the last output range the only possible overlap.
                merged[-1][1] = max(merged[-1][1], end)
            # Copying the first range avoids mutating the caller's interval endpoint.
            else:
                merged.append([start, end])
        return merged


if __name__ == "__main__":
    solution = Solution()
    assert solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert solution.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert solution.merge([[4, 7], [1, 4]]) == [[1, 7]]
    assert solution.merge([]) == []
    print("All tests passed")
