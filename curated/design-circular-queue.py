from typing import List, Optional, Union


class MyCircularQueue:
    # Fixed storage and a count provide constant-time bounded queue operations.
    def __init__(self, k: int):
        # Allocate once so operations never need to resize or shift the queue.
        self.data: List[int] = [0] * k
        self.capacity = k
        # Front points at the oldest item; size separates empty from full.
        self.front_index = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        # The next tail position is computed from front plus current length.
        tail = (self.front_index + self.size) % self.capacity
        self.data[tail] = value
        self.size += 1
        # The count, rather than a reserved empty slot, tracks fullness.
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        # Advancing the head releases one slot without shifting stored values.
        self.front_index = (self.front_index + 1) % self.capacity
        self.size -= 1
        # Modulo wrapping reuses storage freed at the start of the array.
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.front_index]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        # Modulo maps the logical last element to its wrapped physical slot.
        return self.data[(self.front_index + self.size - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


def replay(
    ops: List[str], args: List[List[int]]
) -> List[Optional[Union[int, bool]]]:
    outputs: List[Optional[Union[int, bool]]] = []
    queue = None
    for operation, values in zip(ops, args):
        if operation == "MyCircularQueue":
            queue = MyCircularQueue(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(queue, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue",
         "Rear", "isFull", "deQueue", "enQueue", "Rear"],
        [[3], [1], [2], [3], [4], [], [], [], [4], []],
    ) == [None, True, True, True, False, 3, True, True, True, 4]
    assert replay(
        ["MyCircularQueue", "Front", "Rear", "deQueue", "enQueue", "Front"],
        [[1], [], [], [], [9], []],
    ) == [None, -1, -1, False, True, 9]
    print("All tests passed")
