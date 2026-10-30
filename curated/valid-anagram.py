from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Unequal lengths cannot have matching character counts.
        if len(s) != len(t):
            return False
        # Counter retains multiplicities, unlike comparing sets of characters.
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    solution = Solution()
    assert solution.isAnagram("anagram", "nagaram") is True
    assert solution.isAnagram("rat", "car") is False
    assert solution.isAnagram("", "") is True
    assert solution.isAnagram("aacc", "ccac") is False
    print("All tests passed")
