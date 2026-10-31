"""
LeetCode 108: Convert Sorted Array to Binary Search Tree
Difficulty: Easy
Pattern: Trees
Video Reference: https://www.youtube.com/watch?v=0K0uCMYq5ng
Complexity:
    - Time: O(n)
    - Space: O(log n) recursion for a balanced result
"""

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


def inorder_values(root: Optional[TreeNode]) -> List[int]:
    # Inorder traversal should reproduce the original sorted input.
    if root is None:
        return []
    return inorder_values(root.left) + [root.val] + inorder_values(root.right)


def height_or_unbalanced(root: Optional[TreeNode]) -> int:
    # A negative height propagates the first detected balance violation.
    if root is None:
        return 0
    left_height = height_or_unbalanced(root.left)
    right_height = height_or_unbalanced(root.right)
    if left_height < 0 or right_height < 0:
        return -1
    if abs(left_height - right_height) > 1:
        return -1
    return max(left_height, right_height) + 1


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left: int, right: int) -> Optional[TreeNode]:
            # Empty half-open ranges contain no tree nodes.
            if left >= right:
                return None
            middle = (left + right) // 2
            # Either central index is valid when an even-sized range has two.
            # A middle element leaves similarly sized values on both sides.
            root = TreeNode(nums[middle])
            # Recursive halves preserve the sorted inorder sequence.
            root.left = build(left, middle)
            root.right = build(middle + 1, right)
            # Each recursive choice balances its own range independently.
            return root

        # The half-open interval contains each input index exactly once.
        return build(0, len(nums))


if __name__ == "__main__":
    solution = Solution()
    for values in ([-10, -3, 0, 5, 9], [1, 3], [], [1]):
        root = solution.sortedArrayToBST(values)
        assert inorder_values(root) == values
        assert height_or_unbalanced(root) >= 0
    print("All tests passed")
