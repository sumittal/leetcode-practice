"""
LeetCode 1804: Implement Trie II (Prefix Tree)
Difficulty: Medium
Pattern: Hash Table
Video Reference: https://www.youtube.com/results?search_query=leetcode+1804+Implement+Trie+II+%28Prefix+Tree%29+neetcode
Complexity:
    - Time: insert/erase/search/prefix count O(L)
    - Space: O(total distinct prefix nodes)
"""

from typing import Dict, List, Optional


class TrieNode:
    def __init__(self):
        # Passing and ending counts make duplicate words independently erasable.
        self.children: Dict[str, "TrieNode"] = {}
        self.pass_count = 0
        self.end_count = 0


class Trie:
    def __init__(self):
        # The root's pass count tracks all inserted words, including duplicates.
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        node.pass_count += 1
        # Every visited node counts all inserted words sharing this prefix.
        for character in word:
            node = node.children.setdefault(character, TrieNode())
            node.pass_count += 1
        node.end_count += 1

    def _find(self, text: str) -> Optional[TrieNode]:
        node = self.root
        # A missing edge is enough to reject either exact-word or prefix queries.
        for character in text:
            node = node.children.get(character)
            if node is None:
                return None
        return node

    def countWordsEqualTo(self, word: str) -> int:
        node = self._find(word)
        # Ending counts distinguish a complete word from a longer shared prefix.
        return node.end_count if node else 0

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self._find(prefix)
        # Passing counts include every duplicate word through the prefix node.
        return node.pass_count if node else 0

    def erase(self, word: str) -> None:
        # The problem guarantees the word exists, so its full path is present.
        node = self.root
        # Decrement every prefix count exactly once for this erased copy.
        node.pass_count -= 1
        path = []
        for character in word:
            path.append((node, character))
            node = node.children[character]
            node.pass_count -= 1
        node.end_count -= 1
        # Remove dead branches so the trie stores only live prefixes.
        for parent, character in reversed(path):
            child = parent.children[character]
            if child.pass_count == 0:
                del parent.children[character]
            else:
                break


def replay(ops: List[str], args: List[List[object]]) -> List[object]:
    outputs: List[object] = []
    trie = None
    for operation, values in zip(ops, args):
        if operation == "Trie":
            trie = Trie()
            outputs.append(None)
        else:
            outputs.append(getattr(trie, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["Trie", "insert", "countWordsEqualTo", "countWordsEqualTo",
         "countWordsStartingWith", "insert", "countWordsEqualTo", "erase",
         "countWordsEqualTo"],
        [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"],
         ["app"], ["app"]],
    ) == [None, None, 1, 0, 1, None, 1, None, 0]
    assert replay(
        ["Trie", "insert", "insert", "erase", "countWordsEqualTo",
         "countWordsStartingWith"],
        [[], ["same"], ["same"], ["same"], ["same"], ["sam"]],
    ) == [None, None, None, None, 1, 1]
    print("All tests passed")
