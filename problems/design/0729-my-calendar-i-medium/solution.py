"""
LeetCode 729: My Calendar I
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+729+My+Calendar+I+neetcode
Complexity:
    - Time: book O(log n) search plus O(n) insertion
    - Space: O(n)
"""

from bisect import bisect_left
from typing import List, Optional


class MyCalendar:
    # Sorted non-overlapping intervals make predecessor and successor decisive.
    # Half-open endpoints permit meetings to touch without overlapping.
    # Accepted bookings are inserted only after both neighbors are checked.
    def __init__(self):
        # Bookings remain ordered by start time for neighbor-only conflict checks.
        self.bookings: List[List[int]] = []

    def book(self, startTime: int, endTime: int) -> bool:
        # Binary search locates the only position where this interval can fit.
        position = bisect_left(self.bookings, [startTime, endTime])
        if position > 0 and self.bookings[position - 1][1] > startTime:
            return False
        if position < len(self.bookings) and self.bookings[position][0] < endTime:
            return False
        # Half-open intervals permit touching endpoints without overlap.
        self.bookings.insert(position, [startTime, endTime])
        # A rejected interval never reaches this mutation.
        # Sorted starts mean only adjacent intervals can conflict at insertion.
        return True


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[bool]]:
    outputs: List[Optional[bool]] = []
    calendar = None
    for operation, values in zip(ops, args):
        if operation == "MyCalendar":
            calendar = MyCalendar()
            outputs.append(None)
        else:
            outputs.append(getattr(calendar, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["MyCalendar", "book", "book", "book"],
        [[], [10, 20], [15, 25], [20, 30]],
    ) == [None, True, False, True]
    assert replay(
        ["MyCalendar", "book", "book", "book"],
        [[], [5, 10], [5, 10], [10, 12]],
    ) == [None, True, False, True]
    print("All tests passed")
