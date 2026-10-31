class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[j] counts source prefixes that form the first j target characters.
        ways = [0] * (len(t) + 1)
        # The empty target is a subsequence of every source in exactly one way.
        ways[0] = 1
        # Each source character is considered once, either skipped or matched.
        for source_character in s:
            # Descending target lengths preserve the previous source-prefix row.
            # This direction prevents one source position from matching twice.
            for target_length in range(len(t), 0, -1):
                if source_character == t[target_length - 1]:
                    # Matching extends each prior prefix by this source character.
                    ways[target_length] += ways[target_length - 1]
                # A mismatch leaves the existing ways count unchanged.
            # The state recurrence is skip-or-match, with a match added only on equality.
            # The one-dimensional array compresses the standard prefix-pair table.
        # The final state counts embeddings of the complete target in s.
        # Different index choices count separately even when characters are equal.
        # Empty-target base ways remain one throughout the source scan.
        return ways[-1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.numDistinct("rabbbit", "rabbit") == 3
    assert solution.numDistinct("babgbag", "bag") == 5
    assert solution.numDistinct("abc", "") == 1
    assert solution.numDistinct("a", "aa") == 0
    print("All tests passed")
