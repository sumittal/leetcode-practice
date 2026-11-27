"""
LeetCode 763: Partition Labels
Difficulty: Medium
Pattern: Greedy
Video Reference: https://www.youtube.com/watch?v=B7m8UmZE-vw
Complexity:
    - Time: O(n)
    - Space: O(1) for a fixed alphabet
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Last positions define how far a partition must extend for each character.
        last_position = {character: index for index, character in enumerate(s)}
        partitions = []
        start = 0
        end = 0
        # start marks the first character not yet assigned to a closed partition.
        # The active end expands whenever a seen character appears again later.
        for index, character in enumerate(s):
            end = max(end, last_position[character])
            if index == end:
                # No character in this prefix occurs beyond the current boundary.
                partitions.append(end - start + 1)
                start = index + 1
                # The next partition begins immediately after the closed segment.
                # Resetting the active boundary lets the next segment grow independently.
            # Advancing only at a valid boundary guarantees no character is split.
        # The collected lengths cover the full string without overlap.
        # Their sum equals the input length because each boundary advances monotonically.
        return partitions


if __name__ == "__main__":
    solution = Solution()
    assert solution.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert solution.partitionLabels("eccbbbbdec") == [10]
    assert solution.partitionLabels("a") == [1]
    assert solution.partitionLabels("") == []
    print("All tests passed")
