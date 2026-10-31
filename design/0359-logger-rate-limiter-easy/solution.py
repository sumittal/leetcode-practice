"""
LeetCode 359: Logger Rate Limiter
Difficulty: Easy
Pattern: Hash Table
Video Reference: https://www.youtube.com/results?search_query=leetcode+359+Logger+Rate+Limiter+neetcode
Complexity:
    - Time: shouldPrintMessage O(1) average
    - Space: O(unique messages)
"""

from typing import Dict, List, Optional, Union


class Logger:
    # The latest accepted timestamp is sufficient for each message's rule.
    # Rejected attempts never extend the suppression interval.
    # Dictionary lookup gives average constant-time decisions.
    def __init__(self):
        # Entries represent accepted messages, not rejected attempts.
        self.last_printed: Dict[str, int] = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        previous = self.last_printed.get(message)
        # A missing timestamp distinguishes unseen messages from time zero.
        # Reject only while fewer than ten seconds separate accepted copies.
        if previous is not None and timestamp - previous < 10:
            return False
        # Rejected attempts do not move the cooldown's starting timestamp.
        self.last_printed[message] = timestamp
        # The hash lookup and update give constant average time per call.
        return True


def replay(
    ops: List[str], args: List[List[Union[int, str]]]
) -> List[Optional[bool]]:
    outputs: List[Optional[bool]] = []
    logger = None
    for operation, values in zip(ops, args):
        if operation == "Logger":
            logger = Logger()
            outputs.append(None)
        else:
            outputs.append(getattr(logger, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["Logger", "shouldPrintMessage", "shouldPrintMessage",
         "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage",
         "shouldPrintMessage"],
        [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"],
         [10, "foo"], [11, "foo"]],
    ) == [None, True, True, False, False, False, True]
    assert replay(
        ["Logger", "shouldPrintMessage", "shouldPrintMessage",
         "shouldPrintMessage"],
        [[], [5, "x"], [14, "x"], [15, "x"]],
    ) == [None, True, False, True]
    print("All tests passed")
