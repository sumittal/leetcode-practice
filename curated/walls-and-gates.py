from collections import deque
from typing import Deque, List, Tuple

INF = 2147483647


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms or not rooms[0]:
            return
        # Distances start at INF and shrink only when reached from a gate.
        rows = len(rooms)
        columns = len(rooms[0])
        gates: Deque[Tuple[int, int]] = deque()
        # Queue every gate as a distance-zero source while leaving walls untouched.
        for row in range(rows):
            for column in range(columns):
                if rooms[row][column] == 0:
                    gates.append((row, column))
        # Multi-source BFS reaches each empty room first by a shortest gate path.
        # Every gate enters at level zero, so all queue layers represent exact distances.
        while gates:
            row, column = gates.popleft()
            # FIFO order guarantees the current room already has its shortest distance.
            next_distance = rooms[row][column] + 1
            for next_row, next_column in (
                (row + 1, column),
                (row - 1, column),
                (row, column + 1),
                (row, column - 1),
            ):
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and rooms[next_row][next_column] == 2147483647
                ):
                    # Writing the distance marks this room so it is enqueued once.
                    # A non-INF cell is either blocked or already has an equal/shorter route.
                    rooms[next_row][next_column] = next_distance
                    gates.append((next_row, next_column))
            # Walls, gates, and previously reached rooms are never overwritten.


if __name__ == "__main__":
    solution = Solution()
    rooms = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF],
    ]
    assert solution.wallsAndGates(rooms) is None
    assert rooms == [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4],
    ]
    second = [[0, INF], [-1, INF]]
    solution.wallsAndGates(second)
    assert second == [[0, 1], [-1, 2]]
    unreachable = [[INF, -1], [-1, INF]]
    solution.wallsAndGates(unreachable)
    assert unreachable == [[INF, -1], [-1, INF]]
    empty = []
    assert solution.wallsAndGates(empty) is None
    print("All tests passed")
