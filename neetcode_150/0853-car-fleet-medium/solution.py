"""
LeetCode 853: Car Fleet
Difficulty: Medium
Pattern: Stack
Video Reference: https://www.youtube.com/watch?v=Pr6T-3yB9RM
Complexity:
    - Time: O(n log n)
    - Space: O(n)
"""

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Cars must be considered from the one nearest the target backward.
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        slowest_arrival = 0.0
        # The recorded time belongs to the nearest fleet that can block cars behind.
        # That arrival time is a lower bound for any car that catches this fleet.
        for car_position, car_speed in cars:
            # Each car's solo arrival time determines whether it catches a fleet.
            arrival = (target - car_position) / car_speed
            if arrival > slowest_arrival:
                # A slower arrival cannot catch the fleet ahead and starts a new one.
                fleets += 1
                slowest_arrival = arrival
            # Equal arrival times merge too, since cars reach the target together.
            # An earlier/equal arrival joins the fleet whose time is already recorded.
        # Every uncaught car contributes exactly one fleet.
        # Sorting costs O(n log n); the subsequent scan is linear.
        return fleets


if __name__ == "__main__":
    solution = Solution()
    assert solution.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert solution.carFleet(10, [3], [3]) == 1
    assert solution.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
    assert solution.carFleet(10, [0, 4], [2, 1]) == 1
    assert solution.carFleet(10, [], []) == 0
    print("All tests passed")
