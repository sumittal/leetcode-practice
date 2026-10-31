from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # At most two values fit automatically before the comparison window exists.
        write = 0
        for value in nums:
            # The kept prefix is always valid before this candidate is considered.
            # In sorted order, matching two slots back would create a third copy.
            if write >= 2 and value == nums[write - 2]:
                continue
            nums[write] = value
            # The prefix invariant allows at most two copies of every value.
            write += 1
            # Future checks compare against the second-most-recent kept slot.
        # The unexamined suffix is ignored by the problem's contract.
        # The write count is the compacted array length.
        # The single forward scan uses constant extra memory.
        return write


if __name__ == "__main__":
    solution = Solution()
    values = [1, 1, 1, 2, 2, 3]
    length = solution.removeDuplicates(values)
    assert length == 5 and values[:length] == [1, 1, 2, 2, 3]
    values = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    length = solution.removeDuplicates(values)
    assert length == 7 and values[:length] == [0, 0, 1, 1, 2, 3, 3]
    assert solution.removeDuplicates([1]) == 1
    print("All tests passed")
