"""
LeetCode 19: Remove Nth Node From End of List
Difficulty: Medium
Pattern: Linked List
Video Reference: https://www.youtube.com/watch?v=XVuQxVej6y8
Complexity:
    - Time: O(n)
    - Space: O(1)
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


# Test helper: build a fresh chain, including None for the empty-list case.
def build_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


# Test helper: serialize the remaining chain after a node is removed.
def to_list(head: Optional[ListNode]) -> List[int]:
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        # The sentinel gives the head a predecessor when the head itself is removed.
        dummy = ListNode(0, head)
        # Starting together, fast is advanced n links to establish a fixed gap.
        fast = dummy
        slow = dummy
        for _ in range(n):
            fast = fast.next
        # Move in lockstep until fast reaches the tail; slow then precedes the target.
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        # The n-node gap leaves slow immediately before the node to remove.
        # The problem guarantees n is valid, so slow.next is the target node here.
        slow.next = slow.next.next
        # Return through the sentinel to handle both head removal and other positions.
        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    assert to_list(solution.removeNthFromEnd(build_list([1, 2, 3, 4, 5]), 2)) == [
        1,
        2,
        3,
        5,
    ]
    assert to_list(solution.removeNthFromEnd(build_list([1]), 1)) == []
    assert to_list(solution.removeNthFromEnd(build_list([1, 2]), 1)) == [1]
    assert to_list(solution.removeNthFromEnd(build_list([1, 2, 3]), 3)) == [2, 3]
    assert to_list(solution.removeNthFromEnd(build_list([1, 2]), 2)) == [2]
    print("All tests passed")
