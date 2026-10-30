"""
LeetCode 39: Combination Sum
Difficulty: Medium
Pattern: Backtracking
Video Reference: https://www.youtube.com/watch?v=GBKI9VSKdGg
Complexity:
    - Time: O(N^(T/M))
    - Space: O(T/M)
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        # Sorting enables early termination and canonical ordering within each result.
        candidates = sorted(candidates)

        def search(start: int, remaining: int) -> None:
            # Each call owns one partial path and must undo choices before returning.
            # A zero remainder completes one unique nondecreasing candidate sequence.
            if remaining == 0:
                # Copy because path will continue changing during backtracking.
                result.append(path[:])
                return
            # Each recursion level chooses the next value in the combination.
            for i in range(start, len(candidates)):
                value = candidates[i]
                if value > remaining:
                    break  # Sorted values make later choices impossible too.
                path.append(value)  # Reuse is allowed, so recurse from this same index.
                search(i, remaining - value)
                # Pop restores the parent's path before the next candidate is tried.
                path.pop()  # Undo this choice before exploring a sibling combination.

        search(0, target)
        return result


if __name__ == "__main__":
    solution = Solution()
    assert sorted(map(tuple, solution.combinationSum([2, 3, 6, 7], 7))) == [(2, 2, 3), (7,)]
    assert sorted(map(tuple, solution.combinationSum([2, 3, 5], 8))) == [
        (2, 2, 2, 2),
        (2, 3, 3),
        (3, 5),
    ]
    assert solution.combinationSum([2], 1) == []
    assert solution.combinationSum([1], 1) == [[1]]
    print("All tests passed")
