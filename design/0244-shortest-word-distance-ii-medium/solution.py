"""
LeetCode 244: Shortest Word Distance II
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+244+Shortest+Word+Distance+II+neetcode
Complexity:
    - Time: construction O(n), shortest O(f1 + f2)
    - Space: O(n)
"""

from typing import Dict, List


class WordDistance:
    def __init__(self, wordsDict: List[str]):
        # Occurrence lists are naturally sorted by the input traversal.
        # Each query then needs only two monotonically advancing positions.
        self.positions: Dict[str, List[int]] = {}
        for index, word in enumerate(wordsDict):
            self.positions.setdefault(word, []).append(index)

    def shortest(self, word1: str, word2: str) -> int:
        first = self.positions[word1]
        second = self.positions[word2]
        left = right = 0
        # The total number of occurrences provides a safe initial upper bound.
        best = len(self.positions) + sum(map(len, self.positions.values()))
        # Advancing the earlier index cannot discard a better future pairing.
        while left < len(first) and right < len(second):
            # Each loop records a valid pair before discarding one endpoint.
            best = min(best, abs(first[left] - second[right]))
            if first[left] < second[right]:
                # The earlier occurrence cannot pair better with a later opposite index.
                left += 1
            else:
                # The later endpoint is the only one worth pairing with future positions.
                right += 1
        return best


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    index = None
    for op, values in zip(ops, args):
        if op == "WordDistance":
            index = WordDistance(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(index, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["WordDistance", "shortest", "shortest"],
        [[["practice", "makes", "perfect", "coding", "makes"]],
         ["coding", "practice"], ["makes", "coding"]],
    ) == [None, 3, 1]
    # Repeated positions can give a closer pair than each word's first index.
    assert WordDistance(["a", "b", "a", "c", "b"]).shortest("a", "b") == 1
    print("All tests passed")
