from collections import deque
from typing import Deque, List, Optional


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


# Test helper: construct a tree from level-order values and None markers.
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue: Deque[TreeNode] = deque([root])
    index = 1
    while queue and index < len(values):
        parent = queue.popleft()
        if values[index] is not None:
            parent.left = TreeNode(values[index])
            queue.append(parent.left)
        index += 1
        if index < len(values) and values[index] is not None:
            parent.right = TreeNode(values[index])
            queue.append(parent.right)
        index += 1
    return root


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        # Queue order visits each level from left to right.
        queue: Deque[TreeNode] = deque([root])
        visible = []
        # Breadth-first order makes the last dequeued node the rightmost at its depth.
        # Each outer iteration consumes exactly one current depth.
        while queue:
            level_width = len(queue)
            # The saved width prevents children from entering this level's scan.
            for index in range(level_width):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                # Children are queued for the next depth, never this saved level width.
                if index == level_width - 1:
                    # The final node visited at this depth is visible from the right.
                    visible.append(node.val)
        # One value was recorded per nonempty tree depth.
        return visible


if __name__ == "__main__":
    solution = Solution()
    assert solution.rightSideView(
        build_tree([1, 2, 3, None, 5, None, 4])
    ) == [1, 3, 4]
    assert solution.rightSideView(build_tree([1, None, 3])) == [1, 3]
    assert solution.rightSideView(build_tree([])) == []
    assert solution.rightSideView(build_tree([1])) == [1]
    print("All tests passed")
