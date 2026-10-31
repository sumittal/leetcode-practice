"""
LeetCode 383: Ransom Note
Difficulty: Easy
Pattern: Hash Table
Video Reference: https://www.youtube.com/results?search_query=leetcode+383+Ransom+Note+neetcode
Complexity:
    - Time: O(n+m)
    - Space: O(Σ)
"""

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Counts represent the remaining supply of each magazine character.
        # Counter defaults missing keys to zero for the early failure check.
        supply = Counter(magazine)
        for character in ransomNote:
            # A missing supply cannot satisfy this required occurrence.
            if supply[character] == 0:
                return False
            supply[character] -= 1
            # Consuming once prevents reusing the same magazine character.
            # The remaining count is the unused inventory after this choice.
        # Reaching the end means all required multiplicities were available.
        # Extra magazine characters are irrelevant to construction.
        # No character order constraint exists, only multiplicity constraints.
        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.canConstruct("a", "b") is False
    assert solution.canConstruct("aa", "ab") is False
    assert solution.canConstruct("aa", "aab") is True
    assert solution.canConstruct("", "anything") is True
    print("All tests passed")
