from typing import List, Optional, Union


class BookMyShow:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.remaining = [m] * n
        size = 4 * n
        self.maximum = [0] * size
        self.total = [0] * size
        # Every leaf initially has m seats and both summaries agree.
        self._build(1, 0, n - 1)

    def _build(self, node: int, left: int, right: int) -> None:
        # The maximum supports gather; the sum supports scatter capacity checks.
        self.maximum[node] = self.m
        self.total[node] = (right - left + 1) * self.m
        if left == right:
            return
        middle = (left + right) // 2
        # Splitting the range makes each point update logarithmic in row count.
        self._build(node * 2, left, middle)
        self._build(node * 2 + 1, middle + 1, right)

    def _update(self, node: int, left: int, right: int, row: int) -> None:
        if left == right:
            self.maximum[node] = self.remaining[row]
            self.total[node] = self.remaining[row]
            return
        middle = (left + right) // 2
        if row <= middle:
            self._update(node * 2, left, middle, row)
        else:
            self._update(node * 2 + 1, middle + 1, right, row)
        # The parent keeps separate summaries for the two request types.
        self.maximum[node] = max(
            self.maximum[node * 2], self.maximum[node * 2 + 1]
        )
        self.total[node] = self.total[node * 2] + self.total[node * 2 + 1]

    def _find_row(
        self, node: int, left: int, right: int, limit: int, seats: int
    ) -> int:
        if left > limit or self.maximum[node] < seats:
            return -1
        if left == right:
            return left
        middle = (left + right) // 2
        # Search left first to satisfy the smallest-row rule.
        result = self._find_row(node * 2, left, middle, limit, seats)
        if result != -1:
            return result
        return self._find_row(node * 2 + 1, middle + 1, right, limit, seats)

    def _prefix_sum(
        self, node: int, left: int, right: int, limit: int
    ) -> int:
        if left > limit:
            return 0
        if right <= limit:
            # Fully covered nodes contribute their cached total in O(1).
            return self.total[node]
        middle = (left + right) // 2
        return self._prefix_sum(node * 2, left, middle, limit) + \
            self._prefix_sum(node * 2 + 1, middle + 1, right, limit)

    def _first_nonempty(
        self, node: int, left: int, right: int, limit: int
    ) -> int:
        if left > limit or self.maximum[node] == 0:
            return -1
        if left == right:
            # This leaf is the earliest nonempty eligible row.
            return left
        middle = (left + right) // 2
        row = self._first_nonempty(node * 2, left, middle, limit)
        if row != -1:
            return row
        return self._first_nonempty(node * 2 + 1, middle + 1, right, limit)

    def gather(self, k: int, maxRow: int) -> List[int]:
        # Search only through maxRow, preserving the smallest valid row.
        row = self._find_row(1, 0, self.n - 1, maxRow, k)
        if row == -1:
            return []
        # The first free seat is the row's original capacity minus remainder.
        start = self.m - self.remaining[row]
        self.remaining[row] -= k
        self._update(1, 0, self.n - 1, row)
        return [row, start]

    def scatter(self, k: int, maxRow: int) -> bool:
        # Check the whole prefix before making any changes, so failure is atomic.
        if self._prefix_sum(1, 0, self.n - 1, maxRow) < k:
            return False
        remaining_to_book = k
        # Each iteration empties a row or finishes the request in one row.
        while remaining_to_book:
            row = self._first_nonempty(1, 0, self.n - 1, maxRow)
            taken = min(remaining_to_book, self.remaining[row])
            self.remaining[row] -= taken
            remaining_to_book -= taken
            self._update(1, 0, self.n - 1, row)
        return True


def replay(
    ops: List[str], args: List[List[int]]
) -> List[Optional[Union[List[int], bool]]]:
    outputs: List[Optional[Union[List[int], bool]]] = []
    hall = None
    for operation, values in zip(ops, args):
        if operation == "BookMyShow":
            hall = BookMyShow(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(hall, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["BookMyShow", "gather", "gather", "gather", "scatter", "scatter"],
        [[2, 5], [4, 0], [2, 0], [2, 1], [1, 1], [1, 1]],
    ) == [None, [0, 0], [], [1, 0], True, True]
    assert replay(
        ["BookMyShow", "scatter", "gather", "scatter"],
        [[3, 2], [1, 1], [2, 1], [2, 2]],
    ) == [None, True, [1, 0], True]
    print("All tests passed")
