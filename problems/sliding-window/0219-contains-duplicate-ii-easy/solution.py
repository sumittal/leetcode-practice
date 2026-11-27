"""
LeetCode 219: Contains Duplicate II
Difficulty: Easy
Pattern: Sliding Window
Video Reference: https://www.youtube.com/watch?v=ypn0aZ0nrL4
Complexity:
    - Time: O(n)
    - Space: O(k)
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # The distance constraint cannot be satisfied for nonpositive k.
        if k <= 0:
            return False
        # The set contains only values at eligible preceding indices.
        window = set()
        for index, value in enumerate(nums):
            # Remove the item whose distance would now exceed k.
            if index > k:
                window.remove(nums[index - k - 1])
            # A present value has an earlier copy at distance at most k.
            if value in window:
                return True
            window.add(value)
            # Adding after the lookup avoids matching an index to itself.
            # The set contains values from indices no more than k behind.
        # The window never needs to hold more than k prior values.
        # Every input position is checked once against its eligible window.
        return False


if __name__ == "__main__":
    solution = Solution()
    assert solution.containsNearbyDuplicate([1, 2, 3, 1], 3) is True
    assert solution.containsNearbyDuplicate([1, 0, 1, 1], 1) is True
    assert solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) is False
    assert solution.containsNearbyDuplicate([1, 1], 0) is False
    print("All tests passed")
