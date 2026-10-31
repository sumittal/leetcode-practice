class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # matched counts the prefix of s already found in t.
        # Source characters are consumed only in their given order.
        matched = 0
        for character in t:
            # Only the next required character can advance the subsequence.
            if matched < len(s) and s[matched] == character:
                matched += 1
            # Skipped source characters do not invalidate an ordered match.
            # A successful match advances the next required target position.
        # Reaching the end of s proves every character appeared in order.
        # Empty s succeeds without consuming any source character.
        # The scan uses constant auxiliary state regardless of string length.
        return matched == len(s)


if __name__ == "__main__":
    solution = Solution()
    assert solution.isSubsequence("abc", "ahbgdc") is True
    assert solution.isSubsequence("axc", "ahbgdc") is False
    assert solution.isSubsequence("", "anything") is True
    assert solution.isSubsequence("long", "lo") is False
    print("All tests passed")
