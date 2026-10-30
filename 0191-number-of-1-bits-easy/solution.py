"""
LeetCode 191: Number of 1 Bits
Difficulty: Easy
Pattern: Bit Manipulation
Video Reference: https://www.youtube.com/watch?v=5Km3utixwZs
Complexity:
    - Time: O(number of set bits)
    - Space: O(1)
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        # The loop terminates because each operation removes one set bit.
        count = 0
        # Zero bits never change the answer; each iteration removes one set bit.
        # Count increments once for each set bit removed from the current value.
        # The problem supplies a 32-bit unsigned representation, so rightward progress ends at zero.
        while n:
            # The lowest set bit is removed regardless of how many zero bits precede it.
            # n & (n-1) leaves all higher bits unchanged.
            n &= n - 1  # Clear exactly the lowest set bit each iteration.
            count += 1
        # Returning after the loop also handles n=0 without a special branch.
        return count


if __name__ == "__main__":
    solution = Solution()
    assert solution.hammingWeight(11) == 3
    assert solution.hammingWeight(128) == 1
    assert solution.hammingWeight(2147483645) == 30
    assert solution.hammingWeight(0) == 0
    print("All tests passed")
