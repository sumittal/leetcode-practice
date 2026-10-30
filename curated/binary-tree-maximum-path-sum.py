from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val, self.left, self.right = val, left, right


# Test helper: create a tree from level-order values and None child markers.
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = [root]
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


# Test helper: serialize level order and remove only redundant trailing None values.
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []
    out = []
    q = [root]
    while q:
        node = q.pop(0)
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            q.extend([node.left, node.right])
    while out and out[-1] is None:
        out.pop()
    return out


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # best records complete paths anywhere, including paths that turn at a node.
        best = float("-inf")

        def gain(node: Optional[TreeNode]) -> int:
            # Return the best downward path this parent can extend through one child.
            nonlocal best
            if node is None:
                # A missing branch contributes no value rather than blocking a path.
                return 0
            # Negative branches can only lower a path, so clamp each child gain at zero.
            left = max(0, gain(node.left))
            right = max(0, gain(node.right))
            # This candidate turns at node and may use both child gains.
            best = max(best, node.val + left + right)
            # A parent may extend through only one child, not both sides of this turn.
            return node.val + max(left, right)

        # A nonempty LeetCode tree is required; initialize best below all values.
        gain(root)
        return int(best)


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxPathSum(build_tree([1, 2, 3])) == 6
    assert solution.maxPathSum(build_tree([-10, 9, 20, None, None, 15, 7])) == 42
    assert solution.maxPathSum(build_tree([-3])) == -3
    print("All tests passed")
