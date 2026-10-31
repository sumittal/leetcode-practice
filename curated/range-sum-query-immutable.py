from typing import List


class NumArray:
    # One-dimensional prefixes trade linear setup and storage for constant queries.
    # Inclusive range sums subtract the prefix immediately before left.
    # The input values themselves never need to be mutated.
    # Prefix zero represents an empty segment.
    def __init__(self, nums: List[int]):
        # prefix[0] represents the empty prefix before the input begins.
        self.prefix: List[int] = [0]
        for value in nums:
            # Prefix[i] stores the sum of exactly the first i input values.
            self.prefix.append(self.prefix[-1] + value)

    def sumRange(self, left: int, right: int) -> int:
        # The precomputed table makes query time independent of range width.
        # The leading zero converts inclusive [left, right] to a clean difference.
        return self.prefix[right + 1] - self.prefix[left]


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs = []
    array = None
    for operation, values in zip(ops, args):
        if operation == "NumArray":
            array = NumArray(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(array, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["NumArray", "sumRange", "sumRange", "sumRange"],
        [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]],
    ) == [None, 1, -1, -3]
    assert replay(
        ["NumArray", "sumRange"],
        [[[5]], [0, 0]],
    ) == [None, 5]
    print("All tests passed")
