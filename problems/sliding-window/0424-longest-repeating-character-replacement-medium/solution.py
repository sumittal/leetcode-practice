"""
LeetCode 424: Longest Repeating Character Replacement
Difficulty: Medium
Pattern: Sliding Window
Video Reference: https://www.youtube.com/watch?v=gqXU1UyA8pk
Complexity:
    - Time: O(n)
    - Space: O(1)
"""

from typing import Dict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # counts describes characters in the current window [left, right].
        counts = {}  # type: Dict[str, int]
        # left advances only when the current window needs more than k replacements.
        left = 0
        # This is a historical maximum and intentionally is not reduced when left moves.
        max_frequency = 0
        # Keep the best valid-length candidate even while scanning later windows.
        longest = 0
        for right, character in enumerate(s):
            # Adding the new right endpoint updates its frequency in the window.
            counts[character] = counts.get(character, 0) + 1
            # Keep the historical max: if stale it may delay shrinking, but not lower the optimum.
            max_frequency = max(max_frequency, counts[character])
            # Window length minus its most frequent character count is replacements needed.
            if right - left + 1 - max_frequency > k:
                # Remove the old left endpoint so the next iteration uses the shifted window.
                counts[s[left]] -= 1
                left += 1
            # With the one-step shrink, the resulting width preserves the best attainable size.
            longest = max(longest, right - left + 1)
        # Return the longest window that can be made uniform with at most k changes.
        return longest


if __name__ == "__main__":
    solution = Solution()
    assert solution.characterReplacement("ABAB", 2) == 4
    assert solution.characterReplacement("AABABBA", 1) == 4
    assert solution.characterReplacement("", 0) == 0
    assert solution.characterReplacement("AAAA", 0) == 4
    assert solution.characterReplacement("ABCDE", 1) == 2
    print("All tests passed")
