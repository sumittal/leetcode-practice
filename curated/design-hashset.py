from typing import List, Optional


class MyHashSet:
    # Bucket lists hold only keys that share the same modulo index.
    # Add, remove, and contains inspect a single chain on average.
    # Duplicate insertion is guarded so each key has one stored copy.
    def __init__(self):
        # Fixed buckets implement the set without relying on Python's set type.
        self.bucket_count = 1009
        self.buckets: List[List[int]] = [[] for _ in range(self.bucket_count)]

    def _bucket(self, key: int) -> List[int]:
        # Integer modulo maps the nonnegative key to one candidate bucket.
        return self.buckets[key % self.bucket_count]

    def add(self, key: int) -> None:
        bucket = self._bucket(key)
        if key not in bucket:
            # A key is appended only once, keeping set membership semantics.
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self._bucket(key)
        if key in bucket:
            # Only one matching key can be present in its chain.
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        # Expected constant time follows from keeping chains short on average.
        return key in self._bucket(key)


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[bool]]:
    outputs: List[Optional[bool]] = []
    hashset = None
    for operation, values in zip(ops, args):
        if operation == "MyHashSet":
            hashset = MyHashSet()
            outputs.append(None)
        else:
            outputs.append(getattr(hashset, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["MyHashSet", "add", "add", "contains", "contains", "add",
         "contains", "remove", "contains"],
        [[], [1], [2], [1], [3], [2], [2], [2], [2]],
    ) == [None, None, None, True, False, None, True, None, False]
    assert replay(
        ["MyHashSet", "add", "add", "contains", "remove", "contains"],
        [[], [5], [5], [5], [5], [5]],
    ) == [None, None, None, True, None, False]
    print("All tests passed")
