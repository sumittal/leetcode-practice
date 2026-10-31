

class Solution:
    def isValid(self, s: str) -> bool:
        # Each closing token maps to the only opener that may match it.
        opening_for = {")": "(", "]": "[", "}": "{"}
        openings = set(opening_for.values())
        # Keep unmatched opening brackets in their original nesting order.
        stack = []  # type: List[str]
        for character in s:
            if character in openings:
                # A future closer must match this opener unless a later opener intervenes.
                stack.append(character)
            else:
                # A closer must match the most recent unmatched opener.
                if not stack or stack.pop() != opening_for[character]:
                    return False
        # Any leftover opener is unmatched; an empty stack means all brackets paired.
        return not stack


if __name__ == "__main__":
    solution = Solution()
    assert solution.isValid("()") is True
    assert solution.isValid("()[]{}") is True
    assert solution.isValid("(]") is False
    assert solution.isValid("([])") is True
    assert solution.isValid("([)]") is False
    assert solution.isValid("") is True
    assert solution.isValid("(") is False
    assert solution.isValid(")") is False
    print("All tests passed")
