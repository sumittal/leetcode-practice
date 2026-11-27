"""
LeetCode 121: Best Time to Buy and Sell Stock
Difficulty: Easy
Pattern: Sliding Window
Video Reference: https://www.youtube.com/watch?v=1pkOgXD63yU
Complexity:
    - Time: O(n)
    - Space: O(1)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # minimum_price is the lowest buy price from days already scanned.
        minimum_price = float("inf")
        # Zero represents choosing no trade when prices only fall or input is short.
        best_profit = 0
        for price in prices:
            if price < minimum_price:
                # A new low is a better future buy; it cannot be sold on the same day.
                minimum_price = price
            else:
                # The stored minimum came from an earlier day, preserving buy-before-sell.
                best_profit = max(best_profit, price - minimum_price)
        # The maximum profit over all valid earlier-buy/current-sell pairs is the answer.
        return best_profit


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
    assert solution.maxProfit([5]) == 0
    assert solution.maxProfit([2, 2, 2]) == 0
    print("All tests passed")
