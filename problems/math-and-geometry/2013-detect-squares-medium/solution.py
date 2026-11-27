"""
LeetCode 2013: Detect Squares
Difficulty: Medium
Pattern: Math & Geometry
Video Reference: https://www.youtube.com/watch?v=bahebearrDc
Complexity:
    - Time: O(P) per count
    - Space: O(P)
"""

from typing import Dict, List, Tuple


class DetectSquares:
    def __init__(self) -> None:
        # Multiplicities matter because duplicate points are distinct selections.
        self.points: Dict[Tuple[int, int], int] = {}

    def add(self, point: List[int]) -> None:
        coordinate = (point[0], point[1])
        # Count rather than store a set so repeated adds affect future square counts.
        self.points[coordinate] = self.points.get(coordinate, 0) + 1

    def count(self, point: List[int]) -> int:
        query_x, query_y = point
        squares = 0
        # The query itself need not have been added to the data structure.
        # Choose the opposite vertical corner; the side length fixes both other x values.
        for (x, y), vertical_count in self.points.items():
            if x != query_x or y == query_y:
                # A square needs a nonzero vertical side on the query's x-coordinate.
                continue
            side = abs(y - query_y)
            # Either horizontal direction forms a square of the same side length.
            for other_x in (query_x - side, query_x + side):
                lower_corner = self.points.get((other_x, query_y), 0)
                upper_corner = self.points.get((other_x, y), 0)
                # Multiply corner multiplicities to count all point selections.
                squares += vertical_count * lower_corner * upper_corner
            # Checking both horizontal directions includes squares on either side.
        # Every axis-aligned square with this query is counted at its vertical corner.
        # The side length is nonzero, so the two directions never describe one square twice.
        return squares


if __name__ == "__main__":
    squares = DetectSquares()
    squares.add([3, 10])
    squares.add([11, 2])
    squares.add([3, 2])
    assert squares.count([11, 10]) == 1
    assert squares.count([14, 8]) == 0
    squares.add([11, 2])
    assert squares.count([11, 10]) == 2
    squares = DetectSquares()
    squares.add([0, 0])
    squares.add([0, 1])
    squares.add([1, 0])
    assert squares.count([1, 1]) == 1
    print("All tests passed")
