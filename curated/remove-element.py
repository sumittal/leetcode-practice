from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # write always points to the first unused position in the kept prefix.
        write = 0
        for value in nums:
            # Reading proceeds left-to-right while writes never pass the read item.
            # Skipping val leaves the compact prefix unchanged.
            if value == val:
                continue
            nums[write] = value
            # Advancing after a copy preserves the relative order of survivors.
            write += 1
            # Thus each retained value appears once in its original order.
        # Values beyond write are irrelevant under the in-place contract.
        # The prefix length is the required return value.
        # The input array is compacted without allocating a second list.
        return write


if __name__ == "__main__":
    solution = Solution()
    values = [3, 2, 2, 3]
    length = solution.removeElement(values, 3)
    assert length == 2
    assert values[:length] == [2, 2]
    values = [0, 1, 2, 2, 3, 0, 4, 2]
    length = solution.removeElement(values, 2)
    assert length == 5
    assert sorted(values[:length]) == [0, 0, 1, 3, 4]
    values = [1, 1]
    length = solution.removeElement(values, 2)
    assert length == 2 and values[:length] == [1, 1]
    print("All tests passed")
