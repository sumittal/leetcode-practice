

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        if window_size > len(s2):
            return False
        # Fixed alphabet counters represent the needed and current multiplicities.
        target_counts = [0] * 26
        window_counts = [0] * 26
        for char in s1:
            target_counts[ord(char) - ord("a")] += 1
        for char in s2[:window_size]:
            window_counts[ord(char) - ord("a")] += 1
        # This initial slice establishes a full-size window before sliding begins.
        # Every permutation must occupy exactly one complete window of this size.
        if window_counts == target_counts:
            return True
        for right in range(window_size, len(s2)):
            # Add the incoming character and remove the character leaving the window.
            window_counts[ord(s2[right]) - ord("a")] += 1
            outgoing = s2[right - window_size]
            window_counts[ord(outgoing) - ord("a")] -= 1
            # Adding and removing one character keeps the window length invariant.
            # Characters outside the current window no longer affect its comparison.
            # Matching multiplicities, not just a matching set, proves inclusion.
            if window_counts == target_counts:
                return True
        # No length-s1 window has the same character counts.
        return False


if __name__ == "__main__":
    solution = Solution()
    assert solution.checkInclusion("ab", "eidbaooo") is True
    assert solution.checkInclusion("ab", "eidboaoo") is False
    assert solution.checkInclusion("adc", "dcda") is True
    assert solution.checkInclusion("aab", "eidbaaoo") is True
    assert solution.checkInclusion("abcd", "abc") is False
    print("All tests passed")
