"""
LeetCode 76: Minimum Window Substring
Difficulty: Hard
Pattern: Sliding Window
Video Reference: https://www.youtube.com/watch?v=jSto0O4AJbM
Complexity:
    - Time: O(m+n)
    - Space: O(k)
"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # An empty target is already covered by an empty window.
        if not t:
            return ""
        # need stores required multiplicities; presence alone is insufficient for repeats.
        need = Counter(t)
        # window tracks only source characters that also have a target requirement.
        window = Counter()
        # satisfied counts distinct required characters currently meeting their counts.
        satisfied = 0
        # left marks the start of the candidate window being contracted.
        left = 0
        best_start = 0
        # A sentinel larger than every source window means no valid window has been found.
        best_length = len(s) + 1

        # Expand the candidate window one source character at a time.
        for right, character in enumerate(s):
            if character in need:
                # Irrelevant characters do not change whether the target is covered.
                window[character] += 1
                # A requirement becomes satisfied only on reaching its full count.
                if window[character] == need[character]:
                    satisfied += 1

            # All distinct requirements are met, so try every tighter left boundary.
            while satisfied == len(need):
                current_length = right - left + 1
                if current_length < best_length:
                    # Save the shortest valid window seen before removing its left edge.
                    best_start = left
                    best_length = current_length

                outgoing = s[left]
                if outgoing in need:
                    # Removing a required character may make this window deficient.
                    window[outgoing] -= 1
                    # Crossing below the required count makes the window invalid again.
                    if window[outgoing] < need[outgoing]:
                        satisfied -= 1
                # Advance even over irrelevant characters to keep shrinking the candidate.
                left += 1

        # The sentinel remains unchanged when no source interval covered the target.
        if best_length > len(s):
            return ""
        # Return the saved shortest interval; end is exclusive.
        return s[best_start : best_start + best_length]


if __name__ == "__main__":
    solution = Solution()
    assert solution.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert solution.minWindow("a", "a") == "a"
    assert solution.minWindow("a", "aa") == ""
    assert solution.minWindow("", "a") == ""
    assert solution.minWindow("abc", "") == ""
    assert solution.minWindow("aa", "aa") == "aa"
    print("All tests passed")
