"""
LeetCode 371: Sum of Two Integers
Difficulty: Medium
Pattern: Bit Manipulation
Video Reference: https://www.youtube.com/watch?v=gVUrDV4tZfY
Complexity:
    - Time: O(1)
    - Space: O(1)
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Python integers do not overflow, so mask to emulate 32-bit two's complement.
        mask = 0xFFFFFFFF
        sign = 0x80000000
        # Normalize operands first so carry propagation stays within the fixed word.
        a &= mask
        b &= mask
        # XOR is the partial sum; b stores carries still needing to be added.
        while b:
            carry = (
                (a & b) << 1
            ) & mask  # Shared 1 bits generate carries one position left.
            # The mask prevents sign extension from introducing bits beyond bit 31.
            a = (a ^ b) & mask  # XOR adds each bit without carrying.
            b = carry
        # With no carry left, a is the wrapped 32-bit sum.
        return (
            a if a < sign else ~(a ^ mask)
        )  # Convert the sign-bit form back to negative.


if __name__ == "__main__":
    solution = Solution()
    assert solution.getSum(1, 2) == 3
    assert solution.getSum(2, 3) == 5
    assert solution.getSum(-2, 3) == 1
    assert solution.getSum(-1, 1) == 0
    print("All tests passed")
