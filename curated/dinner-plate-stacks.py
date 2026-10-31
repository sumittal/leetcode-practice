import heapq
from typing import List, Set


class DinnerPlates:
    def __init__(self, capacity: int):
        # Candidate sets make lazy heap invalidation safe when indices recur.
        self.capacity = capacity
        self.stacks: List[List[int]] = []
        self.available: List[int] = []
        self.nonempty: List[int] = []
        self.available_set: Set[int] = set()
        self.nonempty_set: Set[int] = set()

    def _mark_available(self, index: int) -> None:
        # An index is stored once per heap while it remains a valid candidate.
        if index not in self.available_set:
            heapq.heappush(self.available, index)
            self.available_set.add(index)

    def _mark_nonempty(self, index: int) -> None:
        if index not in self.nonempty_set:
            heapq.heappush(self.nonempty, -index)
            self.nonempty_set.add(index)

    def push(self, val: int) -> None:
        # The minimum valid index implements leftmost non-full placement.
        # Lazy cleanup removes indices whose stacks have since filled.
        while self.available and self.available[0] not in self.available_set:
            heapq.heappop(self.available)
        if not self.available:
            self.stacks.append([])
            index = len(self.stacks) - 1
            self._mark_available(index)
        index = self.available[0]
        stack = self.stacks[index]
        was_empty = not stack
        stack.append(val)
        if len(stack) == self.capacity:
            heapq.heappop(self.available)
            self.available_set.remove(index)
        if was_empty:
            self._mark_nonempty(index)

    def _pop_index(self, index: int) -> int:
        stack = self.stacks[index]
        value = stack.pop()
        # If it becomes empty, its max-heap entry is invalidated by the set.
        # A removed value always creates a place for the next push.
        self._mark_available(index)
        if not stack:
            self.nonempty_set.remove(index)
        return value

    def pop(self) -> int:
        # Discard empty indices so the largest remaining stack is selected.
        while self.nonempty and -self.nonempty[0] not in self.nonempty_set:
            heapq.heappop(self.nonempty)
        if not self.nonempty:
            return -1
        # Negated heap indices expose the rightmost stack in logarithmic time.
        index = -self.nonempty[0]
        value = self._pop_index(index)
        if index not in self.nonempty_set:
            heapq.heappop(self.nonempty)
        return value

    def popAtStack(self, index: int) -> int:
        # Arbitrary-index removal uses the same state updates as global pop.
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1
        value = self._pop_index(index)
        return value


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    plates = None
    for op, values in zip(ops, args):
        if op == "DinnerPlates":
            plates = DinnerPlates(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(plates, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack",
         "push", "push", "popAtStack", "popAtStack", "pop", "pop", "pop",
         "pop", "pop"],
        [[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [],
         [], [], []],
    ) == [None, None, None, None, None, None, 2, None, None, 20, 21,
          5, 4, 3, 1, -1]
    print("All tests passed")
