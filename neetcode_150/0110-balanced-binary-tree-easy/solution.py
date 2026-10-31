"""
LeetCode 110: Balanced Binary Tree
Difficulty: Easy
Pattern: Trees
Video Reference: https://www.youtube.com/watch?v=QfJsau0ItOY
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


# Test helper: build a tree from level-order values with None child slots.
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height_or_unbalanced(node: Optional[TreeNode]) -> int:
            # Return height for balanced subtrees and -1 to propagate failure upward.
            if node is None:
                # An empty subtree has height zero.
                return 0
            left_height = height_or_unbalanced(node.left)
            if left_height == -1:
                # No ancestor needs heights once a child is already unbalanced.
                return -1
            right_height = height_or_unbalanced(node.right)
            if right_height == -1:
                # An unbalanced right subtree also makes this whole subtree unbalanced.
                return -1
            # Balanced nodes differ by at most one level between child heights.
            if abs(left_height - right_height) > 1:
                return -1
            # The parent receives this subtree's height only after both checks pass.
            return 1 + max(left_height, right_height)

        # A nonnegative height means the sentinel never found an imbalance.
        return height_or_unbalanced(root) != -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.isBalanced(build_tree([3, 9, 20, None, None, 15, 7])) is True
    assert solution.isBalanced(
        build_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    ) is False
    assert solution.isBalanced(build_tree([])) is True
    assert solution.isBalanced(build_tree([1, 2, None, 3, None, 4])) is False
    print("All tests passed")
