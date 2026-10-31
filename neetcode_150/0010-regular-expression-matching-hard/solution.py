"""
LeetCode 10: Regular Expression Matching
Difficulty: Hard
Pattern: 2-D Dynamic Programming
Video Reference: https://www.youtube.com/watch?v=HAA8mgxlov8
Complexity:
    - Time: O(mn)
    - Space: O(mn)
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        text_length = len(s)
        pattern_length = len(p)
        # dp[i][j] means s[:i] matches p[:j].
        matched = [
            [False] * (pattern_length + 1) for _ in range(text_length + 1)
        ]
        # Empty text matches the empty pattern.
        matched[0][0] = True
        # Other cells default false until a valid prefix transition proves them.
        # A star pair may disappear entirely when matching empty text.
        for column in range(2, pattern_length + 1):
            if p[column - 1] == "*":
                matched[0][column] = matched[0][column - 2]
        # Prefix rows advance through text; columns advance through pattern tokens.
        for row in range(1, text_length + 1):
            for column in range(1, pattern_length + 1):
                token = p[column - 1]
                if token == "." or token == s[row - 1]:
                    # A literal or dot consumes one character from both prefixes.
                    matched[row][column] = matched[row - 1][column - 1]
                elif token == "*":
                    # Zero occurrences remove the preceding token and this star.
                    matched[row][column] = matched[row][column - 2]
                    previous_token = p[column - 2]
                    if previous_token == "." or previous_token == s[row - 1]:
                        # One-more occurrence consumes text but keeps the star active.
                        matched[row][column] = (
                            matched[row][column] or matched[row - 1][column]
                        )
                    # These two transitions cover every valid zero-or-more use of *.
                    # The repeated token must itself match this text character.
                # Other mismatches leave the default state false.
            # Every recurrence reads an earlier row or a shorter pattern prefix.
        # The bottom-right cell compares both complete strings.
        # Pattern syntax is valid by contract, so every star has a preceding token.
        return matched[text_length][pattern_length]


if __name__ == "__main__":
    solution = Solution()
    assert solution.isMatch("aa", "a") is False
    assert solution.isMatch("aa", "a*") is True
    assert solution.isMatch("ab", ".*") is True
    assert solution.isMatch("aab", "c*a*b") is True
    assert solution.isMatch("mississippi", "mis*is*p*.") is False
    assert solution.isMatch("", "c*") is True
    print("All tests passed")
