"""
LeetCode 98: Validate Binary Search Tree
Difficulty: Medium
Pattern: Trees
Video Reference: https://www.youtube.com/watch?v=s6ATEkipzow
Complexity:
    - Time: O(n)
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
        self.val, self.left, self.right = val, left, right


# Test helper: parse a LeetCode level-order sequence with None child slots.
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = [root]
    # Each queued parent consumes at most two values, left child before right.
    i = 1
    while q and i < len(values):
        node = q.pop(0)
        # i points to the next serialized child slot after each increment.
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root


# Test helper: convert a tree to level-order values with None child slots.
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
            # Enqueue both slots so later values retain their parent alignment.
            out.append(node.val)
            q.extend([node.left, node.right])
    while out and out[-1] is None:
        out.pop()
    return out


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(
            node: Optional[TreeNode], low: Optional[int], high: Optional[int]
        ) -> bool:
            # Bounds are exclusive because duplicate values violate BST ordering.
            if node is None:
                return True
            # Bounds are tightened independently along each root-to-leaf route.
            # Exclusive ancestor bounds catch violations beyond immediate children.
            if (
                low is not None
                and node.val <= low
                or high is not None
                and node.val >= high
            ):
                return False
            # Left descendants inherit the upper bound; right descendants inherit lower.
            return valid(node.left, low, node.val) and valid(node.right, node.val, high)

        # An empty root is valid because it violates no ordering constraint.
        return valid(root, None, None)


if __name__ == "__main__":
    solution = Solution()
    assert solution.isValidBST(build_tree([2, 1, 3])) is True
    assert solution.isValidBST(build_tree([5, 1, 4, None, None, 3, 6])) is False
    assert solution.isValidBST(None) is True
    assert solution.isValidBST(build_tree([2, 2, 2])) is False
    print("All tests passed")
