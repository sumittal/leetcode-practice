from typing import List, Optional


class TicTacToe:
    # Signed row, column, and diagonal totals summarize all moves so far.
    # A magnitude of n means one player filled a complete winning line.
    def __init__(self, n: int):
        self.n = n
        # Separate counters avoid storing the full board after construction.
        self.rows: List[int] = [0] * n
        self.columns: List[int] = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        # Player two's negative contribution keeps both players distinguishable.
        score = 1 if player == 1 else -1
        self.rows[row] += score
        self.columns[col] += score
        # Signed counts distinguish one player's complete line from mixed cells.
        if row == col:
            self.diagonal += score
        if row + col == self.n - 1:
            self.anti_diagonal += score
        # Counters are updated in constant time regardless of board size.
        # A full line has magnitude n because every cell contributes one sign.
        if any(
            abs(value) == self.n
            for value in (
                self.rows[row],
                self.columns[col],
                self.diagonal,
                self.anti_diagonal,
            )
        ):
            return player
        # Only the affected row, column, and diagonals can become winning now.
        return 0


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    game = None
    for operation, values in zip(ops, args):
        if operation == "TicTacToe":
            game = TicTacToe(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(game, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["TicTacToe", "move", "move", "move", "move", "move", "move",
         "move"],
        [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1],
         [1, 0, 2], [2, 1, 1]],
    ) == [None, 0, 0, 0, 0, 0, 0, 1]
    assert replay(
        ["TicTacToe", "move", "move", "move"],
        [[2], [0, 0, 2], [1, 1, 1], [0, 1, 2]],
    ) == [None, 0, 0, 2]
    print("All tests passed")
