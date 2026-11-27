"""
LeetCode 677: Map Sum Pairs
Difficulty: Medium
Pattern: Hash Table
Video Reference: https://www.youtube.com/results?search_query=leetcode+677+Map+Sum+Pairs+neetcode
Complexity:
    - Time: insert O(L), sum O(L)
    - Space: O(total key characters)
"""

from typing import Dict


class TrieNode:
    def __init__(self):
        # Every node caches the sum of keys passing through this prefix.
        self.children: Dict[str, "TrieNode"] = {}
        # Root total also represents the empty prefix.
        self.total = 0


class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.values: Dict[str, int] = {}

    def insert(self, key: str, val: int) -> None:
        # Replacements contribute only their change to each prefix total.
        delta = val - self.values.get(key, 0)
        # The old value is subtracted before the replacement is added.
        self.values[key] = val
        node = self.root
        node.total += delta
        # Updating every path node keeps every prefix query ready in O(1) there.
        for char in key:
            # Creating missing nodes does not alter previously stored key values.
            node = node.children.setdefault(char, TrieNode())
            node.total += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            # A missing trie edge means no key has this prefix.
            if char not in node.children:
                return 0
            node = node.children[char]
        # The cached node sum includes keys ending at or below this prefix.
        return node.total


def replay(ops: list, args: list) -> list:
    outputs = []
    mapping = None
    for op, values in zip(ops, args):
        if op == "MapSum":
            mapping = MapSum()
            outputs.append(None)
        else:
            outputs.append(getattr(mapping, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["MapSum", "insert", "sum", "insert", "sum"],
        [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]],
    ) == [None, None, 3, None, 5]
    assert replay(
        ["MapSum", "insert", "insert", "sum"],
        [[], ["app", 2], ["app", 5], ["app"]],
    ) == [None, None, None, 5]
    print("All tests passed")
