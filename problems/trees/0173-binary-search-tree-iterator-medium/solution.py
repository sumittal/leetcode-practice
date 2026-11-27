"""
LeetCode 173: Binary Search Tree Iterator
Difficulty: Medium
Pattern: Trees
Video Reference: https://www.youtube.com/watch?v=RXy5RzGF5wo
Complexity:
    - Time: O(1) amortized next, O(h) worst case
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


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]) -> None:
        # The stack holds the pending nodes on the current inorder path.
        # Initialization reaches the first value without materializing the traversal.
        self.stack = []
        self._push_left(root)

    def _push_left(self, node: Optional[TreeNode]) -> None:
        # The leftmost pending node is always the next smallest value.
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # Pop the smallest pending node and defer its right subtree.
        # The right subtree can only follow this node in inorder order.
        node = self.stack.pop()
        self._push_left(node.right)
        # Remaining stack entries preserve inorder continuation.
        # Each node is pushed and popped once over the full iteration.
        return node.val

    def hasNext(self) -> bool:
        # A nonempty stack means at least one inorder value remains.
        return bool(self.stack)


if __name__ == "__main__":
    iterator = BSTIterator(build_tree([7, 3, 15, None, None, 9, 20]))
    assert iterator.hasNext() is True
    assert iterator.next() == 3
    assert iterator.next() == 7
    assert iterator.hasNext() is True
    assert iterator.next() == 9
    assert iterator.next() == 15
    assert iterator.next() == 20
    assert iterator.hasNext() is False
    assert BSTIterator(build_tree([1])).next() == 1
    print("All tests passed")
