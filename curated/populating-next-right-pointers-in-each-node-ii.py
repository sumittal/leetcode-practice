from typing import List, Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: Optional["Node"] = None,
        right: Optional["Node"] = None,
        next: Optional["Node"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def build_tree(values: List[Optional[int]]) -> Optional[Node]:
    if not values or values[0] is None:
        return None
    root = Node(values[0])
    queue = [root]
    cursor = 0
    index = 1
    while cursor < len(queue) and index < len(values):
        node = queue[cursor]
        cursor += 1
        if values[index] is not None:
            node.left = Node(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = Node(values[index])
            queue.append(node.right)
        index += 1
    return root


def levels_via_next(root: Optional[Node]) -> List[List[int]]:
    # Each next chain is the serialized order of one completed level.
    levels = []
    level = root
    while level:
        values = []
        next_level = None
        node = level
        while node:
            values.append(node.val)
            if next_level is None:
                next_level = node.left or node.right
            node = node.next
        levels.append(values)
        level = next_level
    return levels


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        # Traverse each level after its next pointers have been established.
        # Only one temporary dummy node is needed at a time.
        level = root
        while level:
            dummy = Node()
            tail = dummy
            current = level
            while current:
                # The current-level chain supplies the traversal without a queue.
                # Append children in left-to-right order to the next-level chain.
                for child in (current.left, current.right):
                    if child:
                        tail.next = child
                        tail = child
                current = current.next
            # Terminate the last child even if it arrived with a stale next link.
            tail.next = None
            level = dummy.next
            # Dummy is a temporary anchor and is not included in the tree.
            # The next iteration starts at the first child, if any.
        return root


if __name__ == "__main__":
    solution = Solution()
    root = build_tree([1, 2, 3, 4, 5, None, 7])
    assert levels_via_next(solution.connect(root)) == [[1], [2, 3], [4, 5, 7]]
    assert solution.connect(None) is None
    root = build_tree([1, 2, 3, 4, None, None, 5])
    assert levels_via_next(solution.connect(root)) == [[1], [2, 3], [4, 5]]
    print("All tests passed")
