"""
LeetCode 208: Implement Trie (Prefix Tree)
Difficulty: Medium
Pattern: Tries
Video Reference: https://www.youtube.com/watch?v=oobqoCJlHA0
Complexity:
    - Time: O(L) per operation
    - Space: O(total chars)
"""

from typing import Dict, Optional


class _Node:
    def __init__(self) -> None:
        self.children = {}  # type: Dict[str, _Node]
        self.terminal = False


class Trie:
    def __init__(self) -> None:
        self.root = _Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # Reuse shared prefixes and create only missing edges.
            node = node.children.setdefault(char, _Node())
        # Marking only the final node keeps prefixes distinct from stored words.
        node.terminal = True

    def _walk(self, text: str) -> Optional[_Node]:
        node = self.root
        for char in text:
            # The first absent edge proves no stored word can continue this prefix.
            if char not in node.children:
                return None
            # Moving along this edge preserves the matched-prefix invariant.
            node = node.children[char]
        # Reaching the end returns the node even when the text is not a full word.
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        # A traversable prefix is not enough unless insertion marked its end.
        return node is not None and node.terminal

    def startsWith(self, prefix: str) -> bool:
        # Prefix queries intentionally ignore the terminal flag.
        return self._walk(prefix) is not None


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True and trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True
    assert trie.search("") is False and trie.startsWith("") is True
    print("All tests passed")
