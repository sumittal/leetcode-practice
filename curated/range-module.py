from typing import List, Optional, Tuple


class RangeModule:
    # Sorted disjoint half-open ranges are the complete coverage representation.
    # Add merges touched intervals; remove preserves any surviving boundary pieces.
    def __init__(self):
        self.ranges: List[Tuple[int, int]] = []

    def addRange(self, left: int, right: int) -> None:
        merged: List[Tuple[int, int]] = []
        inserted = False
        # A single pass preserves intervals before and after the merged union.
        for start, end in self.ranges:
            if end < left:
                # Intervals strictly before the addition remain unchanged.
                merged.append((start, end))
            elif right < start:
                if not inserted:
                    merged.append((left, right))
                    inserted = True
                # Later intervals remain sorted after the merged interval.
                merged.append((start, end))
            else:
                # Overlap or touching endpoints can be represented as one union.
                left = min(left, start)
                right = max(right, end)
        if not inserted:
            merged.append((left, right))
        # The resulting list stays sorted and contains no overlapping segments.
        self.ranges = merged

    def queryRange(self, left: int, right: int) -> bool:
        for start, end in self.ranges:
            if start <= left and right <= end:
                return True
            if start > left:
                # Sorted starts prove no later interval can cover this query.
                return False
        return False

    def removeRange(self, left: int, right: int) -> None:
        remaining: List[Tuple[int, int]] = []
        # Removal can preserve zero, one, or two pieces from each old interval.
        for start, end in self.ranges:
            if end <= left or start >= right:
                # Disjoint half-open intervals survive removal unchanged.
                remaining.append((start, end))
                continue
            if start < left:
                # Keep the tracked portion before the removed interval.
                remaining.append((start, left))
            if end > right:
                # Keep the tracked portion after the removed interval.
                remaining.append((right, end))
        self.ranges = remaining


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[bool]]:
    outputs: List[Optional[bool]] = []
    module = None
    for operation, values in zip(ops, args):
        if operation == "RangeModule":
            module = RangeModule()
            outputs.append(None)
        else:
            outputs.append(getattr(module, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["RangeModule", "addRange", "removeRange", "queryRange",
         "queryRange", "queryRange"],
        [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]],
    ) == [None, None, None, True, False, True]
    assert replay(
        ["RangeModule", "addRange", "addRange", "queryRange",
         "removeRange", "queryRange", "queryRange"],
        [[], [1, 5], [8, 10], [1, 10], [3, 9], [1, 3], [9, 10]],
    ) == [None, None, None, False, None, True, True]
    print("All tests passed")
