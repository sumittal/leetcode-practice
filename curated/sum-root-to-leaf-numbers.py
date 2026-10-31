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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Visit carries the decimal prefix represented by the current path.
        # The local recursion keeps each branch's prefix independent.
        def visit(node: Optional[TreeNode], prefix: int) -> int:
            if node is None:
                # Missing children contribute no root-to-leaf number.
                return 0
            number = prefix * 10 + node.val
            # A leaf completes one number and must not be counted twice.
            if node.left is None and node.right is None:
                return number
            # Branch totals combine all complete paths below this prefix.
            # Missing branches contribute zero through the base case above.
            return visit(node.left, number) + visit(node.right, number)

        # The root begins with no digits in its prefix.
        # Every leaf number is added once as the recursion unwinds.
        return visit(root, 0)


if __name__ == "__main__":
    solution = Solution()
    assert solution.sumNumbers(build_tree([1, 2, 3])) == 25
    assert solution.sumNumbers(build_tree([4, 9, 0, 5, 1])) == 1026
    assert solution.sumNumbers(build_tree([7])) == 7
    assert solution.sumNumbers(build_tree([])) == 0
    print("All tests passed")
