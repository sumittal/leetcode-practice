"""
LeetCode 215: Kth Largest Element in an Array
Difficulty: Medium
Pattern: Heap / Priority Queue
Video Reference: https://www.youtube.com/watch?v=XEmy13g1Qxc
Complexity:
    - Time: O(n log k) worst case
    - Space: O(k)
"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize from k values so heap size never needs to exceed k.
        largest = nums[:k]
        heapq.heapify(largest)
        # The root is the smallest member of the current top-k candidate set.
        # A size-k heap is O(n log k) in both average and worst cases.
        # Quickselect is O(n) on average but can degrade to O(n^2) in the worst case.
        # The input is not modified because the heap is built from a slice.
        for value in nums[k:]:
            if value > largest[0]:
                # Replace only the current kth value when a larger candidate arrives.
                heapq.heapreplace(largest, value)
            # Values no greater than the root cannot enter the top k.
        # The smallest value retained is the kth largest in the entire array.
        return largest[0]


if __name__ == "__main__":
    solution = Solution()
    assert solution.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert solution.findKthLargest([1], 1) == 1
    assert solution.findKthLargest([7, 6, 5, 4], 4) == 4
    assert solution.findKthLargest([5, 5, 5], 2) == 5
    print("All tests passed")
