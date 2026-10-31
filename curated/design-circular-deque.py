from typing import List


class MyCircularDeque:
    def __init__(self, k: int):
        # A fixed buffer avoids shifting elements at either end.
        self.data: List[int] = [0] * k
        # Size distinguishes full from empty even when head wraps around.
        self.capacity = k
        self.head = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        # Move the logical head backward with wraparound before writing.
        # Modulo arithmetic also wraps correctly when head is at physical zero.
        # Modulo arithmetic also handles a head currently at physical index zero.
        self.head = (self.head - 1) % self.capacity
        self.data[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        # Tail is derived from the logical head and number of stored items.
        self.data[(self.head + self.size) % self.capacity] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        # The physical slot need not be cleared because size hides it.
        self.size -= 1
        return True

    def getFront(self) -> int:
        # Empty reads use the problem's sentinel rather than stale buffer data.
        return -1 if self.isEmpty() else self.data[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        # Rear wraps to the final occupied slot before the logical head.
        # Reading does not change head or size, so both operations stay constant time.
        return self.data[(self.head + self.size - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    queue = None
    for op, values in zip(ops, args):
        if op == "MyCircularDeque":
            queue = MyCircularDeque(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(queue, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["MyCircularDeque", "insertLast", "insertLast", "insertFront",
         "insertFront", "getRear", "isFull", "deleteLast", "insertFront",
         "getFront"],
        [[3], [1], [2], [3], [4], [], [], [], [4], []],
    ) == [None, True, True, True, False, 2, True, True, True, 4]
    assert replay(
        ["MyCircularDeque", "getFront", "deleteLast", "insertFront",
         "getRear"],
        [[1], [], [], [8], []],
    ) == [None, -1, False, True, 8]
    print("All tests passed")
