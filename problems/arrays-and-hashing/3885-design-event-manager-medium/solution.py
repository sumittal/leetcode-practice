"""
LeetCode 3885: Design Event Manager
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+3885+Design+Event+Manager+neetcode
Complexity:
    - Time: updatePriority O(log n), pollHighest O(log n) amortized
    - Space: O(n + updates)
"""

import heapq
from typing import Dict, List, Optional, Tuple


class EventManager:
    def __init__(self, events: List[List[int]]):
        # Heap records carry a version so updates never require an in-place search.
        self.active: Dict[int, Tuple[int, int]] = {}
        self.heap: List[Tuple[int, int, int]] = []
        # A global counter gives every heap snapshot a unique generation.
        self.version = 0
        for event_id, priority in events:
            self.active[event_id] = (priority, self.version)
            heapq.heappush(self.heap, (-priority, event_id, self.version))
            self.version += 1

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        # A higher priority is represented by a smaller negated heap key.
        self.version += 1
        self.active[eventId] = (newPriority, self.version)
        # Push a new record rather than searching inside the heap.
        heapq.heappush(self.heap, (-newPriority, eventId, self.version))
        # Previous records remain harmless until lazily popped.

    def pollHighest(self) -> int:
        # Event ID is the tie-breaker after equal priority in the heap tuple.
        while self.heap:
            negative_priority, event_id, version = heapq.heappop(self.heap)
            current = self.active.get(event_id)
            if current == (-negative_priority, version):
                # Removing the active map entry makes all old heap records stale.
                del self.active[event_id]
                return event_id
            # A removed event or superseded priority makes this record stale.
        return -1


def replay(
    ops: List[str], args: List[List[object]]
) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    manager = None
    for operation, values in zip(ops, args):
        if operation == "EventManager":
            manager = EventManager(*values)
            outputs.append(None)
        else:
            result = getattr(manager, operation)(*values)
            outputs.append(result)
    return outputs


if __name__ == "__main__":
    assert replay(
        ["EventManager", "pollHighest", "updatePriority", "pollHighest",
         "pollHighest"],
        [[[[5, 7], [2, 7], [9, 4]]], [], [9, 7], [], []],
    ) == [None, 2, None, 5, 9]
    assert replay(
        ["EventManager", "pollHighest", "pollHighest", "pollHighest"],
        [[[[4, 1], [7, 2]]], [], [], []],
    ) == [None, 7, 4, -1]
    print("All tests passed")
