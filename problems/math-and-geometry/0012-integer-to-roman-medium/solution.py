"""
LeetCode 12: Integer to Roman
Difficulty: Medium
Pattern: Math & Geometry
Video Reference: https://www.youtube.com/watch?v=ohBNdSJyLh8
Complexity:
    - Time: O(1)
    - Space: O(1)
"""

from typing import List, Tuple


class Solution:
    def intToRoman(self, num: int) -> str:
        # Subtractive tokens precede the smaller additive tokens they replace.
        values: List[Tuple[int, str]] = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
        ]
        # Greedy tokens are ordered by descending decimal value.
        parts = []
        for value, symbol in values:
            # Each value is emitted until the remaining number is smaller.
            count, num = divmod(num, value)
            parts.append(symbol * count)
            # Processing from largest to smallest preserves canonical order.
            # divmod leaves a remainder smaller than the token just considered.
            # A zero count contributes an empty fragment to the output.
        # The allowed input range keeps the number of symbols bounded.
        # Concatenating fragments yields the unique canonical representation.
        return "".join(parts)


if __name__ == "__main__":
    solution = Solution()
    assert solution.intToRoman(3) == "III"
    assert solution.intToRoman(58) == "LVIII"
    assert solution.intToRoman(1994) == "MCMXCIV"
    assert solution.intToRoman(3999) == "MMMCMXCIX"
    print("All tests passed")
