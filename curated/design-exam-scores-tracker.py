from bisect import bisect_left, bisect_right
from typing import List


class ExamTracker:
    # Strictly increasing times make binary search valid without reordering.
    # Prefix sums avoid scanning exams inside each requested interval.
    def __init__(self):
        # Chronological records make prefix sums monotone in their index.
        self.times: List[int] = []
        # Prefix index i stores the sum of the first i exam scores.
        self.prefix = [0]

    def record(self, time: int, score: int) -> None:
        # Exactly one cumulative entry is appended for each new exam.
        self.times.append(time)
        self.prefix.append(self.prefix[-1] + score)

    def totalScore(self, startTime: int, endTime: int) -> int:
        # Strictly increasing record times make both boundaries searchable.
        left = bisect_left(self.times, startTime)
        # left identifies the first exam included in the range.
        right = bisect_right(self.times, endTime)
        # right excludes the first exam after the inclusive end time.
        return self.prefix[right] - self.prefix[left]


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    tracker = None
    for op, values in zip(ops, args):
        if op == "ExamTracker":
            tracker = ExamTracker()
            outputs.append(None)
        else:
            result = getattr(tracker, op)(*values)
            outputs.append(result)
    return outputs


if __name__ == "__main__":
    assert replay(
        ["ExamTracker", "record", "totalScore", "record", "totalScore",
         "totalScore", "totalScore", "totalScore"],
        [[], [1, 98], [1, 1], [5, 99], [1, 3], [1, 5], [3, 4], [2, 5]],
    ) == [None, None, 98, None, 98, 197, 0, 99]
    print("All tests passed")
