from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val, self.left, self.right = val, left, right


# Test helper: construct nodes from LeetCode's level-order representation.
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = [root]
    # The queue order matches the parent order in the level-order encoding.
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


# Test helper: render a tree in level order, keeping interior missing-child markers.
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


def find_node(root: Optional[TreeNode], value: int) -> Optional[TreeNode]:
    # The BST invariant chooses exactly one child at each step toward the value.
    while root and root.val != value:
        root = root.left if value < root.val else root.right
    return root


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # The LCA lies where the two target values stop sharing one strict side.
        low, high = sorted((p.val, q.val))
        while root:
            # Both targets below this value share the left branch.
            if high < root.val:
                root = root.left
            # Both targets above it share the right branch.
            elif low > root.val:
                root = root.right
            else:
                return root  # Their paths split here, or this node is one target.
        # Valid LeetCode inputs contain both targets, so this is only a type-safe fallback.
        return root


if __name__ == "__main__":
    solution = Solution()
    r = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    assert solution.lowestCommonAncestor(r, find_node(r, 2), find_node(r, 8)).val == 6
    assert solution.lowestCommonAncestor(r, find_node(r, 2), find_node(r, 4)).val == 2
    r = build_tree([2, 1])
    assert solution.lowestCommonAncestor(r, find_node(r, 2), find_node(r, 1)).val == 2
    print("All tests passed")
