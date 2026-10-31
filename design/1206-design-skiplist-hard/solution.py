"""
LeetCode 1206: Design Skiplist
Difficulty: Hard
Pattern: Linked List
Video Reference: https://www.youtube.com/results?search_query=leetcode+1206+Design+Skiplist+neetcode
Complexity:
    - Time: search O(log n) expected, add O(log n) expected, erase O(log n) expected
    - Space: O(n) expected
"""

import random
from typing import List, Optional


class SkipNode:
    def __init__(self, value: int, level: int):
        self.value = value
        self.forward: List[Optional["SkipNode"]] = [None] * level


class Skiplist:
    # Random tower heights keep expected search paths logarithmic.
    # Forward links at each level skip over spans of lower-level nodes.
    # The bottom level remains a complete ordered linked list.
    def __init__(self):
        # A fixed maximum height bounds the search's number of levels.
        self.maximum_level = 16
        self.head = SkipNode(-1, self.maximum_level)

    def _random_level(self) -> int:
        level = 1
        # Coin flips give exponentially fewer nodes access to higher levels.
        while level < self.maximum_level and random.random() < 0.5:
            level += 1
        return level

    def search(self, target: int) -> bool:
        node = self.head
        # Starting high skips long runs before the final level checks neighbors.
        for level in range(self.maximum_level - 1, -1, -1):
            # Move forward while the next key is still strictly below target.
            while node.forward[level] and node.forward[level].value < target:
                node = node.forward[level]
        candidate = node.forward[0]
        # Level zero contains every value, including duplicates.
        return candidate is not None and candidate.value == target

    def add(self, num: int) -> None:
        # Predecessors are recorded at every level before inserting the tower.
        update: List[SkipNode] = [self.head] * self.maximum_level
        node = self.head
        for level in range(self.maximum_level - 1, -1, -1):
            while node.forward[level] and node.forward[level].value < num:
                node = node.forward[level]
            update[level] = node
        tower = SkipNode(num, self._random_level())
        # Each pointer splice preserves sorted order at its own level.
        for level in range(len(tower.forward)):
            tower.forward[level] = update[level].forward[level]
            update[level].forward[level] = tower

    def erase(self, num: int) -> bool:
        update: List[SkipNode] = [self.head] * self.maximum_level
        node = self.head
        for level in range(self.maximum_level - 1, -1, -1):
            while node.forward[level] and node.forward[level].value < num:
                node = node.forward[level]
            update[level] = node
        target = node.forward[0]
        # If level zero lacks the value, no upper level can contain it.
        if target is None or target.value != num:
            return False
        # Bypass one matching tower at all levels it participates in.
        for level in range(len(target.forward)):
            if update[level].forward[level] is target:
                update[level].forward[level] = target.forward[level]
        return True


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[bool]]:
    outputs: List[Optional[bool]] = []
    skiplist = None
    for operation, values in zip(ops, args):
        if operation == "Skiplist":
            skiplist = Skiplist()
            outputs.append(None)
        else:
            outputs.append(getattr(skiplist, operation)(*values))
    return outputs


if __name__ == "__main__":
    random.seed(0)
    assert replay(
        ["Skiplist", "add", "add", "add", "search", "add", "search",
         "erase", "erase", "search"],
        [[], [1], [2], [3], [0], [4], [1], [0], [1], [1]],
    ) == [None, None, None, None, False, None, True, False, True, False]
    random.seed(10)
    structure = Skiplist()
    for value in range(30):
        structure.add(value)
    assert all(structure.search(value) for value in range(30))
    assert all(structure.erase(value) for value in range(0, 30, 2))
    assert all(not structure.search(value) for value in range(0, 30, 2))
    assert all(structure.search(value) for value in range(1, 30, 2))
    print("All tests passed")
