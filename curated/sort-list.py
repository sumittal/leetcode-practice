from typing import List, Optional


class ListNode:
    def __init__(
        self, val: int = 0, next: Optional["ListNode"] = None
    ) -> None:
        self.val = val
        self.next = next


def list_from_values(values: List[int]) -> Optional[ListNode]:
    # A dummy head keeps construction uniform for empty and nonempty lists.
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def list_values(head: Optional[ListNode]) -> List[int]:
    # Serialization follows next pointers until the sorted tail.
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Zero or one node is already a sorted list.
        if head is None or head.next is None:
            return head
        # Slow and fast pointers find the midpoint without counting nodes.
        # Fast advances twice as quickly to locate the split point.
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Detach the halves so recursive calls terminate independently.
        right = slow.next
        slow.next = None
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(right)
        # Merge by relinking existing nodes, not copying values.
        dummy = ListNode()
        tail = dummy
        while left_sorted and right_sorted:
            if left_sorted.val <= right_sorted.val:
                tail.next = left_sorted
                left_sorted = left_sorted.next
            else:
                tail.next = right_sorted
                right_sorted = right_sorted.next
            tail = tail.next
        tail.next = left_sorted or right_sorted
        # Every merge level processes all nodes once.
        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    assert list_values(solution.sortList(list_from_values([4, 2, 1, 3]))) == [
        1,
        2,
        3,
        4,
    ]
    assert list_values(
        solution.sortList(list_from_values([-1, 5, 3, 4, 0]))
    ) == [-1, 0, 3, 4, 5]
    assert list_values(solution.sortList(list_from_values([]))) == []
    assert list_values(solution.sortList(list_from_values([1, 1, -2]))) == [
        -2,
        1,
        1,
    ]
    print("All tests passed")
