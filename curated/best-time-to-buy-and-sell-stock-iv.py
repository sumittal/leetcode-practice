from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        days = len(prices)
        # At most half as many transactions as days is effectively unlimited.
        if k >= days // 2:
            return sum(
                max(0, prices[index] - prices[index - 1])
                for index in range(1, days)
            )
        # buys[t] and sells[t] track balances after the t-th buy or sale.
        buys = [float("-inf")] * (k + 1)
        sells = [0] * (k + 1)
        for price in prices:
            # Transaction counts advance from one through the allowed maximum.
            for transaction in range(1, k + 1):
                # Buying uses the previous transaction's completed-sale balance.
                buys[transaction] = max(
                    buys[transaction], sells[transaction - 1] - price
                )
                # Selling returns the best balance after this transaction count.
                sells[transaction] = max(
                    sells[transaction], buys[transaction] + price
                )
                # Same-day buy and sell cannot improve a state.
            # Unchanged states represent choosing to skip today's price.
        # sells[k] is the maximum profit using at most k transactions.
        return sells[k]


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxProfit(2, [2, 4, 1]) == 2
    assert solution.maxProfit(2, [3, 2, 6, 5, 0, 3]) == 7
    assert solution.maxProfit(100, [1, 2, 3, 4, 5]) == 4
    assert solution.maxProfit(2, [7, 6, 4, 3, 1]) == 0
    assert solution.maxProfit(0, [1, 5]) == 0
    print("All tests passed")
