from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # Starting with one input bounds the candidate by a real string.
        prefix = strs[0]
        # The candidate can only shrink as more strings constrain it.
        for word in strs[1:]:
            # Remove one trailing character until the candidate fits this word.
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
            # The candidate now matches the beginning of every processed word.
            # Previously processed words still share every retained character.
        # Each iteration can only shorten the common prefix.
        # A single input skips the loop and is returned unchanged.
        # Empty candidate is decisive because no shorter prefix exists.
        return prefix


if __name__ == "__main__":
    solution = Solution()
    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert solution.longestCommonPrefix([""]) == ""
    assert solution.longestCommonPrefix(["alone"]) == "alone"
    print("All tests passed")
