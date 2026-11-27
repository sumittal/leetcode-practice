"""
LeetCode 1912: Design Movie Rental System
Difficulty: Hard
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+1912+Design+Movie+Rental+System+neetcode
Complexity:
    - Time: rent/drop O(log n), search/report O(k log n) amortized for k returned items
    - Space: O(n + updates)
"""

import heapq
from collections import defaultdict
from typing import Dict, List, Set, Tuple


class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        # The price map supports direct validation of every lazy heap candidate.
        self.price: Dict[Tuple[int, int], int] = {}
        self.available: Dict[int, List[Tuple[int, int, int]]] = defaultdict(list)
        self.rented: List[Tuple[int, int, int, int]] = []
        self.is_rented: Set[Tuple[int, int]] = set()
        self.version: Dict[Tuple[int, int], int] = defaultdict(int)
        for shop, movie, price in entries:
            self.price[(shop, movie)] = price
            heapq.heappush(self.available[movie], (price, shop, 0))

    def search(self, movie: int) -> List[int]:
        heap = self.available[movie]
        chosen: List[Tuple[int, int, int]] = []
        # Temporarily removing the top five avoids copying an entire heap.
        result: List[int] = []
        while heap and len(result) < 5:
            entry = heapq.heappop(heap)
            price, shop, version = entry
            if (
                (shop, movie) not in self.is_rented
                and self.version[(shop, movie)] == version
            ):
                # Heap tuple order gives price first and shop ID as the tie break.
                chosen.append(entry)
                result.append(shop)
        # Restore valid entries so search remains a read-only operation.
        for entry in chosen:
            heapq.heappush(heap, entry)
        return result

    def rent(self, shop: int, movie: int) -> None:
        self.is_rented.add((shop, movie))
        self.version[(shop, movie)] += 1
        # A generation number distinguishes a re-rent from its older heap record.
        price = self.price[(shop, movie)]
        heapq.heappush(
            self.rented,
            (price, shop, movie, self.version[(shop, movie)]),
        )

    def drop(self, shop: int, movie: int) -> None:
        self.is_rented.remove((shop, movie))
        self.version[(shop, movie)] += 1
        # The new available version supersedes all earlier availability entries.
        heapq.heappush(
            self.available[movie],
            (self.price[(shop, movie)], shop, self.version[(shop, movie)]),
        )

    def report(self) -> List[List[int]]:
        chosen: List[Tuple[int, int, int, int]] = []
        result: List[List[int]] = []
        while self.rented and len(result) < 5:
            entry = heapq.heappop(self.rented)
            price, shop, movie, version = entry
            # Only the latest rent action can represent a currently rented copy.
            if (
                (shop, movie) in self.is_rented
                and self.version[(shop, movie)] == version
                and self.price[(shop, movie)] == price
            ):
                # Valid entries are restored below so reports do not consume state.
                chosen.append(entry)
                result.append([shop, movie])
        for entry in chosen:
            heapq.heappush(self.rented, entry)
        return result


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    system = None
    for op, values in zip(ops, args):
        if op == "MovieRentingSystem":
            system = MovieRentingSystem(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(system, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["MovieRentingSystem", "search", "rent", "rent", "report", "drop",
         "search"],
        [[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7],
              [2, 1, 5]]], [1], [0, 1], [1, 2], [], [1, 2], [2]],
    ) == [None, [1, 0, 2], None, None, [[0, 1], [1, 2]], None, [0, 1]]
    system = MovieRentingSystem(1, [[0, 9, 2]])
    system.rent(0, 9)
    system.drop(0, 9)
    system.rent(0, 9)
    # A repeated rent cannot make obsolete heap entries appear as duplicates.
    assert system.report() == [[0, 9]]
    print("All tests passed")
