class Solution:
    def reverse(self, x: int) -> int:
        # Keep sign separate so digit extraction operates on a nonnegative magnitude.
        negative = x < 0
        remaining = abs(x)
        reversed_value = 0
        # Extract least-significant decimal digits until no input remains.
        while remaining:
            digit = remaining % 10
            reversed_value = reversed_value * 10 + digit
            remaining //= 10
            # Python integers do not overflow, so the platform bound must be checked later.
            # Arithmetic reversal naturally drops zeroes that were at the input's end.
        # Applying the sign after reversal also handles negative trailing zeroes.
        if negative:
            reversed_value = -reversed_value
        # LeetCode requires a signed 32-bit result despite Python's arbitrary precision.
        # The negative limit includes one more magnitude than the positive limit.
        if reversed_value < -(2**31) or reversed_value > 2**31 - 1:
            return 0
        # Leading zeroes disappear naturally during arithmetic digit extraction.
        # Input zero skips the loop and remains zero after the same range check.
        return reversed_value


if __name__ == "__main__":
    solution = Solution()
    assert solution.reverse(123) == 321
    assert solution.reverse(-123) == -321
    assert solution.reverse(120) == 21
    assert solution.reverse(1534236469) == 0
    assert solution.reverse(-2147483648) == 0
    assert solution.reverse(0) == 0
    print("All tests passed")
