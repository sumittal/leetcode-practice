"""
LeetCode 2408: Design SQL
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+2408+Design+SQL+neetcode
Complexity:
    - Time: ins/rmv/sel O(1) expected, exp O(r log r)
    - Space: O(live rows + table metadata)
"""

from typing import Dict, List, Tuple


class SQL:
    def __init__(self, names: List[str], columns: List[int]):
        # Each table tracks schema, sparse live rows, and its next permanent ID.
        self.tables: Dict[str, Tuple[int, Dict[int, List[str]], int]] = {}
        # A row dictionary permits deletion without shifting future identifiers.
        for name, count in zip(names, columns):
            self.tables[name] = (count, {}, 1)

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.tables:
            return False
        columns, rows, next_id = self.tables[name]
        # Validation happens before consuming the table's next row ID.
        if len(row) != columns:
            return False
        # Successful insertion consumes the next ID even if older rows were deleted.
        rows[next_id] = row[:]
        self.tables[name] = (columns, rows, next_id + 1)
        return True

    def rmv(self, name: str, rowId: int) -> None:
        if name in self.tables:
            _, rows, _ = self.tables[name]
            # Missing IDs are harmless and do not rewind the auto-increment.
            rows.pop(rowId, None)

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.tables:
            return "<null>"
        columns, rows, _ = self.tables[name]
        if rowId not in rows or not 1 <= columnId <= columns:
            return "<null>"
        # Column identifiers are one-based in the external API.
        return rows[rowId][columnId - 1]

    def exp(self, name: str) -> List[str]:
        if name not in self.tables:
            return []
        _, rows, _ = self.tables[name]
        # CSV row IDs precede cells and only current rows are exported.
        # Sorting IDs makes CSV exports deterministic and row-ID ordered.
        return [
            str(row_id) + "," + ",".join(rows[row_id])
            for row_id in sorted(rows)
        ]


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    database = None
    for op, values in zip(ops, args):
        if op == "SQL":
            database = SQL(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(database, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["SQL", "ins", "sel", "ins", "exp", "rmv", "sel", "exp"],
        [[["one", "two", "three"], [2, 3, 1]],
         ["two", ["first", "second", "third"]], ["two", 1, 3],
         ["two", ["fourth", "fifth", "sixth"]], ["two"], ["two", 1],
         ["two", 2, 2], ["two"]],
    ) == [None, True, "third", True,
          ["1,first,second,third", "2,fourth,fifth,sixth"], None, "fifth",
          ["2,fourth,fifth,sixth"]]
    assert replay(
        ["SQL", "ins", "sel", "rmv", "sel", "ins", "ins"],
        [[["one", "two", "three"], [2, 3, 1]],
         ["two", ["first", "second", "third"]], ["two", 1, 3], ["two", 1],
         ["two", 1, 2], ["two", ["fourth", "fifth"]],
         ["two", ["fourth", "fifth", "sixth"]]],
    ) == [None, True, "third", None, "<null>", False, True]
    print("All tests passed")
