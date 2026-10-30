class Solution:
    def climbStairs(self, n: int) -> int:
        # n=1 is the recurrence base; n=2 is produced by its first transition.
        # One stair has one arrangement, which seeds the rolling recurrence.
        # The empty prefix contributes one starting arrangement before any step is taken.
        # ways counts arrangements through the previous step; prev2 is two steps back.
        prev2, ways = 1, 1
        # Iterating from step two avoids a separate branch for the recurrence base.
        for _ in range(2, n + 1):
            # Update both states together so the old ways remains available as prev2.
            prev2, ways = ways, prev2 + ways  # Final move is one step or two steps.
        # The rolling pair ends at the requested stair count.
        return ways


if __name__ == "__main__":
    solution = Solution()
    assert solution.climbStairs(2) == 2
    assert solution.climbStairs(3) == 3
    assert solution.climbStairs(1) == 1
    assert solution.climbStairs(5) == 8
    print("All tests passed")
