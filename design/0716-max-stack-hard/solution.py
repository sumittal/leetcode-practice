"""
LeetCode 716: Max Stack
Difficulty: Hard
Pattern: Linked List
Video Reference: https://www.youtube.com/results?search_query=leetcode+716+Max+Stack+neetcode
Complexity:
    - Time: push O(log n), pop O(log n), top O(1), peekMax O(1), popMax O(log n)
    - Space: O(n)
"""

from typing import List, Optional


class MaxStack:
    # A single list favors constant-time push and pop over maximum-query speed.
    # popMax removes the rightmost maximum to satisfy the closest-to-top rule.
    def __init__(self):
        # A list provides constant-time ordinary stack operations.
        self.values: List[int] = []

    def push(self, x: int) -> None:
        # New equal maxima are later in the list and therefore removed first.
        self.values.append(x)

    def pop(self) -> int:
        # Standard pop needs no maximum tracking.
        return self.values.pop()

    def top(self) -> int:
        # The final list entry is exactly the stack top.
        return self.values[-1]

    def peekMax(self) -> int:
        # The linear scan is the deliberate space-light maximum index.
        return max(self.values)

    def popMax(self) -> int:
        maximum = max(self.values)
        # Reverse search selects the most recently pushed copy of a tied maximum.
        index = len(self.values) - 1 - self.values[::-1].index(maximum)
        return self.values.pop(index)


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    stack = None
    for operation, values in zip(ops, args):
        if operation == "MaxStack":
            stack = MaxStack()
            outputs.append(None)
        else:
            outputs.append(getattr(stack, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["MaxStack", "push", "push", "push", "top", "popMax", "top",
         "peekMax", "pop", "top"],
        [[], [5], [1], [5], [], [], [], [], [], []],
    ) == [None, None, None, None, 5, 5, 1, 5, 1, 5]
    assert replay(
        ["MaxStack", "push", "push", "popMax", "top"],
        [[], [-2], [-2], [], []],
    ) == [None, None, None, -2, -2]
    print("All tests passed")
