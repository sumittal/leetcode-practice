"""
LeetCode 604: Design Compressed String Iterator
Difficulty: Easy
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+604+Design+Compressed+String+Iterator+neetcode
Complexity:
    - Time: construction O(encoded length), next O(1) amortized, hasNext O(1)
    - Space: O(number of runs)
"""

from typing import List, Tuple


class StringIterator:
    # Run counts are kept compact instead of allocating the expanded string.
    # A cursor and remaining count are sufficient to represent iterator state.
    # Exhausted iteration follows the API's single-space sentinel convention.
    def __init__(self, compressedString: str):
        # Parsing stores one pair per run rather than expanding repeated text.
        self.runs: List[Tuple[str, int]] = []
        index = 0
        while index < len(compressedString):
            char = compressedString[index]
            index += 1
            start = index
            while index < len(compressedString) and compressedString[index].isdigit():
                index += 1
            self.runs.append((char, int(compressedString[start:index])))
        self.run_index = 0
        self.remaining = self.runs[0][1] if self.runs else 0

    def next(self) -> str:
        if not self.hasNext():
            return " "
        char = self.runs[self.run_index][0]
        # A call consumes one character from exactly the current run.
        self.remaining -= 1
        # Advance only after fully consuming the current run.
        if self.remaining == 0:
            self.run_index += 1
            if self.run_index < len(self.runs):
                self.remaining = self.runs[self.run_index][1]
        return char

    def hasNext(self) -> bool:
        # Zero-length runs are skipped by next's advance logic.
        while self.run_index < len(self.runs) and self.remaining == 0:
            # Skip empty runs before reporting whether output remains.
            self.run_index += 1
            if self.run_index < len(self.runs):
                self.remaining = self.runs[self.run_index][1]
        return self.run_index < len(self.runs)


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    iterator = None
    for op, values in zip(ops, args):
        if op == "StringIterator":
            iterator = StringIterator(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(iterator, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["StringIterator", "next", "next", "next", "next", "hasNext"],
        [["L1e2t1"], [], [], [], [], []],
    ) == [None, "L", "e", "e", "t", False]
    assert replay(
        ["StringIterator", "next", "hasNext", "next"],
        [["x0a1"], [], [], []],
    ) == [None, "a", False, " "]
    print("All tests passed")
