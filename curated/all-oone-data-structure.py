from typing import Dict, List, Optional, Set


class Bucket:
    def __init__(self, count: int):
        self.count = count
        # Keys in a bucket all share exactly this count.
        self.keys: Set[str] = set()
        self.previous: Optional["Bucket"] = None
        self.following: Optional["Bucket"] = None


class AllOne:
    # The linked list keeps occupied frequencies in ascending order.
    # A key-to-bucket map makes key moves independent of total key count.
    def __init__(self):
        # Sentinel buckets simplify insertion and removal at both list ends.
        self.head = Bucket(0)
        self.tail = Bucket(0)
        self.head.following = self.tail
        self.tail.previous = self.head
        self.key_bucket: Dict[str, Bucket] = {}

    def _insert_after(self, current: Bucket, new_bucket: Bucket) -> None:
        following = current.following
        # Link both directions before exposing the new bucket to key operations.
        new_bucket.previous = current
        new_bucket.following = following
        current.following = new_bucket
        following.previous = new_bucket

    def _remove(self, bucket: Bucket) -> None:
        # Empty count buckets are removed so neighbors remain adjacent counts.
        bucket.previous.following = bucket.following
        bucket.following.previous = bucket.previous

    def inc(self, key: str) -> None:
        if key not in self.key_bucket:
            first = self.head.following
            if first is self.tail or first.count > 1:
                self._insert_after(self.head, Bucket(1))
            self.head.following.keys.add(key)
            self.key_bucket[key] = self.head.following
            return
        bucket = self.key_bucket[key]
        # A key can move only to the immediately following count.
        following = bucket.following
        if following is self.tail or following.count > bucket.count + 1:
            self._insert_after(bucket, Bucket(bucket.count + 1))
        # Moving between adjacent buckets changes the key count by exactly one.
        self.key_bucket[key] = bucket.following
        bucket.keys.remove(key)
        bucket.following.keys.add(key)
        if not bucket.keys:
            self._remove(bucket)
        # The key map is updated with the destination before its source disappears.

    def dec(self, key: str) -> None:
        if key not in self.key_bucket:
            return
        bucket = self.key_bucket[key]
        # Remove the old membership before deleting or inserting its new count.
        bucket.keys.remove(key)
        if bucket.count == 1:
            del self.key_bucket[key]
        else:
            previous = bucket.previous
            if previous is self.head or previous.count < bucket.count - 1:
                self._insert_after(previous, Bucket(bucket.count - 1))
            self.key_bucket[key] = bucket.previous
            bucket.previous.keys.add(key)
        if not bucket.keys:
            self._remove(bucket)
        # Only buckets that become empty are unlinked.

    def getMaxKey(self) -> str:
        bucket = self.tail.previous
        # Any key in the last bucket has the maximum count.
        return next(iter(bucket.keys)) if bucket is not self.head else ""

    def getMinKey(self) -> str:
        bucket = self.head.following
        # Any key in the first bucket has the minimum positive count.
        return next(iter(bucket.keys)) if bucket is not self.tail else ""


def replay(ops: List[str], args: List[List[str]]) -> List[Optional[str]]:
    outputs: List[Optional[str]] = []
    structure = None
    for operation, values in zip(ops, args):
        if operation == "AllOne":
            structure = AllOne()
            outputs.append(None)
        else:
            outputs.append(getattr(structure, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc",
         "getMaxKey", "getMinKey"],
        [[], ["hello"], ["hello"], [], [], ["leet"], [], []],
    ) == [None, None, None, "hello", "hello", None, "hello", "leet"]
    result = replay(
        ["AllOne", "inc", "inc", "dec", "getMaxKey", "getMinKey", "dec",
         "getMaxKey", "getMinKey"],
        [[], ["x"], ["y"], ["x"], [], [], ["y"], [], []],
    )
    assert result[4] in ("x", "y") and result[5] in ("x", "y")
    assert result[7:] == ["", ""]
    print("All tests passed")
