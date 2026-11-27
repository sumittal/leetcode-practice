"""
LeetCode 1261: Find Elements in a Contaminated Binary Tree
Difficulty: Medium
Pattern: Hash Table
Video Reference: https://www.youtube.com/results?search_query=leetcode+1261+Find+Elements+in+a+Contaminated+Binary+Tree+neetcode
Complexity:
    - Time: construction O(n), find O(1) expected
    - Space: O(n)
"""

from collections import deque
from typing import Deque, List, Optional, Set


class TreeNode:
    def __init__(
        self, val: int = -1, left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    # Recovery is performed once so subsequent membership queries are constant time.
    def __init__(self, root: Optional[TreeNode]):
        self.values: Set[int] = set()
        # Recovered values are independent of the original contaminated labels.
        if root is None:
            return
        # Recover values in breadth-first order from each parent's value.
        queue: Deque[tuple] = deque([(root, 0)])
        while queue:
            node, value = queue.popleft()
            # Recording each recovered value supports expected O(1) queries.
            node.val = value
            self.values.add(value)
            # Left and right children have distinct deterministic labels.
            if node.left:
                queue.append((node.left, 2 * value + 1))
            if node.right:
                # The right-child formula is paired with the left-child formula.
                queue.append((node.right, 2 * value + 2))

    def find(self, target: int) -> bool:
        # No traversal is necessary after recovery is complete.
        # Membership avoids traversing the recovered tree for each query.
        return target in self.values


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue: Deque[TreeNode] = deque([root])
    index = 1
    while queue and index < len(values):
        parent = queue.popleft()
        for side in ("left", "right"):
            if index < len(values) and values[index] is not None:
                child = TreeNode(values[index])
                setattr(parent, side, child)
                queue.append(child)
            index += 1
    return root


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    recovered = None
    for op, values in zip(ops, args):
        if op == "FindElements":
            recovered = FindElements(build_tree(values[0]))
            outputs.append(None)
        else:
            outputs.append(getattr(recovered, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["FindElements", "find", "find", "find"],
        [[[-1, None, -1]], [1], [2], [3]],
    ) == [None, False, True, False]
    root = build_tree([-1, -1, -1, -1, None, -1])
    recovered = FindElements(root)
    assert [recovered.find(value) for value in [0, 1, 2, 5]] == [
        True, True, True, True
    ]
    second = FindElements(build_tree([-1, -1, -1, -1, -1]))
    assert [second.find(value) for value in [1, 3, 5]] == [True, True, False]
    print("All tests passed")
