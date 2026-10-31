import random
from typing import Dict, List


class RandomizedSet:
    def __init__(self) -> None:
        # Values support random access, and positions make removal constant time.
        # Each stored value appears once in the list and once in the map.
        self.values: List[int] = []
        self.positions: Dict[int, int] = {}

    def insert(self, val: int) -> bool:
        # Existing values already have exactly one position in both structures.
        if val in self.positions:
            return False
        self.positions[val] = len(self.values)
        self.values.append(val)
        # The map index always points to this value's list slot.
        return True

    def remove(self, val: int) -> bool:
        # A missing key leaves the representation unchanged.
        if val not in self.positions:
            return False
        index = self.positions.pop(val)
        last = self.values.pop()
        if index < len(self.values):
            # Move the former last value into the hole before updating its index.
            self.values[index] = last
            self.positions[last] = index
        # Pop and swap preserve the map/list bijection without shifting elements.
        # Removing the last slot itself needs no replacement assignment.
        return True

    def getRandom(self) -> int:
        # Uniform list indexing gives each currently stored value equal probability.
        return random.choice(self.values)


if __name__ == "__main__":
    random.seed(7)
    randomized_set = RandomizedSet()
    assert randomized_set.insert(1) is True
    assert randomized_set.remove(2) is False
    assert randomized_set.insert(2) is True
    assert randomized_set.getRandom() in {1, 2}
    assert randomized_set.remove(1) is True
    assert randomized_set.insert(2) is False
    assert randomized_set.getRandom() == 2
    assert randomized_set.remove(2) is True
    print("All tests passed")
