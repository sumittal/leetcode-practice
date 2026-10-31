import heapq
from typing import Dict, List, Optional, Tuple, Union


class AuthenticationManager:
    # The map tracks live state; the heap only schedules possible expirations.
    def __init__(self, timeToLive: int):
        self.time_to_live = timeToLive
        # The map is authoritative when old heap events become stale.
        self.expirations: Dict[str, int] = {}
        self.events: List[Tuple[int, str]] = []

    def _expire(self, currentTime: int) -> None:
        # Expiration is exclusive at its timestamp: expiry <= now is invalid.
        while self.events and self.events[0][0] <= currentTime:
            expiry, token = heapq.heappop(self.events)
            # Ignore an old heap event when the token was renewed later.
            if self.expirations.get(token) == expiry:
                del self.expirations[token]

    def generate(self, tokenId: str, currentTime: int) -> None:
        expiry = currentTime + self.time_to_live
        self.expirations[tokenId] = expiry
        # Heap entries make the next expiration available without scanning tokens.
        heapq.heappush(self.events, (expiry, tokenId))
        # Heap insertion costs logarithmic time and keeps expiry events ordered.

    def renew(self, tokenId: str, currentTime: int) -> None:
        self._expire(currentTime)
        if tokenId not in self.expirations:
            return
        expiry = currentTime + self.time_to_live
        self.expirations[tokenId] = expiry
        heapq.heappush(self.events, (expiry, tokenId))
        # The previous expiry event is safely ignored when it later surfaces.

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self._expire(currentTime)
        # Expiration cleanup leaves the map containing only currently valid tokens.
        return len(self.expirations)


def replay(
    ops: List[str], args: List[list]
) -> List[Optional[Union[int, str]]]:
    outputs: List[Optional[Union[int, str]]] = []
    manager = None
    for operation, values in zip(ops, args):
        if operation == "AuthenticationManager":
            manager = AuthenticationManager(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(manager, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["AuthenticationManager", "renew", "generate",
         "countUnexpiredTokens", "generate", "renew", "renew",
         "countUnexpiredTokens"],
        [[5], ["aaa", 1], ["aaa", 2], [6], ["bbb", 7], ["aaa", 8],
         ["bbb", 10], [15]],
    ) == [None, None, None, 1, None, None, None, 0]
    assert replay(
        ["AuthenticationManager", "generate", "countUnexpiredTokens",
         "renew", "countUnexpiredTokens"],
        [[4], ["x", 3], [7], ["x", 7], [8]],
    ) == [None, None, 0, None, 0]
    print("All tests passed")
