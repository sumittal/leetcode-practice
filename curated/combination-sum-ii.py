from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        current = []

        def build(start: int, remaining: int) -> None:
            # Only a zero remainder is a complete combination.
            if remaining == 0:
                result.append(current[:])
                return
            # Each branch uses a later candidate occurrence to avoid permutation duplicates.
            for index in range(start, len(candidates)):
                value = candidates[index]
                # Skip duplicate siblings so each value sequence is emitted once.
                if index > start and value == candidates[index - 1]:
                    continue
                # Sorted order means this and every later candidate exceed the remainder.
                if value > remaining:
                    break
                current.append(value)
                # Advancing the index enforces that each candidate occurrence is used once.
                build(index + 1, remaining - value)
                current.pop()  # Undo the chosen occurrence before trying a sibling.
            # Nonzero remainders return without adding incomplete paths.

        # Sorting supports duplicate skipping and the early over-target cutoff.
        build(0, target)
        return result


if __name__ == "__main__":
    solution = Solution()
    assert sorted(map(tuple, solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))) == [
        (1, 1, 6),
        (1, 2, 5),
        (1, 7),
        (2, 6),
    ]
    assert sorted(map(tuple, solution.combinationSum2([2, 5, 2, 1, 2], 5))) == [
        (1, 2, 2),
        (5,),
    ]
    assert solution.combinationSum2([2], 1) == []
    assert solution.combinationSum2([1], 1) == [[1]]
    print("All tests passed")
