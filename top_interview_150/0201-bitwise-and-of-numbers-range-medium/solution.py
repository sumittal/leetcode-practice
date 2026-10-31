"""
LeetCode 201: Bitwise AND of Numbers Range
Difficulty: Medium
Pattern: Bit Manipulation
Video Reference: https://www.youtube.com/results?search_query=leetcode+201+Bitwise+AND+of+Numbers+Range+neetcode
Complexity:
    - Time: O(log right)
    - Space: O(1)
"""

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Equal endpoints already share the full prefix and require no shifts.
        shifts = 0
        # The common prefix is the only part shared by every value in the range.
        # Differing low bits must become zero somewhere in the inclusive range.
        while left < right:
            left >>= 1
            right >>= 1
            # Shifting removes one suffix bit that differs somewhere in the range.
            shifts += 1
            # Each shift shortens the prefix search by one bit.
            # Shift both endpoints until only their common prefix remains.
        # Restoring the prefix appends the common zero suffix.
        # The shifted endpoints are equal when their prefix is fully common.
        return left << shifts


if __name__ == "__main__":
    solution = Solution()
    assert solution.rangeBitwiseAnd(5, 7) == 4
    assert solution.rangeBitwiseAnd(0, 0) == 0
    assert solution.rangeBitwiseAnd(1, 2147483647) == 0
    assert solution.rangeBitwiseAnd(12, 12) == 12
    print("All tests passed")
