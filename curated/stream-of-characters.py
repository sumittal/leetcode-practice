from collections import deque
from typing import Deque, Dict, List


class StreamChecker:
    def __init__(self, words: List[str]):
        # Trie edges follow reversed words so suffix checks proceed backward.
        self.trie: Dict[str, dict] = {}
        # Only the longest possible word can contribute to a match.
        self.max_length = max((len(word) for word in words), default=0)
        self.history: Deque[str] = deque(maxlen=self.max_length)
        for word in words:
            node = self.trie
            # A shared reversed prefix represents suffixes of multiple words.
            for char in reversed(word):
                node = node.setdefault(char, {})
            # The empty key marks a complete reversed dictionary word.
            node[""] = {}

    def query(self, letter: str) -> bool:
        # Newest stream characters are placed at the front for trie traversal.
        self.history.appendleft(letter)
        node = self.trie
        # A missing edge proves no longer suffix can match.
        for char in self.history:
            # A terminal marker can match before the stored stream ends.
            if "" in node:
                return True
            if char not in node:
                return False
            node = node[char]
        # Exhausting history without a terminal marker means no word matched.
        # A word may end exactly at the retained history boundary.
        return "" in node


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    checker = None
    for op, values in zip(ops, args):
        if op == "StreamChecker":
            checker = StreamChecker(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(checker, op)(*values))
    return outputs


if __name__ == "__main__":
    letters = list("abcdefghijkl")
    expected = [False, False, False, True, False, True, False, False,
                False, False, False, True]
    assert replay(
        ["StreamChecker"] + ["query"] * len(letters),
        [[["cd", "f", "kl"]]] + [[char] for char in letters],
    ) == [None] + expected
    assert replay(
        ["StreamChecker", "query", "query"],
        [[["a"]], ["a"], ["b"]],
    ) == [None, True, False]
    print("All tests passed")
