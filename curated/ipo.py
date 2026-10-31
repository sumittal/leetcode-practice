import heapq
from typing import List


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        # Sort once so each capital requirement enters the candidate heap once.
        projects = sorted(zip(capital, profits))
        # Heap entries are negated because heapq exposes the smallest item.
        available = []
        project_index = 0
        for _ in range(k):
            # Add every project affordable with the capital at this round's start.
            while project_index < len(projects) and projects[project_index][0] <= w:
                heapq.heappush(available, -projects[project_index][1])
                project_index += 1
            # No eligible project can increase the capital in a later round.
            if not available:
                break
            # Projects not yet affordable stay sorted for a future round.
            # Greedy choice is the highest profit among currently feasible projects.
            w -= heapq.heappop(available)
            # The selected project is removed and cannot be used again.
        # Capital never decreases because project profits are nonnegative.
        return w


if __name__ == "__main__":
    solution = Solution()
    assert solution.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]) == 4
    assert solution.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]) == 6
    assert solution.findMaximizedCapital(1, 0, [1, 2, 3], [1, 1, 2]) == 0
    assert solution.findMaximizedCapital(0, 7, [1], [0]) == 7
    print("All tests passed")
