"""
LeetCode 1500: Design a File Sharing System
Difficulty: Medium
Pattern: Hash Table
Video Reference: https://www.youtube.com/results?search_query=leetcode+1500+Design+a+File+Sharing+System+neetcode
Complexity:
    - Time: join O(chunks + log users), leave O(chunks + log users), request O(owners log owners)
    - Space: O(total ownership pairs + users)
"""

import heapq
from collections import defaultdict
from typing import Dict, List, Set


class FileSharing:
    # Ownership indexes stay synchronized as users join, leave, and request chunks.
    def __init__(self, m: int):
        # Chunk ownership is indexed in both directions for leave and request.
        self.chunk_count = m
        self.next_user = 1
        self.reusable: List[int] = []
        self.users: Dict[int, Set[int]] = {}
        self.owners: Dict[int, Set[int]] = defaultdict(set)

    def join(self, ownedChunks: List[int]) -> int:
        # Reuse the smallest released identifier before allocating a fresh one.
        user = heapq.heappop(self.reusable) if self.reusable else self.next_user
        if user == self.next_user:
            self.next_user += 1
        chunks = set(ownedChunks)
        # Duplicate chunks in one join do not create duplicate owner records.
        self.users[user] = chunks
        # The reverse index supports efficient provider queries and departure.
        for chunk in chunks:
            self.owners[chunk].add(user)
        return user

    def leave(self, userID: int) -> None:
        chunks = self.users.pop(userID)
        # Remove this user from each reverse owner set before recycling its ID.
        for chunk in chunks:
            self.owners[chunk].remove(userID)
        heapq.heappush(self.reusable, userID)

    def request(self, userID: int, chunkID: int) -> List[int]:
        # Return the provider snapshot before granting a copy to the requester.
        providers = sorted(self.owners[chunkID])
        # Sorting is required because owner sets themselves have no order.
        if providers and chunkID not in self.users[userID]:
            self.users[userID].add(chunkID)
            self.owners[chunkID].add(userID)
        return providers


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    sharing = None
    for op, values in zip(ops, args):
        if op == "FileSharing":
            sharing = FileSharing(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(sharing, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["FileSharing", "join", "join", "request", "leave", "request"],
        [[4], [[1, 2]], [[2, 3]], [1, 2], [1], [2, 1]],
    ) == [None, 1, 2, [1, 2], None, []]
    assert replay(
        ["FileSharing", "join", "leave", "join"],
        [[3], [[1]], [1], [[2]]],
    ) == [None, 1, None, 1]
    print("All tests passed")
