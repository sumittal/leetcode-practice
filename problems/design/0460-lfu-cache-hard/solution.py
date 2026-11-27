"""
LeetCode 460: LFU Cache
Difficulty: Hard
Pattern: Linked List
Video Reference: https://www.youtube.com/watch?v=bLEIHn-DgoA
Complexity:
    - Time: get O(1), put O(1) average
    - Space: O(capacity)
"""

from collections import OrderedDict
from typing import Dict, List, Optional


class LFUCache:
    # Frequency buckets plus per-bucket recency implement LFU/LRU eviction.
    # minimum_frequency is repaired only when its last key is promoted or removed.
    def __init__(self, capacity: int):
        self.capacity = capacity
        # The value map defines which keys currently occupy cache slots.
        self.values: Dict[int, int] = {}
        # Frequencies move upward after every successful access or update.
        self.frequencies: Dict[int, int] = {}
        # Each bucket's insertion order is the LRU order for that frequency.
        self.groups: Dict[int, OrderedDict] = {}
        # This is always the smallest frequency among resident keys.
        self.minimum_frequency = 0

    def _promote(self, key: int) -> None:
        frequency = self.frequencies[key]
        bucket = self.groups[frequency]
        # OrderedDict keeps the least-recent key at the front of each frequency.
        del bucket[key]
        if not bucket and frequency == self.minimum_frequency:
            self.minimum_frequency += 1
        next_frequency = frequency + 1
        # Promotion changes only two adjacent frequency buckets.
        self.groups.setdefault(next_frequency, OrderedDict())[key] = None
        self.frequencies[key] = next_frequency

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        # A successful read counts as use and therefore changes eviction rank.
        self._promote(key)
        return self.values[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.values:
            self.values[key] = value
            self._promote(key)
            return
        # Capacity is checked only for a new key; updates never evict another.
        if len(self.values) == self.capacity:
            # The first key in the minimum bucket is both least frequent and LRU.
            least_recent_key, _ = self.groups[self.minimum_frequency].popitem(
                last=False
            )
            del self.values[least_recent_key]
            del self.frequencies[least_recent_key]
        self.values[key] = value
        self.frequencies[key] = 1
        # Every new entry starts with frequency one and becomes most recent there.
        self.groups.setdefault(1, OrderedDict())[key] = None
        self.minimum_frequency = 1


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    cache = None
    for operation, values in zip(ops, args):
        if operation == "LFUCache":
            cache = LFUCache(*values)
            outputs.append(None)
        else:
            result = getattr(cache, operation)(*values)
            outputs.append(result)
    return outputs


if __name__ == "__main__":
    assert replay(
        ["LFUCache", "put", "put", "get", "put", "get", "get", "put",
         "get", "get", "get"],
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]],
    ) == [None, None, None, 1, None, -1, 3, None, -1, 3, 4]
    assert replay(
        ["LFUCache", "put", "get", "put", "get"],
        [[1], [1, 10], [1], [2, 20], [1]],
    ) == [None, None, 10, None, -1]
    assert replay(["LFUCache", "put", "get"], [[0], [1, 1], [1]]) == [
        None, None, -1
    ]
    print("All tests passed")
