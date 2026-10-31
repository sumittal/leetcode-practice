import heapq
from typing import List, Optional, Tuple


class WorstLocation:
    def __init__(self, score: int, name: str):
        self.score = score
        self.name = name

    @property
    def key(self) -> Tuple[int, str]:
        # Smaller score ranks later; lexicographically larger names lose ties.
        return (-self.score, self.name)

    def __lt__(self, other: "WorstLocation") -> bool:
        # The queried heap exposes the least desirable of its top-ranked items.
        # Reverse comparison makes Python's min-heap act as the needed max-heap.
        return self.key > other.key


class SORTracker:
    def __init__(self):
        # Remaining items are a min-heap in the problem's ranking order.
        self.remaining: List[Tuple[int, str]] = []
        # The opposite ordering exposes the worst item among already queried ranks.
        self.queried: List[WorstLocation] = []

    def add(self, name: str, score: int) -> None:
        # Negated scores put the best unqueried location at heap index zero.
        key = (-score, name)
        heapq.heappush(self.remaining, key)
        # A newly added location may displace the current boundary item.
        if self.queried and self.remaining[0] < self.queried[0].key:
            displaced = heapq.heappop(self.queried)
            promoted = heapq.heappop(self.remaining)
            heapq.heappush(
                self.queried, WorstLocation(-promoted[0], promoted[1])
            )
            heapq.heappush(self.remaining, displaced.key)

    def get(self) -> str:
        # Each query extends the prefix of ranks already returned by one.
        # The boundary invariant leaves the next answer at the remaining heap top.
        best = heapq.heappop(self.remaining)
        heapq.heappush(self.queried, WorstLocation(-best[0], best[1]))
        return best[1]


def replay(ops: List[str], args: List[List[object]]) -> List[Optional[str]]:
    outputs: List[Optional[str]] = []
    tracker = None
    for operation, values in zip(ops, args):
        if operation == "SORTracker":
            tracker = SORTracker()
            outputs.append(None)
        else:
            result = getattr(tracker, operation)(*values)
            outputs.append(result)
    return outputs


if __name__ == "__main__":
    assert replay(
        ["SORTracker", "add", "add", "get", "add", "get", "add", "get",
         "add", "get", "add", "get", "get"],
        [[], ["bradford", 2], ["branford", 3], [], ["alps", 2], [],
         ["orland", 2], [], ["orlando", 3], [], ["alpine", 2], [], []],
    ) == [
        None, None, None, "branford", None, "alps", None, "bradford",
        None, "bradford", None, "bradford", "orland",
    ]
    assert replay(
        ["SORTracker", "add", "get", "add", "get"],
        [[], ["zoo", 5], [], ["apple", 6], []],
    ) == [None, None, "zoo", None, "zoo"]
    print("All tests passed")
