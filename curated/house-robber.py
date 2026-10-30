from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Empty prefixes are worth zero, so the first house can be skipped safely.
        # The current house is compared against skipping it or pairing with two_back.
        # The rolling values represent optimum totals through i-2 and i-1.
        two_back = one_back = 0
        # A house can be taken only with the best total ending two positions earlier.
        for value in nums:
            # These two values summarize the only earlier subproblems this step needs.
            # Skip keeps one_back; take adds this value to the nonadjacent total.
            two_back, one_back = one_back, max(one_back, two_back + value)
        # The recurrence also handles an empty list because both initial states are zero.
        # one_back always represents the optimum for all houses seen so far.
        return one_back


if __name__ == "__main__":
    solution = Solution()
    assert solution.rob([1, 2, 3, 1]) == 4
    assert solution.rob([2, 7, 9, 3, 1]) == 12
    assert solution.rob([]) == 0
    assert solution.rob([5]) == 5
    print("All tests passed")
