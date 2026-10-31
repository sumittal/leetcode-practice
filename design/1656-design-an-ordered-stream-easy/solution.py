"""
LeetCode 1656: Design an Ordered Stream
Difficulty: Easy
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+1656+Design+an+Ordered+Stream+neetcode
Complexity:
    - Time: insert O(k) for the newly released chunk
    - Space: O(n)
"""

from typing import List, Optional


class OrderedStream:
    # The cursor partitions emitted values from buffered future IDs.
    def __init__(self, n: int):
        # One-based IDs map directly to their buffer positions.
        # Unfilled slots use None, distinct from every valid string.
        self.values: List[Optional[str]] = [None] * (n + 1)
        self.pointer = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        # The problem guarantees each key is inserted once.
        self.values[idKey] = value
        # Values beyond a gap stay buffered until earlier IDs arrive.
        chunk: List[str] = []
        # Advance only through the contiguous prefix now available.
        while self.pointer < len(self.values) and self.values[self.pointer]:
            # Each slot is emitted at most once over the stream's lifetime.
            chunk.append(self.values[self.pointer])
            # Advancing the pointer prevents any emitted ID from repeating.
            self.pointer += 1
        return chunk


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    stream = None
    for op, values in zip(ops, args):
        if op == "OrderedStream":
            stream = OrderedStream(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(stream, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["OrderedStream", "insert", "insert", "insert", "insert", "insert"],
        [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"],
         [4, "ddddd"]],
    ) == [None, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]
    assert replay(
        ["OrderedStream", "insert", "insert"],
        [[2], [2, "b"], [1, "a"]],
    ) == [None, [], ["a", "b"]]
    print("All tests passed")
