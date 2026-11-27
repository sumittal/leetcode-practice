"""
LeetCode 3391: Design a 3D Binary Matrix with Efficient Layer Tracking
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+3391+Design+a+3D+Binary+Matrix+with+Efficient+Layer+Tracking+neetcode
Complexity:
    - Time: setCell/unsetCell O(log q), largestMatrix O(1) amortized
    - Space: O(n^3 + q)
"""

import heapq
from typing import List, Optional


class Matrix3D:
    def __init__(self, n: int):
        self.n = n
        # Flatten each layer's n-by-n cells for compact membership tests.
        self.layers = [bytearray(n * n) for _ in range(n)]
        self.counts = [0] * n
        self.version = [0] * n
        # Negated fields prioritize more ones, then the larger layer index.
        self.heap = [(0, -layer, 0) for layer in range(n)]
        # Initial entries encode the all-zero tie rule: largest layer wins.
        heapq.heapify(self.heap)

    def _record_layer(self, layer: int) -> None:
        self.version[layer] += 1
        # The version distinguishes an updated count from older heap snapshots.
        # Heap maintenance costs logarithmic time and avoids rescanning n layers.
        heapq.heappush(
            self.heap,
            (-self.counts[layer], -layer, self.version[layer]),
        )

    def setCell(self, x: int, y: int, z: int) -> None:
        position = y * self.n + z
        # Idempotent writes must not inflate the layer's population count.
        if self.layers[x][position]:
            return
        self.layers[x][position] = 1
        self.counts[x] += 1
        # A fresh version invalidates earlier heap records for this layer.
        self._record_layer(x)

    def unsetCell(self, x: int, y: int, z: int) -> None:
        position = y * self.n + z
        # Likewise, clearing an already-empty cell leaves counts unchanged.
        if not self.layers[x][position]:
            return
        self.layers[x][position] = 0
        self.counts[x] -= 1
        self._record_layer(x)

    def largestMatrix(self) -> int:
        # Heap ordering already prefers greater layer IDs when counts tie.
        while True:
            negative_count, negative_layer, version = self.heap[0]
            layer = -negative_layer
            if version == self.version[layer] and \
                    -negative_count == self.counts[layer]:
                return layer
            heapq.heappop(self.heap)


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    matrix = None
    for operation, values in zip(ops, args):
        if operation == "Matrix3D":
            matrix = Matrix3D(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(matrix, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["Matrix3D", "largestMatrix", "setCell", "setCell", "setCell",
         "largestMatrix", "unsetCell", "largestMatrix"],
        [[3], [], [0, 0, 0], [0, 1, 1], [2, 0, 0], [], [0, 0, 0], []],
    ) == [None, 2, None, None, None, 0, None, 2]
    assert replay(
        ["Matrix3D", "setCell", "setCell", "largestMatrix", "unsetCell",
         "largestMatrix"],
        [[2], [0, 0, 0], [1, 0, 0], [], [1, 0, 0], []],
    ) == [None, None, None, 1, None, 0]
    print("All tests passed")
