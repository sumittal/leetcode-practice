"""
LeetCode 1993: Operations on Tree
Difficulty: Medium
Pattern: Trees
Video Reference: https://www.youtube.com/watch?v=qK4PtjrVD0U
Complexity:
    - Time: lock/unlock O(1), upgrade O(subtree size + height)
    - Space: O(n)
"""

from typing import List, Optional


class LockingTree:
    def __init__(self, parent: List[int]):
        # Parent links are also used to validate ancestor locks in O(height).
        self.parent = parent
        self.children: List[List[int]] = [[] for _ in parent]
        for node, ancestor in enumerate(parent):
            if ancestor != -1:
                self.children[ancestor].append(node)
        # None means unlocked; otherwise the slot records its owner's ID.
        self.owner: List[Optional[int]] = [None] * len(parent)

    def lock(self, num: int, user: int) -> bool:
        # A lock belongs to exactly one user until explicitly released.
        if self.owner[num] is not None:
            return False
        self.owner[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.owner[num] != user:
            return False
        self.owner[num] = None
        # Clearing an owner makes the node available to every other user.
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.owner[num] is not None:
            return False
        # Any locked ancestor forbids an upgrade at this node.
        ancestor = self.parent[num]
        while ancestor != -1:
            if self.owner[ancestor] is not None:
                return False
            ancestor = self.parent[ancestor]
        descendants: List[int] = []
        # Traverse only descendants rather than scanning unrelated branches.
        stack = self.children[num][:]
        while stack:
            node = stack.pop()
            if self.owner[node] is not None:
                descendants.append(node)
            stack.extend(self.children[node])
        # An upgrade requires a locked descendant and clears every such lock.
        if not descendants:
            return False
        for node in descendants:
            self.owner[node] = None
        # The requested node becomes the single surviving lock in its subtree.
        self.owner[num] = user
        return True


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    tree = None
    for op, values in zip(ops, args):
        if op == "LockingTree":
            tree = LockingTree(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(tree, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade",
         "lock"],
        [[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5],
         [0, 1], [0, 1]],
    ) == [None, True, False, True, True, True, False]
    assert replay(
        ["LockingTree", "lock", "upgrade", "unlock"],
        [[[-1, 0, 0]], [1, 9], [0, 4], [0, 4]],
    ) == [None, True, True, True]
    print("All tests passed")
