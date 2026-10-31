from typing import List


class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int,
    ) -> int:
        # At most k stops permits no more than k + 1 flight edges.
        prices = [float("inf")] * n
        prices[src] = 0
        # prices stores the cheapest route using no more than the rounds completed.
        for _ in range(k + 1):
            previous_round = prices[:]
            # Snapshotting prevents one round from chaining multiple new flights.
            for origin, destination, price in flights:
                if previous_round[origin] == float("inf"):
                    # Unreachable origins cannot extend a route in this round.
                    continue
                candidate = previous_round[origin] + price
                prices[destination] = min(prices[destination], candidate)
                # Updates come only from the snapshot, limiting this round to one edge.
            # Keeping earlier prices allows any route with fewer edges as well.
        # Infinity remains only when no route meets the allowed edge count.
        # Converting only finite totals keeps the public result an integer.
        return int(prices[dst]) if prices[dst] != float("inf") else -1


if __name__ == "__main__":
    solution = Solution()
    flights = [
        [0, 1, 100],
        [1, 2, 100],
        [2, 0, 100],
        [1, 3, 600],
        [2, 3, 200],
    ]
    assert solution.findCheapestPrice(4, flights, 0, 3, 1) == 700
    assert solution.findCheapestPrice(4, flights, 0, 3, 2) == 400
    assert (
        solution.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1)
        == 200
    )
    assert solution.findCheapestPrice(3, [[1, 2, 100]], 0, 2, 1) == -1
    print("All tests passed")
