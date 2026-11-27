"""
LeetCode 1851: Minimum Interval to Include Each Query
Difficulty: Hard
Pattern: Intervals
Video Reference: https://www.youtube.com/watch?v=5hQ5WWW5awQ
Complexity:
    - Time: O((n+q) log(n+q))
    - Space: O(n+q)
"""

import heapq
from typing import List, Tuple


class Solution:
    def minInterval(
        self, intervals: List[List[int]], queries: List[int]
    ) -> List[int]:
        # Sorting intervals lets each query add only newly eligible start positions.
        intervals.sort()
        # Sorted query values make interval eligibility advance monotonically.
        # Store query indices so sorting does not change the required output order.
        ordered_queries: List[Tuple[int, int]] = sorted(
            (query, index) for index, query in enumerate(queries)
        )
        answers = [-1] * len(queries)
        candidates = []
        interval_index = 0
        for query, original_index in ordered_queries:
            # Every interval with start <= query is now eligible for consideration.
            while interval_index < len(intervals) and intervals[interval_index][0] <= query:
                start, end = intervals[interval_index]
                heapq.heappush(candidates, (end - start + 1, end))
                interval_index += 1
            # Heap entries retain their right endpoint for later validity checks.
            # Expired intervals cannot cover this or any later sorted query.
            while candidates and candidates[0][1] < query:
                heapq.heappop(candidates)
                # Only expired roots need removal before selecting a minimum length.
            if candidates:
                # Heap ordering selects the shortest currently valid interval.
                answers[original_index] = candidates[0][0]
                # Closed interval endpoints include a query equal to either boundary.
            # Expired intervals hidden deeper in the heap cannot beat a valid root.
            # Results go to original indices even though queries are processed sorted.
        # Unfilled positions remain -1 when no interval contains their query.
        # Restoring by saved index preserves duplicate and unsorted query positions.
        return answers


if __name__ == "__main__":
    solution = Solution()
    assert solution.minInterval(
        [[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]
    ) == [3, 3, 1, 4]
    assert solution.minInterval(
        [[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]
    ) == [2, -1, 4, 6]
    assert solution.minInterval([[1, 2]], [2, 1]) == [2, 2]
    assert solution.minInterval([], [1]) == [-1]
    print("All tests passed")
