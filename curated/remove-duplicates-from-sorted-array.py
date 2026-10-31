from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # The first occurrence is already the first distinct value.
        write = 1
        for read in range(1, len(nums)):
            # The read position never falls behind the compacted write prefix.
            # Sorted order makes equality with the last kept value sufficient.
            if nums[read] == nums[write - 1]:
                continue
            # Copying a new value extends the unique prefix by one.
            nums[write] = nums[read]
            write += 1
            # A newly copied value becomes the comparison boundary for the next run.
        # The suffix after write may contain stale duplicates.
        # Return only the compacted prefix length.
        # The scan and writes require constant extra storage.
        return write


if __name__ == "__main__":
    solution = Solution()
    values = [1, 1, 2]
    length = solution.removeDuplicates(values)
    assert length == 2 and values[:length] == [1, 2]
    values = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    length = solution.removeDuplicates(values)
    assert length == 5 and values[:length] == [0, 1, 2, 3, 4]
    assert solution.removeDuplicates([]) == 0
    print("All tests passed")
