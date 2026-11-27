"""
LeetCode 875: Koko Eating Bananas
Difficulty: Medium
Pattern: Binary Search
Video Reference: https://www.youtube.com/watch?v=U2SozAs9RzA
Complexity:
    - Time: O(n log(max(piles)))
    - Space: O(1)
"""

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Feasible speeds form a monotone interval from some minimum to max pile.
        left = 1
        right = max(piles)
        # The upper bound is feasible because each pile then takes at most one hour.
        # The search narrows to the first speed whose total hours fit within h.
        while left < right:
            speed = (left + right) // 2
            # Each nonempty pile consumes a whole hour fraction rounded upward.
            hours = sum((pile + speed - 1) // speed for pile in piles)
            if hours <= h:
                # This speed works, so a smaller feasible speed may still exist.
                right = speed
            else:
                # Too many hours means every lower speed also fails.
                left = speed + 1
            # The midpoint remains in range only when it may still be optimal.
        # The converged boundary is the smallest speed that meets the deadline.
        return left


if __name__ == "__main__":
    solution = Solution()
    assert solution.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert solution.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert solution.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
    assert solution.minEatingSpeed([1], 1) == 1
    assert solution.minEatingSpeed([4, 4, 4], 3) == 4
    print("All tests passed")
