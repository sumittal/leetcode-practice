"""
LeetCode 28: Find the Index of the First Occurrence in a String
Difficulty: Easy
Pattern: Arrays & Hashing
Video Reference: https://www.youtube.com/watch?v=JoF0Z7nVSrA
Complexity:
    - Time: O(n+m)
    - Space: O(m)
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        # lps[i] is the longest proper prefix ending at needle index i.
        lps = [0] * len(needle)
        prefix = 0
        for index in range(1, len(needle)):
            # Fall back through previous borders when characters disagree.
            while prefix and needle[index] != needle[prefix]:
                prefix = lps[prefix - 1]
            if needle[index] == needle[prefix]:
                prefix += 1
            lps[index] = prefix
            # Each prefix value lets the scan reuse known matching characters.
        # Scan haystack once; i and j never move backward together.
        text_index = 0
        pattern_index = 0
        while text_index < len(haystack):
            if haystack[text_index] == needle[pattern_index]:
                text_index += 1
                pattern_index += 1
                if pattern_index == len(needle):
                    # The matched range ends here, so return its starting offset.
                    return text_index - pattern_index
            elif pattern_index:
                # Preserve the longest viable needle prefix after a mismatch.
                pattern_index = lps[pattern_index - 1]
            else:
                text_index += 1
            # A zero-prefix mismatch advances to a new candidate start.
        # Exhausting the text means no complete needle occurrence exists.
        return -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.strStr("sadbutsad", "sad") == 0
    assert solution.strStr("leetcode", "leeto") == -1
    assert solution.strStr("aaaaa", "bba") == -1
    assert solution.strStr("abc", "") == 0
    print("All tests passed")
