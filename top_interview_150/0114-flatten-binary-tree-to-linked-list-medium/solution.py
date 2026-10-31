"""
LeetCode 114: Flatten Binary Tree to Linked List
Difficulty: Medium
Pattern: Linked List
Video Reference: https://www.youtube.com/results?search_query=leetcode+114+Flatten+Binary+Tree+to+Linked+List+neetcode
Complexity:
    - Time: O(n)
    - Space: O(1)
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


def right_chain(root: Optional[TreeNode]) -> List[int]:
    # Collecting values also detects any accidental cycle in the flattened chain.
    values = []
    while root:
        assert root.left is None
        values.append(root.val)
        root = root.right
    return values


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        # The current pointer visits nodes in the chain being built.
        # Its right pointer is the next node in preorder after each splice.
        current = root
        while current:
            if current.left:
                # Find the last node of the left subtree's existing right boundary.
                predecessor = current.left
                while predecessor.right:
                    predecessor = predecessor.right
                # Preserve the old right subtree after the left subtree.
                predecessor.right = current.right
                current.right = current.left
                current.left = None
                # This splice places the left subtree at its preorder position.
                # The predecessor's new link preserves the original right branch.
            # Advancing along right pointers visits the resulting preorder chain.
            current = current.right
        # Every node is rewired in place; the method returns None.


if __name__ == "__main__":
    solution = Solution()
    root = build_tree([1, 2, 5, 3, 4, None, 6])
    assert solution.flatten(root) is None
    assert right_chain(root) == [1, 2, 3, 4, 5, 6]
    assert right_chain(build_tree([0])) == [0]
    assert solution.flatten(None) is None
    print("All tests passed")
