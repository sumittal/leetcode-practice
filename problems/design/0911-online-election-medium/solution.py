"""
LeetCode 911: Online Election
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+911+Online+Election+neetcode
Complexity:
    - Time: construction O(n), q O(log n)
    - Space: O(n)
"""

from bisect import bisect_right
from typing import Dict, List


class TopVotedCandidate:
    # Precomputed leaders turn arbitrary-time queries into binary searches.
    def __init__(self, persons: List[int], times: List[int]):
        # Leader snapshots align one-to-one with the chronological vote times.
        self.times = times
        self.leaders: List[int] = []
        counts: Dict[int, int] = {}
        leader = -1
        maximum = 0
        for person in persons:
            counts[person] = counts.get(person, 0) + 1
            # Counts need not be retained outside construction.
            # Later votes win ties because the current person becomes leader.
            if counts[person] >= maximum:
                # A later voter takes over on a tie under the problem's rule.
                leader = person
                maximum = counts[person]
            self.leaders.append(leader)
            # A snapshot answers all later queries between adjacent vote times.

    def q(self, t: int) -> int:
        # The latest voting event no later than t determines the answer.
        index = bisect_right(self.times, t) - 1
        # bisect_right selects the vote at t when the query exactly matches it.
        return self.leaders[index]


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    election = None
    for op, values in zip(ops, args):
        if op == "TopVotedCandidate":
            election = TopVotedCandidate(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(election, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"],
        [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]],
         [3], [12], [25], [15], [24], [8]],
    ) == [None, 0, 1, 1, 0, 0, 1]
    print("All tests passed")
