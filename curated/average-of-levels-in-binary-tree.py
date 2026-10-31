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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Breadth-first batches contain exactly one tree depth.
        if root is None:
            return []
        # Queue order is breadth-first, so each fixed-size batch is one level.
        averages = []
        queue = [root]
        while queue:
            # Capture this depth's size before its children enter the queue.
            level_size = len(queue)
            level_sum = 0
            for _ in range(level_size):
                node = queue.pop(0)
                level_sum += node.val
                # Children enter the queue for the next level only.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Divide after consuming exactly the current level's nodes.
            averages.append(level_sum / level_size)
            # Once appended, a level's mean never needs to be revisited.
        # Every node contributes to exactly one level average.
        # The queue processes each node once for O(n) total traversal.
        return averages


if __name__ == "__main__":
    solution = Solution()
    actual = solution.averageOfLevels(build_tree([3, 9, 20, None, None, 15, 7]))
    assert all(
        abs(left - right) < 1e-9
        for left, right in zip(actual, [3.0, 14.5, 11.0])
    )
    assert solution.averageOfLevels(build_tree([3])) == [3.0]
    assert solution.averageOfLevels(build_tree([])) == []
    print("All tests passed")
