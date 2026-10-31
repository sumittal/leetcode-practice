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
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        # A dummy predecessor handles reversal beginning at the original head.
        dummy = ListNode(0, head)
        before = dummy
        # before stops immediately before the segment that will be reordered.
        for _ in range(left - 1):
            before = before.next
        segment_head = before.next
        # Head insertion moves each next node to the front of the chosen segment.
        for _ in range(right - left):
            moved = segment_head.next
            segment_head.next = moved.next
            moved.next = before.next
            before.next = moved
            # The original segment head becomes the tail as nodes are moved.
            # Each splice preserves the untouched suffix after the segment.
        # Links outside [left, right] remain attached through before and segment_head.
        # The dummy also returns the new head when left is one.
        # Only pointers are changed; the selected values are not copied.
        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    assert list_values(
        solution.reverseBetween(build_list([1, 2, 3, 4, 5]), 2, 4)
    ) == [1, 4, 3, 2, 5]
    assert list_values(solution.reverseBetween(build_list([5]), 1, 1)) == [5]
    assert list_values(
        solution.reverseBetween(build_list([1, 2, 3]), 1, 3)
    ) == [3, 2, 1]
    print("All tests passed")
