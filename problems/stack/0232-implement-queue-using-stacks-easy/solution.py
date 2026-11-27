"""
LeetCode 232: Implement Queue using Stacks
Difficulty: Easy
Pattern: Stack
Video Reference: https://www.youtube.com/results?search_query=leetcode+232+Implement+Queue+using+Stacks+neetcode
Complexity:
    - Time: push O(1), pop O(1) amortized, peek O(1) amortized, empty O(1)
    - Space: O(n)
"""

from typing import List, Optional


class MyQueue:
    # Each value transfers between stacks at most once.
    # Reversal is postponed until outgoing becomes empty.
    def __init__(self):
        # Incoming accepts new values; outgoing exposes the queue front.
        self.incoming: List[int] = []
        self.outgoing: List[int] = []

    def push(self, x: int) -> None:
        # Enqueue never needs to disturb the current front.
        self.incoming.append(x)

    def _prepare(self) -> None:
        if not self.outgoing:
            # Reverse only when needed so each item moves stacks at most once.
            while self.incoming:
                self.outgoing.append(self.incoming.pop())

    def pop(self) -> int:
        # Preparation makes the oldest value available at outgoing's top.
        self._prepare()
        return self.outgoing.pop()

    def peek(self) -> int:
        # Preparing on demand preserves FIFO order across interleaved calls.
        self._prepare()
        return self.outgoing[-1]

    def empty(self) -> bool:
        # Values may be split across the two stacks.
        return not self.incoming and not self.outgoing


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[object]]:
    outputs = []
    queue = None
    for operation, values in zip(ops, args):
        if operation == "MyQueue":
            queue = MyQueue()
            outputs.append(None)
        else:
            outputs.append(getattr(queue, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["MyQueue", "push", "push", "peek", "pop", "empty"],
        [[], [1], [2], [], [], []],
    ) == [None, None, None, 1, 1, False]
    assert replay(
        ["MyQueue", "push", "pop", "empty"],
        [[], [7], [], []],
    ) == [None, None, 7, True]
    print("All tests passed")
