from collections import deque
from typing import List, Set, Tuple


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows, cols = len(heights), len(heights[0])

        def reach(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            # This reverse search computes cells that can drain downhill to these borders.
            # Ocean-border cells are reachable without traversing another island cell.
            seen = set(starts)
            queue = deque(starts)
            # Each cell enters the queue once, making this a linear grid traversal.
            # The same border corner may seed both oceans, harmlessly deduplicated here.
            while queue:
                r, c = queue.popleft()
                # Each popped coordinate is already in seen, so it is processed once.
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    # Reverse flow can climb only to an equal or higher neighbor.
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in seen
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        seen.add((nr, nc))
                        queue.append((nr, nc))
            return seen

        pac = [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)]
        # Seed every cell along each ocean-facing edge, including shared corners.
        atl = [(r, cols - 1) for r in range(rows)] + [
            (rows - 1, c) for c in range(cols)
        ]
        # A cell drains to both oceans exactly when both reverse searches reach it.
        both = reach(pac) & reach(atl)
        # Sorting makes a deterministic result while preserving the accepted coordinate set.
        return [[r, c] for r, c in sorted(both)]


if __name__ == "__main__":
    solution = Solution()
    expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    assert sorted(
        map(
            tuple,
            solution.pacificAtlantic(
                [
                    [1, 2, 2, 3, 5],
                    [3, 2, 3, 4, 4],
                    [2, 4, 5, 3, 1],
                    [6, 7, 1, 4, 5],
                    [5, 1, 1, 2, 4],
                ]
            ),
        )
    ) == sorted(map(tuple, expected))
    assert solution.pacificAtlantic([[1]]) == [[0, 0]]
    assert sorted(map(tuple, solution.pacificAtlantic([[1, 2], [4, 3]]))) == [
        (0, 1),
        (1, 0),
        (1, 1),
    ]
    print("All tests passed")
