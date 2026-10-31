import heapq
from typing import List, Optional, Set


class SmallestInfiniteSet:
    # next_value separates never-popped values from explicitly restored values.
    # A min-heap orders only the finite set of restored candidates.
    # addBack ignores values that remain in the untouched suffix.
    def __init__(self):
        # Values below next_value have already been popped unless restored.
        self.next_value = 1
        self.restored: List[int] = []
        self.in_heap: Set[int] = set()

    def popSmallest(self) -> int:
        if self.restored:
            # The heap always chooses the smallest explicitly restored number.
            value = heapq.heappop(self.restored)
            self.in_heap.remove(value)
            return value
        # The pointer advances through the untouched positive integer suffix.
        value = self.next_value
        self.next_value += 1
        return value

    def addBack(self, num: int) -> None:
        if num < self.next_value and num not in self.in_heap:
            # The membership set prevents duplicate heap copies of one value.
            # Only removed values below the pointer need to be restored.
            heapq.heappush(self.restored, num)
            self.in_heap.add(num)


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    numbers = None
    for operation, values in zip(ops, args):
        if operation == "SmallestInfiniteSet":
            numbers = SmallestInfiniteSet()
            outputs.append(None)
        else:
            outputs.append(getattr(numbers, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest",
         "popSmallest", "addBack", "popSmallest", "popSmallest",
         "popSmallest"],
        [[], [2], [], [], [], [1], [], [], []],
    ) == [None, None, 1, 2, 3, None, 1, 4, 5]
    assert replay(
        ["SmallestInfiniteSet", "popSmallest", "popSmallest", "addBack",
         "addBack", "popSmallest"],
        [[], [], [], [1], [1], []],
    ) == [None, 1, 2, None, None, 1]
    print("All tests passed")
