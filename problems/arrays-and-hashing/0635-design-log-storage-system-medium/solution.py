"""
LeetCode 635: Design Log Storage System
Difficulty: Medium
Pattern: Hash Table
Video Reference: https://www.youtube.com/results?search_query=leetcode+635+Design+Log+Storage+System+neetcode
Complexity:
    - Time: put O(n), retrieve O(n)
    - Space: O(n)
"""

from bisect import insort
from typing import List, Tuple


class LogSystem:
    def __init__(self):
        # Sorted records make every result chronological.
        self.logs: List[Tuple[str, int]] = []
        # The fixed layout makes lexical time comparisons equivalent to numeric.
        # Prefix widths are the fields retained at each requested granularity.
        self.width = {
            "Year": 4, "Month": 7, "Day": 10, "Hour": 13,
            "Minute": 16, "Second": 19,
        }

    def put(self, identifier: int, timestamp: str) -> None:
        # The tuple tie-breaker makes equal timestamps deterministic.
        # Insertion maintains sorted order even if timestamps arrive out of order.
        insort(self.logs, (timestamp, identifier))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        width = self.width[granularity]
        # Truncation is performed on both endpoints and stored timestamp strings.
        lower = start[:width]
        upper = end[:width]
        # Fixed-width timestamp components sort lexicographically by time.
        # Filtering a sorted list also keeps returned IDs in chronological order.
        return [
            identifier for timestamp, identifier in self.logs
            if lower <= timestamp[:width] <= upper
        ]


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    system = None
    for op, values in zip(ops, args):
        if op == "LogSystem":
            system = LogSystem()
            outputs.append(None)
        else:
            outputs.append(getattr(system, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["LogSystem", "put", "put", "retrieve"],
        [[], [1, "2017:01:01:23:59:59"], [2, "2017:01:02:00:00:00"],
         ["2017:01:01:00:00:00", "2017:01:01:23:59:59", "Day"]],
    ) == [None, None, None, [1]]
    assert replay(
        ["LogSystem", "put", "put", "retrieve"],
        [[], [1, "2017:01:01:23:59:59"], [2, "2017:01:02:00:00:00"],
         ["2017:01:01:00:00:00", "2017:01:02:23:59:59", "Day"]],
    ) == [None, None, None, [1, 2]]
    print("All tests passed")
