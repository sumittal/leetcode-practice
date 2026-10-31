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


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []
    # Keep null slots so reconstructed child placement can be asserted.
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
    def buildTree(
        self, inorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        # The index map finds each root's inorder boundary in constant time.
        # Recursive ranges are inclusive and refer to the original inorder array.
        positions = {value: index for index, value in enumerate(inorder)}
        post_index = len(postorder) - 1

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal post_index
            if left > right:
                return None
            # Reverse postorder visits root, right subtree, then left subtree.
            value = postorder[post_index]
            post_index -= 1
            root = TreeNode(value)
            split = positions[value]
            # Build right first to consume the reverse traversal in order.
            root.right = build(split + 1, right)
            root.left = build(left, split - 1)
            # Each child range excludes the current root's inorder position.
            # Inorder boundaries partition the current subtree's values.
            return root

        # Empty input creates an empty range and returns None.
        # Every postorder value is consumed exactly once by one recursive frame.
        return build(0, len(inorder) - 1)


if __name__ == "__main__":
    solution = Solution()
    assert tree_to_list(
        solution.buildTree(
            [9, 3, 15, 20, 7], [9, 15, 7, 20, 3]
        )
    ) == [3, 9, 20, None, None, 15, 7]
    assert tree_to_list(solution.buildTree([-1], [-1])) == [-1]
    assert tree_to_list(solution.buildTree([], [])) == []
    print("All tests passed")
