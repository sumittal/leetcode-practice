"""
LeetCode 150: Evaluate Reverse Polish Notation
Difficulty: Medium
Pattern: Stack
Video Reference: https://www.youtube.com/watch?v=iu0082c4HDE
Complexity:
    - Time: O(n)
    - Space: O(n)
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # The stack contains completed operands waiting for a later operator.
        values = []
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in operators:
                # Numeric tokens become operands for the next operator encountered.
                values.append(int(token))
                continue
            # Pop right before left because subtraction and division are ordered.
            right = values.pop()
            left = values.pop()
            # Every binary operator consumes two stack values and produces one.
            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            else:
                # Integer division must truncate toward zero, not floor negatives.
                magnitude = abs(left) // abs(right)
                result = -magnitude if (left < 0) != (right < 0) else magnitude
                # The sign check applies the quotient's sign after exact integer division.
            # Replace the two operands with their single computed value.
            values.append(result)
        # Valid postfix input leaves exactly one value: the expression result.
        return values[-1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert solution.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert solution.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    ) == 22
    assert solution.evalRPN(["-7", "2", "/"]) == -3
    assert solution.evalRPN(["18"]) == 18
    print("All tests passed")
