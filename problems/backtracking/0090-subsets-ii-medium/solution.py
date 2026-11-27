"""
LeetCode 90: Subsets II
Difficulty: Medium
Pattern: Backtracking
Video Reference: https://www.youtube.com/watch?v=Vn2v6ajA7U0
Complexity:
    - Time: O(n 2^n)
    - Space: O(n) besides output
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        current = []

        def build(start: int) -> None:
            # Each current prefix is one distinct subset to include in the output.
            result.append(current[:])
            # Candidates before start are already fixed in this path.
            for index in range(start, len(nums)):
                # Equal siblings would create the same subset at this depth.
                if index > start and nums[index] == nums[index - 1]:
                    continue
                current.append(nums[index])
                # Descending one level allows later copies but never earlier positions.
                build(index + 1)
                current.pop()  # Undo this choice before considering the next sibling.
            # The recursion returns with exactly the prefix it received.
            # The caller's prefix is restored after all extensions are explored.

        # Sorting makes equal values adjacent so duplicate sibling branches are visible.
        build(0)
        return result


if __name__ == "__main__":
    solution = Solution()
    assert sorted(map(tuple, solution.subsetsWithDup([1, 2, 2]))) == [
        (),
        (1,),
        (1, 2),
        (1, 2, 2),
        (2,),
        (2, 2),
    ]
    assert sorted(map(tuple, solution.subsetsWithDup([0]))) == [(), (0,)]
    assert sorted(map(tuple, solution.subsetsWithDup([2, 2]))) == [
        (),
        (2,),
        (2, 2),
    ]
    assert solution.subsetsWithDup([]) == [[]]
    print("All tests passed")
