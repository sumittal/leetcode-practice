from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val, self.left, self.right = val, left, right


# Test helper: parse level-order node values and None markers.
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    # A parent is removed only after its left and right value slots are read.
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# Test helper: return LeetCode level-order values, omitting only trailing None slots.
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []
    out = []
    q = [root]
    while q:
        node = q.pop(0)
        if node is None:
            # Preserve interior empty child slots to reconstruct the same shape.
            out.append(None)
        else:
            out.append(node.val)
            q.extend([node.left, node.right])
    while out and out[-1] is None:
        out.pop()
    return out


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            # A paired null test also verifies that the candidate's shape is exact.
            if a is None or b is None:
                return a is b
            # Equal root values alone are insufficient if either subtree shape differs.
            return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)

        # An empty candidate matches; a missing main tree cannot contain a nonempty one.
        if subRoot is None:
            return True
        if root is None:
            return False
        # Try an exact structural match at this root, then search either descendant.
        return (
            same(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )


if __name__ == "__main__":
    solution = Solution()
    assert solution.isSubtree(build_tree([3, 4, 5, 1, 2]), build_tree([4, 1, 2])) is True
    assert (
        solution.isSubtree(
            build_tree([3, 4, 5, 1, 2, None, None, None, None, 0]),
            build_tree([4, 1, 2]),
        )
        is False
    )
    assert solution.isSubtree(build_tree([1, 2]), None) is True
    assert solution.isSubtree(None, build_tree([1])) is False
    print("All tests passed")
