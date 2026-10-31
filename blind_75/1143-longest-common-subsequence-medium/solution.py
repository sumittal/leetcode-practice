"""
LeetCode 1143: Longest Common Subsequence
Difficulty: Medium
Pattern: 2-D Dynamic Programming
Video Reference: https://www.youtube.com/watch?v=Ua0GhsJSlWM
Complexity:
    - Time: O(m*n)
    - Space: O(m*n)
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Each transition uses already-computed shorter prefix pairs.
        # Zero row and column model an empty prefix of either string.
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        # All prefix-pair states are filled from shorter prefixes to longer ones.
        # Each cell measures the two prefixes ending at indices i-1 and j-1.
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                # Indices are shifted by one so dp row/column zero stay as empty prefixes.
                # Matching characters extend the diagonal common prefix by one.
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # On mismatch, dropping either last character preserves the better prefix.
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # The final cell compares both complete strings.
        return dp[-1][-1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.longestCommonSubsequence("abcde", "ace") == 3
    assert solution.longestCommonSubsequence("abc", "abc") == 3
    assert solution.longestCommonSubsequence("abc", "def") == 0
    assert solution.longestCommonSubsequence("", "a") == 0
    print("All tests passed")
