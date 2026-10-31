"""
LeetCode 239: Sliding Window Maximum
Difficulty: Hard
Pattern: Sliding Window
Video Reference: https://www.youtube.com/watch?v=DfljaUwZsOk
Complexity:
    - Time: O(n)
    - Space: O(k)
"""

from collections import deque
from typing import Deque, List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Store indices so the deque can expire values when they leave the window.
        candidates: Deque[int] = deque()
        maxima = []
        # The deque front is always in the active window after expiration.
        for right, value in enumerate(nums):
            # The left boundary moves one step per new value after the first window.
            window_start = right - k + 1
            # Compare indices rather than values so duplicates expire at the right time.
            if candidates and candidates[0] < window_start:
                candidates.popleft()
            # A newer value at least as large permanently dominates smaller tail values.
            while candidates and nums[candidates[-1]] <= value:
                candidates.pop()
            # Remove all dominated tails before restoring the decreasing-value invariant.
            # Candidate indices stay increasing while their values stay decreasing.
            candidates.append(right)
            # Before the first full window, candidate maxima are not emitted.
            if right >= k - 1:
                # The front is the largest value among indices in the current window.
                # The threshold also ensures no partial-window result is emitted.
                maxima.append(nums[candidates[0]])
        # Each completed window contributes one maximum in left-to-right order.
        # Every index is appended once and removed at most once.
        return maxima


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxSlidingWindow(
        [1, 3, -1, -3, 5, 3, 6, 7], 3
    ) == [3, 3, 5, 5, 6, 7]
    assert solution.maxSlidingWindow([1], 1) == [1]
    assert solution.maxSlidingWindow([1, -1], 1) == [1, -1]
    assert solution.maxSlidingWindow([9, 11], 2) == [11]
    assert solution.maxSlidingWindow([4, 2, 12], 3) == [12]
    print("All tests passed")
