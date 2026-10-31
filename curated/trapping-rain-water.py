from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # The shorter outer wall determines which side's water is already known.
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        water = 0
        # Narrowing the interval avoids storing left and right maxima per index.
        # Each maximum is the tallest boundary already processed on its side.
        while left < right:
            if height[left] <= height[right]:
                # The right wall is at least as tall, so left_max bounds this column.
                # A valid right boundary is already known for every column left of it.
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                # No unseen height to the right can reduce the established right bound.
                left += 1
            else:
                # Symmetrically, the known left wall makes right_max the limiting bound.
                # Any possible left boundary is at least as tall as this right column.
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                # Consume this right column after its trapped depth is accounted for.
                right -= 1
        # The two outer bars cannot trap water without an interior column.
        # Water is accumulated only after both a limiting wall and column height are known.
        # Every interior index was processed exactly once by one of the two sides.
        return water


if __name__ == "__main__":
    solution = Solution()
    assert solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert solution.trap([4, 2, 0, 3, 2, 5]) == 9
    assert solution.trap([]) == 0
    assert solution.trap([2, 0, 2]) == 2
    assert solution.trap([1, 2, 3]) == 0
    print("All tests passed")
