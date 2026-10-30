from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Empty or single-meeting schedules pass because no overlapping pair exists.
        # Sorting turns all-pairs overlap checks into adjacent comparisons.
        intervals.sort(key=lambda item: item[0])
        # No non-adjacent pair can overlap without an adjacent sorted pair overlapping.
        # Only the immediately previous meeting can overlap the current sorted one.
        # The loop excludes index zero because it has no predecessor to compare.
        for i in range(1, len(intervals)):
            # Start at one because only a previous sorted interval can conflict.
            # Equal boundary times do not overlap because the earlier meeting ends first.
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        # Passing every adjacent comparison means the entire schedule is compatible.
        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.canAttendMeetings([[0, 30], [5, 10], [15, 20]]) is False
    assert solution.canAttendMeetings([[7, 10], [2, 4]]) is True
    assert solution.canAttendMeetings([]) is True
    assert solution.canAttendMeetings([[1, 2], [2, 3]]) is True
    print("All tests passed")
