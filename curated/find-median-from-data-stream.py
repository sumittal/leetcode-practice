import heapq


class MedianFinder:
    def __init__(self) -> None:
        self.low = []  # Max-heap via negated values.
        self.high = []  # Min-heap; low has equal size or one extra.

    def addNum(self, num: int) -> None:
        # low holds the smaller half; high holds values no smaller than low's maximum.
        # Inserting to low first keeps all values represented before balancing.
        # Push through low, then move its maximum to high to preserve ordering.
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            # Restore the size invariant so low is never smaller.
            heapq.heappush(self.low, -heapq.heappop(self.high))
        # Rebalancing leaves low equal in size or one element larger than high.

    def findMedian(self) -> float:
        # Odd streams use low's root; even streams average both boundary values.
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2.0


if __name__ == "__main__":
    median_finder = MedianFinder()
    median_finder.addNum(1)
    median_finder.addNum(2)
    assert median_finder.findMedian() == 1.5
    median_finder.addNum(3)
    assert median_finder.findMedian() == 2.0
    median_finder = MedianFinder()
    median_finder.addNum(-1)
    assert median_finder.findMedian() == -1.0
    median_finder.addNum(-2)
    assert median_finder.findMedian() == -1.5
    print("All tests passed")
