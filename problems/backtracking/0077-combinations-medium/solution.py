"""
LeetCode 77: Combinations
Difficulty: Medium
Pattern: Backtracking
Video Reference: https://www.youtube.com/watch?v=q0s6m7AiM7o
Complexity:
    - Time: O(k * C(n,k))
    - Space: O(k) excluding output
"""

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Output stores copies of each completed increasing choice sequence.
        combinations = []
        current = []

        def backtrack(start: int) -> None:
            # A complete path is copied so later undo steps cannot alter output.
            if len(current) == k:
                combinations.append(current[:])
                return
            needed = k - len(current)
            # The upper bound leaves enough values to finish this combination.
            # Candidates beyond it would leave fewer than needed values available.
            last_start = n - needed + 1
            for value in range(start, last_start + 1):
                current.append(value)
                # Increasing choices ensure each subset has exactly one path.
                backtrack(value + 1)
                # Undo this choice before exploring its sibling candidate.
                current.pop()
                # Restoring path length keeps siblings independent.
            # Every recursive branch restores current to its entry state.

        backtrack(1)
        return combinations


if __name__ == "__main__":
    solution = Solution()
    assert sorted(tuple(item) for item in solution.combine(4, 2)) == sorted(
        [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    )
    assert sorted(tuple(item) for item in solution.combine(1, 1)) == [(1,)]
    assert sorted(tuple(item) for item in solution.combine(5, 3)) == sorted(
        [
            (1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5),
            (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5),
        ]
    )
    print("All tests passed")
