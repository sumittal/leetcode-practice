import heapq
from typing import List, Set


class PhoneDirectory:
    # The released-number heap and untouched-number cursor partition free IDs.
    # A membership set prevents repeated release calls from duplicating numbers.
    def __init__(self, maxNumbers: int):
        # IDs below next_number were issued before; the rest remain untouched.
        self.limit = maxNumbers
        self.next_number = 0
        self.released: List[int] = []
        self.available: Set[int] = set()

    def get(self) -> int:
        if self.released:
            # Reused numbers are selected in ascending numeric order.
            number = heapq.heappop(self.released)
            # Keep the set synchronized with the heap's allocated result.
            self.available.remove(number)
            return number
        if self.next_number == self.limit:
            return -1
        number = self.next_number
        self.next_number += 1
        return number

    def check(self, number: int) -> bool:
        # Unissued numbers and explicitly released numbers are both free.
        return number in self.available or self.next_number <= number < self.limit

    def release(self, number: int) -> None:
        # Avoid duplicate heap entries when a free number is released twice.
        if (
            0 <= number < self.next_number
            and number not in self.available
        ):
            # A returned ID joins the released heap only once.
            heapq.heappush(self.released, number)
            self.available.add(number)


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    directory = None
    for op, values in zip(ops, args):
        if op == "PhoneDirectory":
            directory = PhoneDirectory(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(directory, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["PhoneDirectory", "get", "get", "get", "check", "release", "get",
         "check"],
        [[3], [], [], [], [2], [2], [], [2]],
    ) == [None, 0, 1, 2, False, None, 2, False]
    assert replay(
        ["PhoneDirectory", "get", "release", "release", "get"],
        [[1], [], [0], [0], []],
    ) == [None, 0, None, None, 0]
    print("All tests passed")
