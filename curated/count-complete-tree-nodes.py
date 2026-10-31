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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Empty child ranges contribute no nodes.
        # The height shortcut relies on the complete-tree input guarantee.
        if root is None:
            return 0
        # Complete-tree paths determine whether this subtree is perfect.
        # Both height walks follow one boundary path, not every node.
        left_height = 0
        node = root
        while node:
            left_height += 1
            node = node.left
        right_height = 0
        node = root
        while node:
            right_height += 1
            node = node.right
        # Equal extreme heights imply every level is full in a complete tree.
        if left_height == right_height:
            return (1 << left_height) - 1
        # Otherwise count the two complete child subtrees recursively.
        # At least one child subtree is shorter, so recursion skips full levels.
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        # Height computations and recursion yield O(log^2 n) on a complete tree.


if __name__ == "__main__":
    solution = Solution()
    assert solution.countNodes(build_tree([1, 2, 3, 4, 5, 6])) == 6
    assert solution.countNodes(build_tree([])) == 0
    assert solution.countNodes(build_tree([1])) == 1
    assert solution.countNodes(build_tree([1, 2, 3, 4])) == 4
    print("All tests passed")
