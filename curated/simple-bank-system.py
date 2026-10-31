from typing import List, Optional, Union


class Bank:
    # Account numbers are one-based externally and positions are zero-based.
    # Every transfer validates both accounts and funds before mutating balances.
    # Invalid operations leave the entire balance list unchanged.
    def __init__(self, balance: List[int]):
        # The input list is the live balance table for one-based account IDs.
        self.balance = balance

    def _valid(self, account: int) -> bool:
        # Accounts outside the input's one-based range are rejected unchanged.
        return 1 <= account <= len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self._valid(account1) or not self._valid(account2):
            return False
        # Convert both public account numbers to zero-based storage positions.
        source = account1 - 1
        destination = account2 - 1
        if self.balance[source] < money:
            return False
        # Validate the source first so a failed transfer is atomic.
        self.balance[source] -= money
        self.balance[destination] += money
        # Once validated, both balance updates complete as one transfer.
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._valid(account):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._valid(account):
            return False
        index = account - 1
        if self.balance[index] < money:
            return False
        self.balance[index] -= money
        return True


def replay(
    ops: List[str], args: List[list]
) -> List[Optional[Union[int, bool]]]:
    outputs: List[Optional[Union[int, bool]]] = []
    bank = None
    for operation, values in zip(ops, args):
        if operation == "Bank":
            bank = Bank(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(bank, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"],
        [[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20],
         [3, 4, 15], [10, 50]],
    ) == [None, True, True, True, False, False]
    assert replay(
        ["Bank", "deposit", "transfer", "withdraw"],
        [[[1, 2]], [3, 9], [1, 3, 1], [2, 3]],
    ) == [None, False, False, False]
    print("All tests passed")
