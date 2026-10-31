from collections import deque
from typing import Deque, List, Optional


class Fenwick:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, index: int, delta: int) -> None:
        # Point changes update logarithmically many prefix-tree nodes.
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def prefix(self, index: int) -> int:
        total = 0
        while index:
            total += self.tree[index]
            index -= index & -index
        return total

    def kth(self, rank: int) -> int:
        # Find the smallest value index whose cumulative count reaches rank.
        index = 0
        bit = 1 << (self.size.bit_length() - 1)
        while bit:
            candidate = index + bit
            if candidate <= self.size and self.tree[candidate] < rank:
                index = candidate
                rank -= self.tree[candidate]
            bit >>= 1
        return index + 1


class MKAverage:
    LIMIT = 100000

    def __init__(self, m: int, k: int):
        # Values fit directly into Fenwick indices under the problem constraints.
        self.m = m
        self.k = k
        self.window: Deque[int] = deque()
        self.counts = Fenwick(self.LIMIT)
        # Separate trees support order statistics and weighted value sums.
        self.sums = Fenwick(self.LIMIT)
        self.total = 0

    def addElement(self, num: int) -> None:
        self.window.append(num)
        self.counts.add(num, 1)
        self.sums.add(num, num)
        self.total += num
        # Expiring one value keeps the data structure aligned with the last m.
        if len(self.window) > self.m:
            expired = self.window.popleft()
            self.counts.add(expired, -1)
            self.sums.add(expired, -expired)
            self.total -= expired

    def _sum_smallest(self, rank: int) -> int:
        if rank <= 0:
            return 0
        value = self.counts.kth(rank)
        count_before = self.counts.prefix(value - 1)
        sum_before = self.sums.prefix(value - 1)
        # The kth value can be repeated, so include only the required copies.
        # Only some copies of the boundary value may belong to the prefix.
        return sum_before + (rank - count_before) * value

    def calculateMKAverage(self) -> int:
        if len(self.window) < self.m:
            return -1
        # Subtract the smallest k and the smallest m-k values from the total.
        low_sum = self._sum_smallest(self.k)
        through_middle = self._sum_smallest(self.m - self.k)
        middle_sum = self.total - low_sum - (self.total - through_middle)
        # LeetCode requires floor division for the trimmed mean.
        return middle_sum // (self.m - 2 * self.k)


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    average = None
    for operation, values in zip(ops, args):
        if operation == "MKAverage":
            average = MKAverage(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(average, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["MKAverage", "addElement", "addElement", "calculateMKAverage",
         "addElement", "calculateMKAverage", "addElement", "addElement",
         "addElement", "calculateMKAverage"],
        [[3, 1], [3], [1], [], [10], [], [5], [5], [5], []],
    ) == [None, None, None, -1, None, 3, None, None, None, 5]
    assert replay(
        ["MKAverage", "addElement", "addElement", "addElement",
         "calculateMKAverage", "addElement", "calculateMKAverage"],
        [[3, 1], [1], [1], [100], [], [2], []],
    ) == [None, None, None, None, 1, None, 2]
    print("All tests passed")
