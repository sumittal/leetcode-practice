"""
LeetCode 381: Insert Delete GetRandom O(1) - Duplicates allowed
Difficulty: Hard
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+381+Insert+Delete+GetRandom+O%281%29+-+Duplicates+allowed+neetcode
Complexity:
    - Time: insert O(1) average, remove O(1) average, getRandom O(1)
    - Space: O(n)
"""

import random
from typing import Dict, List, Optional, Set, Union


class RandomizedCollection:
    def __init__(self):
        # Dense storage supports random selection without scanning unique keys.
        self.values: List[int] = []
        # Each value tracks every list slot containing one of its copies.
        self.positions: Dict[int, Set[int]] = {}

    def insert(self, val: int) -> bool:
        existed = val in self.positions
        self.positions.setdefault(val, set()).add(len(self.values))
        # The list contains one slot per occurrence, including duplicates.
        self.values.append(val)
        # The set's existence before insertion determines the required boolean.
        return not existed

    def remove(self, val: int) -> bool:
        if val not in self.positions:
            return False
        removed_index = self.positions[val].pop()
        last_index = len(self.values) - 1
        last_value = self.values[last_index]
        if removed_index != last_index:
            # Moving the final slot fills the hole without shifting other values.
            self.values[removed_index] = last_value
            self.positions[last_value].remove(last_index)
            self.positions[last_value].add(removed_index)
        self.values.pop()
        if not self.positions[val]:
            del self.positions[val]
        # Removing empty index sets keeps future inserts reporting correctly.
        # Each set now describes exactly the current indices of its value.
        return True

    def getRandom(self) -> int:
        # Uniform list-index sampling weights values by their number of copies.
        return random.choice(self.values)


def replay(
    ops: List[str], args: List[List[int]]
) -> List[Optional[Union[int, bool]]]:
    outputs: List[Optional[Union[int, bool]]] = []
    collection = None
    for operation, values in zip(ops, args):
        if operation == "RandomizedCollection":
            collection = RandomizedCollection()
            outputs.append(None)
        else:
            outputs.append(getattr(collection, operation)(*values))
    return outputs


if __name__ == "__main__":
    random.seed(7)
    first = replay(
        ["RandomizedCollection", "insert", "insert", "insert", "getRandom",
         "remove", "getRandom"],
        [[], [1], [1], [2], [], [1], []],
    )
    assert first[:4] == [None, True, False, True]
    assert first[4] in (1, 2) and first[5] is True and first[6] in (1, 2)
    random.seed(11)
    second = replay(
        ["RandomizedCollection", "insert", "insert", "remove", "remove",
         "remove", "insert", "getRandom"],
        [[], [4], [4], [4], [4], [4], [9], []],
    )
    assert second == [None, True, False, True, True, False, True, 9]
    print("All tests passed")
