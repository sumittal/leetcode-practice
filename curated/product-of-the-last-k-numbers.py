from typing import List, Optional


class ProductOfNumbers:
    # Prefix division answers any suffix product that contains no zero.
    # A zero resets the current prefix so division never crosses zero.
    # Prefix length detects whether the requested suffix includes that reset.
    def __init__(self):
        # A leading one is the empty product for the current zero-free suffix.
        self.prefix: List[int] = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Reset because every product reaching across this zero is zero.
            self.prefix = [1]
        else:
            # Prefix products remain nonzero between resets.
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # The suffix began after a zero when k reaches beyond this prefix list.
        if k >= len(self.prefix):
            return 0
        # Dividing two nonzero prefix products isolates the final k factors.
        return self.prefix[-1] // self.prefix[-k - 1]


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    numbers = None
    for operation, values in zip(ops, args):
        if operation == "ProductOfNumbers":
            numbers = ProductOfNumbers()
            outputs.append(None)
        else:
            outputs.append(getattr(numbers, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["ProductOfNumbers", "add", "add", "add", "add", "add",
         "getProduct", "getProduct", "getProduct", "add", "getProduct"],
        [[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]],
    ) == [None, None, None, None, None, None, 20, 40, 0, None, 32]
    assert replay(
        ["ProductOfNumbers", "add", "getProduct", "add", "getProduct"],
        [[], [7], [1], [0], [1]],
    ) == [None, None, 7, None, 0]
    print("All tests passed")
