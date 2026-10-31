"""
LeetCode 353: Design Snake Game
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+353+Design+Snake+Game+neetcode
Complexity:
    - Time: move O(1) average
    - Space: O(length + food)
"""

from collections import deque
from typing import Deque, List, Optional, Set, Tuple, Union


class SnakeGame:
    # The deque preserves body order and a set mirrors its occupied cells.
    # Removing the tail before collision checks permits legal tail-follow moves.
    def __init__(self, width: int, height: int, food: List[List[int]]):
        # Body order is tail-to-head, so both end operations are constant time.
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0
        self.body: Deque[Tuple[int, int]] = deque([(0, 0)])
        # Occupancy membership detects self-collisions without scanning body.
        self.occupied: Set[Tuple[int, int]] = {(0, 0)}
        self.over = False
        self.directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    def move(self, direction: str) -> int:
        if self.over:
            return -1
        row, col = self.body[-1]
        dr, dc = self.directions[direction]
        next_cell = (row + dr, col + dc)
        if not (0 <= next_cell[0] < self.height and 0 <= next_cell[1] < self.width):
            self.over = True
            return -1
        # Bounds are checked before mutating either body representation.
        growing = (
            self.food_index < len(self.food)
            and [next_cell[0], next_cell[1]] == self.food[self.food_index]
        )
        # The tail vacates on ordinary moves, so it is not a collision target.
        if not growing:
            tail = self.body.popleft()
            self.occupied.remove(tail)
        if next_cell in self.occupied:
            self.over = True
            return -1
        self.body.append(next_cell)
        self.occupied.add(next_cell)
        # Both structures contain the same cells after a successful move.
        if growing:
            # Food keeps the tail in place and increases the body length by one.
            self.food_index += 1
        return len(self.body) - 1


def replay(
    ops: List[str], args: List[list]
) -> List[Optional[Union[int, str]]]:
    outputs: List[Optional[Union[int, str]]] = []
    game = None
    for operation, values in zip(ops, args):
        if operation == "SnakeGame":
            game = SnakeGame(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(game, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["SnakeGame", "move", "move", "move", "move", "move", "move"],
        [[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["U"]],
    ) == [None, 0, 0, 1, 1, 2, -1]
    assert replay(
        ["SnakeGame", "move", "move"],
        [[2, 2, [[0, 1], [1, 1]]], ["R"], ["D"]],
    ) == [None, 1, 2]
    print("All tests passed")
