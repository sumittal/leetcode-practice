"""
LeetCode 2166: Design Bitset
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+2166+Design+Bitset+neetcode
Complexity:
    - Time: fix/unfix/flip/all/one/count O(1), toString O(n)
    - Space: O(n)
"""

from typing import List, Optional


class Bitset:
    def __init__(self, size: int):
        # Logical bits are stored XOR the shared flip flag.
        self.bits = [False] * size
        self.flipped = False
        self.ones = 0

    def fix(self, idx: int) -> None:
        # A logical zero is stored equal to the current inversion flag.
        if self.bits[idx] == self.flipped:
            self.bits[idx] = not self.flipped
            self.ones += 1

    def unfix(self, idx: int) -> None:
        # Undo only a logical one so the aggregate count remains exact.
        if self.bits[idx] != self.flipped:
            self.bits[idx] = self.flipped
            self.ones -= 1

    def flip(self) -> None:
        # Inverting all bits changes the count without visiting each position.
        self.flipped = not self.flipped
        self.ones = len(self.bits) - self.ones

    def all(self) -> bool:
        # The maintained counter makes this aggregate check constant time.
        return self.ones == len(self.bits)

    def one(self) -> bool:
        # This is true when the logical vector contains any set bit.
        return self.ones > 0

    def count(self) -> int:
        # The counter is updated by fix, unfix, and flip rather than rescanned.
        return self.ones

    def toString(self) -> str:
        # Materialize logical values only when the caller requests the string.
        return "".join(
            "1" if bit != self.flipped else "0" for bit in self.bits
        )


def replay(ops: List[str], args: List[List[object]]) -> List[Optional[object]]:
    outputs: List[Optional[object]] = []
    bitset = None
    for operation, values in zip(ops, args):
        if operation == "Bitset":
            bitset = Bitset(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(bitset, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one",
         "unfix", "count", "toString"],
        [[5], [3], [1], [], [], [0], [], [], [0], [], []],
    ) == [
        None, None, None, None, False, None, None, True, None, 2, "01010"
    ]
    assert replay(
        ["Bitset", "all", "one", "fix", "all", "flip", "count", "toString"],
        [[1], [], [], [0], [], [], [], []],
    ) == [None, False, False, None, True, None, 0, "0"]
    print("All tests passed")
