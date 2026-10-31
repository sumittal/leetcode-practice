from bisect import bisect_left
from typing import List


class SummaryRanges:
    def __init__(self):
        # Intervals remain sorted and pairwise separated by at least one gap.
        self.intervals: List[List[int]] = []

    def addNum(self, value: int) -> None:
        index = bisect_left(self.intervals, [value, value])
        # The insertion point leaves at most one predecessor and successor to merge.
        # Existing values are already represented in one interval.
        if index and self.intervals[index - 1][1] >= value:
            return
        joins_left = index > 0 and self.intervals[index - 1][1] + 1 == value
        joins_right = (
            index < len(self.intervals)
            and self.intervals[index][0] - 1 == value
        )
        # Adjacency tests use +1 because intervals represent integer values.
        if joins_left and joins_right:
            # One inserted value bridges and merges both neighboring ranges.
            self.intervals[index - 1][1] = self.intervals[index][1]
            self.intervals.pop(index)
        elif joins_left:
            # Extend the predecessor by one adjacent value.
            self.intervals[index - 1][1] = value
        elif joins_right:
            # Extend the successor backward to include the new value.
            self.intervals[index][0] = value
        else:
            self.intervals.insert(index, [value, value])

    def getIntervals(self) -> List[List[int]]:
        # Return copies so callers cannot mutate the internal representation.
        return [interval[:] for interval in self.intervals]


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    ranges = None
    for op, values in zip(ops, args):
        if op == "SummaryRanges":
            ranges = SummaryRanges()
            outputs.append(None)
        else:
            result = getattr(ranges, op)(*values)
            outputs.append(result)
    return outputs


if __name__ == "__main__":
    assert replay(
        ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals",
         "addNum", "getIntervals", "addNum", "getIntervals"],
        [[], [1], [], [3], [], [7], [], [2], []],
    ) == [None, None, [[1, 1]], None, [[1, 1], [3, 3]], None,
          [[1, 1], [3, 3], [7, 7]], None, [[1, 3], [7, 7]]]
    print("All tests passed")
