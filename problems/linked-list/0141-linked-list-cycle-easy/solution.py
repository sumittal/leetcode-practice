"""
LeetCode 141: Linked List Cycle
Difficulty: Easy
Pattern: Linked List
Video Reference: https://www.youtube.com/watch?v=gBTe7lFR3vc
Complexity:
    - Time: O(n)
    - Space: O(1)
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


# Test helper: pos=-1 leaves the tail open; otherwise it reconnects the tail to nodes[pos].
def build_cycle(values: List[int], pos: int) -> Optional[ListNode]:
    nodes = [ListNode(value) for value in values]
    for index in range(len(nodes) - 1):
        # Link the ordinary prefix before adding the optional final back edge.
        nodes[index].next = nodes[index + 1]
    if nodes and pos >= 0:
        # LeetCode's pos is the zero-based node that the tail reconnects to.
        nodes[-1].next = nodes[pos]
    # Empty input has no head to return, regardless of pos.
    return nodes[0] if nodes else None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow moves one link and fast two, so they can meet only after entering a cycle.
        slow = head
        fast = head
        # The guard ensures both links needed for fast's two-step move exist.
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            # Identity meeting means both pointers entered the same cycle.
            if slow is fast:
                return True
        # A fast pointer that reaches None proves the chain terminates without a cycle.
        return False


if __name__ == "__main__":
    solution = Solution()
    assert solution.hasCycle(build_cycle([3, 2, 0, -4], 1)) is True
    assert solution.hasCycle(build_cycle([1, 2], 0)) is True
    assert solution.hasCycle(build_cycle([1], -1)) is False
    assert solution.hasCycle(build_cycle([], -1)) is False
    assert solution.hasCycle(build_cycle([1], 0)) is True
    print("All tests passed")
