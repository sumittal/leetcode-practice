"""
LeetCode 58: Length of Last Word
Difficulty: Easy
Pattern: Arrays & Hashing
Video Reference: https://www.youtube.com/watch?v=KT9rltZTybQ
Complexity:
    - Time: O(n)
    - Space: O(1)
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Begin at the right edge and ignore any trailing separators.
        # The index moves monotonically left, so each character is inspected once.
        index = len(s) - 1
        while index >= 0 and s[index] == " ":
            index -= 1
        # Stop counting at the first separator before the final word.
        length = 0
        while index >= 0 and s[index] != " ":
            length += 1
            index -= 1
        # The first preceding space is excluded from the word length.
        # Scanning stops at the word boundary without allocating split tokens.
        # Leading spaces do not affect the final count.
        # The resulting count is zero only for an input without a word.
        # No substring or token list is needed.
        return length


if __name__ == "__main__":
    solution = Solution()
    assert solution.lengthOfLastWord("Hello World") == 5
    assert solution.lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert solution.lengthOfLastWord("luffy is still joyboy") == 6
    assert solution.lengthOfLastWord("a") == 1
    print("All tests passed")
