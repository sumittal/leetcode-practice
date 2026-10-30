from typing import Dict, List, Tuple


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Each signature maps to all words with exactly the same character counts.
        groups = {}  # type: Dict[Tuple[int, ...], List[str]]
        for word in strs:
            # The problem guarantees lowercase English letters, so 26 counts suffice.
            counts = [0] * 26
            for character in word:
                # Incrementing counts makes the signature independent of character order.
                counts[ord(character) - ord("a")] += 1
            # Tuples are hashable dictionary keys; the mutable counts list is not.
            key = tuple(counts)
            # Create a group on first sight of this signature, then append the word.
            groups.setdefault(key, []).append(word)
        # The keys are only grouping aids; callers need the grouped word lists.
        return list(groups.values())


if __name__ == "__main__":
    solution = Solution()
    result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted(sorted(group) for group in result) == sorted(
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    )
    assert sorted(sorted(group) for group in solution.groupAnagrams([""])) == [[""]]
    assert solution.groupAnagrams(["a"]) == [["a"]]
    assert sorted(
        sorted(group) for group in solution.groupAnagrams(["ab", "ba", "a"])
    ) == [["a"], ["ab", "ba"]]
    print("All tests passed")
