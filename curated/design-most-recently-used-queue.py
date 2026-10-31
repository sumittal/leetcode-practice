from typing import List, Optional


class MRUQueue:
    def __init__(self, n: int):
        # The constraints cap fetches at 2000, so reserve one fresh slot per call.
        self.capacity = n + 2000
        self.tree = [0] * (self.capacity + 1)
        self.values = [0] * (self.capacity + 1)
        self.next_slot = n
        # Removed positions stay empty, so a fetch never shifts later values.
        # Initially, each value occupies its one-based rank position.
        for position in range(1, n + 1):
            self.values[position] = position
            self._add(position, 1)

    def _add(self, position: int, delta: int) -> None:
        # Fenwick updates touch only the ancestors of one position.
        while position <= self.capacity:
            self.tree[position] += delta
            position += position & -position

    def _kth(self, rank: int) -> int:
        # Binary lifting finds the position whose prefix count reaches rank.
        # Fenwick tree nodes summarize occupancy, not the stored queue values.
        position = 0
        bit = 1 << (self.capacity.bit_length() - 1)
        while bit:
            candidate = position + bit
            if candidate <= self.capacity and self.tree[candidate] < rank:
                position = candidate
                rank -= self.tree[candidate]
            bit >>= 1
        return position + 1

    def fetch(self, k: int) -> int:
        # Rank selection is based on the current queue, not original positions.
        # Deletion and reinsertion each cost O(log capacity).
        position = self._kth(k)
        value = self.values[position]
        self._add(position, -1)
        # A fresh position makes the selected value the new tail.
        self.next_slot += 1
        self.values[self.next_slot] = value
        self._add(self.next_slot, 1)
        return value


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    queue = None
    for operation, values in zip(ops, args):
        if operation == "MRUQueue":
            queue = MRUQueue(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(queue, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["MRUQueue", "fetch", "fetch", "fetch", "fetch"],
        [[8], [3], [5], [2], [8]],
    ) == [None, 3, 6, 2, 2]
    assert replay(
        ["MRUQueue", "fetch", "fetch"],
        [[4], [1], [4]],
    ) == [None, 1, 1]
    assert replay(["MRUQueue", "fetch"], [[1], [1]]) == [None, 1]
    print("All tests passed")
