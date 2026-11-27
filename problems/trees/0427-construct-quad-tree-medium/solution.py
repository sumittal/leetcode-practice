"""
LeetCode 427: Construct Quad Tree
Difficulty: Medium
Pattern: Trees
Video Reference: https://www.youtube.com/watch?v=UQ-1sBMV0v4
Complexity:
    - Time: O(n^2)
    - Space: O(n^2) for prefix sums and output nodes
"""

from typing import List, Optional


class Node:
    def __init__(
        self,
        val: bool,
        isLeaf: bool,
        topLeft: Optional["Node"] = None,
        topRight: Optional["Node"] = None,
        bottomLeft: Optional["Node"] = None,
        bottomRight: Optional["Node"] = None,
    ) -> None:
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def serialize(root: Optional[Node]) -> List[List[int]]:
    # Leaf values and internal-node markers match the judge's pair format.
    if root is None:
        return []
    # LeetCode serializes each node before its four children.
    output = [[int(root.isLeaf), int(root.val)]]
    if not root.isLeaf:
        for child in (
            root.topLeft,
            root.topRight,
            root.bottomLeft,
            root.bottomRight,
        ):
            output.extend(serialize(child))
    return output


class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        size = len(grid)
        # Prefix cells exclude row zero and column zero for simple rectangle sums.
        # A summed-area table makes each square's uniformity test constant-time.
        prefix = [[0] * (size + 1) for _ in range(size + 1)]
        for row in range(size):
            for column in range(size):
                prefix[row + 1][column + 1] = (
                    grid[row][column]
                    + prefix[row][column + 1]
                    + prefix[row + 1][column]
                    - prefix[row][column]
                )

        def build(row: int, column: int, width: int) -> Node:
            bottom = row + width
            # Coordinates describe a half-open square in the prefix table.
            right = column + width
            ones = (
                prefix[bottom][right]
                - prefix[row][right]
                - prefix[bottom][column]
                + prefix[row][column]
            )
            # Zero or width-squared ones means every cell has the same value.
            if ones == 0 or ones == width * width:
                return Node(ones > 0, True)
            half = width // 2
            # Quadrants are constructed in the order used by LeetCode's Node.
            return Node(
                True,
                False,
                build(row, column, half),
                build(row, column + half, half),
                build(row + half, column, half),
                build(row + half, column + half, half),
            )

        # The input is a nonempty square whose side is a power of two.
        return build(0, 0, size)


if __name__ == "__main__":
    solution = Solution()
    assert serialize(solution.construct([[0, 1], [1, 0]])) == [
        [0, 1],
        [1, 0],
        [1, 1],
        [1, 1],
        [1, 0],
    ]
    assert serialize(solution.construct([[1, 1], [1, 1]])) == [[1, 1]]
    assert serialize(solution.construct([[0, 0], [0, 0]])) == [[1, 0]]
    print("All tests passed")
