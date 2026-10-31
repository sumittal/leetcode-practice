"""
LeetCode 225: Implement Stack using Queues
Difficulty: Easy
Pattern: Stack
Video Reference: https://www.youtube.com/watch?v=rW4vm0-DLYc
Complexity:
    - Time: push O(n), pop O(1), top O(1), empty O(1)
    - Space: O(n)
"""

from collections import deque
from typing import Deque, List, Optional


class MyStack:
    # Rotating on push keeps the newest element at the queue front.
    # Pop and top are then constant-time operations.
    # Each push is linear in the number of existing elements.
    def __init__(self):
        # Queue front is maintained as the stack's top element.
        self.queue: Deque[int] = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        # Rotate old elements behind x so the queue front behaves like a stack top.
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        # Every existing item rotates exactly once for this push.

    def pop(self) -> int:
        # Removal is constant time because push paid the reordering cost.
        return self.queue.popleft()

    def top(self) -> int:
        # The front is maintained as the most recently pushed, unpopped item.
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[object]]:
    outputs = []
    stack = None
    for operation, values in zip(ops, args):
        if operation == "MyStack":
            stack = MyStack()
            outputs.append(None)
        else:
            outputs.append(getattr(stack, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["MyStack", "push", "push", "top", "pop", "empty"],
        [[], [1], [2], [], [], []],
    ) == [None, None, None, 2, 2, False]
    assert replay(
        ["MyStack", "push", "pop", "empty"],
        [[], [7], [], []],
    ) == [None, None, 7, True]
    print("All tests passed")
