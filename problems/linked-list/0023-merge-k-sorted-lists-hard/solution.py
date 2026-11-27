"""
LeetCode 23: Merge k Sorted Lists
Difficulty: Hard
Pattern: Linked List
Video Reference: https://www.youtube.com/watch?v=q5a5OiGbT6Q
Complexity:
    - Time: O(n log k)
    - Space: O(k) heap
"""

import heapq
from typing import List, Optional, Tuple


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


# Test helper: build one sorted linked list from its level-order value sequence.
def build_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


# Test helper: build independent list heads for the merge test cases.
def build_lists(values: List[List[int]]) -> List[Optional[ListNode]]:
    return [build_list(items) for items in values]


# Test helper: flatten the merged list to compare its sorted values.
def to_list(head: Optional[ListNode]) -> List[int]:
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Heap entries hold one available head per list; index breaks value ties.
        heap = []  # type: List[Tuple[int, int, ListNode]]
        for index, node in enumerate(lists):
            if node is not None:
                # Seed only nonempty lists so every heap entry is a real candidate node.
                heapq.heappush(heap, (node.val, index, node))

        # The sentinel makes appending the first and later nodes use the same operation.
        dummy = ListNode()
        # tail ends the sorted prefix assembled from nodes already removed from the heap.
        tail = dummy
        # The smallest remaining head is always the next node in the global merge.
        while heap:
            value, list_index, node = heapq.heappop(heap)
            tail.next = node
            tail = node
            if node.next is not None:
                # The list index breaks equal-value ties; ListNode is not comparable.
                # Push only this list's successor, preserving one active heap entry per list.
                heapq.heappush(heap, (node.next.val, list_index, node.next))
        # The heap empties after every input node has been appended in sorted order.
        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    assert to_list(
        solution.mergeKLists(build_lists([[1, 4, 5], [1, 3, 4], [2, 6]]))
    ) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert to_list(solution.mergeKLists(build_lists([]))) == []
    assert to_list(solution.mergeKLists(build_lists([[]]))) == []
    assert to_list(solution.mergeKLists(build_lists([[1], [1]]))) == [1, 1]
    assert to_list(solution.mergeKLists(build_lists([[-2, 3], [-1, 2]]))) == [
        -2,
        -1,
        2,
        3,
    ]
    print("All tests passed")
