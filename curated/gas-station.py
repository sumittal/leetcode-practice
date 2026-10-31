from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_balance = 0
        segment_balance = 0
        start = 0
        # Net gas is the only quantity relevant to reaching the next station.
        for index, (available, price) in enumerate(zip(gas, cost)):
            balance = available - price
            total_balance += balance
            segment_balance += balance
            if segment_balance < 0:
                # No station in this failed segment can reach its endpoint as a start.
                start = index + 1
                segment_balance = 0
                # The new candidate begins strictly after the failed prefix.
            # Restarting after the deficit preserves a feasible candidate suffix.
        # A nonnegative total is necessary and sufficient for some circular start.
        # Total balance accounts for the wraparound fuel needed after the array end.
        if total_balance < 0:
            return -1
        # The surviving candidate is the unique valid start under the problem guarantee.
        # No simulation from each station is needed after this linear pass.
        return start


if __name__ == "__main__":
    solution = Solution()
    assert solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert solution.canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
    assert solution.canCompleteCircuit([5], [4]) == 0
    assert solution.canCompleteCircuit([2, 2], [2, 2]) == 0
    print("All tests passed")
