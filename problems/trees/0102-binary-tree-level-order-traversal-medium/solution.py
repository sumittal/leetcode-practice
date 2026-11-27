"""
LeetCode 102: Binary Tree Level Order Traversal
Difficulty: Medium
Pattern: Trees
Video Reference: https://www.youtube.com/watch?v=6ZnyEApgFYg
Complexity:
    - Time: O(n)
    - Space: O(n)
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val, self.left, self.right = val, left, right


# Test helper: build a tree from level-order values; None represents a missing child.
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    # i identifies the next child token while q supplies the parent for both slots.
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root


# Test helper: convert a tree back to LeetCode's level-order notation.
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []
    out = []
    q = deque([root])
    # Appending both children preserves positions of missing nodes in later levels.
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            q.extend([node.left, node.right])
    while out and out[-1] is None:
        out.pop()
    return out


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        # An empty tree has no levels to enqueue or emit.
        # The root seeds the first level and guarantees the initial queue is nonempty.
        levels = []
        queue = deque([root])
        while queue:
            # Queue order is left-to-right because children are appended in that order.
            # Freeze this level's width so newly appended children wait for next round.
            width = len(queue)
            level = []
            for _ in range(width):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        # Appending levels in queue order preserves left-to-right depth order.
        return levels


if __name__ == "__main__":
    solution = Solution()
    assert solution.levelOrder(build_tree([3, 9, 20, None, None, 15, 7])) == [
        [3],
        [9, 20],
        [15, 7],
    ]
    assert solution.levelOrder(build_tree([1])) == [[1]]
    assert solution.levelOrder(None) == []
    print("All tests passed")
