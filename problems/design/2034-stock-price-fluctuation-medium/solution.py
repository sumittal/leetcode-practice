"""
LeetCode 2034: Stock Price Fluctuation 
Difficulty: Medium
Pattern: Hash Table
Video Reference: https://www.youtube.com/results?search_query=leetcode+2034+Stock+Price+Fluctuation++neetcode
Complexity:
    - Time: update O(log n), current O(1), maximum O(log n) amortized, minimum O(log n) amortized
    - Space: O(number of updates)
"""

import heapq
from typing import Dict, List, Optional, Tuple


class StockPrice:
    # The heaps are candidate indexes; the timestamp map decides validity.
    # Repeated updates append versions rather than locating old heap entries.
    def __init__(self):
        # Timestamp map is authoritative; both heaps may contain old versions.
        self.prices: Dict[int, int] = {}
        self.minimum_heap: List[Tuple[int, int]] = []
        self.maximum_heap: List[Tuple[int, int]] = []
        self.latest_timestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price
        self.latest_timestamp = max(self.latest_timestamp, timestamp)
        # Latest timestamp, not update arrival order, defines current().
        # Heaps retain old versions and validate them lazily when queried.
        heapq.heappush(self.minimum_heap, (price, timestamp))
        heapq.heappush(self.maximum_heap, (-price, timestamp))

    def current(self) -> int:
        # The map directly resolves the price at the greatest timestamp.
        return self.prices[self.latest_timestamp]

    def maximum(self) -> int:
        # Lazy deletion removes overwritten prices only when they reach the root.
        while True:
            negative_price, timestamp = self.maximum_heap[0]
            if self.prices[timestamp] == -negative_price:
                return -negative_price
            # A mismatch means this heap record belongs to an overwritten price.
            heapq.heappop(self.maximum_heap)

    def minimum(self) -> int:
        while True:
            price, timestamp = self.minimum_heap[0]
            if self.prices[timestamp] == price:
                return price
            heapq.heappop(self.minimum_heap)


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    stock = None
    for operation, values in zip(ops, args):
        if operation == "StockPrice":
            stock = StockPrice()
            outputs.append(None)
        else:
            outputs.append(getattr(stock, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["StockPrice", "update", "update", "current", "maximum", "update",
         "maximum", "update", "minimum"],
        [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []],
    ) == [None, None, None, 5, 10, None, 5, None, 2]
    assert replay(
        ["StockPrice", "update", "update", "update", "maximum", "minimum",
         "current"],
        [[], [5, 4], [5, 9], [2, 11], [], [], []],
    ) == [None, None, None, None, 11, 9, 9]
    print("All tests passed")
