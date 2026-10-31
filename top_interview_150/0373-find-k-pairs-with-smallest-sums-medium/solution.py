"""
LeetCode 373: Find K Pairs with Smallest Sums
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+373+Find+K+Pairs+with+Smallest+Sums+neetcode
Complexity:
    - Time: O(k log(min(k, m)))
    - Space: O(min(k, m))
"""

import heapq
from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []
        # The arrays' sorted order makes each seeded row monotone.
        # Each fixed nums1 index forms a sorted row of increasing pair sums.
        heap = [
            (nums1[index] + nums2[0], index, 0)
            for index in range(min(k, len(nums1)))
        ]
        heapq.heapify(heap)
        pairs = []
        while heap and len(pairs) < k:
            # The heap root is the globally smallest remaining row head.
            pair_sum, first_index, second_index = heapq.heappop(heap)
            pairs.append([nums1[first_index], nums2[second_index]])
            # Each index pair is reached once from its preceding row neighbor.
            # Advance only this row; its next sum cannot be smaller.
            next_index = second_index + 1
            if next_index < len(nums2):
                heapq.heappush(
                    heap,
                    (nums1[first_index] + nums2[next_index], first_index, next_index),
                )
            # At most k candidates are removed and each row is monotone.
        # Seeding only k rows is enough because no later row can beat k earlier heads.
        # Tuple indices make equal sums deterministic without changing pair validity.
        return pairs


if __name__ == "__main__":
    solution = Solution()
    assert solution.kSmallestPairs([1, 7, 11], [2, 4, 6], 3) == [
        [1, 2],
        [1, 4],
        [1, 6],
    ]
    assert sorted(map(tuple, solution.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))) == [
        (1, 1),
        (1, 1),
    ]
    assert solution.kSmallestPairs([], [1], 2) == []
    assert len(solution.kSmallestPairs([1, 2], [3], 10)) == 2
    print("All tests passed")
