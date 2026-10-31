"""
LeetCode 745: Prefix and Suffix Search
Difficulty: Hard
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+745+Prefix+and+Suffix+Search+neetcode
Complexity:
    - Time: construction O(n * L^2), f O(1)
    - Space: O(n * L^2)
"""

from typing import Dict, List


class WordFilter:
    # A direct pair lookup trades preprocessing space for constant-time queries.
    # The stored index is overwritten in input order to preserve max-index behavior.
    # The separator makes prefix and suffix boundaries unambiguous.
    def __init__(self, words: List[str]):
        self.best: Dict[str, int] = {}
        # At most (L + 1)^2 combinations are stored for each word.
        # Increasing indices overwrite older words with the same prefix/suffix.
        for index, word in enumerate(words):
            prefixes = [word[:end] for end in range(len(word) + 1)]
            suffixes = [word[start:] for start in range(len(word) + 1)]
            # Include empty strings so unconstrained sides need no special case.
            for prefix in prefixes:
                for suffix in suffixes:
                    # Later words overwrite entries so the answer is the max index.
                    self.best[prefix + "#" + suffix] = index

    def f(self, pref: str, suff: str) -> int:
        # A delimiter prevents accidental overlap between the two components.
        return self.best.get(pref + "#" + suff, -1)


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    word_filter = None
    for op, values in zip(ops, args):
        if op == "WordFilter":
            word_filter = WordFilter(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(word_filter, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["WordFilter", "f", "f", "f", "f"],
        [[["apple", "apply", "maple"]], ["a", "e"], ["ap", "ly"],
         ["", "le"], ["x", ""]],
    ) == [None, 0, 1, 2, -1]
    print("All tests passed")
