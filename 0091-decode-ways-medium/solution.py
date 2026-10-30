"""
LeetCode 91: Decode Ways
Difficulty: Medium
Pattern: 1-D Dynamic Programming
Video Reference: https://www.youtube.com/watch?v=6aEyTjOwlJU
Complexity:
    - Time: O(n)
    - Space: O(1)
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        # The recurrence counts decodings of prefixes ending at each scan index.
        # Empty input has no decoding under the problem's nonempty-string rule.
        if not s or s[0] == "0":
            return 0
        # The empty prefix and the first nonzero digit each have one decoding.
        two_back, one_back = 1, 1
        # These are dp[i-2] and dp[i-1] before processing position i.
        for i in range(1, len(s)):
            current = one_back if s[i] != "0" else 0
            # A zero cannot stand alone, so it starts this position with no one-digit path.
            pair = int(s[i - 1 : i + 1])
            # A pair contributes only for values 10 through 26.
            if 10 <= pair <= 26:
                # A valid two-digit token extends every decoding two positions back.
                current += two_back
            # Roll the DP window after both single and pair transitions are combined.
            two_back, one_back = one_back, current
        # A leading zero was rejected above; trailing zeroes were handled by pair transitions.
        return one_back


if __name__ == "__main__":
    solution = Solution()
    assert solution.numDecodings("12") == 2
    assert solution.numDecodings("226") == 3
    assert solution.numDecodings("06") == 0
    assert solution.numDecodings("10") == 1
    assert solution.numDecodings("27") == 1
    print("All tests passed")
