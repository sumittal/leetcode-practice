from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []

        def build(start: int) -> None:
            # Copy every prefix because later calls mutate the same working path.
            result.append(current[:])
            # A recursion level enumerates choices for the next included index.
            # Advancing start preserves input order and prevents reusing an index.
            for index in range(start, len(nums)):
                current.append(nums[index])
                # The recursive child can choose only later elements.
                build(index + 1)
                current.pop()  # Undo this choice before trying its sibling.
            # The loop's lower bound ensures combinations are built in one order only.
            # Returning with current restored leaves the caller's prefix intact.

        # Beginning with an empty path includes the empty subset.
        build(0)
        return result


if __name__ == "__main__":
    solution = Solution()
    assert sorted(map(tuple, solution.subsets([1, 2, 3]))) == sorted(
        [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    )
    assert sorted(map(tuple, solution.subsets([0]))) == [(), (0,)]
    assert solution.subsets([]) == [[]]
    print("All tests passed")
