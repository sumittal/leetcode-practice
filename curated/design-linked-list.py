from typing import List, Optional


class ListNode:
    def __init__(self, value: int = 0):
        # Nodes store one value and a pointer to the next list element.
        self.value = value
        self.next: Optional["ListNode"] = None


class MyLinkedList:
    # The dummy head and explicit size simplify boundary operations.
    # Index-based edits walk pointers rather than shifting array elements.
    # Each stored node participates in exactly one forward chain.
    def __init__(self):
        # Dummy head removes special cases for insertions and deletions at zero.
        self.head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        node = self.head.next
        # Walking exactly index links reaches the requested zero-based node.
        for _ in range(index):
            node = node.next
        return node.value

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        index = max(index, 0)
        previous = self.head
        for _ in range(index):
            previous = previous.next
        # Splicing after a predecessor handles the head through the dummy node.
        node = ListNode(val)
        node.next = previous.next
        previous.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        previous = self.head
        for _ in range(index):
            previous = previous.next
        # Bypassing one node removes it without changing the remaining order.
        previous.next = previous.next.next
        self.size -= 1


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    linked_list = None
    for operation, values in zip(ops, args):
        if operation == "MyLinkedList":
            linked_list = MyLinkedList()
            outputs.append(None)
        else:
            outputs.append(getattr(linked_list, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get",
         "deleteAtIndex", "get"],
        [[], [1], [3], [1, 2], [1], [1], [1]],
    ) == [None, None, None, None, 2, None, 3]
    assert replay(
        ["MyLinkedList", "addAtIndex", "get", "addAtIndex", "get",
         "deleteAtIndex", "get"],
        [[], [-1, 4], [0], [3, 9], [1], [2], [0]],
    ) == [None, None, 4, None, -1, None, 4]
    print("All tests passed")
