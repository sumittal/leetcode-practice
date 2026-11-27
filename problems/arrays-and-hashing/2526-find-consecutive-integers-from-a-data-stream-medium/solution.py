"""
LeetCode 2526: Find Consecutive Integers from a Data Stream
Difficulty: Medium
Pattern: Hash Table
Video Reference: https://www.youtube.com/results?search_query=leetcode+2526+Find+Consecutive+Integers+from+a+Data+Stream+neetcode
Complexity:
    - Time: consec O(1)
    - Space: O(1)
"""

from typing import List, Optional


class DataStream:
    def __init__(self, value: int, k: int):
        # No historical values are needed beyond the current matching suffix.
        self.value = value
        # The stream's target and required suffix length never change.
        self.k = k
        self.streak = 0

    def consec(self, num: int) -> bool:
        # The streak is exactly the target-valued suffix length.
        # Any other incoming value resets the consecutive run immediately.
        if num == self.value:
            # Extending a matching suffix needs only one integer update.
            self.streak += 1
        else:
            # A mismatch breaks every suffix that could reach the threshold.
            self.streak = 0
        # Once the suffix reaches k, later matches keep the predicate true.
        # No queue is needed because earlier nonmatching values cannot matter.
        return self.streak >= self.k


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[bool]]:
    outputs: List[Optional[bool]] = []
    stream = None
    for operation, values in zip(ops, args):
        if operation == "DataStream":
            stream = DataStream(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(stream, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["DataStream", "consec", "consec", "consec", "consec"],
        [[4, 3], [4], [4], [4], [3]],
    ) == [None, False, False, True, False]
    assert replay(
        ["DataStream", "consec", "consec", "consec"],
        [[7, 1], [7], [8], [7]],
    ) == [None, True, False, True]
    print("All tests passed")
