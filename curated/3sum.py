from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sorting enables monotonic two-pointer moves and adjacent duplicate checks.
        nums.sort()
        # Store each distinct value-triplet whose sum is zero.
        triplets = []
        # The last two positions must remain available for a pair.
        for first in range(len(nums) - 2):
            if nums[first] > 0:
                # All later values are at least as large, so no remaining sum can be zero.
                break
            # Repeated fixed values would produce the same family of triplets.
            if first and nums[first] == nums[first - 1]:
                continue

            # Search the remaining sorted suffix for a pair opposite nums[first].
            left = first + 1
            right = len(nums) - 1
            # Crossing pointers means every candidate pair for this first value is spent.
            while left < right:
                total = nums[first] + nums[left] + nums[right]
                if total < 0:
                    # The sum is too small; moving left rightward is the only way to raise it.
                    left += 1
                elif total > 0:
                    # The sum is too large; moving right leftward is the only way to lower it.
                    right -= 1
                else:
                    # This triple is unique at the current pointers and sums to zero.
                    triplets.append([nums[first], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip matching values so each distinct triplet is emitted once.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        # Each result is value-sorted, with duplicate triples skipped during the scan.
        return triplets


if __name__ == "__main__":
    solution = Solution()
    assert sorted(sorted(items) for items in solution.threeSum([-1, 0, 1, 2, -1, -4])) == [
        [-1, -1, 2],
        [-1, 0, 1],
    ]
    assert sorted(sorted(items) for items in solution.threeSum([0, 1, 1])) == []
    assert sorted(sorted(items) for items in solution.threeSum([0, 0, 0])) == [
        [0, 0, 0]
    ]
    assert solution.threeSum([]) == []
    assert sorted(
        sorted(items) for items in solution.threeSum([-2, 0, 1, 1, 2])
    ) == [[-2, 0, 2], [-2, 1, 1]]
    print("All tests passed")
