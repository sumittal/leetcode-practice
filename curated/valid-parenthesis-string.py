class Solution:
    def checkValidString(self, s: str) -> bool:
        # low and high bound the open count achievable after the current prefix.
        # This interval compactly represents all star interpretations seen so far.
        low = 0
        high = 0
        for character in s:
            if character == "(":
                # An opening parenthesis increments every possible balance.
                low += 1
                high += 1
            elif character == ")":
                # A close decrements balances, but a star may have kept low at zero.
                low = max(0, low - 1)
                high -= 1
            else:
                # A star can close, disappear, or open, widening the possible range.
                low = max(0, low - 1)
                high += 1
            if high < 0:
                # Even treating every star as open cannot repair this prefix.
                return False
            # Clamping low discards negative balances, which are never valid prefixes.
            # Every feasible balance between the bounds remains represented.
        # Some interpretation works exactly when zero remains a possible final balance.
        return low == 0


if __name__ == "__main__":
    solution = Solution()
    assert solution.checkValidString("()") is True
    assert solution.checkValidString("(*)") is True
    assert solution.checkValidString("(*))") is True
    assert solution.checkValidString(")(") is False
    assert solution.checkValidString("") is True
    print("All tests passed")
