"""
LeetCode 518: Coin Change II
Difficulty: Medium
Pattern: 2-D Dynamic Programming
Video Reference: https://www.youtube.com/watch?v=Mjy4hd2xgrs
Complexity:
    - Time: O(amount * number of coins)
    - Space: O(amount)
"""

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # ways[value] counts combinations using denominations processed so far.
        ways = [0] * (amount + 1)
        # There is one way to make zero: choose no coins.
        ways[0] = 1
        # Keeping denominations outside avoids counting different coin orders twice.
        # Each combination is introduced when its largest processed denomination arrives.
        for coin in coins:
            # Ascending totals allow this denomination to be used repeatedly.
            for subtotal in range(coin, amount + 1):
                # Add combinations that append this coin to a prior smaller amount.
                ways[subtotal] += ways[subtotal - coin]
            # This one-dimensional table compresses the denomination-by-total DP.
        # Unreachable amounts remain zero because no transition reaches them.
        return ways[amount]


if __name__ == "__main__":
    solution = Solution()
    assert solution.change(5, [1, 2, 5]) == 4
    assert solution.change(3, [2]) == 0
    assert solution.change(10, [10]) == 1
    assert solution.change(0, [1, 2, 5]) == 1
    print("All tests passed")
