"""
LeetCode 706: Design HashMap
Difficulty: Easy
Pattern: Arrays & Hashing
Video Reference: https://www.youtube.com/watch?v=cNWsgbKwwoU
Complexity:
    - Time: put O(1) average, get O(1) average, remove O(1) average
    - Space: O(n + bucket count)
"""

from typing import List, Optional


class MyHashMap:
    # Separate chaining resolves collisions while keeping keys independent.
    def __init__(self):
        self.bucket_count = 1009
        # Buckets are lists so this implementation does not rely on a built-in map.
        self.buckets: List[List[List[int]]] = [
            [] for _ in range(self.bucket_count)
        ]

    def _bucket(self, key: int) -> List[List[int]]:
        # Modulo spreads the bounded integer key domain across fixed buckets.
        return self.buckets[key % self.bucket_count]

    def put(self, key: int, value: int) -> None:
        bucket = self._bucket(key)
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                # Reusing the pair implements replacement for an existing key.
                return
        # Separate chaining keeps colliding keys distinct within the same bucket.
        bucket.append([key, value])

    def get(self, key: int) -> int:
        # Only colliding keys in one chain need comparison.
        for stored_key, value in self._bucket(key):
            if stored_key == key:
                return value
        return -1

    def remove(self, key: int) -> None:
        bucket = self._bucket(key)
        # Removing a missing key leaves every other mapping intact.
        for index, pair in enumerate(bucket):
            if pair[0] == key:
                # Removing only the matching pair preserves other colliding keys.
                bucket.pop(index)
                return


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    hashmap = None
    for operation, values in zip(ops, args):
        if operation == "MyHashMap":
            hashmap = MyHashMap()
            outputs.append(None)
        else:
            outputs.append(getattr(hashmap, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove",
         "get"],
        [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]],
    ) == [None, None, None, 1, -1, None, 1, None, -1]
    assert replay(
        ["MyHashMap", "put", "put", "get", "remove", "get"],
        [[], [1, 4], [1010, 8], [1010], [1], [1010]],
    ) == [None, None, None, 8, None, 8]
    print("All tests passed")
