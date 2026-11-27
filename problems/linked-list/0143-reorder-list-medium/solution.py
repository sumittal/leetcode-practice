"""
LeetCode 143: Reorder List
Difficulty: Medium
Pattern: Linked List
Video Reference: https://www.youtube.com/watch?v=S5bfdUTrKLM
Complexity:
    - Time: O(n)
    - Space: O(1)
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


# Test helper: build a fresh chain so mutation assertions do not reuse old links.
def build_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


# Test helper: observe the reordered links as a plain value sequence.
def to_list(head: Optional[ListNode]) -> List[int]:
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Lists shorter than two nodes already have the requested order.
        if head is None or head.next is None:
            return None

        # slow finds the end of the first half while fast advances two links at a time.
        slow = head
        fast = head
        # This bound leaves slow at the first-half end for both odd and even lengths.
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Detach the second half before reversing so the original halves are separate.
        second = slow.next
        slow.next = None
        # Reverse the detached back half so its nodes can be woven from the tail inward.
        previous = None
        while second is not None:
            # Keep the remaining second-half suffix before redirecting this link.
            following = second.next
            second.next = previous
            previous = second
            second = following

        # The first half stays forward; previous is the reversed second-half head.
        first = head
        second = previous
        # Each iteration inserts one back-half node after the next front-half node.
        while second is not None:
            # Save both next links before the weave overwrites either one.
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            # Advance both cursors to the unlinked portions of their respective halves.
            first = first_next
            second = second_next
        # LeetCode requires in-place mutation and an explicit None return.
        return None


if __name__ == "__main__":
    solution = Solution()
    head = build_list([1, 2, 3, 4])
    assert solution.reorderList(head) is None
    assert to_list(head) == [1, 4, 2, 3]
    head = build_list([1, 2, 3, 4, 5])
    assert solution.reorderList(head) is None
    assert to_list(head) == [1, 5, 2, 4, 3]
    head = build_list([])
    assert solution.reorderList(head) is None
    assert to_list(head) == []
    head = build_list([1])
    assert solution.reorderList(head) is None
    assert to_list(head) == [1]
    head = build_list([1, 2, 3])
    assert solution.reorderList(head) is None
    assert to_list(head) == [1, 3, 2]
    print("All tests passed")
