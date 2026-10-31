import heapq
from typing import List


class SeatManager:
    def __init__(self, n: int):
        # Unreserved seats that were returned are chosen before untouched ones.
        # The pointer never moves backward after an untouched seat is issued.
        self.returned: List[int] = []
        self.next_seat = 1
        self.limit = n

    def reserve(self) -> int:
        if self.returned:
            # The heap guarantees the smallest released seat is selected.
            return heapq.heappop(self.returned)
        seat = self.next_seat
        # Untouched seats are already in ascending order and need no heap.
        # The valid input sequence guarantees an unissued seat remains here.
        self.next_seat += 1
        return seat

    def unreserve(self, seatNumber: int) -> None:
        # Inputs guarantee this seat was reserved and is not already free.
        # Returning it to the heap restores smallest-seat priority immediately.
        heapq.heappush(self.returned, seatNumber)
        # The min-heap is sufficient because each reservation is unique.


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    manager = None
    for op, values in zip(ops, args):
        if op == "SeatManager":
            manager = SeatManager(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(manager, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["SeatManager", "reserve", "reserve", "unreserve", "reserve",
         "reserve", "reserve", "reserve"],
        [[5], [], [], [1], [], [], [], []],
    ) == [None, 1, 2, None, 1, 3, 4, 5]
    assert replay(
        ["SeatManager", "reserve", "unreserve", "reserve"],
        [[1], [], [1], []],
    ) == [None, 1, None, 1]
    print("All tests passed")
