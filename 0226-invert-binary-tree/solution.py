"""
LeetCode 226: Invert Binary Tree
Difficulty: Easy
Pattern: Trees
Video Reference: https://www.youtube.com/watch?v=OnSn2XEQ4MY
Complexity:
    - Time: O(n)
    - Space: O(h) recursion stack
"""

from collections import deque
from typing import Deque, List, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


# Test helper: consume LeetCode level-order values, where None marks a missing child.
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    # No first value means there is no root, even if the list contains only None.
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    # Parents are processed in level order so subsequent values fill left then right.
    queue = deque([root])  # type: Deque[TreeNode]
    index = 1
    while queue and index < len(values):
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        # Advance the level-order cursor even when this child slot is explicitly None.
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    # Return the root after all represented child slots have been consumed.
    return root


# Test helper: serialize in level order and omit only trailing absent child slots.
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []
    values = []
    # Include missing children during traversal to preserve their level-order positions.
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            values.append(None)
        else:
            values.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    # Trailing None entries carry no structure and LeetCode omits them in examples.
    while values and values[-1] is None:
        values.pop()
    return values


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # An empty subtree stays empty and is the recursion's terminating case.
        if root is None:
            return None
        # Each node swaps the already-inverted child subtrees.
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # Return this same root after recursively mirroring both subtrees in place.
        return root


if __name__ == "__main__":
    solution = Solution()
    assert tree_to_list(solution.invertTree(build_tree([4, 2, 7, 1, 3, 6, 9]))) == [
        4,
        7,
        2,
        9,
        6,
        3,
        1,
    ]
    assert tree_to_list(solution.invertTree(build_tree([2, 1, 3]))) == [2, 3, 1]
    assert tree_to_list(solution.invertTree(build_tree([]))) == []
    assert tree_to_list(solution.invertTree(build_tree([1]))) == [1]
    assert tree_to_list(solution.invertTree(build_tree([1, 2, None]))) == [1, None, 2]
    print("All tests passed")
