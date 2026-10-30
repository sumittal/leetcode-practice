class Solution:
    def longestPalindrome(self, s: str) -> str:
        # The empty interval is the answer for empty input and a fallback for short strings.
        # Half-open bounds identify the best palindrome found so far.
        best_left, best_right = 0, 0
        # The empty interval is the initial answer for empty input.

        def expand(left: int, right: int) -> None:
            nonlocal best_left, best_right
            # The expanding interval remains centered at the chosen one- or two-cell seed.
            # The center may be one character (odd) or a gap (even).
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # The loop crossed the matching boundary, so [left+1:right] is the palindrome.
            if right - left - 1 > best_right - best_left:
                best_left, best_right = left + 1, right

        for center in range(len(s)):
            # Checking every center guarantees the global longest interval is considered.
            # Test both parity choices at every character position.
            expand(center, center)
            expand(center, center + 1)
        return s[best_left:best_right]  # Empty input keeps the initialized empty slice.


if __name__ == "__main__":
    solution = Solution()
    assert solution.longestPalindrome("babad") in ("bab", "aba")
    assert solution.longestPalindrome("cbbd") == "bb"
    assert solution.longestPalindrome("") == ""
    assert solution.longestPalindrome("a") == "a"
    print("All tests passed")
