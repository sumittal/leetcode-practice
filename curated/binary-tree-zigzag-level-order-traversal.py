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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        # The direction flag changes after each complete breadth-first level.
        # A fixed-size row lets values be placed without reversing the queue.
        result = []
        queue = [root]
        left_to_right = True
        while queue:
            level_size = len(queue)
            values = [0] * level_size
            for index in range(level_size):
                node = queue.pop(0)
                # Reverse placement avoids a separate list-reversal pass.
                target = index if left_to_right else level_size - index - 1
                values[target] = node.val
                # The same child enqueue order works for either displayed direction.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # Children stay in natural order for the next level's placement.
            result.append(values)
            left_to_right = not left_to_right
            # Toggle only after all nodes at this depth have been processed.
            # Each completed row is appended in its final presentation order.
        # Queue order determines levels; target indices determine zigzag direction.
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.zigzagLevelOrder(
        build_tree([3, 9, 20, None, None, 15, 7])
    ) == [[3], [20, 9], [15, 7]]
    assert solution.zigzagLevelOrder(build_tree([1])) == [[1]]
    assert solution.zigzagLevelOrder(build_tree([])) == []
    assert solution.zigzagLevelOrder(
        build_tree([1, 2, 3, 4, None, None, 5])
    ) == [[1], [3, 2], [4, 5]]
    print("All tests passed")
