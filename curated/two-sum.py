from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # type: Dict[int, int]
        for index, value in enumerate(nums):
            complement = target - value
            # Only earlier indices are stored, so this lookup cannot reuse this element.
            if complement in indices:
                return [indices[complement], index]
            # Store after lookup so equal values at different indices can form a pair.
            indices[value] = index
        return []


if __name__ == "__main__":
    solution = Solution()
    assert sorted(solution.twoSum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(solution.twoSum([3, 2, 4], 6)) == [1, 2]
    assert sorted(solution.twoSum([3, 3], 6)) == [0, 1]
    assert solution.twoSum([], 0) == []
    print("All tests passed")
