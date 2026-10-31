from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Map values already scanned to indices, so a match always uses two positions.
        indices = {}  # type: Dict[int, int]
        for index, value in enumerate(nums):
            # The complement is the only earlier value that can complete this pair.
            complement = target - value
            # Only earlier indices are stored, so this lookup cannot reuse this element.
            if complement in indices:
                # Return both indices as soon as the unique required pair is complete.
                return [indices[complement], index]
            # Store after lookup so equal values at different indices can form a pair.
            indices[value] = index
        # No pair was found; valid LeetCode inputs guarantee one exists.
        return []


if __name__ == "__main__":
    solution = Solution()
    assert sorted(solution.twoSum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(solution.twoSum([3, 2, 4], 6)) == [1, 2]
    assert sorted(solution.twoSum([3, 3], 6)) == [0, 1]
    assert solution.twoSum([], 0) == []
    print("All tests passed")
