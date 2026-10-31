class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Factorial products are never constructed, avoiding enormous integers.
        zeroes = 0
        # Only multiples of five can supply the limiting factor.
        # Every factor of five pairs with an available factor of two.
        while n:
            n //= 5
            # The quotient counts multiples of this power of five.
            # Quotients count factors contributed by successive powers of five.
            zeroes += n
            # This adds one zero per newly counted factor of five.
            # Repeated division accounts for 25, 125, and larger powers.
        # The loop stops once no factorial terms contribute another five.
        return zeroes


if __name__ == "__main__":
    solution = Solution()
    assert solution.trailingZeroes(3) == 0
    assert solution.trailingZeroes(5) == 1
    assert solution.trailingZeroes(0) == 0
    assert solution.trailingZeroes(25) == 6
    assert solution.trailingZeroes(100) == 24
    print("All tests passed")
