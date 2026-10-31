from typing import Any, Iterator, List, Optional


class NestedInteger:
    def __init__(self, value):
        # The helper can hold either one integer or a nested list of helpers.
        self.value = value

    def isInteger(self) -> bool:
        # This distinction mirrors LeetCode's NestedInteger interface.
        return isinstance(self.value, int)

    def getInteger(self) -> Optional[int]:
        return self.value if self.isInteger() else None

    def getList(self) -> Optional[List["NestedInteger"]]:
        return self.value if not self.isInteger() else None


class NestedIterator:
    # The iterator stack stores only lists along the active depth-first path.
    def __init__(self, nestedList: List[NestedInteger]):
        # One iterator per active list keeps memory proportional to nesting depth.
        self.iterators: List[Iterator[NestedInteger]] = [iter(nestedList)]
        self.ready = False
        self.next_value: Optional[int] = None

    def hasNext(self) -> bool:
        if self.ready:
            return True
        while self.iterators:
            item = next(self.iterators[-1], None)
            if item is None:
                # Exhausted child iterators unwind to their parent list.
                self.iterators.pop()
            elif item.isInteger():
                self.next_value = item.getInteger()
                self.ready = True
                return True
            else:
                # Descend only into the next list, preserving left-to-right order.
                self.iterators.append(iter(item.getList() or []))
        return False

    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration
        self.ready = False
        value = self.next_value
        self.next_value = None
        # hasNext has already advanced the stack to this buffered integer.
        return value


def make_nested(value) -> NestedInteger:
    # Convert plain test lists into the same interface consumed by the iterator.
    if isinstance(value, list):
        return NestedInteger([make_nested(item) for item in value])
    return NestedInteger(value)


def replay(ops: List[str], args: List[List[Any]]) -> List[Any]:
    outputs: List[Any] = []
    iterator = None
    for operation, values in zip(ops, args):
        if operation == "NestedIterator":
            nested = [make_nested(item) for item in values[0]]
            iterator = NestedIterator(nested)
            outputs.append(None)
        else:
            outputs.append(getattr(iterator, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["NestedIterator", "hasNext", "next", "hasNext", "next",
         "hasNext", "next", "hasNext", "next", "hasNext", "next",
         "hasNext"],
        [[[[1, 1], 2, [1, 1]]], [], [], [], [], [], [], [], [], [], [], []],
    ) == [None, True, 1, True, 1, True, 2, True, 1, True, 1, False]
    assert replay(
        ["NestedIterator", "hasNext", "next", "hasNext", "next",
         "hasNext", "next", "hasNext"],
        [[[1, [4, [6]]]], [], [], [], [], [], [], []],
    ) == [None, True, 1, True, 4, True, 6, False]
    assert replay(
        ["NestedIterator", "hasNext", "next", "hasNext", "next",
         "hasNext"],
        [[[[[], -2], [[]], 7]], [], [], [], [], []],
    ) == [None, True, -2, True, 7, False]
    print("All tests passed")
