"""
LeetCode 647: Palindromic Substrings
Difficulty: Medium
Pattern: 1-D Dynamic Programming
Video Reference: https://www.youtube.com/watch?v=4RACzI5-du8
Complexity:
    - Time: O(n^2)
    - Space: O(1)
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        # Each center is independent; count expansions rather than unique text values.
        # The running total increases once for every valid [left, right] interval.
        count = 0
        # The loop tests both character centers and gaps between adjacent characters.

        def expand(left: int, right: int) -> None:
            nonlocal count
            # A mismatch or boundary crossing ends this center's nested palindrome chain.
            # Every successful expansion is a distinct palindrome substring.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                # Continue outward because any larger palindrome shares this center.
                left -= 1
                right += 1

        for center in range(len(s)):
            # Every substring has exactly one odd or even center in this scan.
            # Every odd palindrome has a character center.
            expand(center, center)  # Odd-length centers.
            expand(center, center + 1)  # Even-length centers.
        return count


if __name__ == "__main__":
    solution = Solution()
    assert solution.countSubstrings("abc") == 3
    assert solution.countSubstrings("aaa") == 6
    assert solution.countSubstrings("") == 0
    assert solution.countSubstrings("a") == 1
    print("All tests passed")
