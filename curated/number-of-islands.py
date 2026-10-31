from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # A zero-row grid has no components and avoids indexing an absent first row.
        if not grid:
            return 0
        # seen tracks land already assigned to a previously counted island.
        rows, cols = len(grid), len(grid[0])
        seen = set()
        # count increases once per land component, not once per land cell.
        count = 0
        for r in range(rows):
            for c in range(cols):
                # Only unseen land starts a new component traversal.
                if grid[r][c] != "1" or (r, c) in seen:
                    continue
                count += 1
                # Mark the seed before pushing so a neighboring land cell cannot reschedule it.
                stack = [(r, c)]
                seen.add((r, c))
                # Exhaust this entire connected land component before scanning onward.
                while stack:
                    x, y = stack.pop()
                    for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        # Four-neighbor bounds exclude diagonals and outside water.
                        if (
                            0 <= nx < rows
                            and 0 <= ny < cols
                            and grid[nx][ny] == "1"
                            and (nx, ny) not in seen
                        ):
                            seen.add(
                                (nx, ny)
                            )  # Mark at push time so no cell enters twice.
                            stack.append((nx, ny))
        return count


if __name__ == "__main__":
    solution = Solution()
    assert solution.numIslands([list(x) for x in ["11110", "11010", "11000", "00000"]]) == 1
    assert solution.numIslands([list(x) for x in ["11000", "11000", "00100", "00011"]]) == 3
    assert solution.numIslands([list("0")]) == 0
    print("All tests passed")
