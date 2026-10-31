"""
LeetCode 1381: Design a Stack With Increment Operation
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+1381+Design+a+Stack+With+Increment+Operation+neetcode
Complexity:
    - Time: push O(1), pop O(1), increment O(1)
    - Space: O(n)
"""

from typing import List, Optional


class CustomStack:
    # Push and pop touch only the top slot; increment marks one prefix boundary.
    # Deferred values flow toward the bottom only when entries are removed.
    def __init__(self, maxSize: int):
        # Parallel arrays keep each value paired with its deferred increment.
        self.capacity = maxSize
        self.values: List[int] = []
        self.increments: List[int] = []

    def push(self, x: int) -> None:
        if len(self.values) == self.capacity:
            return
        self.values.append(x)
        # Each entry carries an increment to apply when it reaches the top.
        self.increments.append(0)

    def pop(self) -> int:
        if not self.values:
            return -1
        index = len(self.values) - 1
        deferred = self.increments.pop()
        # Applying the marker here resolves all increments aimed at this entry.
        value = self.values.pop() + deferred
        if index:
            # Passing deferred work downward applies it to the lower prefix.
            self.increments[index - 1] += deferred
        return value

    def increment(self, k: int, val: int) -> None:
        # The marker at the highest affected index covers its whole lower prefix.
        index = min(k, len(self.values)) - 1
        if index >= 0:
            # One marker represents adding val to every current item below index.
            self.increments[index] += val


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    stack = None
    for operation, values in zip(ops, args):
        if operation == "CustomStack":
            stack = CustomStack(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(stack, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["CustomStack", "push", "push", "pop", "push", "push", "push",
         "increment", "increment", "pop", "pop", "pop", "pop"],
        [[3], [1], [2], [], [2], [3], [4], [5, 100], [2, 100],
         [], [], [], []],
    ) == [None, None, None, 2, None, None, None, None, None, 103, 202, 201, -1]
    assert replay(
        ["CustomStack", "increment", "pop", "push", "increment", "pop"],
        [[2], [2, 5], [], [4], [1, 3], []],
    ) == [None, None, -1, None, None, 7]
    print("All tests passed")
