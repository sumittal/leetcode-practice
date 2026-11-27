"""
LeetCode 431: Encode N-ary Tree to Binary Tree
Difficulty: Hard
Pattern: Tree
Video Reference: https://www.youtube.com/results?search_query=leetcode+431+Encode+N-ary+Tree+to+Binary+Tree+neetcode
Complexity:
    - Time: encode/decode O(n)
    - Space: O(h) recursion plus O(n) output tree
"""

from collections import deque
from typing import Deque, List, Optional


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        # Each node owns an ordered list of children in the original tree.
        self.children = children or []


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class Codec:
    def encode(self, root: Optional[Node]) -> Optional[TreeNode]:
        if root is None:
            return None
        # The binary node keeps the N-ary node's value unchanged.
        binary_root = TreeNode(root.val)
        # A left edge introduces the ordered children of this N-ary node.
        previous = None
        for child in root.children:
            # Recursive encoding preserves each entire child subtree.
            encoded = self.encode(child)
            if previous is None:
                binary_root.left = encoded
            else:
                previous.right = encoded
            previous = encoded
        return binary_root

    def decode(self, root: Optional[TreeNode]) -> Optional[Node]:
        if root is None:
            return None
        # The binary root's value becomes the decoded N-ary value.
        result = Node(root.val)
        child = root.left
        # Following right pointers recovers siblings in their original order.
        while child:
            result.children.append(self.decode(child))
            child = child.right
        return result


def build_nary(level: List[Optional[int]]) -> Optional[Node]:
    if not level or level[0] is None:
        return None
    # LeetCode level order separates each parent's children with None.
    root = Node(level[0])
    parents: Deque[Node] = deque([root])
    index = 2 if len(level) > 1 and level[1] is None else 1
    while parents and index < len(level):
        parent = parents.popleft()
        while index < len(level) and level[index] is not None:
            child = Node(level[index])
            parent.children.append(child)
            parents.append(child)
            index += 1
        index += 1
    return root


def serialize_nary(root: Optional[Node]) -> List[Optional[int]]:
    if root is None:
        return []
    # Emit a separator after each nonfinal group of siblings.
    result: List[Optional[int]] = [root.val, None]
    queue: Deque[Node] = deque([root])
    while queue:
        node = queue.popleft()
        result.extend(child.val for child in node.children)
        queue.extend(node.children)
        if node.children and queue:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def replay(ops: List[str], args: List[List[object]]) -> List[object]:
    codec = Codec()
    outputs: List[object] = []
    for operation, values in zip(ops, args):
        if operation == "encode":
            outputs.append(codec.encode(build_nary(values[0])))
        elif operation == "decode":
            outputs.append(codec.decode(values[0]))
        else:
            outputs.append(None)
    return outputs


if __name__ == "__main__":
    codec = Codec()
    root = build_nary([1, None, 3, 2, 4, None, 5, 6])
    encoded = codec.encode(root)
    assert serialize_nary(codec.decode(encoded)) == \
        [1, None, 3, 2, 4, None, 5, 6]
    assert serialize_nary(codec.decode(codec.encode(Node(7)))) == [7]
    assert codec.encode(None) is None
    assert codec.decode(None) is None
    print("All tests passed")
