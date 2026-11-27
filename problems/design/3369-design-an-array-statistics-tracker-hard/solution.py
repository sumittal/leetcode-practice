"""
LeetCode 3369: Design an Array Statistics Tracker 
Difficulty: Hard
Pattern: Hash Table
Video Reference: https://www.youtube.com/results?search_query=leetcode+3369+Design+an+Array+Statistics+Tracker++neetcode
Complexity:
    - Time: add/remove O(log n), mean O(1), median O(log n), mode O(log n) amortized
    - Space: O(n)
"""

import heapq
import random
from collections import deque
from typing import Deque, Dict, List, Optional, Tuple


class TreapNode:
    def __init__(self, key: int, priority: float):
        self.key = key
        self.priority = priority
        # Duplicate values share a node, while count contributes to subtree size.
        self.count = 1
        self.size = 1
        self.left: Optional["TreapNode"] = None
        self.right: Optional["TreapNode"] = None


def _size(node: Optional[TreapNode]) -> int:
    return node.size if node else 0


def _refresh(node: TreapNode) -> None:
    # Subtree sizes make the median an order-statistic query.
    node.size = node.count + _size(node.left) + _size(node.right)


def _rotate_right(root: TreapNode) -> TreapNode:
    # Restore the heap-priority invariant after inserting on the left.
    child = root.left
    root.left = child.right
    child.right = root
    _refresh(root)
    _refresh(child)
    return child


def _rotate_left(root: TreapNode) -> TreapNode:
    # Restore the heap-priority invariant after inserting on the right.
    child = root.right
    root.right = child.left
    child.left = root
    _refresh(root)
    _refresh(child)
    return child


def _merge(
    left: Optional[TreapNode], right: Optional[TreapNode]
) -> Optional[TreapNode]:
    if left is None:
        return right
    if right is None:
        return left
    # Heap priorities preserve treap balance while ordered keys stay separated.
    if left.priority > right.priority:
        left.right = _merge(left.right, right)
        _refresh(left)
        return left
    right.left = _merge(left, right.left)
    _refresh(right)
    return right


def _change(
    root: Optional[TreapNode], key: int, delta: int, rng: random.Random
) -> Optional[TreapNode]:
    if root is None:
        if delta < 0:
            return None
        return TreapNode(key, rng.random())
    if key == root.key:
        root.count += delta
        if root.count == 0:
            return _merge(root.left, root.right)
    elif key < root.key:
        root.left = _change(root.left, key, delta, rng)
        if root.left and root.left.priority > root.priority:
            root = _rotate_right(root)
    else:
        root.right = _change(root.right, key, delta, rng)
        if root.right and root.right.priority > root.priority:
            root = _rotate_left(root)
    _refresh(root)
    return root


def _kth(root: TreapNode, rank: int) -> int:
    left_size = _size(root.left)
    if rank <= left_size:
        return _kth(root.left, rank)
    if rank <= left_size + root.count:
        return root.key
    return _kth(root.right, rank - left_size - root.count)


class StatisticsTracker:
    def __init__(self):
        self.values: Deque[int] = deque()
        self.frequency: Dict[int, int] = {}
        self.mode_heap: List[Tuple[int, int]] = []
        self.total = 0
        self.root: Optional[TreapNode] = None
        # A fixed seed makes the treap reproducible without changing its invariants.
        self.rng = random.Random(0)

    def addNumber(self, number: int) -> None:
        # The deque, sum, order-statistic tree, and mode index share one update.
        self.values.append(number)
        self.total += number
        self.root = _change(self.root, number, 1, self.rng)
        self.frequency[number] = self.frequency.get(number, 0) + 1
        heapq.heappush(self.mode_heap, (-self.frequency[number], number))

    def removeFirstAddedNumber(self) -> None:
        # FIFO removal changes all aggregates for exactly one oldest value.
        number = self.values.popleft()
        self.total -= number
        self.root = _change(self.root, number, -1, self.rng)
        new_frequency = self.frequency[number] - 1
        if new_frequency:
            self.frequency[number] = new_frequency
            heapq.heappush(self.mode_heap, (-new_frequency, number))
        else:
            del self.frequency[number]

    def getMean(self) -> int:
        return self.total // len(self.values)

    def getMedian(self) -> int:
        # Zero-based n//2 selects the upper median for even lengths.
        return _kth(self.root, len(self.values) // 2 + 1)

    def getMode(self) -> int:
        # Lazy entries are valid exactly when their frequency is still current.
        # Ties favor the smaller value because it is the second heap field.
        while self.mode_heap:
            negative_frequency, number = self.mode_heap[0]
            if self.frequency.get(number, 0) == -negative_frequency:
                return number
            heapq.heappop(self.mode_heap)
        raise RuntimeError("mode requested for an empty tracker")


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    tracker = None
    for operation, values in zip(ops, args):
        if operation == "StatisticsTracker":
            tracker = StatisticsTracker()
            outputs.append(None)
        else:
            outputs.append(getattr(tracker, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["StatisticsTracker", "addNumber", "addNumber", "addNumber",
         "getMean", "getMedian", "getMode", "removeFirstAddedNumber",
         "getMean", "getMedian", "getMode"],
        [[], [1], [2], [2], [], [], [], [], [], [], []],
    ) == [None, None, None, None, 1, 2, 2, None, 2, 2, 2]
    assert replay(
        ["StatisticsTracker", "addNumber", "addNumber", "addNumber",
         "addNumber", "getMode", "removeFirstAddedNumber", "getMode",
         "getMedian"],
        [[], [1], [2], [2], [1], [], [], [], []],
    ) == [None, None, None, None, None, 1, None, 2, 2]
    print("All tests passed")
