class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # A positional mapping requires equal-length input strings.
        if len(s) != len(t):
            return False
        # Forward and reverse maps together enforce a one-to-one substitution.
        # Each mapping is created on its first aligned character pair.
        forward = {}
        reverse = {}
        for source, target in zip(s, t):
            # A source character must keep its first assigned target.
            if source in forward and forward[source] != target:
                return False
            # A target character cannot be claimed by a different source.
            if target in reverse and reverse[target] != source:
                return False
            forward[source] = target
            reverse[target] = source
            # Recording both directions prevents many-to-one mappings.
            # A consistent prefix can be extended without revisiting earlier pairs.
        # Every aligned pair now agrees with the same bijection.
        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.isIsomorphic("egg", "add") is True
    assert solution.isIsomorphic("foo", "bar") is False
    assert solution.isIsomorphic("paper", "title") is True
    assert solution.isIsomorphic("ab", "aa") is False
    print("All tests passed")
