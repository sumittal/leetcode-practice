# 706. Design HashMap

**Difficulty:** Easy  
**Tags:** Array, Hash Table, Linked List, Design, Hash Function  
**Companies:** Palo Alto Networks, TikTok, Apple, Snowflake, Oracle, Goldman Sachs, Amazon, LinkedIn, Microsoft, Meta, Google  
**Pattern:** Arrays & Hashing  
**LeetCode:** [https://leetcode.com/problems/design-hashmap/](https://leetcode.com/problems/design-hashmap/)

## Problem

Design a HashMap without using any built-in hash table libraries.

Implement the `MyHashMap` class:

- `MyHashMap()` initializes the object with an empty map.
- `void put(int key, int value)` inserts a `(key, value)` pair into the HashMap. If the `key` already exists in the map, update the corresponding `value`.
- `int get(int key)` returns the `value` to which the specified `key` is mapped, or `-1` if this map contains no mapping for the `key`.
- `void remove(key)` removes the `key` and its corresponding `value` if the map contains the mapping for the `key`.

**Example 1:**

```

**Input**
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
**Output**
[null, null, null, 1, -1, null, 1, null, -1]

**Explanation**
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

```

**Constraints:**

- `0 <= key, value <= 10^6`
- At most `10^4` calls will be made to `put`, `get`, and `remove`.

## Video Explanation

[Design Hashmap - Leetcode 706 - Python](https://www.youtube.com/watch?v=cNWsgbKwwoU)

## Approach

### Intuition

Hash each key to a bucket and keep colliding key-value pairs together.

### Brute Force

Store key-value pairs in one list and linearly search it for each operation.

### Optimal

Use separate chaining with a fixed array of buckets, updating or removing a matching key within its bucket.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | put O(n), get O(n), remove O(n) | O(n) |
| Optimal | put O(1) average, get O(1) average, remove O(1) average | O(n + bucket count) |

### Edge cases

- Putting an existing key replaces its value.
- A missing key returns -1 and removing it changes nothing.
