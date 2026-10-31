"""
LeetCode 45: Jump Game II
Difficulty: Medium
Pattern: Greedy
Video Reference: https://www.youtube.com/watch?v=dJ7sWiOoK7g
Complexity:
    - Time: O(n)
    - Space: O(1)
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            # Starting at the destination already requires no jumps.
            return 0
        # current_end is the farthest index covered by the current jump layer.
        # Greedy layers correspond to positions reachable with an exact jump count.
        jumps = 0
        current_end = 0
        farthest = 0
        # The final index needs no outgoing jump, so scan only earlier positions.
        for index in range(len(nums) - 1):
            # Every position in this range is reachable with the same jump count.
            farthest = max(farthest, index + nums[index])
            if index == current_end:
                # Reaching the layer boundary commits one jump to enter the next layer.
                jumps += 1
                current_end = farthest
                # The previous layer has now contributed every possible next endpoint.
            # The next layer's boundary is the best reach of all current-layer choices.
        # Reachability is guaranteed, so the committed layer count is minimal.
        # Updating only at boundaries avoids counting alternative paths separately.
        return jumps


if __name__ == "__main__":
    solution = Solution()
    assert solution.jump([2, 3, 1, 1, 4]) == 2
    assert solution.jump([2, 3, 0, 1, 4]) == 2
    assert solution.jump([1]) == 0
    assert solution.jump([1, 2]) == 1
    print("All tests passed")
