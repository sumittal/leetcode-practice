from typing import Dict, List


class Cashier:
    # Discount scheduling depends on completed bills, not specific products.
    # Price lookup is constant time for each item in a requested cart.
    # The order count advances once for every getBill invocation.
    def __init__(
        self, n: int, discount: int, products: List[int], prices: List[int]
    ):
        # Product prices are fixed, and only the order count changes over time.
        self.frequency = n
        self.discount = discount
        self.prices: Dict[int, int] = dict(zip(products, prices))
        self.orders = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        # Each call advances the order count exactly once.
        self.orders += 1
        # Matching positions pair each requested product with its quantity.
        total = sum(
            self.prices[item] * quantity
            for item, quantity in zip(product, amount)
        )
        # Apply a percentage discount only on each nth completed order.
        if self.orders % self.frequency == 0:
            # Compute the percentage as a multiplier after summing the full cart.
            total *= (100 - self.discount) / 100.0
        return total


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    cashier = None
    for op, values in zip(ops, args):
        if op == "Cashier":
            cashier = Cashier(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(cashier, op)(*values))
    return outputs


if __name__ == "__main__":
    results = replay(
        ["Cashier", "getBill", "getBill", "getBill"],
        [[3, 50, [1, 2, 3], [100, 200, 300]],
         [[1, 2], [1, 2]], [[3], [1]], [[2, 3], [1, 1]]],
    )
    assert results[:3] == [None, 500, 300]
    assert abs(results[3] - 250.0) < 1e-9
    print("All tests passed")
