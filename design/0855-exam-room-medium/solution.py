"""
LeetCode 855: Exam Room
Difficulty: Medium
Pattern: Design
Video Reference: https://www.youtube.com/results?search_query=leetcode+855+Exam+Room+neetcode
Complexity:
    - Time: seat O(students), leave O(students)
    - Space: O(students)
"""

from bisect import bisect_left
from typing import List, Optional


class ExamRoom:
    # Scanning sorted occupied seats compares every available boundary or gap.
    # Equal-distance gaps keep the smaller seat because only strict wins replace it.
    # The first empty room is a special case with the greatest possible distance.
    # Insertions preserve order for subsequent nearest-neighbor calculations.
    # Leaving a seat removes it from the ordered occupancy list.
    def __init__(self, n: int):
        # Only occupied positions are stored, in increasing order.
        self.n = n
        self.occupied: List[int] = []

    def seat(self) -> int:
        if not self.occupied:
            self.occupied.append(0)
            return 0
        # The left boundary candidate is always seat zero.
        best_distance = self.occupied[0]
        best_seat = 0
        for index in range(1, len(self.occupied)):
            left = self.occupied[index - 1]
            right = self.occupied[index]
            distance = (right - left) // 2
            candidate = left + distance
            # Only the midpoint of a neighboring gap can be optimal there.
            if distance > best_distance:
                best_distance = distance
                best_seat = candidate
        last_distance = self.n - 1 - self.occupied[-1]
        # The right boundary candidate is the final seat.
        if last_distance > best_distance:
            best_seat = self.n - 1
        # Keeping the first maximum candidate implements the lower-index tie rule.
        self.occupied.insert(bisect_left(self.occupied, best_seat), best_seat)
        # Sorted insertion keeps the next seat operation's gap scan valid.
        return best_seat

    def leave(self, p: int) -> None:
        self.occupied.pop(bisect_left(self.occupied, p))
        # Removing the seat restores its two neighboring gaps for later choices.


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    room = None
    for operation, values in zip(ops, args):
        if operation == "ExamRoom":
            room = ExamRoom(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(room, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"],
        [[10], [], [], [], [], [4], []],
    ) == [None, 0, 9, 4, 2, None, 5]
    assert replay(
        ["ExamRoom", "seat", "seat", "leave", "seat"],
        [[4], [], [], [0], []],
    ) == [None, 0, 3, None, 0]
    print("All tests passed")
