"""
LeetCode 530: Minimum Absolute Difference in BST
Difficulty: Easy
Pattern: Tree
Video Reference: https://www.youtube.com/results?search_query=leetcode+530+Minimum+Absolute+Difference+in+BST+neetcode
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


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Inorder traversal exposes all keys in sorted order.
        # The stack simulates recursive inorder traversal without recursion depth.
        stack = []
        current = root
        previous = None
        minimum = float("inf")
        while current or stack:
            while current:
                # Save ancestors until the next smallest node is ready.
                stack.append(current)
                current = current.left
            current = stack.pop()
            # Inorder values are sorted, so only the preceding value can be closest.
            # Any nonadjacent pair has an intervening value and cannot be smaller.
            if previous is not None:
                minimum = min(minimum, current.val - previous)
            previous = current.val
            current = current.right
            # Moving right begins the next sorted portion of the traversal.
        # The problem guarantees at least two nodes and a finite difference.
        # The finite answer is a difference between two adjacent keys.
        return int(minimum)


if __name__ == "__main__":
    solution = Solution()
    assert solution.getMinimumDifference(build_tree([4, 2, 6, 1, 3])) == 1
    assert solution.getMinimumDifference(
        build_tree([1, 0, 48, None, None, 12, 49])
    ) == 1
    assert solution.getMinimumDifference(build_tree([2, 1, 3])) == 1
    print("All tests passed")
