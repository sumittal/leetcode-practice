from typing import Optional, List


class Segment:
    def __init__(self):
        # Covered length lets a full-range update skip already covered nodes.
        # Children are allocated on demand because the coordinate domain is huge.
        self.count = 0
        self.left: Optional["Segment"] = None
        self.right: Optional["Segment"] = None


class CountIntervals:
    def __init__(self):
        self.root = Segment()
        self.lower = 1
        self.upper = 10 ** 9

    def add(self, left: int, right: int) -> None:
        # Inclusive integer endpoints are represented directly by segment bounds.
        self._add(self.root, self.lower, self.upper, left, right)

    def _add(
        self, node: Segment, low: int, high: int, query_left: int,
        query_right: int,
    ) -> None:
        # A completely covered segment cannot contribute new integers.
        if node.count == high - low + 1:
            return
        if query_left <= low and high <= query_right:
            # Store the segment's full cardinality without visiting descendants.
            node.count = high - low + 1
            node.left = None
            node.right = None
            return
        # Only boundary paths need descent; fully covered interior nodes stop.
        middle = (low + high) // 2
        if query_left <= middle:
            if node.left is None:
                node.left = Segment()
            self._add(node.left, low, middle, query_left, query_right)
        if query_right > middle:
            if node.right is None:
                node.right = Segment()
            self._add(node.right, middle + 1, high, query_left, query_right)
        # Child counts are disjoint, so their sum is the covered parent length.
        # This total prevents repeated additions from counting overlap twice.
        node.count = (node.left.count if node.left else 0)
        node.count += node.right.count if node.right else 0

    def count(self) -> int:
        return self.root.count


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    intervals = None
    for op, values in zip(ops, args):
        if op == "CountIntervals":
            intervals = CountIntervals()
            outputs.append(None)
        else:
            result = getattr(intervals, op)(*values)
            outputs.append(result)
    return outputs


if __name__ == "__main__":
    assert replay(
        ["CountIntervals", "add", "add", "count", "add", "count"],
        [[], [2, 3], [7, 10], [], [5, 8], []],
    ) == [None, None, None, 6, None, 8]
    assert replay(
        ["CountIntervals", "add", "add", "count", "add", "count"],
        [[], [1, 10], [3, 7], [], [11, 11], []],
    ) == [None, None, None, 10, None, 11]
    print("All tests passed")
