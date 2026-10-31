from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR is associative and commutative, so input order does not matter.
        # Zero is the identity value before any elements have been processed.
        unique = 0
        # The accumulator is the XOR of exactly the values visited so far.
        for value in nums:
            # A duplicate pair cancels because x XOR x equals zero.
            unique ^= value
            # XOR with zero preserves the unmatched value accumulated so far.
            # The input guarantee leaves exactly one unpaired occurrence at the end.
        # Every repeated value cancels, leaving the single occurrence.
        # One accumulator gives constant auxiliary space without sorting.
        return unique


if __name__ == "__main__":
    solution = Solution()
    assert solution.singleNumber([2, 2, 1]) == 1
    assert solution.singleNumber([4, 1, 2, 1, 2]) == 4
    assert solution.singleNumber([1]) == 1
    assert solution.singleNumber([-1, 2, 2]) == -1
    print("All tests passed")
