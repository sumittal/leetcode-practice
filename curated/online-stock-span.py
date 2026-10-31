from typing import List, Optional, Tuple


class StockSpanner:
    # Each stack pair summarizes consecutive days dominated by its price.
    # Popping smaller prices merges their spans into the current day.
    # The remaining top, if present, is the closest greater previous price.
    def __init__(self):
        # Stack values decrease from bottom to top after each day is processed.
        self.stack: List[Tuple[int, int]] = []

    def next(self, price: int) -> int:
        # Span one includes the current day before earlier days are merged.
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            # Popped spans are consecutive earlier days no higher than this price.
            span += self.stack.pop()[1]
        # Remaining stack prices decrease, so its top is the nearest blocker.
        self.stack.append((price, span))
        # Every popped pair is absorbed into exactly one later span.
        return span


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    spanner = None
    for operation, values in zip(ops, args):
        if operation == "StockSpanner":
            spanner = StockSpanner()
            outputs.append(None)
        else:
            outputs.append(getattr(spanner, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["StockSpanner", "next", "next", "next", "next", "next", "next",
         "next"],
        [[], [100], [80], [60], [70], [60], [75], [85]],
    ) == [None, 1, 1, 1, 2, 1, 4, 6]
    assert replay(
        ["StockSpanner", "next", "next", "next"],
        [[], [10], [10], [10]],
    ) == [None, 1, 2, 3]
    print("All tests passed")
