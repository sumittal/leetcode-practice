"""
LeetCode 66: Plus One
Difficulty: Easy
Pattern: Math & Geometry
Video Reference: https://www.youtube.com/watch?v=jIaA8boiG1s
Complexity:
    - Time: O(n)
    - Space: O(1) extra apart from output
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Carry can propagate only through the trailing run of nines.
        # At each iteration, all positions to the right have already rolled over.
        # The increment begins at the units place and resolves at the first non-nine.
        for index in range(len(digits) - 1, -1, -1):
            if digits[index] < 9:
                # The first non-nine absorbs the carry and ends propagation.
                digits[index] += 1
                # More significant digits remain unchanged after the carry is resolved.
                return digits
            # A nine rolls over to zero before carrying into the preceding digit.
            digits[index] = 0
        # Carry past the first position grows an all-nine number by one digit.
        # The original digits are already zeroed by the reverse scan.
        return [1] + digits


if __name__ == "__main__":
    solution = Solution()
    assert solution.plusOne([1, 2, 3]) == [1, 2, 4]
    assert solution.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert solution.plusOne([9]) == [1, 0]
    assert solution.plusOne([0]) == [1]
    print("All tests passed")
