from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Each price increase can be realized as one adjacent buy-sell gain.
        # Every positive adjacent rise belongs to some profitable run.
        # Unlimited transactions allow collecting each separate upward segment.
        profit = 0
        for previous, current in zip(prices, prices[1:]):
            # Buying before and selling after each rise telescopes to the run gain.
            if current > previous:
                profit += current - previous
            # Flat or falling steps cannot improve an unlimited transaction plan.
            # Summing rises is equivalent to selling each valley-to-peak segment.
            # Transactions do not overlap because each adjacent step is used once.
            # Declines are skipped rather than carried as losses between trades.
        return profit


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert solution.maxProfit([1, 2, 3, 4, 5]) == 4
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
    print("All tests passed")
