from typing import List, Tuple


class MyCalendarTwo:
    def __init__(self):
        # Accepted bookings are retained for future pairwise intersections.
        self.bookings: List[Tuple[int, int]] = []
        self.overlaps: List[Tuple[int, int]] = []

    def book(self, startTime: int, endTime: int) -> bool:
        # Any intersection with an existing double-booked span would triple-book.
        for start, end in self.overlaps:
            # Intervals are half-open; equal endpoints are not an intersection.
            if max(start, startTime) < min(end, endTime):
                return False
        # Rejected requests leave the accepted calendar unchanged.
        new_overlaps: List[Tuple[int, int]] = []
        # Stage intersections separately so failed bookings remain atomic.
        # Intersections with accepted single bookings become double-booked spans.
        for start, end in self.bookings:
            overlap_start = max(start, startTime)
            overlap_end = min(end, endTime)
            if overlap_start < overlap_end:
                new_overlaps.append((overlap_start, overlap_end))
        self.overlaps.extend(new_overlaps)
        # Only after validation do the new booking and overlap spans commit.
        self.bookings.append((startTime, endTime))
        # A valid insertion may create several new double-booked spans.
        return True


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    calendar = None
    for op, values in zip(ops, args):
        if op == "MyCalendarTwo":
            calendar = MyCalendarTwo()
            outputs.append(None)
        else:
            outputs.append(getattr(calendar, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"],
        [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]],
    ) == [None, True, True, True, False, True, True]
    assert replay(
        ["MyCalendarTwo", "book", "book", "book"],
        [[], [0, 10], [10, 20], [5, 15]],
    ) == [None, True, True, True]
    print("All tests passed")
