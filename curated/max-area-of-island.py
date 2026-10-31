from typing import List, Set, Tuple


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        # The visited set avoids modifying the caller's grid while counting.
        rows = len(grid)
        columns = len(grid[0])
        visited: Set[Tuple[int, int]] = set()
        largest = 0
        # Every unvisited land cell starts exactly one component traversal.
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 0 or (row, column) in visited:
                    continue
                # A fresh area counter is isolated to this connected component.
                area = 0
                stack = [(row, column)]
                visited.add((row, column))
                # Mark when pushing so adjacent paths cannot schedule a cell twice.
                while stack:
                    current_row, current_column = stack.pop()
                    area += 1
                    # Only four orthogonal neighbors belong to this island.
                    for next_row, next_column in (
                        (current_row + 1, current_column),
                        (current_row - 1, current_column),
                        (current_row, current_column + 1),
                        (current_row, current_column - 1),
                    ):
                        if (
                            0 <= next_row < rows
                            and 0 <= next_column < columns
                            and grid[next_row][next_column] == 1
                            and (next_row, next_column) not in visited
                        ):
                            visited.add((next_row, next_column))
                            stack.append((next_row, next_column))
                # Compare only after the whole connected component is counted.
                largest = max(largest, area)
                # Visited cells are skipped by the outer scan from this point onward.
        # Water-only grids never raise the initial zero area.
        return largest


if __name__ == "__main__":
    solution = Solution()
    example = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    assert solution.maxAreaOfIsland(example) == 6
    assert solution.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0
    assert solution.maxAreaOfIsland([[1]]) == 1
    assert solution.maxAreaOfIsland([]) == 0
    print("All tests passed")
