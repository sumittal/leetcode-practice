"""
LeetCode 3829: Design Ride Sharing System
Difficulty: Medium
Pattern: Hash Table
Video Reference: https://www.youtube.com/results?search_query=leetcode+3829+Design+Ride+Sharing+System+neetcode
Complexity:
    - Time: add/cancel O(1), match O(1) amortized
    - Space: O(n)
"""

from collections import deque
from typing import Deque, Set


class RideSharingSystem:
    # A separate waiting set supports O(1) rider cancellation without deque removal.
    # Lazy skips preserve FIFO ordering for every rider who remains active.
    # Driver entries need no cancellation marker in this interface.
    def __init__(self):
        # FIFO queues preserve arrival order for both kinds of participants.
        self.riders: Deque[int] = deque()
        self.drivers: Deque[int] = deque()
        self.waiting: Set[int] = set()

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)
        self.waiting.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> list:
        # Discard canceled riders lazily while preserving FIFO for active ones.
        while self.riders and self.riders[0] not in self.waiting:
            # Canceled riders are removed only when they reach the queue front.
            self.riders.popleft()
        if not self.drivers or not self.riders:
            return [-1, -1]
        # A driver is consumed only after an active rider is available.
        driver = self.drivers.popleft()
        rider = self.riders.popleft()
        self.waiting.remove(rider)
        return [driver, rider]

    def cancelRider(self, riderId: int) -> None:
        # Removing from the active set invalidates the queued entry in O(1).
        self.waiting.discard(riderId)


def replay(ops: list, args: list) -> list:
    outputs = []
    system = None
    for op, values in zip(ops, args):
        if op == "RideSharingSystem":
            system = RideSharingSystem()
            outputs.append(None)
        else:
            result = getattr(system, op)(*values)
            outputs.append(result)
    return outputs


if __name__ == "__main__":
    assert replay(
        ["RideSharingSystem", "addRider", "addDriver", "addRider",
         "matchDriverWithRider", "addDriver", "cancelRider",
         "matchDriverWithRider", "matchDriverWithRider"],
        [[], [3], [2], [1], [], [5], [3], [], []],
    ) == [None, None, None, None, [2, 3], None, None, [5, 1], [-1, -1]]
    assert replay(
        ["RideSharingSystem", "addRider", "addDriver", "addDriver",
         "matchDriverWithRider", "addRider", "cancelRider",
         "matchDriverWithRider"],
        [[], [8], [8], [6], [], [2], [2], []],
    ) == [None, None, None, None, [8, 8], None, None, [-1, -1]]
    print("All tests passed")
