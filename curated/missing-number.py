from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # The input length n implies the complete domain is [0, n].
        n = len(nums)
        # The expected sum differs from the observed sum by exactly one missing value.
        # Exactly one element is absent from the n+1-value inclusive domain.
        # The closed-form total avoids allocating or sorting a second collection.
        # Because all other values occur once, their sum cancels from the difference.
        # The complete range sum minus present values leaves the sole missing value.
        # The formula naturally returns zero when the input is empty.
        return n * (n + 1) // 2 - sum(nums)  # Each present value is subtracted once.


if __name__ == "__main__":
    solution = Solution()
    assert solution.missingNumber([3, 0, 1]) == 2
    assert solution.missingNumber([0, 1]) == 2
    assert solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert solution.missingNumber([]) == 0
    print("All tests passed")
