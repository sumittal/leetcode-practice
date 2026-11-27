"""
LeetCode 543: Diameter of Binary Tree
Difficulty: Easy
Pattern: Trees
Video Reference: https://www.youtube.com/watch?v=bkxqA8Rfv04
Complexity:
    - Time: O(n)
    - Space: O(h)
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


# Test helper: build a binary tree from level-order values and None markers.
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue: Deque[TreeNode] = deque([root])
    index = 1
    while queue and index < len(values):
        parent = queue.popleft()
        if values[index] is not None:
            parent.left = TreeNode(values[index])
            queue.append(parent.left)
        index += 1
        if index < len(values) and values[index] is not None:
            parent.right = TreeNode(values[index])
            queue.append(parent.right)
        index += 1
    return root


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Store the best edge count even when the longest path does not use the root.
        diameter = 0

        def height(node: Optional[TreeNode]) -> int:
            # Return height in nodes so child heights combine into path edge count.
            nonlocal diameter
            if node is None:
                # A missing child contributes zero nodes to its parent's height.
                return 0
            # Postorder traversal finishes both child heights before evaluating this turn.
            left_height = height(node.left)
            right_height = height(node.right)
            # A path turning here has one edge for each level below this node.
            diameter = max(diameter, left_height + right_height)
            # The caller may extend through only one child of this node.
            return 1 + max(left_height, right_height)

        height(root)
        # The accumulated value measures edges, matching the problem definition.
        return diameter


if __name__ == "__main__":
    solution = Solution()
    assert solution.diameterOfBinaryTree(build_tree([1, 2, 3, 4, 5])) == 3
    assert solution.diameterOfBinaryTree(build_tree([1, 2])) == 1
    assert solution.diameterOfBinaryTree(build_tree([1])) == 0
    assert solution.diameterOfBinaryTree(build_tree([])) == 0
    print("All tests passed")
