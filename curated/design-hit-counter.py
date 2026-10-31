from collections import deque
from typing import Deque, List, Optional, Tuple


class HitCounter:
    # Ordered timestamp buckets represent the active trailing five-minute window.
    def __init__(self):
        # Each deque entry compresses all events with one timestamp.
        self.hits: Deque[Tuple[int, int]] = deque()
        # Maintaining a total avoids summing every live bucket on each query.
        self.total = 0

    def hit(self, timestamp: int) -> None:
        # Equal timestamps share one bucket without losing their multiplicity.
        if self.hits and self.hits[-1][0] == timestamp:
            time, count = self.hits[-1]
            self.hits[-1] = (time, count + 1)
        else:
            self.hits.append((timestamp, 1))
        self.total += 1
        # Appends and expirations are constant time per timestamp group.

    def getHits(self, timestamp: int) -> int:
        # The inclusive window [timestamp - 299, timestamp] excludes this boundary.
        while self.hits and self.hits[0][0] <= timestamp - 300:
            _, count = self.hits.popleft()
            self.total -= count
        # Timestamps arrive in order, so every expired bucket is at the front.
        # Each group is appended once and removed once over the full operation stream.
        return self.total


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    counter = None
    for operation, values in zip(ops, args):
        if operation == "HitCounter":
            counter = HitCounter()
            outputs.append(None)
        else:
            outputs.append(getattr(counter, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits",
         "getHits"],
        [[], [1], [2], [3], [4], [300], [300], [301]],
    ) == [None, None, None, None, 3, None, 4, 3]
    assert replay(
        ["HitCounter", "hit", "hit", "getHits", "getHits"],
        [[], [1], [1], [301], [300]],
    ) == [None, None, None, 0, 0]
    print("All tests passed")
