"""
LeetCode 271: Encode and Decode Strings
Difficulty: Medium
Pattern: Arrays & Hashing
Video Reference: https://www.youtube.com/watch?v=B1k_sxOSgv8
Complexity:
    - Time: O(L)
    - Space: O(L)
"""

from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        # Record character counts rather than escaped content so delimiters stay usable.
        # Length prefixes avoid ambiguity when values contain delimiters or are empty.
        return "".join(str(len(value)) + "#" + value for value in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        # index always points at the next unread length header.
        index = 0
        while index < len(s):
            # The next delimiter ends only the numeric header, never the payload.
            marker = s.index("#", index)
            length = int(s[index:marker])
            # Advancing past the delimiter sets the exact payload start offset.
            start = marker + 1
            # Consume exactly the declared payload length; its contents need no escaping.
            result.append(s[start : start + length])
            # The next header begins immediately after this fixed-length payload.
            index = start + length
        # No bytes means the original list was empty; "0#" still yields one empty value.
        return result


if __name__ == "__main__":
    codec = Codec()
    assert codec.decode(codec.encode(["lint", "code", "love", "you"])) == [
        "lint",
        "code",
        "love",
        "you",
    ]
    assert codec.decode(codec.encode(["we", "say", ":", "yes"])) == [
        "we",
        "say",
        ":",
        "yes",
    ]
    assert codec.decode(codec.encode([])) == []
    assert codec.decode(codec.encode(["", "#", "a#b"])) == ["", "#", "a#b"]
    print("All tests passed")
