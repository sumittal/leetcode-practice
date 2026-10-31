"""
LeetCode 312: Burst Balloons
Difficulty: Hard
Pattern: 2-D Dynamic Programming
Video Reference: https://www.youtube.com/watch?v=VFskby7lUbw
Complexity:
    - Time: O(n^3)
    - Space: O(n^2)
"""

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Boundary ones stay present and simplify the coins gained at either edge.
        balloons = [1] + nums + [1]
        size = len(balloons)
        # dp[left][right] is the best score for balloons strictly between boundaries.
        # Open intervals let the final balloon multiply the two surviving boundaries.
        dp = [[0] * size for _ in range(size)]
        # Width grows so both smaller subintervals are complete before their parent.
        for width in range(2, size):
            for left in range(size - width):
                right = left + width
                # Choose the last balloon popped inside this open interval.
                for last in range(left + 1, right):
                    # Its boundary neighbors remain after every interior balloon is gone.
                    coins = (
                        dp[left][last]
                        + dp[last][right]
                        + balloons[left] * balloons[last] * balloons[right]
                    )
                    # The recurrence combines independent left and right intervals.
                    dp[left][right] = max(dp[left][right], coins)
                    # Choosing the last pop avoids needing to model changing neighbors.
                # Empty intervals retain their zero base value from table initialization.
                # Every candidate last index is strictly inside these boundaries.
            # Increasing interval width is the required bottom-up dependency order.
            # Width two has no interior balloon and therefore remains at its zero base.
        # The padded endpoints enclose the full original balloon interval.
        # The full interval's optimum includes every original balloon exactly once.
        return dp[0][size - 1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxCoins([3, 1, 5, 8]) == 167
    assert solution.maxCoins([1, 5]) == 10
    assert solution.maxCoins([]) == 0
    assert solution.maxCoins([7]) == 7
    print("All tests passed")
