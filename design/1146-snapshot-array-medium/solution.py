"""
LeetCode 1146: Snapshot Array
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+1146+Snapshot+Array+neetcode
Complexity:
    - Time: set O(1), snap O(1), get O(log changes at index)
    - Space: O(number of set calls)
"""

from bisect import bisect_right
from typing import List, Optional, Tuple


class SnapshotArray:
    # Each index stores only the writes that differ across snapshot IDs.
    # Snapshot IDs are monotonic, enabling binary search in every history.
    def __init__(self, length: int):
        # Every index starts with the implicit value zero at snapshot zero.
        self.histories: List[List[Tuple[int, int]]] = [
            [(0, 0)] for _ in range(length)
        ]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        history = self.histories[index]
        # Histories stay sorted by snap ID because snapshots only advance.
        # Repeated writes within one snapshot replace, rather than duplicate, state.
        if history[-1][0] == self.snap_id:
            history[-1] = (self.snap_id, val)
        else:
            history.append((self.snap_id, val))

    def snap(self) -> int:
        result = self.snap_id
        self.snap_id += 1
        # The returned ID refers to the state just completed.
        return result

    def get(self, index: int, snap_id: int) -> int:
        history = self.histories[index]
        # Binary search bounds lookup to versions for this index only.
        # Find the first version later than the requested snapshot.
        position = bisect_right(history, (snap_id, float("inf")))
        return history[position - 1][1]


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    array = None
    for operation, values in zip(ops, args):
        if operation == "SnapshotArray":
            array = SnapshotArray(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(array, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["SnapshotArray", "set", "snap", "set", "get"],
        [[3], [0, 5], [], [0, 6], [0, 0]],
    ) == [None, None, 0, None, 5]
    assert replay(
        ["SnapshotArray", "get", "set", "set", "snap", "get", "snap", "get"],
        [[1], [0, 0], [0, 4], [0, 8], [], [0, 0], [], [0, 1]],
    ) == [None, 0, None, None, 0, 8, 1, 8]
    print("All tests passed")
