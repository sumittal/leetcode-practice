from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # The bank defines exactly which generated strings are valid states.
        if start == end:
            return 0
        allowed = set(bank)
        if end not in allowed:
            return -1
        # BFS level count equals the number of mutations used so far.
        queue = deque([(start, 0)])
        visited = {start}
        bases = ("A", "C", "G", "T")
        while queue:
            gene, steps = queue.popleft()
            # Every neighbor differs at one position and uses a permitted base.
            for index, original in enumerate(gene):
                for base in bases:
                    if base == original:
                        continue
                    mutation = gene[:index] + base + gene[index + 1 :]
                    if mutation not in allowed or mutation in visited:
                        continue
                    # Mark before enqueuing so the same gene is never duplicated.
                    if mutation == end:
                        return steps + 1
                    # Every graph edge changes exactly one gene position.
                    visited.add(mutation)
                    queue.append((mutation, steps + 1))
                # Restoring the next position is implicit because strings are immutable.
                # All generated candidates retain the fixed sequence length.
        # Exhausting all reachable bank entries proves no mutation path exists.
        # FIFO traversal returns a minimum-length mutation sequence first.
        return -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]) == 1
    assert solution.minMutation(
        "AACCGGTT",
        "AAACGGTA",
        ["AACCGGTA", "AACCGCTA", "AAACGGTA"],
    ) == 2
    assert solution.minMutation(
        "AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    ) == 3
    assert solution.minMutation("AACCGGTT", "AACCGGTA", []) == -1
    assert solution.minMutation("AACCGGTT", "AACCGGTT", []) == 0
    print("All tests passed")
