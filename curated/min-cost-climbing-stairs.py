from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] is the minimum paid cost to land on indexed stair i.
        # The first two stairs are both valid free starting positions.
        # Their base costs are paid only when a path chooses to land there.
        two_back = cost[0]
        one_back = cost[1]
        # Increasing indices ensure both predecessor states are already available.
        for index in range(2, len(cost)):
            # Land on this stair by paying its cost after either prior stair.
            current = cost[index] + min(two_back, one_back)
            # Roll the state window forward without storing the whole DP table.
            two_back, one_back = one_back, current
            # Keeping two predecessors is sufficient because every move spans at most two.
        # The top is one step beyond the last index and may be reached from either.
        return min(two_back, one_back)


if __name__ == "__main__":
    solution = Solution()
    assert solution.minCostClimbingStairs([10, 15, 20]) == 15
    assert solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    assert solution.minCostClimbingStairs([0, 0]) == 0
    assert solution.minCostClimbingStairs([1, 100, 1]) == 2
    print("All tests passed")
