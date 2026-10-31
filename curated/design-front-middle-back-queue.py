from collections import deque
from typing import Deque, List


class FrontMiddleBackQueue:
    # Balancing the two deques keeps every public operation constant time.
    def __init__(self):
        # left contains the first half and has equal size or one extra value.
        # The split makes the middle available at the end of a deque.
        self.left: Deque[int] = deque()
        self.right: Deque[int] = deque()

    def _balance(self) -> None:
        # Move one boundary value until the size invariant is restored.
        if len(self.left) < len(self.right):
            # Pull the right half's first value to restore the left-heavy split.
            self.left.append(self.right.popleft())
        elif len(self.left) > len(self.right) + 1:
            # Move one left boundary value to the front of the right half.
            self.right.appendleft(self.left.pop())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self._balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) == len(self.right):
            self.left.append(val)
        else:
            # Move the old left-middle value right before inserting the new one.
            self.right.appendleft(self.left.pop())
            self.left.append(val)

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self._balance()

    def popFront(self) -> int:
        if not self.left:
            return -1
        value = self.left.popleft()
        self._balance()
        return value

    def popMiddle(self) -> int:
        if not self.left:
            return -1
        # left.pop is the center for odd lengths and left-middle for even.
        value = self.left.pop()
        self._balance()
        return value

    def popBack(self) -> int:
        if self.right:
            value = self.right.pop()
        elif self.left:
            value = self.left.pop()
        else:
            return -1
        self._balance()
        return value


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    queue = None
    for op, values in zip(ops, args):
        if op == "FrontMiddleBackQueue":
            queue = FrontMiddleBackQueue()
            outputs.append(None)
        else:
            outputs.append(getattr(queue, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle",
         "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack",
         "popFront"],
        [[], [1], [2], [3], [4], [], [], [], [], []],
    ) == [None, None, None, None, None, 1, 3, 4, 2, -1]
    print("All tests passed")
