"""
LeetCode 973: K Closest Points to Origin
Difficulty: Medium
Pattern: Heap / Priority Queue
Video Reference: https://www.youtube.com/watch?v=rI2EBUEMfTk
Complexity:
    - Time: O(n log k)
    - Space: O(k)
"""

import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Negated squared distance turns the heap root into the farthest kept point.
        # Squared distances preserve ordering without computing square roots.
        closest = []
        for x, y in points:
            distance = x * x + y * y
            heapq.heappush(closest, (-distance, x, y))
            # The heap size is capped after every point, so memory is O(k).
            if len(closest) > k:
                # Evict the farthest point whenever the heap exceeds the requested size.
                heapq.heappop(closest)
        # The heap contains k points with no larger distance than any discarded point.
        # Equal-distance points are interchangeable for the requested k closest set.
        # Coordinates are carried in heap entries so the result needs no lookup table.
        # Heap ordering affects output order only, not which distances are retained.
        return [[x, y] for _, x, y in closest]


if __name__ == "__main__":
    solution = Solution()
    assert sorted(solution.kClosest([[1, 3], [-2, 2]], 1)) == [[-2, 2]]
    assert sorted(solution.kClosest([[3, 3], [5, -1], [-2, 4]], 2)) == [
        [-2, 4],
        [3, 3],
    ]
    assert sorted(solution.kClosest([[0, 1], [1, 0]], 1)) in (
        [[0, 1]],
        [[1, 0]],
    )
    assert sorted(solution.kClosest([[1, 1], [1, 1]], 1)) == [[1, 1]]
    print("All tests passed")
