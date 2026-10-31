"""
LeetCode 43: Multiply Strings
Difficulty: Medium
Pattern: Math & Geometry
Video Reference: https://www.youtube.com/watch?v=1vZswirL8Y8
Complexity:
    - Time: O(mn)
    - Space: O(m+n)
"""

from typing import List


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        # A product of m- and n-digit values fits in at most m+n positions.
        digits: List[int] = [0] * (len(num1) + len(num2))
        # Each digit pair contributes to its aligned result position and carry.
        for first_index in range(len(num1) - 1, -1, -1):
            for second_index in range(len(num2) - 1, -1, -1):
                # Decimal place alignment is determined by the two input indices.
                position = first_index + second_index + 1
                product = (
                    int(num1[first_index]) * int(num2[second_index])
                    + digits[position]
                )
                # Existing position contents are carry accumulated by less-significant products.
                # Keep one decimal digit here and add the quotient to its neighbor.
                digits[position] = product % 10
                digits[position - 1] += product // 10
            # Earlier first-string digits contribute to more significant positions.
        # Strip only unused leading zeros; keep the single zero digit if all are zero.
        first_nonzero = 0
        while first_nonzero < len(digits) - 1 and digits[first_nonzero] == 0:
            first_nonzero += 1
        # Joining individual digits avoids converting either full input to an integer.
        # The output length is bounded by the sum of the input lengths.
        return "".join(str(digit) for digit in digits[first_nonzero:])


if __name__ == "__main__":
    solution = Solution()
    assert solution.multiply("2", "3") == "6"
    assert solution.multiply("123", "456") == "56088"
    assert solution.multiply("0", "52") == "0"
    assert solution.multiply("99", "99") == "9801"
    print("All tests passed")
