"""
LeetCode 933: Number of Recent Calls
Difficulty: Easy
Pattern: Design
Video Reference: https://www.youtube.com/results?search_query=leetcode+933+Number+of+Recent+Calls+neetcode
Complexity:
    - Time: ping O(1) amortized
    - Space: O(3000)
"""

from collections import deque
from typing import Deque, List, Optional


class RecentCounter:
    # The active request window is maintained as a contiguous deque suffix.
    # Older requests can never become relevant again as time increases.
    # Each request is appended once and removed at most once.
    # The inclusive left boundary is t - 3000.
    def __init__(self):
        # Deque order follows the guaranteed nondecreasing ping timestamps.
        self.requests: Deque[int] = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        # The lower bound is inclusive, so only strictly older pings expire.
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        # Each ping enters and leaves the deque once across the full stream.
        # Increasing timestamps ensure expired calls form a contiguous prefix.
        return len(self.requests)


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    counter = None
    for operation, values in zip(ops, args):
        if operation == "RecentCounter":
            counter = RecentCounter()
            outputs.append(None)
        else:
            outputs.append(getattr(counter, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["RecentCounter", "ping", "ping", "ping", "ping"],
        [[], [1], [100], [3001], [3002]],
    ) == [None, 1, 2, 3, 3]
    assert replay(
        ["RecentCounter", "ping", "ping", "ping"],
        [[], [1], [3001], [6001]],
    ) == [None, 1, 2, 2]
    print("All tests passed")
