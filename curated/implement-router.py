from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from typing import Deque, Dict, List, Set, Tuple


class Router:
    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.packets: Deque[Tuple[int, int, int]] = deque()
        self.active: Set[Tuple[int, int, int]] = set()
        self.times: Dict[int, List[int]] = defaultdict(list)
        self.heads: Dict[int, int] = defaultdict(int)

    def _remove_oldest(self) -> Tuple[int, int, int]:
        # Capacity eviction and explicit forwarding share the same cleanup path.
        packet = self.packets.popleft()
        self.active.remove(packet)
        _, destination, _ = packet
        # FIFO removal advances each destination's active timestamp prefix.
        self.heads[destination] += 1
        # Per-destination order follows global FIFO because arrivals are monotone.
        times = self.times[destination]
        head = self.heads[destination]
        # Periodically compact old timestamps so history space stays bounded.
        if head >= 64 and head * 2 >= len(times):
            self.times[destination] = times[head:]
            self.heads[destination] = 0
        return packet

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        # Duplicate rejection must not evict a packet from a full router.
        if packet in self.active:
            return False
        if len(self.packets) == self.limit:
            # The queue front is the oldest packet by insertion timestamp.
            self._remove_oldest()
        self.packets.append(packet)
        self.active.add(packet)
        self.times[destination].append(timestamp)
        # The history remains sorted under the API's nondecreasing-time promise.
        return True

    def forwardPacket(self) -> List[int]:
        if not self.packets:
            return []
        # Forwarding returns exactly the packet removed from the active indexes.
        return list(self._remove_oldest())

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        times = self.times.get(destination, [])
        head = self.heads.get(destination, 0)
        # head excludes packets already evicted or forwarded from the active range.
        # Timestamps arrive monotonically, so the active suffix is sorted.
        return bisect_right(times, endTime, lo=head) - bisect_left(
            times, startTime, lo=head
        )


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    router = None
    for op, values in zip(ops, args):
        if op == "Router":
            router = Router(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(router, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["Router", "addPacket", "addPacket", "addPacket", "addPacket",
         "addPacket", "forwardPacket", "addPacket", "getCount"],
        [[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95],
         [4, 5, 105], [], [5, 2, 110], [5, 100, 110]],
    ) == [None, True, True, False, True, True, [2, 5, 90], True, 1]
    assert replay(
        ["Router", "addPacket", "forwardPacket", "forwardPacket"],
        [[2], [7, 4, 90], [], []],
    ) == [None, True, [7, 4, 90], []]
    print("All tests passed")
