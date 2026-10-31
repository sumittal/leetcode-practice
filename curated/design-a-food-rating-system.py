import heapq
from typing import Dict, List, Tuple


class FoodRatings:
    def __init__(
        self, foods: List[str], cuisines: List[str], ratings: List[int]
    ):
        self.food_info: Dict[str, Tuple[str, int]] = {}
        self.heaps: Dict[str, List[Tuple[int, str]]] = {}
        # Keep one cuisine association and current rating per food.
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            # Heap keys use negative rating followed by the food-name tie break.
            self.food_info[food] = (cuisine, rating)
            self.heaps.setdefault(cuisine, []).append((-rating, food))
        # Heapify each cuisine once after loading the initial catalogue.
        for heap in self.heaps.values():
            heapq.heapify(heap)

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.food_info[food]
        self.food_info[food] = (cuisine, newRating)
        # Old heap records remain cheap to invalidate when they reach the top.
        # Push a new version; old entries are discarded lazily by highestRated.
        heapq.heappush(self.heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.heaps[cuisine]
        # The map is authoritative when a food has changed its rating.
        while heap:
            rating, food = heap[0]
            if self.food_info[food] == (cuisine, -rating):
                # Negative rating orders high scores first; tuple order breaks ties.
                return food
            # A stale rating cannot be returned because the map is authoritative.
            heapq.heappop(heap)
        raise ValueError("cuisine has no foods")


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    ratings = None
    for op, values in zip(ops, args):
        if op == "FoodRatings":
            ratings = FoodRatings(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(ratings, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["FoodRatings", "highestRated", "highestRated", "changeRating",
         "highestRated", "changeRating", "highestRated"],
        [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
          ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
          [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"],
         ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]],
    ) == [None, "kimchi", "ramen", None, "sushi", None, "ramen"]
    print("All tests passed")
