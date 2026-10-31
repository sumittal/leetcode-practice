"""
LeetCode 139: Word Break
Difficulty: Medium
Pattern: 1-D Dynamic Programming
Video Reference: https://www.youtube.com/watch?v=Sx9NNgInc3A
Complexity:
    - Time: O(n^2)
    - Space: O(n)
"""

from typing import List, Set


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Prefix DP avoids retrying the same segmentation boundaries recursively.
        # A set makes dictionary membership constant-time for each candidate substring.
        words: Set[str] = set(wordDict)
        # reachable[i] means exactly the prefix s[:i] can be segmented.
        reachable = [False] * (len(s) + 1)
        reachable[0] = True
        # A false prefix stays unreachable until a prior split and suffix both match.
        # The empty prefix is the starting split for any first dictionary word.
        for end in range(1, len(s) + 1):
            # Check all possible final words, but only after a reachable split point.
            # A reachable prefix plus a dictionary word ending here forms a valid split.
            reachable[end] = any(
                reachable[start] and s[start:end] in words for start in range(end)
            )
        # The final prefix is the full string.
        return reachable[-1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.wordBreak("leetcode", ["leet", "code"]) is True
    assert solution.wordBreak("applepenapple", ["apple", "pen"]) is True
    assert solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
    assert solution.wordBreak("", ["a"]) is True
    print("All tests passed")
