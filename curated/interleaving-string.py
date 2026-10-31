class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        first_length = len(s1)
        second_length = len(s2)
        if first_length + second_length != len(s3):
            # Every source character must be consumed exactly once.
            return False
        # dp[j] means the processed prefixes of s1 and s2 form s3's prefix.
        reachable = [False] * (second_length + 1)
        # The empty prefixes match before either source contributes a character.
        reachable[0] = True
        # The first DP row can consume only a prefix from s2.
        for column in range(1, second_length + 1):
            reachable[column] = (
                reachable[column - 1] and s2[column - 1] == s3[column - 1]
            )
        # Rows advance through s1; columns advance through s2 in place.
        for row in range(1, first_length + 1):
            # Before updating the row, reachable[0] still represents only s1.
            reachable[0] = reachable[0] and s1[row - 1] == s3[row - 1]
            for column in range(1, second_length + 1):
                result_index = row + column - 1
                # The old cell comes from s1; the updated left cell comes from s2.
                from_first = (
                    reachable[column] and s1[row - 1] == s3[result_index]
                )
                from_second = (
                    reachable[column - 1] and s2[column - 1] == s3[result_index]
                )
                reachable[column] = from_first or from_second
            # Increasing columns preserves the current row's left-neighbor state.
        # The last cell represents both complete source strings.
        return reachable[second_length]


if __name__ == "__main__":
    solution = Solution()
    assert solution.isInterleave("aabcc", "dbbca", "aadbbcbcac") is True
    assert solution.isInterleave("aabcc", "dbbca", "aadbbbaccc") is False
    assert solution.isInterleave("", "", "") is True
    assert solution.isInterleave("a", "", "a") is True
    print("All tests passed")
