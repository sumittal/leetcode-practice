from typing import List, Optional


class ParkingSystem:
    # Remaining spaces are independent counters for the three car categories.
    # A failed arrival must not consume capacity.
    # Vehicle types index the counter array directly.
    # The input guarantees carType is one of the supported categories.
    def __init__(self, big: int, medium: int, small: int):
        # Index zero is unused because vehicle types are numbered one through three.
        self.available: List[int] = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        # Checking before decrement prevents capacity from becoming negative.
        if self.available[carType] == 0:
            return False
        # One direct indexed counter models each vehicle-sized parking pool.
        self.available[carType] -= 1
        # Constant-index updates keep each category independent.
        return True


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[bool]]:
    outputs: List[Optional[bool]] = []
    parking = None
    for operation, values in zip(ops, args):
        if operation == "ParkingSystem":
            parking = ParkingSystem(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(parking, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"],
        [[1, 1, 0], [1], [2], [3], [1]],
    ) == [None, True, True, False, False]
    assert replay(
        ["ParkingSystem", "addCar", "addCar"],
        [[0, 0, 1], [3], [3]],
    ) == [None, True, False]
    print("All tests passed")
