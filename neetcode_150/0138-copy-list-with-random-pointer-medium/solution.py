"""
LeetCode 138: Copy List with Random Pointer
Difficulty: Medium
Pattern: Linked List
Video Reference: https://www.youtube.com/watch?v=5Y2EiZST97Y
Complexity:
    - Time: O(n)
    - Space: O(n)
"""

from typing import Dict, List, Optional


class Node:
    def __init__(
        self,
        x: int,
        next: Optional["Node"] = None,
        random: Optional["Node"] = None,
    ) -> None:
        self.val = x
        self.next = next
        self.random = random


# Test helper: build next links and random links from value/index pairs.
def build_random_list(
    records: List[List[Optional[int]]],
) -> Optional[Node]:
    nodes = [Node(record[0]) for record in records]
    for index, record in enumerate(records):
        # Adjacent records form the ordinary next chain.
        if index + 1 < len(nodes):
            nodes[index].next = nodes[index + 1]
        # Random indices refer to the corresponding node in the input list.
        if record[1] is not None:
            nodes[index].random = nodes[record[1]]
    return nodes[0] if nodes else None


# Test helper: expose random edges as indices without relying on node identity.
def random_list_signature(head: Optional[Node]) -> List[List[Optional[int]]]:
    nodes = []
    current = head
    while current is not None:
        nodes.append(current)
        current = current.next
    positions = {node: index for index, node in enumerate(nodes)}
    # A null random edge remains None; all others map to copied-list positions.
    return [[node.val, positions.get(node.random)] for node in nodes]


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None
        # The map guarantees one distinct clone per source node.
        copies: Dict[Node, Node] = {}
        current = head
        while current is not None:
            copies[current] = Node(current.val)
            current = current.next
        current = head
        while current is not None:
            clone = copies[current]
            # Rewire both edge types through the map, preserving null pointers.
            clone.next = copies.get(current.next)
            clone.random = copies.get(current.random)
            current = current.next
        # Returning the mapped head leaves the source list and its links untouched.
        return copies[head]


if __name__ == "__main__":
    solution = Solution()
    examples = [
        [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        [[1, 1], [2, 1]],
        [[3, None]],
    ]
    for records in examples:
        original = build_random_list(records)
        copied = solution.copyRandomList(original)
        assert random_list_signature(copied) == records
        original_nodes = []
        copied_nodes = []
        original_current = original
        copied_current = copied
        while original_current is not None and copied_current is not None:
            original_nodes.append(original_current)
            copied_nodes.append(copied_current)
            original_current = original_current.next
            copied_current = copied_current.next
        assert len(original_nodes) == len(copied_nodes)
        assert all(source is not clone for source, clone in zip(original_nodes, copied_nodes))
        assert not (set(original_nodes) & set(copied_nodes))
        clone_for_source = dict(zip(original_nodes, copied_nodes))
        # Identity checks prove that neither next nor random edges point to originals.
        for source, clone in zip(original_nodes, copied_nodes):
            assert clone.next is clone_for_source.get(source.next)
            assert clone.random is clone_for_source.get(source.random)
    assert solution.copyRandomList(None) is None
    print("All tests passed")
