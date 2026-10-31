"""
LeetCode 13: Roman to Integer
Difficulty: Easy
Pattern: Math & Geometry
Video Reference: https://www.youtube.com/watch?v=3jdxYj3DD98
Complexity:
    - Time: O(n)
    - Space: O(1)
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        # Values let the scan apply one rule to every Roman symbol.
        # Each lookup is constant time, so the scan stays linear in numeral length.
        values = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}
        total = 0
        for index, symbol in enumerate(s):
            value = values[symbol]
            # A smaller symbol before a larger one forms a subtractive pair.
            if index + 1 < len(s) and value < values[s[index + 1]]:
                total -= value
            else:
                # All non-subtractive symbols contribute positively.
                total += value
            # Each symbol is accounted for exactly once.
            # Valid numeral syntax guarantees any subtraction is a legal pair.
        # The input is guaranteed to be a valid Roman numeral.
        # Net subtraction followed by addition encodes each subtractive pair.
        return total


if __name__ == "__main__":
    solution = Solution()
    assert solution.romanToInt("III") == 3
    assert solution.romanToInt("LVIII") == 58
    assert solution.romanToInt("MCMXCIV") == 1994
    assert solution.romanToInt("IV") == 4
    print("All tests passed")
