"""
LeetCode 146: LRU Cache
Difficulty: Medium
Pattern: Linked List
Video Reference: https://www.youtube.com/watch?v=7ABFKPK2hD4
Complexity:
    - Time: O(1) per operation
    - Space: O(capacity)
"""

from typing import Dict, Optional


class _Node:
    def __init__(self, key: int = 0, value: int = 0) -> None:
        self.key = key
        self.value = value
        self.previous: Optional["_Node"] = None
        self.next: Optional["_Node"] = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        # Sentinels make insertion and eviction independent of endpoint cases.
        self.head = _Node()
        self.tail = _Node()
        self.head.next = self.tail
        self.tail.previous = self.head
        self.capacity = capacity
        self.nodes: Dict[int, _Node] = {}

    def _remove(self, node: _Node) -> None:
        # Neighbor links bypass the node before its own links are cleared.
        previous = node.previous
        following = node.next
        if previous is not None and following is not None:
            previous.next = following
            following.previous = previous
        node.previous = None
        node.next = None

    def _add_after_head(self, node: _Node) -> None:
        # The first real node is always the most recently used entry.
        first = self.head.next
        node.previous = self.head
        node.next = first
        self.head.next = node
        if first is not None:
            first.previous = node

    def _move_to_front(self, node: _Node) -> None:
        # Detach before reinserting so the recency list contains each node once.
        self._remove(node)
        self._add_after_head(node)

    def get(self, key: int) -> int:
        node = self.nodes.get(key)
        if node is None:
            # A miss does not change recency and uses the required -1 result.
            return -1
        # A successful access promotes this key to most recently used.
        self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.nodes.get(key)
        if node is not None:
            # Updating an existing key refreshes both its value and recency.
            node.value = value
            self._move_to_front(node)
            return
        node = _Node(key, value)
        self.nodes[key] = node
        self._add_after_head(node)
        if len(self.nodes) > self.capacity:
            # The tail predecessor is the least recently used real entry.
            least_recent = self.tail.previous
            if least_recent is not None and least_recent is not self.head:
                self._remove(least_recent)
                del self.nodes[least_recent.key]
        # OrderedDict can also track recency; explicit links make the invariant visible.


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
    single = LRUCache(1)
    single.put(1, 1)
    single.put(1, 10)
    assert single.get(1) == 10
    single.put(2, 2)
    assert single.get(1) == -1
    assert single.get(2) == 2
    print("All tests passed")
