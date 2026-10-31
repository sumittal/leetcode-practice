from collections import deque
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


# Test helper: consume LeetCode level-order values, where None marks a missing child.
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    # Empty input or a missing root represents an empty tree.
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    # Queue parents in level order so each next pair fills left then right.
    queue = deque([root])  # type: Deque[TreeNode]
    index = 1
    while queue and index < len(values):
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        # Consume this left slot even when it is None, preserving input positions.
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    # Return the root after the level-order description has been consumed.
    return root


# Test helper: serialize the tree level by level and trim absent trailing children.
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []
    values = []
    # Keep None placeholders while traversing so missing branches retain their positions.
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            values.append(None)
        else:
            values.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    # Trailing missing children do not change the tree and are omitted by LeetCode.
    while values and values[-1] is None:
        values.pop()
    return values


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # The empty subtree contributes zero and terminates this root-to-leaf recursion.
        if root is None:
            return 0
        # A missing child contributes zero; only the deepest root-to-leaf path wins.
        # Add one for this node, then choose the deeper of its two child paths.
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxDepth(build_tree([3, 9, 20, None, None, 15, 7])) == 3
    assert solution.maxDepth(build_tree([1, None, 2])) == 2
    assert solution.maxDepth(build_tree([])) == 0
    assert solution.maxDepth(build_tree([1])) == 1
    assert solution.maxDepth(build_tree([1, None, 2, None, 3])) == 3
    print("All tests passed")
