"""
LeetCode 346: Moving Average from Data Stream
Difficulty: Easy
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+346+Moving+Average+from+Data+Stream+neetcode
Complexity:
    - Time: next O(1)
    - Space: O(size)
"""

from collections import deque
from typing import Deque, List, Optional


class MovingAverage:
    # The queue contains at most size recent values.
    # Its running sum avoids recomputing the window total per insertion.
    # Expiration removes exactly the oldest excess observation.
    # Division uses the current count before the window fills.
    def __init__(self, size: int):
        # A deque retains only values that can still affect a future average.
        self.size = size
        self.values: Deque[int] = deque()
        self.total = 0

    def next(self, val: int) -> float:
        if len(self.values) == self.size:
            # Remove the outgoing value before incorporating the new reading.
            self.total -= self.values.popleft()
        self.values.append(val)
        self.total += val
        # The running total always matches the entries currently in the deque.
        # The queue never exceeds the requested rolling-window length.
        return self.total / len(self.values)


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[float]]:
    outputs: List[Optional[float]] = []
    average = None
    for operation, values in zip(ops, args):
        if operation == "MovingAverage":
            average = MovingAverage(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(average, operation)(*values))
    return outputs


if __name__ == "__main__":
    result = replay(
        ["MovingAverage", "next", "next", "next", "next"],
        [[3], [1], [10], [3], [5]],
    )
    assert result[0:3] == [None, 1.0, 5.5]
    assert abs(result[3] - 14.0 / 3.0) < 1e-9 and result[4] == 6.0
    assert replay(
        ["MovingAverage", "next", "next"],
        [[1], [4], [8]],
    ) == [None, 4.0, 8.0]
    print("All tests passed")
