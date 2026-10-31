"""
LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal
Difficulty: Medium
Pattern: Trees
Video Reference: https://www.youtube.com/watch?v=ihj4IQGZ2zc
Complexity:
    - Time: O(n)
    - Space: O(n)
"""

from typing import Dict, List, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val, self.left, self.right = val, left, right


# Test helper: parse level order, where None explicitly marks a missing child.
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = [root]
    # Queue order associates each pair of child slots with its parent.
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


# Test helper: serialize a tree in level order, retaining interior None markers.
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []
    result = []
    q = [root]
    while q:
        node = q.pop(0)
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            q.extend([node.left, node.right])
    while result and result[-1] is None:
        result.pop()
    return result


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Unique values let each inorder position identify one subtree split.
        positions = {value: i for i, value in enumerate(inorder)}
        # cursor consumes preorder exactly once, in root-left-right order.
        cursor = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal cursor
            # Half-open inorder bounds describe exactly this recursive subtree.
            if left >= right:
                return None
            # Preorder's next value is this subtree root; inorder splits its children.
            value = preorder[cursor]
            cursor += 1
            middle = positions[value]
            # Consume left before right because preorder lists root-left-right.
            return TreeNode(value, build(left, middle), build(middle + 1, right))

        return build(0, len(inorder))


if __name__ == "__main__":
    solution = Solution()
    assert tree_to_list(solution.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])) == [
        3,
        9,
        20,
        None,
        None,
        15,
        7,
    ]
    assert tree_to_list(solution.buildTree([-1], [-1])) == [-1]
    assert tree_to_list(solution.buildTree([], [])) == []
    print("All tests passed")
