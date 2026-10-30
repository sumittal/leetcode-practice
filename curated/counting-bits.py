from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Index zero is the base case for every value in the range.
        counts = [0] * (n + 1)
        # Each state is final as soon as its smaller predecessor has been computed.
        # The recurrence removes the least significant set bit from each value.
        # Ascending order makes every smaller dependency available.
        for value in range(1, n + 1):
            # The loop starts at one because counts[0] was initialized as the base case.
            # The cleared-bit predecessor is nonnegative and less than value.
            # Removing one set bit reaches an already computed smaller value.
            counts[value] = counts[value & (value - 1)] + 1
        # The output array itself is the requested inclusive range.
        return counts


if __name__ == "__main__":
    solution = Solution()
    assert solution.countBits(2) == [0, 1, 1]
    assert solution.countBits(5) == [0, 1, 1, 2, 1, 2]
    assert solution.countBits(0) == [0]
    print("All tests passed")
