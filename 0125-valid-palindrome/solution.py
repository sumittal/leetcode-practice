"""
LeetCode 125: Valid Palindrome
Difficulty: Easy
Pattern: Two Pointers
Video Reference: https://www.youtube.com/watch?v=jJXJ16kPFWg
Complexity:
    - Time: O(n)
    - Space: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            # Advance each side to the next character that participates in the palindrome.
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            # Compare case-insensitively, then consume the matched pair by moving inward.
            if s[left].casefold() != s[right].casefold():
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.isPalindrome("A man, a plan, a canal: Panama") is True
    assert solution.isPalindrome("race a car") is False
    assert solution.isPalindrome(" ") is True
    assert solution.isPalindrome("0P") is False
    assert solution.isPalindrome("A\u00c5a") is True
    print("All tests passed")
