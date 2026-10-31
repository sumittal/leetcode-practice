"""
LeetCode 151: Reverse Words in a String
Difficulty: Medium
Pattern: Two Pointers
Video Reference: https://www.youtube.com/results?search_query=leetcode+151+Reverse+Words+in+a+String+neetcode
Complexity:
    - Time: O(n)
    - Space: O(n)
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        # split without an explicit separator discards empty whitespace runs.
        # Tokenization preserves each non-space word exactly as written.
        words = s.split()
        # Reversing tokens changes word order but preserves each word's spelling.
        words.reverse()
        # Joining with one space normalizes all original spacing.
        result = " ".join(words)
        # Reversing the list changes no character order within a token.
        # An input containing only whitespace becomes the empty string.
        # The original string remains untouched.
        # The result contains no leading or trailing separator.
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.reverseWords("the sky is blue") == "blue is sky the"
    assert solution.reverseWords("  hello world  ") == "world hello"
    assert solution.reverseWords("a good   example") == "example good a"
    assert solution.reverseWords("  ") == ""
    print("All tests passed")
