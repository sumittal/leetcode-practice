class Solution:
    def reverseBits(self, n: int) -> int:
        # A fixed 32 iterations also preserves leading zeroes in the input bit pattern.
        result = 0
        # Leading input zeros are shifted through too, preserving the 32-bit width.
        # Each iteration consumes one source bit and appends it to the output.
        # The result grows by one bit per iteration, ending as the reversed 32-bit value.
        for _ in range(32):
            # A 32-step bound prevents unbounded shifts and fixes the result width.
            result = (result << 1) | (
                n & 1
            )  # Append the current least-significant bit.
            # The loop shifts bits out after they have been copied to the result.
            n >>= 1  # Move the next source bit into the low position.
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.reverseBits(43261596) == 964176192
    assert solution.reverseBits(4294967293) == 3221225471
    assert solution.reverseBits(2147483644) == 1073741822
    assert solution.reverseBits(0) == 0
    assert solution.reverseBits(1) == 2147483648
    print("All tests passed")
