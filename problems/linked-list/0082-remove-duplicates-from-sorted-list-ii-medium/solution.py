"""
LeetCode 82: Remove Duplicates from Sorted List II
Difficulty: Medium
Pattern: Linked List
Video Reference: https://www.youtube.com/results?search_query=leetcode+82+Remove+Duplicates+from+Sorted+List+II+neetcode
Complexity:
    - Time: O(n)
    - Space: O(1)
"""

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
    def deleteDuplicates(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        # The dummy node gives the first kept node a stable predecessor.
        dummy = ListNode(0, head)
        previous = dummy
        current = head
        # current scans input nodes while previous anchors the retained prefix.
        while current:
            # Detect a repeated run by comparing adjacent sorted values.
            if current.next and current.val == current.next.val:
                duplicate_value = current.val
                while current and current.val == duplicate_value:
                    current = current.next
                # Bypass every occurrence so none of a duplicate run survives.
                previous.next = current
            else:
                # A unique node remains linked and becomes the next predecessor.
                previous = current
                current = current.next
            # Removed nodes never replace previous, so the skipped run stays detached.
            # previous always points to the last retained node or the dummy.
        # The retained list is the original nodes with duplicate runs unlinked.
        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    assert list_values(
        solution.deleteDuplicates(build_list([1, 2, 3, 3, 4, 4, 5]))
    ) == [1, 2, 5]
    assert list_values(
        solution.deleteDuplicates(build_list([1, 1, 1, 2, 3]))
    ) == [2, 3]
    assert list_values(solution.deleteDuplicates(build_list([]))) == []
    assert list_values(solution.deleteDuplicates(build_list([1]))) == [1]
    print("All tests passed")
