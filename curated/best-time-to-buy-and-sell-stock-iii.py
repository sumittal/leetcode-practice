from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Each state is the best cash balance after its named transaction step.
        first_buy = second_buy = float("-inf")
        first_sell = second_sell = 0
        # Initial sell states encode doing fewer than two transactions.
        for price in prices:
            # Buying subtracts today's price from the best prior sale balance.
            first_buy = max(first_buy, -price)
            # Selling realizes the first transaction's profit.
            first_sell = max(first_sell, first_buy + price)
            # A second buy may spend the profit from the first transaction.
            second_buy = max(second_buy, first_sell - price)
            # The final state is the best profit after at most two completed sales.
            second_sell = max(second_sell, second_buy + price)
            # In-place updates are safe because same-day buy and sell adds no profit.
        # Initial zero sell states allow either transaction to remain unused.
        return int(second_sell)


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert solution.maxProfit([1, 2, 3, 4, 5]) == 4
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
    assert solution.maxProfit([]) == 0
    print("All tests passed")
