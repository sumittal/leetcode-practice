"""
LeetCode 535: Encode and Decode TinyURL
Difficulty: Medium
Pattern: Arrays & Hashing
Video Reference: https://www.youtube.com/watch?v=VyBOaboQLGc
Complexity:
    - Time: encode O(1), decode O(1)
    - Space: O(number of encoded URLs)
"""

from typing import Dict, List


class Codec:
    # A growing integer ID guarantees unique short keys for distinct inputs.
    # Forward and reverse maps make repeated encode calls idempotent.
    def __init__(self):
        # The bijection allows decoding without depending on URL contents.
        self.alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.next_id = 1
        self.long_to_short: Dict[str, str] = {}
        self.short_to_long: Dict[str, str] = {}

    def _encode_id(self, number: int) -> str:
        # Repeated division converts a monotonically increasing integer to base 62.
        digits = []
        while number:
            number, remainder = divmod(number, len(self.alphabet))
            digits.append(self.alphabet[remainder])
        # Reversing base digits yields a compact deterministic path component.
        return "".join(reversed(digits)) or "0"

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.long_to_short:
            short = "http://tinyurl.com/" + self._encode_id(self.next_id)
            self.next_id += 1
            self.long_to_short[longUrl] = short
            self.short_to_long[short] = longUrl
            # Both dictionaries are written together to preserve reversibility.
        # Repeated encoding of one URL reuses its previously assigned key.
        return self.long_to_short[longUrl]

    def decode(self, shortUrl: str) -> str:
        # The problem only decodes identifiers previously produced by encode.
        return self.short_to_long[shortUrl]


def replay(ops: List[str], args: List[List[str]]) -> List[object]:
    outputs = []
    codec = None
    for operation, values in zip(ops, args):
        if operation == "Codec":
            codec = Codec()
            outputs.append(None)
        else:
            outputs.append(getattr(codec, operation)(*values))
    return outputs


if __name__ == "__main__":
    url = "https://leetcode.com/problems/design-tinyurl"
    codec = Codec()
    tiny = codec.encode(url)
    assert codec.decode(tiny) == url
    assert codec.encode(url) == tiny
    assert replay(
        ["Codec", "encode", "decode"],
        [[], [url], [tiny]],
    ) == [None, tiny, url]
    print("All tests passed")
