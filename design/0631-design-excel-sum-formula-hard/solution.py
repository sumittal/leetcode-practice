"""
LeetCode 631: Design Excel Sum Formula
Difficulty: Hard
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+631+Design+Excel+Sum+Formula+neetcode
Complexity:
    - Time: set O(1), get O(dependency graph), sum O(referenced cells + dependency graph)
    - Space: O(cells + formula references)
"""

from collections import Counter
from typing import Dict, List, Tuple


class Excel:
    # Formula cells store reference multiplicities, not a cached value.
    # Re-evaluation lets later source-cell changes flow into dependent formulas.
    # Counter entries preserve repeated ranges and overlapping references.
    # Direct set removes prior formula dependencies for the target cell.
    def __init__(self, H: int, W: str):
        # Dimensions are retained for the worksheet contract.
        self.height = H
        self.width = ord(W) - ord("A") + 1
        self.values: Dict[Tuple[int, int], int] = {}
        self.formulas: Dict[Tuple[int, int], Counter] = {}

    def _column(self, column: str) -> int:
        # Cell coordinates use one-based row and column indices.
        return ord(column) - ord("A") + 1

    def _parse_cell(self, cell: str) -> Tuple[int, int]:
        column = self._column(cell[0])
        row = int(cell[1:])
        # A tuple is a stable key for the value and formula maps.
        return row, column

    def _value(self, cell: Tuple[int, int]) -> int:
        if cell not in self.formulas:
            return self.values.get(cell, 0)
        # Counter multiplicities preserve repeated references in a formula.
        # Formula references are recalculated so edits to dependencies propagate.
        return sum(
            count * self._value(reference)
            for reference, count in self.formulas[cell].items()
        )

    def set(self, row: int, column: str, val: int) -> None:
        cell = (row, self._column(column))
        # Direct assignment cancels any formula formerly attached to the cell.
        self.formulas.pop(cell, None)
        self.values[cell] = val

    def get(self, row: int, column: str) -> int:
        return self._value((row, self._column(column)))

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        cell = (row, self._column(column))
        references: Counter = Counter()
        # Each input term contributes its own references, even if repeated.
        for term in numbers:
            if ":" not in term:
                references[self._parse_cell(term)] += 1
                continue
            first, last = term.split(":")
            first_row, first_col = self._parse_cell(first)
            last_row, last_col = self._parse_cell(last)
            # Inclusive rectangles expand to each cell once per listed range.
            for current_row in range(first_row, last_row + 1):
                for current_col in range(first_col, last_col + 1):
                    references[(current_row, current_col)] += 1
        self.values.pop(cell, None)
        self.formulas[cell] = references
        return self._value(cell)


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs = []
    sheet = None
    for operation, values in zip(ops, args):
        if operation == "Excel":
            sheet = Excel(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(sheet, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["Excel", "set", "sum", "set", "get"],
        [[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]],
         [2, "B", 2], [3, "C"]],
    ) == [None, None, 4, None, 6]
    assert replay(
        ["Excel", "get", "sum", "set", "get"],
        [[2, "B"], [1, "A"], [2, "B", ["A1", "A1"]],
         [1, "A", 5], [2, "B"]],
    ) == [None, 0, 0, None, 10]
    print("All tests passed")
