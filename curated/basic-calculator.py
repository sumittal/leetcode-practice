from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        # result and sign describe the expression parsed at the current depth.
        # number is committed only when an operator or parenthesis closes it.
        result = 0
        number = 0
        sign = 1
        stack: List[int] = []
        for character in s:
            if character.isdigit():
                # Consecutive digits build one potentially multi-digit operand.
                number = number * 10 + int(character)
            elif character in "+-":
                # Commit the previous operand before changing its sign.
                result += sign * number
                number = 0
                sign = 1 if character == "+" else -1
            elif character == "(":
                # Save the enclosing expression context before entering a subexpression.
                # The stored sign will apply to the whole nested result.
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif character == ")":
                # Finish the inner operand, apply its saved outer sign, and restore sum.
                result += sign * number
                number = 0
                result *= stack.pop()
                result += stack.pop()
            # Spaces require no state change and are ignored.
            # Parenthesis markers need no explicit token because context is stacked.
        # The last number has no following operator to trigger its accumulation.
        return result + sign * number


if __name__ == "__main__":
    solution = Solution()
    assert solution.calculate("1 + 1") == 2
    assert solution.calculate(" 2-1 + 2 ") == 3
    assert solution.calculate("(1+(4+5+2)-3)+(6+8)") == 23
    assert solution.calculate("-(3 + (4 + 5))") == -12
    print("All tests passed")
