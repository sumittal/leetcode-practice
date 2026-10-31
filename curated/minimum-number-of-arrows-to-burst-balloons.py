from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Closed intervals can share an arrow exactly at an endpoint.
        if not points:
            return 0
        # End-ordering chooses the earliest finishing uncovered balloon first.
        # Earliest finishing intervals leave the most room for later balloons.
        ordered = sorted(points, key=lambda interval: interval[1])
        arrows = 1
        arrow_position = ordered[0][1]
        for start, end in ordered[1:]:
            # A start after the current shot proves this balloon is disjoint.
            # An arrow at the previous end also bursts intervals touching it.
            if start > arrow_position:
                arrows += 1
                arrow_position = end
            # Overlapping intervals share the current arrow position.
        # Sorting a copy leaves the caller's interval order unchanged.
        # Each disjoint interval forces one new shot at its end.
        return arrows


if __name__ == "__main__":
    solution = Solution()
    assert solution.findMinArrowShots(
        [[10, 16], [2, 8], [1, 6], [7, 12]]
    ) == 2
    assert solution.findMinArrowShots(
        [[1, 2], [3, 4], [5, 6], [7, 8]]
    ) == 4
    assert solution.findMinArrowShots(
        [[1, 2], [2, 3], [3, 4], [4, 5]]
    ) == 2
    assert solution.findMinArrowShots([]) == 0
    print("All tests passed")
