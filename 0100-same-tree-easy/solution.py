"""
LeetCode 100: Same Tree
Difficulty: Easy
Pattern: Trees
Video Reference: https://www.youtube.com/watch?v=vRbbcKXCxOw
Complexity:
    - Time: O(min(n,m))
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
        self.val, self.left, self.right = val, left, right


# Test helper: build a tree from LeetCode level-order values, with None child slots.
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    # Each dequeued parent consumes its two serialized child positions in order.
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# Test helper: flatten level order and trim trailing missing-child markers.
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []
    out = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node is None:
            # Keep interior null slots so child positions remain aligned.
            out.append(None)
        else:
            out.append(node.val)
            q.extend([node.left, node.right])
    while out and out[-1] is None:
        out.pop()
    return out


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Paired empty branches match; a one-sided missing node breaks structure equality.
        if p is None or q is None:
            return p is q
        # Recursive calls compare matching left/right positions, not just values.
        # Values and both corresponding branches must match recursively.
        # Short-circuiting avoids descending once any paired branch differs.
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )


if __name__ == "__main__":
    solution = Solution()
    assert solution.isSameTree(build_tree([1, 2, 3]), build_tree([1, 2, 3])) is True
    assert solution.isSameTree(build_tree([1, 2]), build_tree([1, None, 2])) is False
    assert solution.isSameTree(build_tree([1, 2, 1]), build_tree([1, 1, 2])) is False
    assert solution.isSameTree(None, None) is True
    assert solution.isSameTree(build_tree([1]), build_tree([2])) is False
    print("All tests passed")
