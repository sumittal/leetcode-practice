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


class BSTIterator:
    # An inorder list supports both directions without rebuilding a traversal.
    # The cursor always denotes the most recently returned value.
    # The leftmost entry is reached by the first call to next().
    # Valid callers use hasPrev/hasNext to guard cursor movement.
    def __init__(self, root: Optional[TreeNode]):
        self.values: List[int] = []
        stack: List[TreeNode] = []
        node = root
        # Iterative inorder traversal stores values in sorted BST order.
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            self.values.append(node.val)
            node = node.right
        self.index = -1
        # Starting before index zero makes the first next call return the minimum.

    def next(self) -> int:
        # hasNext is the guard that keeps this cursor within the inorder list.
        self.index += 1
        return self.values[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.values)

    def hasPrev(self) -> bool:
        return self.index > 0

    def prev(self) -> int:
        # hasPrev ensures a reverse step stays at an already visited element.
        self.index -= 1
        return self.values[self.index]


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue: Deque[TreeNode] = deque([root])
    index = 1
    while queue and index < len(values):
        parent = queue.popleft()
        for side in ("left", "right"):
            if index < len(values) and values[index] is not None:
                child = TreeNode(values[index])
                setattr(parent, side, child)
                queue.append(child)
            index += 1
    return root


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    iterator = None
    for op, values in zip(ops, args):
        if op == "BSTIterator":
            iterator = BSTIterator(build_tree(values[0]))
            outputs.append(None)
        else:
            outputs.append(getattr(iterator, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["BSTIterator", "next", "next", "hasPrev", "prev", "hasNext",
         "next", "hasNext", "next", "next", "next", "hasNext"],
        [[[7, 3, 15, None, None, 9, 20]], [], [], [], [], [], [], [], [],
         [], [], []],
    ) == [None, 3, 7, True, 3, True, 7, True, 9, 15, 20, False]
    print("All tests passed")
