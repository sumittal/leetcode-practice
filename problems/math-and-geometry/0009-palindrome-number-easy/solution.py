"""
LeetCode 9: Palindrome Number
Difficulty: Easy
Pattern: Math & Geometry
Video Reference: https://www.youtube.com/watch?v=yubRKwixN-U
Complexity:
    - Time: O(d)
    - Space: O(1)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # A leading zero in a reversed numeral would not be representable.
        # Negative signs do not have a matching trailing digit.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        # Zero is the only value whose final digit may be zero and still mirror.
        reversed_half = 0
        # Reverse only the lower half to avoid converting the whole number.
        while x > reversed_half:
            # Consume one digit from the prefix and append it to the reversed suffix.
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
            # The remaining prefix shrinks as the suffix is reversed.
        # Odd digit counts leave the middle digit at the end of reversed_half.
        # Even digit counts compare the two halves without discarding a digit.
        return x == reversed_half or x == reversed_half // 10


if __name__ == "__main__":
    solution = Solution()
    assert solution.isPalindrome(121) is True
    assert solution.isPalindrome(-121) is False
    assert solution.isPalindrome(10) is False
    assert solution.isPalindrome(0) is True
    assert solution.isPalindrome(1221) is True
    print("All tests passed")
