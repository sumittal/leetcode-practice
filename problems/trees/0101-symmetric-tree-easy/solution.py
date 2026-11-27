"""
LeetCode 101: Symmetric Tree
Difficulty: Easy
Pattern: Trees
Video Reference: https://www.youtube.com/watch?v=Mao9uzxwvmc
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
        # Consume left then right child slots in level order.
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
    # Null placeholders preserve child positions during serialization.
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


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Mirror compares corresponding positions rather than traversal order.
        def mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            # Paired recursion descends one level from each side at a time.
            if left is None or right is None:
                # Both missing children match; only one missing breaks symmetry.
                return left is right
            if left.val != right.val:
                return False
            # Outer and inner child pairs must each be mirror images.
            # Both comparisons preserve reflected left/right positions.
            return mirror(left.left, right.right) and mirror(
                left.right, right.left
            )

        # The root's left and right subtrees form the initial mirror pair.
        # No tree mutation is needed to test this structural condition.
        return root is None or mirror(root.left, root.right)


if __name__ == "__main__":
    solution = Solution()
    assert solution.isSymmetric(
        build_tree([1, 2, 2, 3, 4, 4, 3])
    ) is True
    assert solution.isSymmetric(
        build_tree([1, 2, 2, None, 3, None, 3])
    ) is False
    assert solution.isSymmetric(build_tree([])) is True
    assert solution.isSymmetric(build_tree([1])) is True
    print("All tests passed")
