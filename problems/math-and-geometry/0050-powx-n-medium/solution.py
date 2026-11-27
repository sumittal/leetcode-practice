"""
LeetCode 50: Pow(x, n)
Difficulty: Medium
Pattern: Math & Geometry
Video Reference: https://www.youtube.com/watch?v=g9YQyYi4IQQ
Complexity:
    - Time: O(log |n|)
    - Space: O(1)
"""

import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Reciprocal conversion lets the loop handle only a nonnegative exponent.
        if n < 0:
            x = 1 / x
            n = -n
        result = 1.0
        factor = x
        # result contains contributions from exponent bits already consumed.
        # factor is the power corresponding to the current lowest remaining bit.
        # Each iteration consumes one binary exponent bit.
        while n:
            if n & 1:
                # A set bit contributes the current squared factor to the result.
                result *= factor
            # Squaring advances the factor to the next power of two.
            factor *= factor
            n >>= 1
            # The exponent shrinks by half, giving logarithmic iteration count.
        # Exponent zero leaves the multiplicative identity unchanged.
        # Negative powers use the reciprocal base established before this loop.
        return result


if __name__ == "__main__":
    solution = Solution()
    assert math.isclose(solution.myPow(2.0, 10), 1024.0, rel_tol=1e-9, abs_tol=1e-9)
    assert math.isclose(solution.myPow(2.1, 3), 9.261, rel_tol=1e-9, abs_tol=1e-9)
    assert math.isclose(solution.myPow(2.0, -2), 0.25, rel_tol=1e-9, abs_tol=1e-9)
    assert math.isclose(solution.myPow(5.0, 0), 1.0, rel_tol=1e-9, abs_tol=1e-9)
    print("All tests passed")
