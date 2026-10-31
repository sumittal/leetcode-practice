from typing import List


class Iterator:
    def __init__(self, nums: List[int]):
        # This small stand-in mirrors the supplied LeetCode iterator interface.
        self.nums = nums
        self.index = 0

    def hasNext(self) -> bool:
        return self.index < len(self.nums)

    def next(self) -> int:
        # The caller checks hasNext before requesting the following value.
        value = self.nums[self.index]
        self.index += 1
        return value


class PeekingIterator:
    def __init__(self, iterator: Iterator):
        self.iterator = iterator
        # A sentinel distinguishes a cached value from an empty lookahead slot.
        # LeetCode inputs contain integers, so None cannot be a stream value.
        self.cached = None

    def _fill(self) -> None:
        # At most one underlying next call is held for future consumers.
        if self.cached is None and self.iterator.hasNext():
            self.cached = self.iterator.next()

    def peek(self) -> int:
        self._fill()
        # Return the buffer without clearing it.
        return self.cached

    def next(self) -> int:
        self._fill()
        value = self.cached
        # Clearing the cache lets the next request refill from the source.
        self.cached = None
        return value

    def hasNext(self) -> bool:
        # Filling is safe because the wrapped iterator advances into the cache.
        self._fill()
        return self.cached is not None


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    iterator = None
    for op, values in zip(ops, args):
        if op == "PeekingIterator":
            iterator = PeekingIterator(Iterator(*values))
            outputs.append(None)
        else:
            outputs.append(getattr(iterator, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["PeekingIterator", "peek", "next", "next", "hasNext", "peek",
         "next", "hasNext"],
        [[[1, 2, 3]], [], [], [], [], [], [], []],
    ) == [None, 1, 1, 2, True, 3, 3, False]
    print("All tests passed")
