"""
LeetCode 384: Shuffle an Array
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+384+Shuffle+an+Array+neetcode
Complexity:
    - Time: reset O(n), shuffle O(n)
    - Space: O(n)
"""

import random
from typing import List, Optional


class Solution:
    # Fisher-Yates yields each permutation with equal probability.
    # Reset always returns a new copy of the original sequence.
    # Shuffle mutates only the local copy, not stored state.
    def __init__(self, nums: List[int]):
        # Keep an immutable baseline so shuffles never accumulate mutations.
        self.original = nums[:]

    def reset(self) -> List[int]:
        # Returning a copy prevents callers from mutating the saved original.
        return self.original[:]

    def shuffle(self) -> List[int]:
        shuffled = self.original[:]
        # Fisher-Yates selects each remaining index with equal probability.
        for index in range(len(shuffled) - 1, 0, -1):
            # Every remaining suffix position is equally likely for this slot.
            swap_index = random.randint(0, index)
            shuffled[index], shuffled[swap_index] = (
                shuffled[swap_index],
                shuffled[index],
            )
        # The input and baseline are untouched because swaps target the copy.
        return shuffled


def replay(ops: List[str], args: List[list]) -> List[Optional[List[int]]]:
    outputs: List[Optional[List[int]]] = []
    array = None
    for operation, values in zip(ops, args):
        if operation == "Solution":
            array = Solution(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(array, operation)(*values))
    return outputs


if __name__ == "__main__":
    random.seed(3)
    original = [1, 2, 3]
    result = replay(
        ["Solution", "shuffle", "reset", "shuffle"],
        [[original], [], [], []],
    )
    assert result[2] == original
    assert sorted(result[1]) == original and sorted(result[3]) == original
    assert original == [1, 2, 3]
    random.seed(7)
    singleton = Solution([9])
    assert singleton.shuffle() == [9] and singleton.reset() == [9]
    print("All tests passed")
