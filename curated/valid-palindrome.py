class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep both indices on the unprocessed interval being compared.
        left = 0
        right = len(s) - 1
        # When the indices meet or cross, every relevant pair has matched.
        while left < right:
            # Advance each side to the next character that participates in the palindrome.
            # The bounds checks also stop safely when punctuation fills the remaining range.
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            # Compare case-insensitively, then consume the matched pair by moving inward.
            if s[left].casefold() != s[right].casefold():
                # One mismatched participating pair is enough to disprove a palindrome.
                return False
            left += 1
            right -= 1
        # No mismatch was found after ignoring punctuation and letter casing.
        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.isPalindrome("A man, a plan, a canal: Panama") is True
    assert solution.isPalindrome("race a car") is False
    assert solution.isPalindrome(" ") is True
    assert solution.isPalindrome("0P") is False
    assert solution.isPalindrome("A\u00c5a") is True
    print("All tests passed")
