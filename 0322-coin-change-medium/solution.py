"""
LeetCode 322: Coin Change
Difficulty: Medium
Pattern: 1-D Dynamic Programming
Video Reference: https://www.youtube.com/watch?v=H9bfqozjoqs
Complexity:
    - Time: O(amount*coins)
    - Space: O(amount)
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Each denomination is considered as the final coin of a candidate solution.
        # amount+1 exceeds any useful answer and acts as an unreachable sentinel.
        # dp[x] is the fewest coins needed for the already-computed amount x.
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        # Zero coins is the base solution for making amount zero.
        # Increasing totals ensure every predecessor state is ready when consulted.
        for total in range(1, amount + 1):
            for coin in coins:
                if coin <= total:
                    # The predecessor total-coin is smaller and already has its optimum.
                    dp[total] = min(dp[total], dp[total - coin] + 1)
        # dp[amount] is minimal because every transition considers all usable coins.
        # The sentinel remains when no denomination can form the target.
        return -1 if dp[amount] > amount else dp[amount]


if __name__ == "__main__":
    solution = Solution()
    assert solution.coinChange([1, 2, 5], 11) == 3
    assert solution.coinChange([2], 3) == -1
    assert solution.coinChange([1], 0) == 0
    assert solution.coinChange([2, 3], 7) == 3
    print("All tests passed")
