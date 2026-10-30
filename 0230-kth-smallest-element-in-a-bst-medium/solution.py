"""
LeetCode 230: Kth Smallest Element in a BST
Difficulty: Medium
Pattern: Trees
Video Reference: https://www.youtube.com/watch?v=5LUXSvjmGCw
Complexity:
    - Time: O(h+k)
    - Space: O(h)
"""

from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val, self.left, self.right = val, left, right


# Test helper: reconstruct a tree from level-order values and None slots.
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = [root]
    i = 1
    while q and i < len(values):
        node = q.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root


# Test helper: serialize level order while retaining meaningful None positions.
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []
    out = []
    q = [root]
    while q:
        node = q.pop(0)
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            q.extend([node.left, node.right])
    while out and out[-1] is None:
        out.pop()
    return out


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # The explicit stack stores ancestors whose left side is already exhausted.
        stack = []
        while root or stack:
            # Descend fully left before visiting a node to preserve inorder ordering.
            while root:
                # Leaving a node on the stack defers it until its left subtree is visited.
                stack.append(root)
                root = root.left
            root = stack.pop()
            # Inorder pops are sorted; the kth pop is the requested one-based rank.
            k -= 1
            if k == 0:
                return root.val
            # Only the current node is consumed; its right subtree comes next.
            root = root.right
        # Valid inputs guarantee k exists; this fallback keeps the signature total.
        return -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.kthSmallest(build_tree([3, 1, 4, None, 2]), 1) == 1
    assert solution.kthSmallest(build_tree([5, 3, 6, 2, 4, None, None, 1]), 3) == 3
    assert solution.kthSmallest(build_tree([1]), 1) == 1
    print("All tests passed")
