from typing import Dict, List, Optional, Union


class Spreadsheet:
    # Cell keys map to explicit values; absent coordinates implicitly equal zero.
    # Formula strings are evaluated from current cells on every request.
    def __init__(self, rows: int):
        # Sparse storage needs no allocation for untouched cells.
        self.rows = rows
        self.values: Dict[str, int] = {}

    def setCell(self, cell: str, value: int) -> None:
        # Cell identifiers are already canonical strings such as A1.
        self.values[cell] = value

    def resetCell(self, cell: str) -> None:
        # Removing an entry makes subsequent reads return the default zero.
        self.values.pop(cell, None)

    def _operand(self, token: str) -> int:
        if token[0].isalpha():
            # Missing references behave as zero without allocating empty cells.
            return self.values.get(token, 0)
        return int(token)

    def getValue(self, formula: str) -> int:
        # Parsing only the two operands keeps formula evaluation constant time.
        # Every supplied expression contains exactly two additive operands.
        left, right = formula[1:].split("+")
        return self._operand(left) + self._operand(right)


def replay(
    ops: List[str], args: List[list]
) -> List[Optional[Union[int, str]]]:
    outputs: List[Optional[Union[int, str]]] = []
    spreadsheet = None
    for operation, values in zip(ops, args):
        if operation == "Spreadsheet":
            spreadsheet = Spreadsheet(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(spreadsheet, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["Spreadsheet", "getValue", "setCell", "getValue", "setCell",
         "getValue", "resetCell", "getValue"],
        [[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15],
         ["=A1+B2"], ["A1"], ["=A1+B2"]],
    ) == [None, 12, None, 16, None, 25, None, 15]
    assert replay(
        ["Spreadsheet", "getValue", "setCell", "getValue"],
        [[1], ["=A1+4"], ["A1", 3], ["=A1+4"]],
    ) == [None, 4, None, 7]
    print("All tests passed")
