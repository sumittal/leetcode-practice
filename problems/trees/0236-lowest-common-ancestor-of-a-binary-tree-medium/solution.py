"""
LeetCode 236: Lowest Common Ancestor of a Binary Tree
Difficulty: Medium
Pattern: Tree
Video Reference: https://www.youtube.com/results?search_query=leetcode+236+Lowest+Common+Ancestor+of+a+Binary+Tree+neetcode
Complexity:
    - Time: O(n)
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
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    cursor = 0
    index = 1
    while cursor < len(queue) and index < len(values):
        node = queue[cursor]
        cursor += 1
        if values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []
    queue = [root]
    values = []
    while queue:
        node = queue.pop(0)
        if node is None:
            values.append(None)
        else:
            values.append(node.val)
            queue.extend([node.left, node.right])
    while values and values[-1] is None:
        values.pop()
    return values


def find_node(root: Optional[TreeNode], value: int) -> Optional[TreeNode]:
    # Search by value so tests pass the actual node objects required by LeetCode.
    if root is None or root.val == value:
        return root
    return find_node(root.left, value) or find_node(root.right, value)


class Solution:
    def lowestCommonAncestor(
        self,
        root: Optional[TreeNode],
        p: TreeNode,
        q: TreeNode,
    ) -> Optional[TreeNode]:
        # Each node is examined once until both targets meet or propagate.
        # A target node is itself the ancestor candidate for its subtree.
        # Identity is used because LeetCode passes references to tree nodes.
        if root is None or root is p or root is q:
            return root
        # Non-null results from both children mean the targets split here.
        # Each recursive result is either a target or their lowest ancestor.
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        # Otherwise propagate the only target-containing subtree upward.
        # A missing result from one side leaves the other side unchanged.
        return left or right


if __name__ == "__main__":
    solution = Solution()
    root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = find_node(root, 5)
    q = find_node(root, 1)
    assert solution.lowestCommonAncestor(root, p, q).val == 3
    p = find_node(root, 5)
    q = find_node(root, 4)
    assert solution.lowestCommonAncestor(root, p, q).val == 5
    p = find_node(root, 6)
    q = find_node(root, 4)
    assert solution.lowestCommonAncestor(root, p, q).val == 5
    print("All tests passed")
