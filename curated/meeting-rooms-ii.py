import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # An empty calendar requires no allocated room.
        if not intervals:
            return 0
        # Sorting ensures every meeting is considered in chronological start order.
        intervals.sort(key=lambda item: item[0])
        # Each heap entry is the end time of one meeting currently using a room.
        endings = []
        for start, end in intervals:
            # The earliest end is the only active meeting that can free first.
            # Release every room whose meeting ends by this start time.
            while endings and endings[0] <= start:
                heapq.heappop(endings)
            # One heap entry represents each meeting still occupying a room.
            heapq.heappush(endings, end)
            # The heap size after allocation reflects currently overlapping meetings.
        # Heap size is the maximum simultaneous active-room requirement reached.
        return len(endings)


if __name__ == "__main__":
    solution = Solution()
    assert solution.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert solution.minMeetingRooms([[7, 10], [2, 4]]) == 1
    assert solution.minMeetingRooms([]) == 0
    assert solution.minMeetingRooms([[1, 2], [2, 3]]) == 1
    print("All tests passed")
