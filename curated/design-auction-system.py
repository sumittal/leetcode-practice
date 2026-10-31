import heapq
from collections import defaultdict
from typing import Dict, List, Tuple


class AuctionSystem:
    def __init__(self):
        # One current version per item/user pair is the source of truth.
        self.bids: Dict[Tuple[int, int], Tuple[int, int]] = {}
        self.heaps: Dict[int, List[Tuple[int, int, int]]] = defaultdict(list)
        self.version = 0

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self._set_bid(userId, itemId, bidAmount)

    def _set_bid(self, user: int, item: int, amount: int) -> None:
        self.version += 1
        # Increasing versions invalidate earlier bids even if amount repeats.
        self.bids[(item, user)] = (amount, self.version)
        # Negative keys make the max bid and greatest user ID the heap minimum.
        heapq.heappush(
            self.heaps[item], (-amount, -user, self.version)
        )

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        # Update uses the same path as replacing a bid on insertion.
        self._set_bid(userId, itemId, newAmount)

    def removeBid(self, userId: int, itemId: int) -> None:
        # Heap cleanup is deferred until the item is next queried.
        self.bids.pop((itemId, userId))

    def getHighestBidder(self, itemId: int) -> int:
        heap = self.heaps[itemId]
        # Version equality rejects stale bids even after an identical re-bid.
        while heap:
            # Heap order resolves amount ties toward the greatest user ID.
            amount, user, version = heap[0]
            if self.bids.get((itemId, -user)) == (-amount, version):
                return -user
            heapq.heappop(heap)
        return -1


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    auction = None
    for op, values in zip(ops, args):
        if op == "AuctionSystem":
            auction = AuctionSystem()
            outputs.append(None)
        else:
            result = getattr(auction, op)(*values)
            outputs.append(result)
    return outputs


if __name__ == "__main__":
    assert replay(
        ["AuctionSystem", "addBid", "addBid", "getHighestBidder",
         "updateBid", "getHighestBidder", "removeBid", "getHighestBidder",
         "getHighestBidder"],
        [[], [1, 7, 5], [2, 7, 6], [7], [1, 7, 8], [7], [2, 7], [7], [3]],
    ) == [None, None, None, 2, None, 1, None, 1, -1]
    # Equal bids choose the larger user ID even after prior heap entries stale.
    auction = AuctionSystem()
    auction.addBid(1, 4, 9)
    auction.addBid(2, 4, 9)
    assert auction.getHighestBidder(4) == 2
    print("All tests passed")
