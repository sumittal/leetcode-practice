from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        # hold, sold, and rest are best profits ending in each distinct state.
        hold = -prices[0]
        sold = float("-inf")
        rest = 0
        # A sale cannot occur before a prior holding exists.
        # The first day initializes the states; each later day reads only yesterday.
        for price in prices[1:]:
            previous_hold = hold
            previous_sold = sold
            previous_rest = rest
            # Buying is allowed only from rest, enforcing the post-sale cooldown.
            hold = max(previous_hold, previous_rest - price)
            # Selling today must follow a position held before today's price.
            sold = previous_hold + price
            # Rest either continues or follows yesterday's completed sale.
            rest = max(previous_rest, previous_sold)
            # Sold stays separate for one day so it cannot fund an immediate purchase.
        # An unsold holding cannot be the completed transaction result.
        return int(max(sold, rest))


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxProfit([1, 2, 3, 0, 2]) == 3
    assert solution.maxProfit([1]) == 0
    assert solution.maxProfit([2, 1, 4]) == 3
    assert solution.maxProfit([1, 2]) == 1
    print("All tests passed")
