"""
LeetCode 621: Task Scheduler
Difficulty: Medium
Pattern: Heap / Priority Queue
Video Reference: https://www.youtube.com/watch?v=s8p8ukTyA2I
Complexity:
    - Time: O(T + A)
    - Space: O(A)
"""

from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        # Task labels matter only through their frequencies, not their identities.
        # The most frequent task defines rows of length n + 1 in a schedule.
        frequencies = Counter(tasks)
        maximum = max(frequencies.values())
        # Every task tied at maximum frequency needs a slot in the final row.
        maximum_count = sum(count == maximum for count in frequencies.values())
        # A final partial row contains exactly the tasks tied for maximum count.
        # Idle slots between maximum-frequency tasks form the cooldown lower bound.
        cooldown_bound = (maximum - 1) * (n + 1) + maximum_count
        # Other tasks can fill idles, but total execution length remains a lower bound.
        # The formula never schedules fewer units than the tasks that actually exist.
        # When the cooldown bound wins, its gaps are the unavoidable idle intervals.
        return max(len(tasks), cooldown_bound)


if __name__ == "__main__":
    solution = Solution()
    assert solution.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert solution.leastInterval(["A", "C", "A", "B", "D", "B"], 1) == 6
    assert solution.leastInterval(["A", "A", "A", "B", "B", "B"], 3) == 10
    assert solution.leastInterval(["A", "A", "A"], 0) == 3
    assert solution.leastInterval([], 2) == 0
    print("All tests passed")
