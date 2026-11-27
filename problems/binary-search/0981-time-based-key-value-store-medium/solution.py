"""
LeetCode 981: Time Based Key-Value Store
Difficulty: Medium
Pattern: Binary Search
Video Reference: https://www.youtube.com/watch?v=fu2cD_6E8Hw
Complexity:
    - Time: O(log n) per get
    - Space: O(n)
"""

from typing import Dict, List, Tuple


class TimeMap:
    def __init__(self) -> None:
        # Appends follow increasing timestamps for each key by problem guarantee.
        self.values: Dict[str, List[Tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Keep each key's records sorted so later gets can use binary search.
        self.values.setdefault(key, []).append((timestamp, value))
        # LeetCode guarantees timestamps are set in increasing order per key.

    def get(self, key: str, timestamp: int) -> str:
        records = self.values.get(key, [])
        # A missing key has no eligible timestamp and returns the empty string.
        # Search for the insertion point after all timestamps at most the query.
        left = 0
        right = len(records)
        while left < right:
            middle = (left + right) // 2
            if records[middle][0] <= timestamp:
                # This record is eligible; search right for a more recent one.
                left = middle + 1
            else:
                # Later records cannot answer a query at this timestamp.
                right = middle
            # The half-open range [left, right) contains the remaining candidates.
        # The predecessor is the most recent eligible record, if any.
        # The insertion point is one past the desired timestamp after the search.
        return records[left - 1][1] if left else ""


if __name__ == "__main__":
    time_map = TimeMap()
    time_map.set("foo", "bar", 1)
    assert time_map.get("foo", 1) == "bar"
    assert time_map.get("foo", 3) == "bar"
    time_map.set("foo", "bar2", 4)
    assert time_map.get("foo", 4) == "bar2"
    assert time_map.get("foo", 5) == "bar2"
    assert time_map.get("foo", 0) == ""
    time_map.set("empty", "value", 10)
    assert time_map.get("other", 10) == ""
    assert time_map.get("empty", 9) == ""
    print("All tests passed")
