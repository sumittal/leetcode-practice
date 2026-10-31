from typing import List, Optional


class ListNode:
    def __init__(
        self, val: int = 0, next: Optional["ListNode"] = None
    ) -> None:
        self.val = val
        self.next = next


def build_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def list_values(head: Optional[ListNode]) -> List[int]:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


class Solution:
    def rotateRight(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        # Lists shorter than two nodes have no distinct rotation.
        if not head or not head.next:
            return head
        # Count nodes and locate the tail before forming the temporary ring.
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        # Full rotations have no effect and avoid unnecessary relinking.
        k %= length
        # Modulo confines the split point to one traversal of the list.
        if k == 0:
            return head
        tail.next = head
        # The new tail is length-k steps from the original head.
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        # Breaking the ring restores a finite list from the new head.
        # Exactly k original tail nodes now precede the old head.
        # The operation changes links but allocates no replacement nodes.
        return new_head


if __name__ == "__main__":
    solution = Solution()
    assert list_values(
        solution.rotateRight(build_list([1, 2, 3, 4, 5]), 2)
    ) == [4, 5, 1, 2, 3]
    assert list_values(
        solution.rotateRight(build_list([0, 1, 2]), 4)
    ) == [2, 0, 1]
    assert list_values(solution.rotateRight(build_list([]), 3)) == []
    assert list_values(solution.rotateRight(build_list([1]), 10)) == [1]
    print("All tests passed")
