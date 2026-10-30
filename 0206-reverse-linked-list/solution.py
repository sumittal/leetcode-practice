"""
LeetCode 206: Reverse Linked List
Difficulty: Easy
Pattern: Linked List
Video Reference: https://www.youtube.com/watch?v=G0_I-ZF0S38
Complexity:
    - Time: O(n)
    - Space: O(1)
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


# Test helper: build a fresh acyclic chain in the same order as the input values.
def build_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


# Test helper: read node values in order without changing the links.
def to_list(head: Optional[ListNode]) -> List[int]:
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # previous is the reversed prefix; current begins the untouched suffix.
        previous = None
        current = head
        # A missing current node means the entire original chain has been processed.
        while current is not None:
            # Preserve the next suffix node before changing current's outgoing edge.
            following = current.next
            # Save the untouched suffix before redirecting this link backward.
            current.next = previous
            # Extend the reversed prefix by one node.
            previous = current
            # Continue from the saved suffix, not from the newly reversed link.
            current = following
        # previous is now the new head; it is None for an empty input.
        return previous


if __name__ == "__main__":
    solution = Solution()
    assert to_list(solution.reverseList(build_list([1, 2, 3, 4, 5]))) == [
        5,
        4,
        3,
        2,
        1,
    ]
    assert to_list(solution.reverseList(build_list([1, 2]))) == [2, 1]
    assert to_list(solution.reverseList(build_list([]))) == []
    assert to_list(solution.reverseList(build_list([7]))) == [7]
    print("All tests passed")
