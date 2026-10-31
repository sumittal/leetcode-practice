import heapq
from typing import List, Set, Tuple


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        # The start elevation is the minimum possible initial water level.
        # Heap priority is the smallest water level sufficient for this path so far.
        frontier: List[Tuple[int, int, int]] = [(grid[0][0], 0, 0)]
        visited: Set[Tuple[int, int]] = set()
        while frontier:
            level, row, column = heapq.heappop(frontier)
            # Multiple routes may enqueue a coordinate with different required levels.
            if (row, column) in visited:
                # A lower-priority path already finalized this cell's minimum level.
                continue
            visited.add((row, column))
            # The first pop finalizes this coordinate's minimum bottleneck cost.
            if row == rows - 1 and column == columns - 1:
                # The first destination popped has the globally minimum path maximum.
                return level
            for next_row, next_column in (
                (row + 1, column),
                (row - 1, column),
                (row, column + 1),
                (row, column - 1),
            ):
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and (next_row, next_column) not in visited
                ):
                    # A path must wait for the higher of its prior level and this cell.
                    next_level = max(level, grid[next_row][next_column])
                    heapq.heappush(frontier, (next_level, next_row, next_column))
            # Finalized cells need not be re-enqueued from another neighbor.
            # Each grid edge is considered only when one endpoint is finalized.
            # The max transition, rather than a sum, models the required water height.
        # A rectangular grid always has a path between its opposite corners.
        # The fallback is unreachable for the nonempty square grids in the constraints.
        return -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.swimInWater([[0, 2], [1, 3]]) == 3
    assert (
        solution.swimInWater(
            [
                [0, 1, 2, 3, 4],
                [24, 23, 22, 21, 5],
                [12, 13, 14, 15, 16],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6],
            ]
        )
        == 16
    )
    assert solution.swimInWater([[7]]) == 7
    print("All tests passed")
