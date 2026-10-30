from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # farthest is the inclusive right edge reachable using scanned positions.
        # Index zero is initially reachable without taking a jump.
        farthest = 0
        # The first position is reachable with zero jumps.
        # Scanning left-to-right only visits positions within the known reachable prefix.
        for index, jump in enumerate(nums):
            # If index lies beyond the boundary, no earlier jump can reach it.
            if index > farthest:
                return False
            # A jump extends the reachable prefix from this reachable position.
            farthest = max(farthest, index + jump)
            # Reaching the final index makes later scanning unnecessary.
            if farthest >= len(nums) - 1:
                return True
        # If the loop ends, its reachable prefix necessarily includes the last index.
        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.canJump([2, 3, 1, 1, 4]) is True
    assert solution.canJump([3, 2, 1, 0, 4]) is False
    assert solution.canJump([0]) is True
    assert solution.canJump([1, 0]) is True
    print("All tests passed")
