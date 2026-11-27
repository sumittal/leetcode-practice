"""
LeetCode 2671: Frequency Tracker
Difficulty: Medium
Pattern: Hash Table
Video Reference: https://www.youtube.com/results?search_query=leetcode+2671+Frequency+Tracker+neetcode
Complexity:
    - Time: add/deleteOne/hasFrequency O(1) expected
    - Space: O(d + f)
"""

from typing import Dict, List, Optional


class FrequencyTracker:
    def __init__(self):
        # Reverse counts answer hasFrequency without scanning the value map.
        self.number_counts: Dict[int, int] = {}
        # frequency_counts[f] is the number of values occurring f times.
        self.frequency_counts: Dict[int, int] = {}

    def _move_frequency(self, number: int, old: int, new: int) -> None:
        # One number leaves its old bucket and, if still present, enters one new bucket.
        if old:
            # Remove its contribution before adding the new multiplicity bucket.
            self.frequency_counts[old] -= 1
        if new:
            # The direct map contains only numbers whose current count is positive.
            self.frequency_counts[new] = self.frequency_counts.get(new, 0) + 1
            self.number_counts[number] = new
        else:
            self.number_counts.pop(number, None)

    def add(self, number: int) -> None:
        old = self.number_counts.get(number, 0)
        # Moving one value changes exactly two frequency buckets.
        self._move_frequency(number, old, old + 1)

    def deleteOne(self, number: int) -> None:
        old = self.number_counts.get(number, 0)
        if old:
            self._move_frequency(number, old, old - 1)
        # A missing number is intentionally ignored.

    def hasFrequency(self, frequency: int) -> bool:
        # Zero-frequency values are removed, so membership is a positive count.
        return self.frequency_counts.get(frequency, 0) > 0


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[bool]]:
    outputs: List[Optional[bool]] = []
    tracker = None
    for operation, values in zip(ops, args):
        if operation == "FrequencyTracker":
            tracker = FrequencyTracker()
            outputs.append(None)
        else:
            outputs.append(getattr(tracker, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["FrequencyTracker", "add", "add", "hasFrequency"],
        [[], [3], [3], [2]],
    ) == [None, None, None, True]
    assert replay(
        ["FrequencyTracker", "add", "deleteOne", "hasFrequency"],
        [[], [1], [1], [1]],
    ) == [None, None, None, False]
    assert replay(
        ["FrequencyTracker", "hasFrequency", "add", "hasFrequency"],
        [[], [2], [3], [1]],
    ) == [None, False, None, True]
    assert replay(
        ["FrequencyTracker", "add", "add", "deleteOne", "hasFrequency",
         "hasFrequency"],
        [[], [5], [5], [5], [1], [2]],
    ) == [None, None, None, None, True, False]
    print("All tests passed")
