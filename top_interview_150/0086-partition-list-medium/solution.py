"""
LeetCode 86: Partition List
Difficulty: Medium
Pattern: Linked List
Video Reference: https://www.youtube.com/watch?v=KT1iUciJr4g
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
    def partition(
        self, head: Optional[ListNode], x: int
    ) -> Optional[ListNode]:
        # Sentinels keep appending independent of whether either side is empty.
        before = ListNode()
        after = ListNode()
        before_tail = before
        after_tail = after
        current = head
        # Each original node is routed to exactly one stable output chain.
        while current:
            following = current.next
            current.next = None
            # Detach first so old links cannot connect the two output partitions.
            if current.val < x:
                before_tail.next = current
                before_tail = current
            else:
                # Equal values belong after the strict-less-than partition.
                after_tail.next = current
                after_tail = current
            # Advancing through the saved successor preserves every input node.
            current = following
            # Appending existing nodes preserves their original relative order.
        before_tail.next = after.next
        # Termination above prevents a stale tail link from creating a cycle.
        # Connecting sentinels handles either empty side without special cases.
        return before.next


if __name__ == "__main__":
    solution = Solution()
    assert list_values(
        solution.partition(build_list([1, 4, 3, 2, 5, 2]), 3)
    ) == [1, 2, 2, 4, 3, 5]
    assert list_values(
        solution.partition(build_list([2, 1]), 2)
    ) == [1, 2]
    assert list_values(solution.partition(build_list([]), 3)) == []
    print("All tests passed")
