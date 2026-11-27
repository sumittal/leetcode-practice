"""
LeetCode 69: Sqrt(x)
Difficulty: Easy
Pattern: Binary Search
Video Reference: https://www.youtube.com/watch?v=zdMhGxRWutQ
Complexity:
    - Time: O(log x)
    - Space: O(1)
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        # The upper bound is exclusive and one past the largest possible root.
        left = 0
        right = x + 1
        # The answer is the last integer whose square is at most x.
        while left < right:
            middle = (left + right) // 2
            # Guard zero before division in the predicate.
            # Division avoids overflow in fixed-width implementations too.
            if middle == 0 or middle <= x // middle:
                left = middle + 1
            else:
                # A too-large midpoint and everything above it are excluded.
                right = middle
            # This upper-exclusive range converges to floor(sqrt(x)) + 1.
        # The predecessor of the first failing candidate is the integer root.
        # No floating-point square root is used.
        return left - 1


if __name__ == "__main__":
    solution = Solution()
    assert solution.mySqrt(4) == 2
    assert solution.mySqrt(8) == 2
    assert solution.mySqrt(0) == 0
    assert solution.mySqrt(1) == 1
    assert solution.mySqrt(2147395600) == 46340
    print("All tests passed")
