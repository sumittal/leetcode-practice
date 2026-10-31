from typing import List, Optional, Union


class LUPrefix:
    def __init__(self, n: int):
        # Video IDs are one-based; slot zero is intentionally unused.
        self.uploaded = [False] * (n + 1)
        self.prefix = 0

    def upload(self, video: int) -> None:
        # Marking an already-uploaded ID is idempotent.
        self.uploaded[video] = True
        # Uploads beyond the first gap cannot change the prefix yet.
        # A single upload can close a gap followed by many earlier uploads.
        # The prefix only moves forward, so total scanning is linear in n.
        while self.prefix + 1 < len(self.uploaded) and \
                self.uploaded[self.prefix + 1]:
            self.prefix += 1
        # Each video advances the pointer at most once over the whole stream.

    def longest(self) -> int:
        # All IDs at or below prefix are known to be present.
        # This cached answer is returned in constant time.
        return self.prefix


def replay(
    ops: List[str], args: List[List[int]]
) -> List[Optional[Union[int, bool]]]:
    outputs: List[Optional[Union[int, bool]]] = []
    server = None
    for operation, values in zip(ops, args):
        if operation == "LUPrefix":
            server = LUPrefix(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(server, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["LUPrefix", "upload", "longest", "upload", "longest", "upload",
         "longest"],
        [[4], [3], [], [1], [], [2], []],
    ) == [None, None, 0, None, 1, None, 3]
    assert replay(
        ["LUPrefix", "upload", "upload", "upload", "longest"],
        [[3], [2], [3], [1], []],
    ) == [None, None, None, None, 3]
    print("All tests passed")
