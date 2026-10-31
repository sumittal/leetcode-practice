from collections import Counter
from typing import Dict, List, Optional


class FindSumPairs:
    # A frequency map avoids scanning the mutable second array for each target.
    # The fixed first array is still scanned because its values are not indexed.
    # Updating the second array changes exactly one frequency.
    def __init__(self, nums1: List[int], nums2: List[int]):
        # The first list remains fixed; the second list supports point additions.
        self.nums1 = nums1
        self.nums2 = nums2
        self.counts: Dict[int, int] = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_value = self.nums2[index]
        self.counts[old_value] -= 1
        # Removing the old frequency before adding the new value handles val zero.
        if self.counts[old_value] == 0:
            del self.counts[old_value]
        # Keep the frequency table synchronized with the mutable array slot.
        self.nums2[index] += val
        self.counts[self.nums2[index]] = self.counts.get(
            self.nums2[index], 0
        ) + 1

    def count(self, tot: int) -> int:
        # Frequency lookup counts all matching second-array duplicates at once.
        # Every first-array occurrence pairs independently with complement copies.
        return sum(self.counts.get(tot - value, 0) for value in self.nums1)


def replay(ops: List[str], args: List[list]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    pairs = None
    for operation, values in zip(ops, args):
        if operation == "FindSumPairs":
            pairs = FindSumPairs(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(pairs, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["FindSumPairs", "count", "add", "count", "count", "add", "add",
         "count"],
        [[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8],
         [4], [0, 1], [1, 1], [7]],
    ) == [None, 8, None, 2, 1, None, None, 11]
    assert replay(
        ["FindSumPairs", "count", "add", "count"],
        [[[0, 0], [0, 0]], [0], [0, 3], [3]],
    ) == [None, 4, None, 2]
    print("All tests passed")
