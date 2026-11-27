"""
LeetCode 449: Serialize and Deserialize BST
Difficulty: Medium
Pattern: String
Video Reference: https://www.youtube.com/results?search_query=leetcode+449+Serialize+and+Deserialize+BST+neetcode
Complexity:
    - Time: serialize O(n), deserialize O(n)
    - Space: O(n)
"""

from collections import deque
from typing import Deque, List, Optional


class TreeNode:
    def __init__(
        self, val: int = 0, left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        values: List[str] = []
        # A stack keeps preorder traversal safe for highly skewed trees.
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            values.append(str(node.val))
            # Push right first because the left subtree must be visited first.
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ",".join(values)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        # The preorder stream itself determines every missing-child boundary.
        values = [int(value) for value in data.split(",")]
        root = TreeNode(values[0])
        ancestors = [root]
        for value in values[1:]:
            node = TreeNode(value)
            # A smaller value begins the left subtree of the current ancestor.
            if value < ancestors[-1].val:
                ancestors[-1].left = node
            else:
                parent = None
                while ancestors and value > ancestors[-1].val:
                    parent = ancestors.pop()
                parent.right = node
            ancestors.append(node)
        return root


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    nodes: Deque[TreeNode] = deque([root])
    index = 1
    while nodes and index < len(values):
        parent = nodes.popleft()
        for side in ("left", "right"):
            if index < len(values) and values[index] is not None:
                child = TreeNode(values[index])
                setattr(parent, side, child)
                nodes.append(child)
            index += 1
    return root


def tree_shape(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []
    result: List[Optional[int]] = []
    nodes: Deque[Optional[TreeNode]] = deque([root])
    while nodes:
        node = nodes.popleft()
        result.append(node.val if node else None)
        if node:
            nodes.extend([node.left, node.right])
    while result and result[-1] is None:
        result.pop()
    return result


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    codec = Codec()
    for op, values in zip(ops, args):
        result = getattr(codec, op)(*values)
        outputs.append(tree_shape(result) if op == "deserialize" else result)
    return outputs


if __name__ == "__main__":
    codec = Codec()
    # Build a tree with both missing and present child links.
    original = build_tree([5, 3, 6, 2, 4, None, 7])
    # The codec emits preorder values, using BST ordering to infer missing links.
    encoded = codec.serialize(original)
    restored = codec.deserialize(encoded)
    # Compare level-order shape as well as values to verify structural preservation.
    assert tree_shape(restored) == tree_shape(original)
    # Empty and single-node inputs exercise the two smallest valid trees.
    assert codec.serialize(None) == ""
    assert tree_shape(codec.deserialize("")) == []
    assert tree_shape(codec.deserialize("1")) == [1]
    assert replay(["serialize", "deserialize"], [[original], [encoded]]) == [
        encoded, tree_shape(original)
    ]
    print("All tests passed")
