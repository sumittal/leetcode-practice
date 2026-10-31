from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Stack indices have increasing heights, delimiting unresolved rectangles.
        increasing = []
        largest = 0
        # A bar remains unresolved until a strictly shorter height closes its span.
        # An index stays until a bar shorter than it fixes its maximal right edge.
        # A zero-height sentinel flushes every real bar at the end.
        for index in range(len(heights) + 1):
            current_height = heights[index] if index < len(heights) else 0
            # A shorter bar fixes the right boundary for each taller stack entry.
            while increasing and heights[increasing[-1]] > current_height:
                # The current index is an exclusive right boundary for the popped bar.
                height = heights[increasing.pop()]
                # The new stack top is the nearest strictly lower bar on the left.
                left_boundary = increasing[-1] if increasing else -1
                width = index - left_boundary - 1
                largest = max(largest, height * width)
            # Pushing after all taller bars are finalized restores monotonic heights.
            # Equal-height bars may share the widest rectangle, so retain their indices.
            # Strict popping lets equal bars extend together when a later boundary appears.
            increasing.append(index)
        # Every bar was finalized at its first shorter right boundary or sentinel.
        # Each bar is pushed and popped at most once, giving linear total work.
        return largest


if __name__ == "__main__":
    solution = Solution()
    assert solution.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert solution.largestRectangleArea([2, 4]) == 4
    assert solution.largestRectangleArea([]) == 0
    assert solution.largestRectangleArea([2, 2, 2]) == 6
    assert solution.largestRectangleArea([1, 2, 3, 4]) == 6
    print("All tests passed")
