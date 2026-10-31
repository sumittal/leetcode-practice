"""
LeetCode 2069: Walking Robot Simulation II
Difficulty: Medium
Pattern: Design
Video Reference: https://www.youtube.com/results?search_query=leetcode+2069+Walking+Robot+Simulation+II+neetcode
Complexity:
    - Time: step O(1), getPos/getDir O(1)
    - Space: O(1)
"""

from typing import List, Optional, Union


class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.perimeter = 2 * width + 2 * height - 4
        # A scalar distance along the perimeter determines position and heading.
        self.steps = 0
        self.has_moved = False

    def step(self, num: int) -> None:
        # Remember any movement because returning to the origin changes heading.
        if num:
            self.has_moved = True
        # The direction/position state repeats after one boundary lap.
        self.steps = (self.steps + num) % self.perimeter

    def _state(self) -> tuple:
        index = self.steps
        # The initial origin points east; after a full lap it points south.
        if index == 0:
            direction = "South" if self.has_moved else "East"
            return [0, 0], direction
        if index < self.width:
            # Bottom edge runs from x=0 toward the right.
            return [index, 0], "East"
        if index < self.width + self.height - 1:
            # The next segment climbs the right edge.
            return [self.width - 1, index - self.width + 1], "North"
        top_start = self.width + self.height - 1
        left_start = 2 * self.width + self.height - 2
        if index < left_start:
            # Subtracting from width walks left across the top edge.
            return [self.width - 2 - (index - top_start),
                    self.height - 1], "West"
        # The final segment descends the left edge back to the origin.
        return [0, self.height - 2 - (index - left_start)], "South"

    def getPos(self) -> List[int]:
        return self._state()[0]

    def getDir(self) -> str:
        return self._state()[1]


def replay(
    ops: List[str], args: List[List[int]]
) -> List[Optional[Union[List[int], str]]]:
    outputs: List[Optional[Union[List[int], str]]] = []
    robot = None
    for operation, values in zip(ops, args):
        if operation == "Robot":
            robot = Robot(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(robot, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["Robot", "step", "step", "getPos", "getDir", "step", "step",
         "step", "getPos", "getDir"],
        [[6, 3], [2], [2], [], [], [2], [1], [4], [], []],
    ) == [None, None, None, [4, 0], "East", None, None, None, [1, 2], "West"]
    assert replay(
        ["Robot", "step", "getPos", "getDir"],
        [[2, 2], [4], [], []],
    ) == [None, None, [0, 0], "South"]
    assert replay(
        ["Robot", "step", "getPos", "getDir"],
        [[2, 2], [1], [], []],
    ) == [None, None, [1, 0], "East"]
    print("All tests passed")
