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


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Each call carries the remaining sum after its ancestors.
        if root is None:
            # An empty path is not a root-to-leaf path.
            return False
        remaining = targetSum - root.val
        # Only leaves can complete a valid path.
        if root.left is None and root.right is None:
            return remaining == 0
        # An internal node cannot succeed without reaching an actual leaf.
        # Either child may continue the remaining path sum.
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(
            root.right, remaining
        )
        # Each recursive call consumes exactly one node from the path.
        # Negative values remain valid because no sum-based pruning is used.
        # The recursion visits at most each tree node once.


if __name__ == "__main__":
    solution = Solution()
    assert solution.hasPathSum(
        build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),
        22,
    ) is True
    assert solution.hasPathSum(build_tree([1, 2, 3]), 5) is False
    assert solution.hasPathSum(build_tree([]), 0) is False
    assert solution.hasPathSum(build_tree([-2, None, -3]), -5) is True
    print("All tests passed")
