from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Sorted order lets the endpoints bound every possible pair sum.
        left = 0
        right = len(numbers) - 1
        # The target pair, if not found, stays inside this shrinking interval.
        # Pointers never cross because every candidate pair uses distinct indices.
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                # Return one-based positions as required by the problem.
                return [left + 1, right + 1]
            if total < target:
                # Increasing the smaller value is the only move that can raise the sum.
                left += 1
            else:
                # Decreasing the larger value is the only move that can lower the sum.
                right -= 1
        # Strict inequality preserves two distinct one-based answer positions.
        # The problem guarantees one solution, so this is unreachable for valid input.
        return []


if __name__ == "__main__":
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert solution.twoSum([2, 3, 4], 6) == [1, 3]
    assert solution.twoSum([-1, 0], -1) == [1, 2]
    assert solution.twoSum([5, 25, 75], 100) == [2, 3]
    print("All tests passed")
