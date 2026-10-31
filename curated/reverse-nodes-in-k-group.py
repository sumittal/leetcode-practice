from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


# Test helper: construct a linked list from its node values.
def build_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


# Test helper: collect list values to verify both order and unchanged suffixes.
def list_values(head: Optional[ListNode]) -> List[int]:
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


class Solution:
    def reverseKGroup(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        # A dummy predecessor simplifies replacing the head after the first reversal.
        dummy = ListNode(0, head)
        group_previous = dummy
        while True:
            # Locate the kth node first so incomplete suffixes are never modified.
            # The search begins at the boundary immediately before this group.
            kth = group_previous
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    # Fewer than k nodes remain; preserve their original links.
                    return dummy.next
            # group_next is an exclusive endpoint and is not part of this reversal.
            group_next = kth.next
            # Reverse links only within this complete group, ending at group_next.
            # Initializing the predecessor to the suffix reconnects the reversed tail.
            previous = group_next
            current = group_previous.next
            while current is not group_next:
                following = current.next
                current.next = previous
                previous = current
                current = following
            # The old first node is now the tail and becomes the next predecessor.
            old_group_head = group_previous.next
            group_previous.next = kth
            # The kth node is now the group's head and its predecessor link is repaired.
            group_previous = old_group_head
        # Every return happens after an incomplete suffix has been left untouched.


if __name__ == "__main__":
    solution = Solution()
    assert list_values(
        solution.reverseKGroup(build_list([1, 2, 3, 4, 5]), 2)
    ) == [2, 1, 4, 3, 5]
    assert list_values(
        solution.reverseKGroup(build_list([1, 2, 3, 4, 5]), 3)
    ) == [3, 2, 1, 4, 5]
    assert list_values(solution.reverseKGroup(build_list([1, 2]), 3)) == [1, 2]
    assert list_values(solution.reverseKGroup(build_list([]), 2)) == []
    assert list_values(solution.reverseKGroup(build_list([1]), 1)) == [1]
    print("All tests passed")
