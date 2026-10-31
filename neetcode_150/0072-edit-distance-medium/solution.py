"""
LeetCode 72: Edit Distance
Difficulty: Medium
Pattern: 2-D Dynamic Programming
Video Reference: https://www.youtube.com/watch?v=XYi2-LPrwm4
Complexity:
    - Time: O(mn)
    - Space: O(min(m,n))
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Keeping the shorter string on columns bounds the rolling table width.
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        # previous[j] is the cost for the prior word1 prefix and word2[:j].
        previous = list(range(len(word2) + 1))
        # This base row transforms the empty prefix using insertions.
        for row, first_character in enumerate(word1, start=1):
            # current[0] deletes every character in this nonempty word1 prefix.
            current = [row] + [0] * len(word2)
            for column, second_character in enumerate(word2, start=1):
                if first_character == second_character:
                    # Matching final characters extends the diagonal state unchanged.
                    current[column] = previous[column - 1]
                else:
                    # Delete, insert, or replace the final character, then add one edit.
                    current[column] = 1 + min(
                        previous[column],
                        current[column - 1],
                        previous[column - 1],
                    )
                # Each cell uses only the previous row and current row's left cell.
            # Advancing rows satisfies the DP's prefix iteration order.
            previous = current
        # The final column compares both complete strings.
        return previous[-1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.minDistance("horse", "ros") == 3
    assert solution.minDistance("intention", "execution") == 5
    assert solution.minDistance("", "abc") == 3
    assert solution.minDistance("same", "same") == 0
    print("All tests passed")
