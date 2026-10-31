from typing import Dict, List, Optional


class Leaderboard:
    # The score dictionary is the complete current ranking state.
    # Recomputing top K avoids stale heap records after score resets.
    def __init__(self):
        # Player IDs are unique keys and inactive players are absent.
        self.scores: Dict[int, int] = {}

    def addScore(self, playerId: int, score: int) -> None:
        # A player's accumulated score is the only stored ranking state.
        self.scores[playerId] = self.scores.get(playerId, 0) + score

    def top(self, K: int) -> int:
        # Sorting provides the exact K largest scores without stale ranking data.
        # Sorting is linearithmic and simple for the bounded leaderboard input.
        return sum(sorted(self.scores.values(), reverse=True)[:K])

    def reset(self, playerId: int) -> None:
        # Removing the map entry resets the player's score to an inactive state.
        self.scores.pop(playerId, None)
        # A missing player is already in the reset state.


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    leaderboard = None
    for operation, values in zip(ops, args):
        if operation == "Leaderboard":
            leaderboard = Leaderboard()
            outputs.append(None)
        else:
            outputs.append(getattr(leaderboard, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["Leaderboard", "addScore", "addScore", "addScore", "addScore",
         "addScore", "top", "reset", "reset", "addScore", "top"],
        [[], [1, 73], [2, 56], [3, 39], [4, 51], [5, 4], [1], [1], [2],
         [2, 51], [3]],
    ) == [None, None, None, None, None, None, 73, None, None, None, 141]
    assert replay(
        ["Leaderboard", "addScore", "addScore", "top", "reset", "top"],
        [[], [7, 10], [7, 5], [1], [7], [0]],
    ) == [None, None, None, 15, None, 0]
    print("All tests passed")
