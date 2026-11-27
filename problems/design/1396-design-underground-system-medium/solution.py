"""
LeetCode 1396: Design Underground System
Difficulty: Medium
Pattern: Arrays & Hashing
Video Reference: https://www.youtube.com/watch?v=W5QOLqXskZM
Complexity:
    - Time: checkIn O(1), checkOut O(1), getAverageTime O(1)
    - Space: O(active riders + distinct routes)
"""

from typing import Dict, List, Optional, Tuple, Union


class UndergroundSystem:
    # Completed journeys collapse to route totals and counts.
    # Check-in records remain separate until their matching checkout.
    # Both maps support constant-time average operations.
    def __init__(self):
        # Active journeys are keyed by rider; completed trips are grouped by route.
        self.check_ins: Dict[int, Tuple[str, int]] = {}
        self.routes: Dict[Tuple[str, str], Tuple[int, int]] = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # A rider has one active check-in record before completing a trip.
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_ins.pop(id)
        route = (start_station, stationName)
        # Removing the rider prevents a finished check-in from being reused.
        total, count = self.routes.get(route, (0, 0))
        # Aggregates retain exactly the information needed for a mean.
        self.routes[route] = (total + t - start_time, count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # Each route's sum and count are sufficient statistics for its mean.
        total, count = self.routes[(startStation, endStation)]
        return total / count


def replay(
    ops: List[str], args: List[list]
) -> List[Optional[Union[int, float]]]:
    outputs: List[Optional[Union[int, float]]] = []
    system = None
    for operation, values in zip(ops, args):
        if operation == "UndergroundSystem":
            system = UndergroundSystem()
            outputs.append(None)
        else:
            outputs.append(getattr(system, operation)(*values))
    return outputs


if __name__ == "__main__":
    first = replay(
        ["UndergroundSystem", "checkIn", "checkIn", "checkIn", "checkOut",
         "checkOut", "checkOut", "getAverageTime", "getAverageTime",
         "checkIn", "getAverageTime", "checkOut", "getAverageTime"],
        [[], [45, "Leyton", 3], [32, "Paradise", 8], [27, "Leyton", 10],
         [45, "Waterloo", 15], [27, "Waterloo", 20],
         [32, "Cambridge", 22], ["Paradise", "Cambridge"],
         ["Leyton", "Waterloo"], [10, "Leyton", 24],
         ["Leyton", "Waterloo"], [10, "Waterloo", 38],
         ["Leyton", "Waterloo"]],
    )
    assert first[:7] == [None, None, None, None, None, None, None]
    assert first[7:] == [14.0, 11.0, None, 11.0, None, 12.0]
    second = replay(
        ["UndergroundSystem", "checkIn", "checkOut", "getAverageTime",
         "checkIn", "checkOut", "getAverageTime", "checkIn", "checkOut",
         "getAverageTime"],
        [[], [10, "Leyton", 3], [10, "Paradise", 8],
         ["Leyton", "Paradise"], [5, "Leyton", 10], [5, "Paradise", 16],
         ["Leyton", "Paradise"], [2, "Leyton", 21], [2, "Paradise", 30],
         ["Leyton", "Paradise"]],
    )
    assert second[:3] == [None, None, None]
    assert all(abs(a - b) < 1e-9 for a, b in zip(second[3::3], [5.0, 5.5, 20.0 / 3]))
    print("All tests passed")
