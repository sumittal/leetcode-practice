"""
LeetCode 242: Valid Anagram
Difficulty: Easy
Pattern: Arrays & Hashing
Video Reference: https://www.youtube.com/watch?v=9UtInBqnCgA
Complexity:
    - Time: O(n)
    - Space: O(k)
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Rearrangement preserves length, so this rejects impossible pairs early.
        if len(s) != len(t):
            return False
        # Counter retains multiplicities, unlike comparing sets of characters.
        # Equality of the counters means every character occurs equally often.
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    solution = Solution()
    assert solution.isAnagram("anagram", "nagaram") is True
    assert solution.isAnagram("rat", "car") is False
    assert solution.isAnagram("", "") is True
    assert solution.isAnagram("aacc", "ccac") is False
    print("All tests passed")
