from typing import List, Tuple


class MinStack:
    def __init__(self) -> None:
        # Each entry caches the minimum through that stack depth.
        self.values: List[Tuple[int, int]] = []

    def push(self, val: int) -> None:
        # Carry the prior minimum forward so getMin never scans the stack.
        current_min = min(val, self.values[-1][1]) if self.values else val
        # Repeating a minimum stores it again, preserving it after a later pop.
        # Each tuple snapshots the minimum for exactly its own stack depth.
        self.values.append((val, current_min))

    def pop(self) -> None:
        # Removing one tuple restores the previous depth and its cached minimum.
        self.values.pop()
        # The operation sequence guarantees pop is called only on a nonempty stack.

    def top(self) -> int:
        # The tuple's first field is the most recently pushed value.
        # The paired minimum belongs to the same stack depth as this top value.
        return self.values[-1][0]

    def getMin(self) -> int:
        # The second field is the minimum of all values still on the stack.
        return self.values[-1][1]


if __name__ == "__main__":
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    assert stack.getMin() == -3
    stack.pop()
    assert stack.top() == 0
    assert stack.getMin() == -2
    stack.push(-2)
    assert stack.getMin() == -2
    stack.pop()
    assert stack.getMin() == -2
    print("All tests passed")
