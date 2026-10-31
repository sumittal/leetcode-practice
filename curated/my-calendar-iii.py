from typing import Dict, List


class MyCalendarThree:
    # Difference events turn interval overlap into a sorted prefix-sum sweep.
    # The stored maximum is monotone as bookings are only added.
    # The sweep treats each booking as a half-open time interval.
    def __init__(self):
        # Boundary deltas encode the active booking count as a prefix sum.
        # Starts add one event and ends remove it at the half-open boundary.
        self.delta: Dict[int, int] = {}
        self.maximum = 0

    def book(self, startTime: int, endTime: int) -> int:
        self.delta[startTime] = self.delta.get(startTime, 0) + 1
        self.delta[endTime] = self.delta.get(endTime, 0) - 1
        # Sorting boundaries reconstructs simultaneous booking counts.
        active = 0
        current_max = 0
        # The small number of bookings makes sorting boundaries practical.
        for time in sorted(self.delta):
            active += self.delta[time]
            # The largest prefix sum is the maximum concurrent booking count.
            current_max = max(current_max, active)
        self.maximum = max(self.maximum, current_max)
        return self.maximum


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    calendar = None
    for op, values in zip(ops, args):
        if op == "MyCalendarThree":
            calendar = MyCalendarThree()
            outputs.append(None)
        else:
            outputs.append(getattr(calendar, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["MyCalendarThree", "book", "book", "book", "book", "book", "book"],
        [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]],
    ) == [None, 1, 1, 2, 3, 3, 3]
    print("All tests passed")
