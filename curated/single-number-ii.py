from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # The input contract has one exceptional value and all others triplicated.
        result = 0
        # Exactly 32 positions cover the full LeetCode signed integer range.
        # Each bit from triplicated values contributes a multiple of three.
        for bit in range(32):
            # Arithmetic right shifts still expose each low-order two's-complement bit.
            count = sum((value >> bit) & 1 for value in nums)
            # Only the unique value's residue survives modulo three.
            if count % 3:
                result |= 1 << bit
            # Fixed-width masking gives Python's negative shifts the intended bits.
        # A set sign bit encodes a negative two's-complement 32-bit result.
        if result >= 1 << 31:
            result -= 1 << 32
        # Python integers are unbounded, so explicitly restore the signed range.
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.singleNumber([2, 2, 3, 2]) == 3
    assert solution.singleNumber([0, 1, 0, 1, 0, 1, 99]) == 99
    assert solution.singleNumber([-2, 1, 1, 1]) == -2
    assert solution.singleNumber([0]) == 0
    print("All tests passed")
