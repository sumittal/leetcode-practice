# 146. LRU Cache

**Difficulty:** Medium  
**Tags:** Hash Table, Linked List, Design, Doubly-Linked List  
**Companies:** TikTok, Apple, Oracle, Snap, Nutanix, eBay, ServiceNow, ByteDance, Palo Alto Networks, Yahoo, Okta, Zenefits, Moloco, Aurora, Rivian (+88 more)  
**Pattern:** Linked List  
**LeetCode:** [https://leetcode.com/problems/lru-cache/](https://leetcode.com/problems/lru-cache/)

## Problem

Design a data structure that follows the constraints of a **Least Recently Used (LRU) cache**.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`.
- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

**Example 1:**

```

**Input**
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
**Output**
[null, null, null, 1, null, -1, null, -1, 3, 4]

**Explanation**
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

```

**Constraints:**

- `1 <= capacity <= 3000`
- `0 <= key <= 10^4`
- `0 <= value <= 10^5`
- At most `2 * 10^5` calls will be made to `get` and `put`.

## Video Explanation

[LRU Cache - Twitch Interview Question - Leetcode 146](https://www.youtube.com/watch?v=7ABFKPK2hD4)

## Approach

### Intuition

A hash map locates entries while a doubly linked list keeps most- and least-recently used entries in order.

### Brute Force

Store key-value pairs in a list and scan or move entries when they are accessed.

### Optimal

Combine a dictionary with a doubly linked list and sentinels so lookups, promotion, and eviction are constant time.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n) per operation | O(capacity) |
| Optimal | O(1) per operation | O(capacity) |

### Edge cases

- Updating an existing key also makes it most recently used.
- Capacity one evicts the previous entry on every new key.
