"""
LeetCode 21: Merge Two Sorted Lists
Difficulty: Easy
Pattern: Linked List
Video Reference: https://www.youtube.com/watch?v=XIdigk956u0
Complexity:
    - Time: O(m+n)
    - Space: O(1) extra
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


# Test helper: build a fresh sorted chain for one input list.
def build_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


# Test helper: collect the merged chain's values for assertions.
def to_list(head: Optional[ListNode]) -> List[int]:
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # A sentinel keeps the result assembly uniform, including when either list is empty.
        dummy = ListNode()
        # tail always marks the final node linked into the merged prefix.
        tail = dummy
        # Continue only while both lists have a head to compare.
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                # Choosing list1 on ties preserves sorted order and consumes one node.
                tail.next = list1
                list1 = list1.next
            else:
                # list2 has the smaller head, so append it and advance that input.
                tail.next = list2
                list2 = list2.next
            # The selected node is now the merged prefix's new tail.
            tail = tail.next

        # Only one remainder can be nonempty; it is already sorted.
        tail.next = list1 if list1 is not None else list2
        # The sentinel itself is not part of the answer.
        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    assert to_list(
        solution.mergeTwoLists(build_list([1, 2, 4]), build_list([1, 3, 4]))
    ) == [1, 1, 2, 3, 4, 4]
    assert to_list(solution.mergeTwoLists(build_list([]), build_list([]))) == []
    assert to_list(solution.mergeTwoLists(build_list([]), build_list([0]))) == [0]
    assert to_list(solution.mergeTwoLists(build_list([1, 2]), build_list([3]))) == [
        1,
        2,
        3,
    ]
    print("All tests passed")
