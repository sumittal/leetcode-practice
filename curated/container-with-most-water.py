from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # left and right delimit the pair of walls for the current candidate container.
        left = 0
        right = len(height) - 1
        # Track the largest area among all pairs not yet ruled out.
        maximum = 0
        # At two remaining endpoints there is one valid container to evaluate.
        while left < right:
            # Width is fixed by the endpoints; the shorter wall sets the water level.
            width = right - left
            maximum = max(maximum, width * min(height[left], height[right]))
            # Drop a limiting wall; for equal heights, either endpoint is safe to discard.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        # Every pair has been considered or eliminated by the shorter-wall argument.
        return maximum


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert solution.maxArea([1, 1]) == 1
    assert solution.maxArea([1, 2]) == 1
    assert solution.maxArea([1, 2, 3]) == 2
    print("All tests passed")
