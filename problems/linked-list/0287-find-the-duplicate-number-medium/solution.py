"""
LeetCode 287: Find the Duplicate Number
Difficulty: Medium
Pattern: Linked List
Video Reference: https://www.youtube.com/watch?v=wjYnzkAhcNk
Complexity:
    - Time: O(n)
    - Space: O(1)
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Treat nums[value] as a next pointer in a functional graph.
        slow = nums[0]
        fast = nums[0]
        # The duplicate creates the cycle because its index has multiple incoming edges.
        while True:
            # Fast advances twice as quickly and must meet slow inside the cycle.
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # Reset one pointer to the start; equal-speed walks now meet at cycle entry.
        slow = nums[0]
        while slow != fast:
            # The shared prefix distance equals the distance from meeting point to entry.
            slow = nums[slow]
            fast = nums[fast]
        # All reads are through values-as-indices, so nums is never modified.
        # The cycle entrance is the duplicate value, even if it occurs many times.
        return slow


if __name__ == "__main__":
    solution = Solution()
    examples = [[1, 3, 4, 2, 2], [3, 1, 3, 4, 2], [1, 1], [2, 2, 2, 2, 2]]
    expected = [2, 3, 1, 2]
    for numbers, duplicate in zip(examples, expected):
        original = numbers[:]
        assert solution.findDuplicate(numbers) == duplicate
        # Floyd's pointer updates must leave the input array unchanged.
        assert numbers == original
    print("All tests passed")
