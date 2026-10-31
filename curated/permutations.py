from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        used = [False] * len(nums)

        def build() -> None:
            # A full-length path has selected each input position exactly once.
            if len(current) == len(nums):
                result.append(current[:])
                return
            for index, value in enumerate(nums):
                if used[index]:
                    # A position already on this path cannot be selected again.
                    continue
                # Mark and append together so path and used state stay synchronized.
                used[index] = True
                current.append(value)
                # The child fills the next slot while this index remains unavailable.
                build()
                current.pop()  # Undo the value before exploring a different position.
                used[index] = False  # Release the index for the caller's next branch.
            # Returning restores both the prefix and its available-index set.

        # An empty input reaches the base case and contributes one empty ordering.
        build()
        return result


if __name__ == "__main__":
    solution = Solution()
    assert sorted(map(tuple, solution.permute([1, 2, 3]))) == sorted(
        [
            (1, 2, 3),
            (1, 3, 2),
            (2, 1, 3),
            (2, 3, 1),
            (3, 1, 2),
            (3, 2, 1),
        ]
    )
    assert sorted(map(tuple, solution.permute([0, 1]))) == [(0, 1), (1, 0)]
    assert solution.permute([]) == [[]]
    assert solution.permute([7]) == [[7]]
    print("All tests passed")
