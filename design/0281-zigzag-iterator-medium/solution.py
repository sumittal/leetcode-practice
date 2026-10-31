"""
LeetCode 281: Zigzag Iterator
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+281+Zigzag+Iterator+neetcode
Complexity:
    - Time: next O(1), hasNext O(1)
    - Space: O(k) iterators
"""

from collections import deque
from typing import Deque, Iterator, List, Tuple


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        # Keep only iterators that still have at least one value.
        # Retaining each source list gives a simple exhaustion position.
        self.iterators: Deque[Tuple[Iterator[int], List[int], int]] = deque()
        if v1:
            self.iterators.append((iter(v1), v1, 0))
        if v2:
            self.iterators.append((iter(v2), v2, 0))

    def next(self) -> int:
        # The queue front is always the next source in alternating order.
        iterator, values, index = self.iterators.popleft()
        value = next(iterator)
        index += 1
        # The local index tracks exhaustion without probing or copying data.
        # Requeue a source after consuming one item to alternate fairly.
        if index < len(values):
            # Nonempty sources return to the back for the next round.
            self.iterators.append((iterator, values, index))
        return value

    def hasNext(self) -> bool:
        # Exhausted sources are never reinserted into the queue.
        return bool(self.iterators)


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    iterator = None
    for op, values in zip(ops, args):
        if op == "ZigzagIterator":
            iterator = ZigzagIterator(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(iterator, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["ZigzagIterator", "next", "next", "next", "next", "next", "next",
         "hasNext"],
        [[[1, 2], [3, 4, 5, 6]], [], [], [], [], [], [], []],
    ) == [None, 1, 3, 2, 4, 5, 6, False]
    # One empty source is skipped while the other continues.
    assert replay(
        ["ZigzagIterator", "hasNext", "next", "hasNext"],
        [[[], [7]], [], [], []],
    ) == [None, True, 7, False]
    print("All tests passed")
