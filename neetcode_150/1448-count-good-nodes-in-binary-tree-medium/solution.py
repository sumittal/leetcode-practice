"""
LeetCode 1448: Count Good Nodes in Binary Tree
Difficulty: Medium
Pattern: Trees
Video Reference: https://www.youtube.com/watch?v=7cp5imvDzl4
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


# Test helper: build level-order tree values, using None for a missing child.
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
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            # No root-to-node paths exist in an empty tree.
            return 0

        def count(node: Optional[TreeNode], path_max: int) -> int:
            # The carried maximum contains exactly the ancestor values on this path.
            if node is None:
                # A missing child contributes no nodes to the count.
                return 0
            # Equality qualifies because a good node need not exceed its ancestors.
            is_good = node.val >= path_max
            # Advancing this maximum prevents smaller descendants from qualifying.
            next_max = max(path_max, node.val)
            # Both children inherit the same updated maximum from their shared path.
            return (
                int(is_good)
                + count(node.left, next_max)
                + count(node.right, next_max)
            )

        # Include the root; its initial path maximum is its own value.
        return count(root, root.val)


if __name__ == "__main__":
    solution = Solution()
    assert solution.goodNodes(build_tree([3, 1, 4, 3, None, 1, 5])) == 4
    assert solution.goodNodes(build_tree([3, 3, None, 4, 2])) == 3
    assert solution.goodNodes(build_tree([1])) == 1
    assert solution.goodNodes(build_tree([-1, -2, -3])) == 1
    assert solution.goodNodes(build_tree([])) == 0
    print("All tests passed")
