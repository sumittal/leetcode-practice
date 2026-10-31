from typing import List


class ATM:
    def __init__(self):
        # Counts are stored in the problem's denomination order.
        self.denominations = [20, 50, 100, 200, 500]
        self.counts = [0] * len(self.denominations)

    def deposit(self, banknotesCount: List[int]) -> None:
        # Deposits add inventory without changing the denomination ordering.
        # The five-count vector mirrors the denominations list index for index.
        for index, count in enumerate(banknotesCount):
            self.counts[index] += count

    def withdraw(self, amount: int) -> List[int]:
        used = [0] * len(self.denominations)
        remaining = amount
        # Work on a temporary vector so failure can leave inventory untouched.
        # Largest notes first minimize the number of notes in the greedy plan.
        for index in range(len(self.denominations) - 1, -1, -1):
            denomination = self.denominations[index]
            used[index] = min(self.counts[index], remaining // denomination)
            remaining -= used[index] * denomination
        # An inexact plan must not consume any of the stored inventory.
        if remaining:
            # Greedy selection is abandoned atomically when exact cash is absent.
            return [-1]
        for index, count in enumerate(used):
            # Inventory is mutated only after the plan is known to be exact.
            self.counts[index] -= count
        return used


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    atm = None
    for op, values in zip(ops, args):
        if op == "ATM":
            atm = ATM()
            outputs.append(None)
        else:
            outputs.append(getattr(atm, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["ATM", "deposit", "withdraw", "deposit", "withdraw", "withdraw",
         "withdraw"],
        [[], [[0, 0, 1, 2, 1]], [600], [[0, 1, 0, 1, 1]], [600], [550],
         [500]],
    ) == [None, None, [0, 0, 1, 0, 1], None, [-1], [0, 1, 0, 0, 1],
          [-1]]
    print("All tests passed")
