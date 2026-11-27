"""
LeetCode 22: Generate Parentheses
Difficulty: Medium
Pattern: Stack
Video Reference: https://www.youtube.com/watch?v=s9fokUqJ76A
Complexity:
    - Time: O(Cn)
    - Space: O(n) besides the output
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        current = []

        def build(opened: int, closed: int) -> None:
            # Every recursive prefix has at least as many opens as closes.
            # A complete path uses exactly n opening and n closing brackets.
            if opened == n and closed == n:
                combinations.append("".join(current))
                return
            if opened < n:
                # Any prefix may open until it has used all n pairs.
                current.append("(")
                build(opened + 1, closed)
                current.pop()  # Undo the choice before exploring another branch.
            # Explore openings before closings to build each prefix without duplicates.
            if closed < opened:
                # Closing is legal only when it cannot make a prefix unbalanced.
                current.append(")")
                build(opened, closed + 1)
                current.pop()  # Restore the prefix for its caller.

        # Starting with an empty prefix ensures every generated string is balanced.
        build(0, 0)
        return combinations


if __name__ == "__main__":
    solution = Solution()
    assert sorted(solution.generateParenthesis(3)) == sorted(
        ["((()))", "(()())", "(())()", "()(())", "()()()"]
    )
    assert solution.generateParenthesis(1) == ["()"]
    assert solution.generateParenthesis(0) == [""]
    assert sorted(solution.generateParenthesis(2)) == ["(())", "()()"]
    print("All tests passed")
