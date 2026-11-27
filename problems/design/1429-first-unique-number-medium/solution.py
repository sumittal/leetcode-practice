"""
LeetCode 1429: First Unique Number
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+1429+First+Unique+Number+neetcode
Complexity:
    - Time: add O(1), showFirstUnique O(1) amortized
    - Space: O(n)
"""

from collections import Counter, deque
from typing import Deque, List


class FirstUnique:
    def __init__(self, nums: List[int]):
        # Counts distinguish unique values from values seen more than once.
        self.counts = Counter(nums)
        # Arrival order is retained; duplicate candidates are removed lazily.
        self.queue: Deque[int] = deque(nums)
        self._discard_repeated()

    def _discard_repeated(self) -> None:
        # Once a value repeats it can never become unique again.
        # Each arrival is removed at most once, keeping cleanup amortized O(1).
        while self.queue and self.counts[self.queue[0]] > 1:
            self.queue.popleft()
        # The surviving front, if any, is the oldest unique arrival.
        # A unique front is the earliest remaining stream value.

    def showFirstUnique(self) -> int:
        # Only queue candidates need inspection; all earlier duplicates are gone.
        self._discard_repeated()
        return self.queue[0] if self.queue else -1

    def add(self, value: int) -> None:
        # Append every arrival so a first occurrence remains ordered.
        # Increment before pruning so a newly duplicated front is removed now.
        self.counts[value] += 1
        self.queue.append(value)
        self._discard_repeated()


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    stream = None
    for op, values in zip(ops, args):
        if op == "FirstUnique":
            stream = FirstUnique(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(stream, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["FirstUnique", "showFirstUnique", "add", "showFirstUnique",
         "add", "showFirstUnique", "add", "showFirstUnique"],
        [[[2, 3, 5]], [], [2], [], [3], [], [5], []],
    ) == [None, 2, None, 3, None, 5, None, -1]
    assert replay(
        ["FirstUnique", "showFirstUnique", "add", "showFirstUnique"],
        [[[7, 7, 7]], [], [8], []],
    ) == [None, -1, None, 8]
    print("All tests passed")
