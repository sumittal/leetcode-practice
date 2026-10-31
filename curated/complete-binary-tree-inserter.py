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


class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.candidates: Deque[TreeNode] = deque()
        # Breadth-first traversal orders candidate parents by insertion position.
        queue: Deque[TreeNode] = deque([root])
        while queue:
            node = queue.popleft()
            # Children enter the queue in the same left-to-right level order.
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            # Level-order order puts the earliest incomplete parent first.
            if not node.left or not node.right:
                self.candidates.append(node)

    def insert(self, val: int) -> int:
        parent = self.candidates[0]
        # The queue front is the earliest node that can accept a child.
        child = TreeNode(val)
        # Fill a left slot before the right slot to preserve completeness.
        if parent.left is None:
            parent.left = child
        else:
            parent.right = child
            self.candidates.popleft()
        self.candidates.append(child)
        # The new leaf is itself a future candidate parent.
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        # The same root object accumulates all newly inserted descendants.
        return self.root


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    # Level-order pairs attach children to successive queued parents.
    queue: Deque[TreeNode] = deque([root])
    index = 1
    while queue and index < len(values):
        parent = queue.popleft()
        if values[index] is not None:
            parent.left = TreeNode(values[index])
            queue.append(parent.left)
        index += 1
        if index < len(values) and values[index] is not None:
            parent.right = TreeNode(values[index])
            queue.append(parent.right)
        index += 1
    return root


def tree_values(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []
    values: List[Optional[int]] = []
    queue: Deque[Optional[TreeNode]] = deque([root])
    while queue:
        node = queue.popleft()
        values.append(node.val if node else None)
        if node:
            queue.extend([node.left, node.right])
    while values and values[-1] is None:
        values.pop()
    return values


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    inserter = None
    for op, values in zip(ops, args):
        if op == "CBTInserter":
            inserter = CBTInserter(build_tree(values[0]))
            outputs.append(None)
        elif op == "get_root":
            outputs.append(tree_values(inserter.get_root()))
        else:
            outputs.append(getattr(inserter, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["CBTInserter", "insert", "insert", "get_root"],
        [[[1, 2, 3, 4, 5, 6]], [7], [8], []],
    ) == [None, 3, 4, [1, 2, 3, 4, 5, 6, 7, 8]]
    print("All tests passed")
