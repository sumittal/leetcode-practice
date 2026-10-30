from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Store each character's latest index to jump past a repeated occurrence.
        last_seen = {}  # type: Dict[str, int]
        # left is the start of the current duplicate-free window.
        left = 0
        # Empty input leaves this at zero and has no candidate window.
        longest = 0
        for right, character in enumerate(s):
            # -1 treats a character not seen before as having no blocking occurrence.
            previous = last_seen.get(character, -1)
            # Never move left backward for an occurrence outside the current window.
            left = max(left, previous + 1)
            # Record the current index only after using the prior occurrence to adjust left.
            last_seen[character] = right
            # The inclusive window [left, right] is now duplicate-free.
            longest = max(longest, right - left + 1)
        # Return the largest valid window length encountered.
        return longest


if __name__ == "__main__":
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    assert solution.lengthOfLongestSubstring("") == 0
    assert solution.lengthOfLongestSubstring("abba") == 2
    assert solution.lengthOfLongestSubstring("dvdf") == 3
    print("All tests passed")
