"""
LeetCode 149: Max Points on a Line
Difficulty: Hard
Pattern: Math & Geometry
Video Reference: https://www.youtube.com/watch?v=Bb9lOXUOnFw
Complexity:
    - Time: O(n^2)
    - Space: O(n)
"""

from collections import defaultdict
from math import gcd
from typing import Dict, List, Tuple


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        best = 0
        # Slope counts for an anchor cover all lines through that point.
        # Every optimal line can be anchored at one of its input points.
        for anchor in range(len(points)):
            slopes: Dict[Tuple[int, int], int] = defaultdict(int)
            duplicates = 1
            x1, y1 = points[anchor]
            for other in range(anchor + 1, len(points)):
                x2, y2 = points[other]
                dx = x2 - x1
                dy = y2 - y1
                # Duplicate coordinates belong to every line through the anchor.
                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue
                # Reduce integer deltas so equivalent rational slopes share a key.
                divisor = gcd(abs(dx), abs(dy))
                dx //= divisor
                dy //= divisor
                # Canonicalize signs; vertical lines use one dedicated direction.
                if dx == 0:
                    slope = (1, 0)
                else:
                    if dx < 0:
                        dx = -dx
                        dy = -dy
                    slope = (dy, dx)
                slopes[slope] += 1
                # No floating point division can merge or split slope identities.
            through_anchor = duplicates + max(slopes.values(), default=0)
            # Duplicate points are included once in each slope's line count.
            best = max(best, through_anchor)
        # At least one point exists under the problem constraints.
        return best


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxPoints([[1, 1], [2, 2], [3, 3]]) == 3
    assert solution.maxPoints(
        [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    ) == 4
    assert solution.maxPoints([[0, 0], [0, 0], [1, 1]]) == 3
    assert solution.maxPoints([[1, 1]]) == 1
    print("All tests passed")
